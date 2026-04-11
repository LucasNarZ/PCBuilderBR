import asyncio
import re
import uuid
from typing import Any

import httpx

from app.core.database import AsyncSessionLocal
from app.models import Component, ComponentOffer

KABUM_BASE_URL = "https://servicespub.prod.api.aws.grupokabum.com.br"
MAX_PAGES_PER_CATEGORY = 5
PAGE_SIZE = 20

CATEGORIES: dict[str, dict[str, Any]] = {
    "Processador": {"part_type": "CPU", "query": "Processador"},
    "Placa Mae": {"part_type": "MOTHERBOARD", "query": "Placa Mae"},
    "Memoria RAM": {"part_type": "RAM", "query": "Memoria RAM"},
    "Placa de Video": {"part_type": "GPU", "query": "Placa de Video"},
    "SSD": {"part_type": "STORAGE", "query": "SSD"},
    "Fonte": {"part_type": "PSU", "query": "Fonte"},
    "Gabinete": {"part_type": "CASE", "query": "Gabinete"},
    "Cooler": {"part_type": "COOLER", "query": "Cooler"},
}

HEADERS = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}


def extract_brand(attrs: dict) -> str:
    manufacturer = attrs.get("manufacturer") or {}
    return manufacturer.get("name", "Unknown")


def extract_image(attrs: dict) -> str | None:
    images = attrs.get("images") or []
    return images[0] if images else None


def clean_product_name(title: str, brand: str) -> str:
    name = title.strip()
    name = re.sub(r"\s+", " ", name)
    if name.endswith("."):
        name = name[:-1]

    prefixes = [
        "Processador",
        "Placa de Vídeo",
        "Placa De Video",
        "Placa de Video",
        "Placa-Mãe",
        "Placa Mae",
        "Memória RAM",
        "Memoria RAM",
        "SSD",
        "Fonte",
        "Gabinete Gamer",
        "Gabinete",
        "Cooler para Processador",
        "Cooler",
        "Ventoinha",
        "Kit Com 3 Ventoinhas",
        "Kit Com",
        "Kit",
    ]

    for prefix in prefixes:
        if name.upper().startswith(prefix.upper()):
            name = name[len(prefix) :].strip()
            break

    spec_separators = [",", " - ", " | "]
    for sep in spec_separators:
        if sep in name:
            name = name.split(sep)[0].strip()

    if brand and brand != "Unknown":
        brand_pattern = re.compile(rf"\b{re.escape(brand)}\b", re.IGNORECASE)
        name = brand_pattern.sub("", name).strip()

    unwanted_words = [
        "AMD",
        "NVIDIA",
        "Radeon",
        "GeForce",
        "Graphics Cards",
        "Series",
        "Gamer",
        "Preto",
        "Branco",
    ]
    for word in unwanted_words:
        name = re.sub(rf"\b{re.escape(word)}\b", "", name, flags=re.IGNORECASE).strip()

    name = re.sub(r"^[\s,\-]+", "", name).strip()
    name = re.sub(r"[\s,\-]+$", "", name).strip()
    name = re.sub(r"\s+", " ", name).strip()

    if brand and brand != "Unknown":
        name = f"{brand} {name}"

    name = name.strip()
    return name


def extract_cpu_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "socket": "AM4",
        "tdp": 65,
        "cores": 4,
        "threads": 8,
        "base_clock": 3.0,
        "boost_clock": 4.0,
        "integrated_graphics": False,
    }

    text = f"{title} {description}".upper()

    socket_match = re.search(r"LGA\s*(\d+)", text)
    if socket_match:
        specs["socket"] = f"LGA{socket_match.group(1)}"
    elif "AM5" in text:
        specs["socket"] = "AM5"
    elif "AM4" in text:
        specs["socket"] = "AM4"

    cores_match = re.search(r"(\d+)\s*(?:N[ÚU]CLEOS|CORES|CORE)", text)
    if cores_match:
        specs["cores"] = int(cores_match.group(1))

    threads_match = re.search(r"(\d+)\s*THREADS?", text)
    if threads_match:
        specs["threads"] = int(threads_match.group(1))

    boost_match = re.search(r"(?:TURBO|BOOST)[:\s]*(\d+[.,]\d+)\s*GHZ", text)
    if boost_match:
        specs["boost_clock"] = float(boost_match.group(1).replace(",", "."))
    else:
        freq_match = re.findall(r"(\d+[.,]\d+)\s*GHZ", text)
        if freq_match:
            freqs = [float(f.replace(",", ".")) for f in freq_match]
            specs["base_clock"] = min(freqs)
            specs["boost_clock"] = max(freqs)

    tdp_match = re.search(r"TDP[:\s]*(\d+)\s*W", text)
    if tdp_match:
        specs["tdp"] = int(tdp_match.group(1))

    igpu_keywords = [
        "INTEGRATED GRAPHICS",
        "GRÁFICOS INTEGRADOS",
        "IGPU",
        " APU",
        "GRAPHICS 4600",
        "GRAPHICS 630",
        "GRAPHICS 770",
        "WITH VIDEO",
        "COM VÍDEO",
    ]
    if any(k in text for k in igpu_keywords):
        specs["integrated_graphics"] = True

    return specs


def extract_motherboard_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "socket": "AM4",
        "chipset": "B550",
        "ram_type": "DDR4",
        "ram_slots": 2,
        "max_ram_capacity": 64,
        "max_ram_speed": 3200,
        "m2_slots": 1,
        "sata_slots": 4,
        "form_factor": "MICRO_ATX",
    }

    text = f"{title} {description}".upper()

    socket_match = re.search(r"LGA\s*(\d+)", text)
    if socket_match:
        specs["socket"] = f"LGA{socket_match.group(1)}"
    elif "AM5" in text:
        specs["socket"] = "AM5"
    elif "AM4" in text:
        specs["socket"] = "AM4"

    known_chipsets = [
        "Z790",
        "Z690",
        "B760",
        "B660",
        "H610",
        "B650",
        "X670",
        "X570",
        "B550",
        "B450",
        "A520",
        "A320",
        "H510",
        "B560",
        "Z590",
        "X299",
    ]
    for cs in known_chipsets:
        if cs in text:
            specs["chipset"] = cs
            break

    if "DDR5" in text:
        specs["ram_type"] = "DDR5"
    elif "DDR4" in text:
        specs["ram_type"] = "DDR4"

    slots_match = re.search(
        r"(\d+)\s*(?:SLOTS?|SOQUETES?)\s*(?:DE\s*)?(?:MEM[ÓO]RIA|RAM|DDR)", text
    )
    if slots_match:
        specs["ram_slots"] = int(slots_match.group(1))
    elif re.search(r"2XDDR|2\s*SLOT", text):
        specs["ram_slots"] = 2
    elif re.search(r"4XDDR|4\s*SLOT", text):
        specs["ram_slots"] = 4

    max_ram_match = re.search(r"(?:MAX[:\s]*(\d+)\s*GB|(\d+)\s*GB\s*MAX)", text)
    if max_ram_match:
        specs["max_ram_capacity"] = int(
            max_ram_match.group(1) or max_ram_match.group(2)
        )

    m2_match = re.search(r"(\d+)\s*(?:M\.?2|NVME)", text)
    if m2_match:
        specs["m2_slots"] = int(m2_match.group(1))
    elif "M.2" in text or "NVME" in text:
        specs["m2_slots"] = 1

    if "E-ATX" in text:
        specs["form_factor"] = "E-ATX"
    elif "MINI" in text and "ITX" in text:
        specs["form_factor"] = "MINI_ITX"
    elif "MICRO" in text or "M-ATX" in text or "MATX" in text or "MATX" in text:
        specs["form_factor"] = "MICRO_ATX"
    elif "ATX" in text:
        specs["form_factor"] = "ATX"

    return specs


def extract_ram_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "type": "DDR4",
        "capacity": 8,
        "speed": 3200,
        "modules": 1,
        "latency": "CL16",
        "voltage": 1.35,
    }

    text = f"{title} {description}".upper()

    if "DDR5" in text:
        specs["type"] = "DDR5"
        specs["voltage"] = 1.1
    elif "DDR4" in text:
        specs["type"] = "DDR4"

    cap_match = re.search(r"(\d+)\s*GB", text)
    if cap_match:
        specs["capacity"] = int(cap_match.group(1))

    speed_match = re.search(r"(\d{3,5})\s*(?:MHZ|MT/S)", text)
    if speed_match:
        specs["speed"] = int(speed_match.group(1))

    kit_match = re.search(r"(\d+)\s*X\s*\d+", text)
    if kit_match:
        specs["modules"] = int(kit_match.group(1))
    else:
        kit = re.search(r"KIT\s*(\d+)", text)
        if kit:
            specs["modules"] = int(kit.group(1))
        else:
            total_cap = specs["capacity"]
            if total_cap >= 32:
                specs["modules"] = 2
            elif total_cap >= 16 and specs["speed"] >= 3600:
                specs["modules"] = 2

    cl_match = re.search(r"CL\s*(\d+)", text)
    if cl_match:
        specs["latency"] = f"CL{cl_match.group(1)}"

    v_match = re.search(r"(\d+[.,]\d+)\s*V", text)
    if v_match:
        specs["voltage"] = float(v_match.group(1).replace(",", "."))

    return specs


def extract_gpu_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "chipset": "Unknown",
        "vram": 4,
        "tdp": 150,
        "length": 240,
        "power_connectors": ["8-pin"],
        "recommended_psu": 500,
    }

    text = f"{title} {description}".upper()

    known_gpus = {
        "RTX 4090": {"vram": 24, "tdp": 450, "psu": 850},
        "RTX 4080 SUPER": {"vram": 16, "tdp": 320, "psu": 750},
        "RTX 4080": {"vram": 16, "tdp": 320, "psu": 750},
        "RTX 4070 TI SUPER": {"vram": 16, "tdp": 285, "psu": 700},
        "RTX 4070 TI": {"vram": 12, "tdp": 285, "psu": 700},
        "RTX 4070 SUPER": {"vram": 12, "tdp": 220, "psu": 650},
        "RTX 4070": {"vram": 12, "tdp": 200, "psu": 650},
        "RTX 4060 TI": {"vram": 8, "tdp": 160, "psu": 600},
        "RTX 4060": {"vram": 8, "tdp": 115, "psu": 550},
        "RTX 3090": {"vram": 24, "tdp": 350, "psu": 750},
        "RTX 3080 TI": {"vram": 12, "tdp": 350, "psu": 750},
        "RTX 3080": {"vram": 10, "tdp": 320, "psu": 750},
        "RTX 3070 TI": {"vram": 8, "tdp": 290, "psu": 650},
        "RTX 3070": {"vram": 8, "tdp": 220, "psu": 650},
        "RTX 3060 TI": {"vram": 8, "tdp": 200, "psu": 600},
        "RTX 3060": {"vram": 12, "tdp": 170, "psu": 550},
        "RTX 3050": {"vram": 8, "tdp": 130, "psu": 550},
        "GTX 1660 SUPER": {"vram": 6, "tdp": 125, "psu": 450},
        "GTX 1660 TI": {"vram": 6, "tdp": 120, "psu": 450},
        "GTX 1660": {"vram": 6, "tdp": 120, "psu": 450},
        "GTX 1650": {"vram": 4, "tdp": 75, "psu": 350},
        "RX 7900 XTX": {"vram": 24, "tdp": 355, "psu": 850},
        "RX 7900 XT": {"vram": 20, "tdp": 315, "psu": 800},
        "RX 7800 XT": {"vram": 16, "tdp": 263, "psu": 700},
        "RX 7700 XT": {"vram": 12, "tdp": 245, "psu": 650},
        "RX 7600": {"vram": 8, "tdp": 165, "psu": 550},
        "RX 6750 XT": {"vram": 12, "tdp": 250, "psu": 650},
        "RX 6700 XT": {"vram": 12, "tdp": 230, "psu": 650},
        "RX 6650 XT": {"vram": 8, "tdp": 180, "psu": 550},
        "RX 6600 XT": {"vram": 8, "tdp": 160, "psu": 550},
        "RX 6600": {"vram": 8, "tdp": 132, "psu": 500},
        "RX 6500 XT": {"vram": 4, "tdp": 107, "psu": 400},
        "RX580": {"vram": 8, "tdp": 185, "psu": 500},
        "RX 580": {"vram": 8, "tdp": 185, "psu": 500},
        "RX570": {"vram": 4, "tdp": 150, "psu": 450},
        "RX 570": {"vram": 4, "tdp": 150, "psu": 450},
        "GT 1030": {"vram": 2, "tdp": 30, "psu": 300},
        "ARC A770": {"vram": 16, "tdp": 225, "psu": 600},
        "ARC A750": {"vram": 8, "tdp": 225, "psu": 600},
        "GTX1050TI": {"vram": 4, "tdp": 75, "psu": 300},
        "GTX 1050 TI": {"vram": 4, "tdp": 75, "psu": 300},
        "GTX1060": {"vram": 6, "tdp": 120, "psu": 400},
        "GTX 1060": {"vram": 6, "tdp": 120, "psu": 400},
        "GTX 1070 TI": {"vram": 8, "tdp": 180, "psu": 500},
        "GTX 1070": {"vram": 8, "tdp": 150, "psu": 500},
        "GTX 1080 TI": {"vram": 11, "tdp": 250, "psu": 600},
        "GTX 1080": {"vram": 8, "tdp": 180, "psu": 500},
    }

    for gpu_name, gpu_specs in sorted(known_gpus.items(), key=lambda x: -len(x[0])):
        if gpu_name in text:
            specs["chipset"] = gpu_name
            specs["vram"] = gpu_specs["vram"]
            specs["tdp"] = gpu_specs["tdp"]
            specs["recommended_psu"] = gpu_specs["psu"]
            break

    vram_match = re.search(r"(\d+)\s*GB\s*(?:GDDR\d|VRAM)", text)
    if vram_match:
        specs["vram"] = int(vram_match.group(1))

    if specs["chipset"] == "Unknown":
        if "GEFORCE" in text or "NVIDIA" in text or "RTX" in text or "GTX" in text:
            gpu_match = re.search(r"(RTX|GTX)\s*(\d{4})\s*(TI|SUPER)?", text)
            if gpu_match:
                specs["chipset"] = f"{gpu_match.group(1)} {gpu_match.group(2)}"
                if gpu_match.group(3):
                    specs["chipset"] += f" {gpu_match.group(3)}"
        elif "RADEON" in text or "AMD" in text:
            gpu_match = re.search(r"(RX)\s*(\d{4})\s*(XT)?", text)
            if gpu_match:
                specs["chipset"] = f"{gpu_match.group(1)} {gpu_match.group(2)}"
                if gpu_match.group(3):
                    specs["chipset"] += f" {gpu_match.group(3)}"

    len_match = re.search(r"(\d{2,3})\s*MM", text)
    if len_match:
        specs["length"] = int(len_match.group(1))

    return specs


def extract_storage_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "type": "NVME",
        "capacity": 480,
        "read_speed": 3500,
        "write_speed": 3000,
        "interface": "PCIe 3.0 x4",
        "form_factor": "M.2 2280",
    }

    text = f"{title} {description}".upper()

    if "NVME" in text or "M.2" in text or "PCIE" in text:
        specs["type"] = "NVME"
        specs["interface"] = "PCIe 3.0 x4"
        specs["form_factor"] = "M.2 2280"
        if "PCIe 5" in text or "GEN 5" in text or "GEN5" in text or "5.0" in text:
            specs["interface"] = "PCIe 5.0 x4"
            specs["read_speed"] = 10000
            specs["write_speed"] = 9000
        elif "PCIe 4" in text or "GEN 4" in text or "GEN4" in text or "4.0" in text:
            specs["interface"] = "PCIe 4.0 x4"
            specs["read_speed"] = 5000
            specs["write_speed"] = 4500
    elif (
        "HDD" in text
        or "HD " in text
        or "BARRACUDA" in text
        or "5400" in text
        or "7200" in text
    ):
        specs["type"] = "HDD"
        specs["interface"] = "SATA III"
        specs["form_factor"] = "3.5"
        specs["read_speed"] = 190
        specs["write_speed"] = 190
    elif "SATA" in text or '2.5"' in text:
        specs["type"] = "SATA_SSD"
        specs["interface"] = "SATA III"
        specs["form_factor"] = "2.5"
        specs["read_speed"] = 550
        specs["write_speed"] = 500

    cap_match = re.search(r"(\d+)\s*(?:TB|GB)", text)
    if cap_match:
        value = int(cap_match.group(1))
        if "TB" in text[cap_match.start() : cap_match.end() + 2]:
            specs["capacity"] = value * 1000
        else:
            specs["capacity"] = value

    read_match = re.search(r"(?:LEITURA|READ)[:\s]*(\d+)\s*(?:MB/?S|MBPS)", text)
    if read_match:
        specs["read_speed"] = int(read_match.group(1))

    write_match = re.search(
        r"(?:GRAVA[ÇC][ÃA]O|WRITE)[:\s]*(\d+)\s*(?:MB/?S|MBPS)", text
    )
    if write_match:
        specs["write_speed"] = int(write_match.group(1))

    return specs


def extract_psu_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "wattage": 550,
        "certification": "80_PLUS_BRONZE",
        "modular": "NON",
        "pcie_8pin": 2,
        "pcie_6pin": 0,
    }

    text = f"{title} {description}".upper()

    watt_match = re.search(r"(\d{3,4})\s*W", text)
    if watt_match:
        specs["wattage"] = int(watt_match.group(1))

    if "TITANIUM" in text:
        specs["certification"] = "80_PLUS_TITANIUM"
    elif "PLATINUM" in text or "PLATINA" in text:
        specs["certification"] = "80_PLUS_PLATINUM"
    elif "GOLD" in text or "OURO" in text:
        specs["certification"] = "80_PLUS_GOLD"
    elif "SILVER" in text or "PRATA" in text:
        specs["certification"] = "80_PLUS_SILVER"
    elif "BRONZE" in text:
        specs["certification"] = "80_PLUS_BRONZE"
    elif "80 PLUS" in text or "80+" in text:
        specs["certification"] = "80_PLUS"

    if "FULL MODULAR" in text or "FULLY MODULAR" in text:
        specs["modular"] = "FULL"
    elif "SEMI MODULAR" in text or "SEMI-MODULAR" in text:
        specs["modular"] = "SEMI"
    else:
        specs["modular"] = "NON"

    pcie8_match = re.search(r"(\d+)\s*(?:X\s*)?(?:8|6\+2)\s*PIN", text)
    if pcie8_match:
        specs["pcie_8pin"] = int(pcie8_match.group(1))

    return specs


def extract_case_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "form_factor": "ATX",
        "max_gpu_length": 350,
        "max_cooler_height": 165,
        "max_psu_length": 200,
        "included_fans": 1,
        "max_fans": 4,
    }

    text = f"{title} {description}".upper()

    if "E-ATX" in text:
        specs["form_factor"] = "ATX"
    elif "MINI ITX" in text:
        specs["form_factor"] = "MINI_ITX"
    elif "MICRO ATX" in text or "M-ATX" in text or "MATX" in text:
        specs["form_factor"] = "MICRO_ATX"
    elif "ATX" in text:
        specs["form_factor"] = "ATX"

    gpu_match = re.search(r"(?:GPU|PLACA|VGA)[:\s]*(\d{2,3})\s*MM", text)
    if gpu_match:
        specs["max_gpu_length"] = int(gpu_match.group(1))

    cooler_match = re.search(r"(?:COOLER|CPU)[:\s]*(\d{2,3})\s*MM", text)
    if cooler_match:
        specs["max_cooler_height"] = int(cooler_match.group(1))

    fans_match = re.search(r"(\d+)\s*(?:FANS?|VENTOINHAS?)", text)
    if fans_match:
        specs["max_fans"] = int(fans_match.group(1))

    included_match = re.search(
        r"(\d+)\s*(?:FAN|VENTOINHA)\s*(?:INCLU[ÍI]DO|INCLUSA)", text
    )
    if included_match:
        specs["included_fans"] = int(included_match.group(1))
    elif "SEM FAN" in text:
        specs["included_fans"] = 0

    return specs


def extract_cooler_specs(title: str, description: str) -> dict:
    specs: dict[str, Any] = {
        "type": "AIR",
        "height": 155,
        "radiator_size": None,
        "tdp_rating": 150,
        "compatible_sockets": ["AM4", "AM5", "LGA1700"],
    }

    text = f"{title} {description}".upper()

    if "AIO" in text or "WATER" in text or "LIQUID" in text or "WATERCOOLER" in text:
        specs["type"] = "AIO"

    rad_match = re.search(r"(\d{2,3})\s*MM", text)
    if rad_match:
        size = int(rad_match.group(1))
        if size >= 120:
            specs["radiator_size"] = size

    height_match = re.search(r"(?:ALTURA|HEIGHT)[:\s]*(\d{2,3})\s*MM", text)
    if height_match:
        specs["height"] = int(height_match.group(1))

    tdp_match = re.search(r"(?:TDP|RATING)[:\s]*(\d{2,4})\s*W", text)
    if tdp_match:
        specs["tdp_rating"] = int(tdp_match.group(1))

    sockets = []
    if "AM4" in text:
        sockets.append("AM4")
    if "AM5" in text:
        sockets.append("AM5")
    if "LGA 1700" in text or "LGA1700" in text:
        sockets.append("LGA1700")
    if "LGA 1200" in text or "LGA1200" in text:
        sockets.append("LGA1200")
    if "LGA 1851" in text or "LGA1851" in text:
        sockets.append("LGA1851")
    if sockets:
        specs["compatible_sockets"] = sockets

    return specs


SPEC_EXTRACTORS = {
    "CPU": extract_cpu_specs,
    "MOTHERBOARD": extract_motherboard_specs,
    "RAM": extract_ram_specs,
    "GPU": extract_gpu_specs,
    "STORAGE": extract_storage_specs,
    "PSU": extract_psu_specs,
    "CASE": extract_case_specs,
    "COOLER": extract_cooler_specs,
}


async def fetch_products_page(
    client: httpx.AsyncClient, query: str, page_number: int
) -> tuple[list[dict], int]:
    params = {
        "query": query,
        "context": "category",
        "page_number": page_number,
        "page_size": PAGE_SIZE,
        "sort": "most_searched",
    }

    response = await client.get(f"{KABUM_BASE_URL}/catalog/v2/products", params=params)
    response.raise_for_status()
    data = response.json()

    total_pages = data.get("meta", {}).get("total_pages_count", 1)
    products = [item for item in data.get("data", []) if item.get("type") == "product"]

    return products, total_pages


async def fetch_products(
    query: str, max_pages: int = MAX_PAGES_PER_CATEGORY
) -> list[dict]:
    all_products: list[dict] = []

    async with httpx.AsyncClient(headers=HEADERS, timeout=30.0) as client:
        products, total_pages = await fetch_products_page(client, query, 1)
        all_products.extend(products)

        pages_to_fetch = min(total_pages, max_pages)

        for page in range(2, pages_to_fetch + 1):
            try:
                products, _ = await fetch_products_page(client, query, page)
                all_products.extend(products)
            except Exception as e:
                print(f"Error fetching page {page}: {e}")
                break

    return all_products


async def seed():
    async with AsyncSessionLocal() as session:
        components: list[Component] = []
        offers: list[ComponentOffer] = []
        seen_names: dict[str, str] = {}

        for category_name, category_info in CATEGORIES.items():
            part_type = category_info["part_type"]
            query = category_info["query"]

            print(f"Fetching {category_name} products from Kabum API...")

            try:
                products = await fetch_products(query)
            except Exception as e:
                print(f"Error fetching {category_name}: {e}")
                continue

            print(f"Found {len(products)} products for {category_name}")

            extractor = SPEC_EXTRACTORS.get(part_type)
            added_components = 0
            added_offers = 0

            for product in products:
                attrs = product.get("attributes", {})
                title = attrs.get("title", "")
                description = attrs.get("description", "")

                if not title:
                    continue

                brand = extract_brand(attrs)
                name = clean_product_name(title, brand)
                name_key = name.lower().strip()

                price = attrs.get("price_with_discount") or attrs.get("price", 0.0)
                product_link = attrs.get("product_link", "")
                kabum_id = product.get("id", "")
                url = f"https://www.kabum.com.br/produto/{kabum_id}/{product_link}"
                in_stock = attrs.get("available", False)

                if name_key in seen_names:
                    component_id = seen_names[name_key]
                else:
                    component_id = str(uuid.uuid4())
                    seen_names[name_key] = component_id
                    image_url = extract_image(attrs)

                    if extractor:
                        specs = extractor(title, description)
                    else:
                        specs = {}

                    component = Component(
                        id=component_id,
                        name=name,
                        part_type=part_type,
                        brand=brand,
                        image_url=image_url,
                        specs=specs,
                    )
                    components.append(component)
                    added_components += 1

                offer = ComponentOffer(
                    id=str(uuid.uuid4()),
                    component_id=component_id,
                    price=price,
                    store="KaBuM",
                    url=url,
                    in_stock=in_stock,
                )
                offers.append(offer)
                added_offers += 1

            print(
                f"  {category_name}: {added_components} components, {added_offers} offers"
            )

        session.add_all(components)
        session.add_all(offers)
        await session.commit()

        print(f"\nSeeded {len(components)} unique components and {len(offers)} offers")


if __name__ == "__main__":
    asyncio.run(seed())
