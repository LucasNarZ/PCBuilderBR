from app.core.database import AsyncSessionLocal
from app.models import Component
import uuid
import asyncio


async def seed():
    async with AsyncSessionLocal() as session:
        components = [
            # -------------------------
            # CPUs (30)
            # -------------------------
            Component(id=str(uuid.uuid4()), name="Ryzen 3 4100", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 4, "threads": 8, "baseClock": 3.8, "boostClock": 4.0, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 3 3200G", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 4, "threads": 4, "baseClock": 3.6, "boostClock": 4.0, "tdp": 65, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 5 5500", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 6, "threads": 12, "baseClock": 3.6, "boostClock": 4.2, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 5 5600", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 6, "threads": 12, "baseClock": 3.5, "boostClock": 4.4, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 5 5600X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 6, "threads": 12, "baseClock": 3.7, "boostClock": 4.6, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 5 5600G", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 6, "threads": 12, "baseClock": 3.9, "boostClock": 4.4, "tdp": 65, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 7 5700X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 8, "threads": 16, "baseClock": 3.4, "boostClock": 4.6, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 7 5800X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 8, "threads": 16, "baseClock": 3.8, "boostClock": 4.7, "tdp": 105, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 9 5900X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 12, "threads": 24, "baseClock": 3.7, "boostClock": 4.8, "tdp": 105, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 9 5950X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM4", "cores": 16, "threads": 32, "baseClock": 3.4, "boostClock": 4.9, "tdp": 105, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 5 7600", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM5", "cores": 6, "threads": 12, "baseClock": 3.8, "boostClock": 5.1, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 5 7600X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM5", "cores": 6, "threads": 12, "baseClock": 4.7, "boostClock": 5.3, "tdp": 105, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 7 7700", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM5", "cores": 8, "threads": 16, "baseClock": 3.8, "boostClock": 5.3, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 7 7700X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM5", "cores": 8, "threads": 16, "baseClock": 4.5, "boostClock": 5.4, "tdp": 105, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 5 8600G", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM5", "cores": 6, "threads": 12, "baseClock": 4.3, "boostClock": 5.0, "tdp": 65, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Ryzen 9 7900X", part_type="cpu", brand="AMD", specs={"cpu": {"socket": "AM5", "cores": 12, "threads": 24, "baseClock": 4.7, "boostClock": 5.6, "tdp": 170, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Core i3-12100F", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 4, "threads": 8, "baseClock": 3.3, "boostClock": 4.3, "tdp": 58, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Core i3-13100F", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 4, "threads": 8, "baseClock": 3.4, "boostClock": 4.5, "tdp": 58, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Core i5-12400F", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 6, "threads": 12, "baseClock": 2.5, "boostClock": 4.4, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Core i5-13400F", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 10, "threads": 16, "baseClock": 2.5, "boostClock": 4.6, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Core i5-13600K", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 14, "threads": 20, "baseClock": 3.5, "boostClock": 5.1, "tdp": 125, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Core i5-14400F", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 10, "threads": 16, "baseClock": 2.5, "boostClock": 4.7, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Core i5-14600K", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 14, "threads": 20, "baseClock": 3.5, "boostClock": 5.3, "tdp": 125, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Core i7-12700F", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 12, "threads": 20, "baseClock": 2.7, "boostClock": 4.9, "tdp": 65, "integratedGraphics": False}}),
            Component(id=str(uuid.uuid4()), name="Core i7-13700K", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 16, "threads": 24, "baseClock": 3.4, "boostClock": 5.4, "tdp": 125, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Core i7-14700K", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 20, "threads": 28, "baseClock": 3.4, "boostClock": 5.6, "tdp": 125, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Core i9-12900K", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 16, "threads": 24, "baseClock": 3.2, "boostClock": 5.2, "tdp": 125, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Core i9-13900K", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 24, "threads": 32, "baseClock": 3.0, "boostClock": 5.8, "tdp": 125, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Core i9-14900K", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 24, "threads": 32, "baseClock": 3.2, "boostClock": 6.0, "tdp": 125, "integratedGraphics": True}}),
            Component(id=str(uuid.uuid4()), name="Core i5-12400", part_type="cpu", brand="Intel", specs={"cpu": {"socket": "LGA1700", "cores": 6, "threads": 12, "baseClock": 2.5, "boostClock": 4.4, "tdp": 65, "integratedGraphics": True}}),

            # -------------------------
            # Motherboards (30)
            # -------------------------
            Component(id=str(uuid.uuid4()), name="A320M-HDV", part_type="motherboard", brand="ASRock", specs={"motherboard": {"socket": "AM4", "chipset": "A320", "ramType": "DDR4", "ramSlots": 2, "maxRamCapacity": 32, "maxRamSpeed": 3200, "m2Slots": 1, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="B450M DS3H", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "AM4", "chipset": "B450", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 64, "maxRamSpeed": 4400, "m2Slots": 1, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="B450 Tomahawk Max", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "AM4", "chipset": "B450", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 4400, "m2Slots": 2, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="Prime B450M-A II", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "AM4", "chipset": "B450", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 64, "maxRamSpeed": 4400, "m2Slots": 1, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="B550M Aorus Pro", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "AM4", "chipset": "B550", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 5100, "m2Slots": 2, "sataSlots": 6, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="MAG B550 Tomahawk", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "AM4", "chipset": "B550", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 5000, "m2Slots": 2, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="Prime B550-Plus", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "AM4", "chipset": "B550", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 4800, "m2Slots": 2, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="B550 Aorus Pro AC", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "AM4", "chipset": "B550", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 5100, "m2Slots": 3, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="X570 Aorus Elite", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "AM4", "chipset": "X570", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 5400, "m2Slots": 3, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="ROG Strix X570-F Gaming", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "AM4", "chipset": "X570", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 5100, "m2Slots": 3, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="B650M Aorus Elite", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "AM5", "chipset": "B650", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6400, "m2Slots": 2, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="B650 Aorus Elite AX", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "AM5", "chipset": "B650", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6600, "m2Slots": 3, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="MAG B650 Tomahawk", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "AM5", "chipset": "B650", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6600, "m2Slots": 3, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="ROG Strix B650-A Gaming WiFi", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "AM5", "chipset": "B650", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6400, "m2Slots": 3, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="X670E Aorus Master", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "AM5", "chipset": "X670E", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6666, "m2Slots": 4, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="H610M DS2H DDR4", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "LGA1700", "chipset": "H610", "ramType": "DDR4", "ramSlots": 2, "maxRamCapacity": 64, "maxRamSpeed": 4800, "m2Slots": 1, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="B660M Gaming X DDR4", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "LGA1700", "chipset": "B660", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 4800, "m2Slots": 2, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="MAG B660 Tomahawk DDR4", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "LGA1700", "chipset": "B660", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 4800, "m2Slots": 3, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="Z690 Aorus Elite DDR4", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "LGA1700", "chipset": "Z690", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6200, "m2Slots": 4, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="MAG Z690 Tomahawk DDR4", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "LGA1700", "chipset": "Z690", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6200, "m2Slots": 4, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="ROG Strix B660-F Gaming WiFi", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "LGA1700", "chipset": "B660", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 4800, "m2Slots": 3, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="Z790 Aorus Elite AX", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "LGA1700", "chipset": "Z790", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 192, "maxRamSpeed": 7600, "m2Slots": 5, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="MPG Z790 Edge WiFi", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "LGA1700", "chipset": "Z790", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 192, "maxRamSpeed": 7200, "m2Slots": 5, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="Prime Z790-P WiFi", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "LGA1700", "chipset": "Z790", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 192, "maxRamSpeed": 7200, "m2Slots": 4, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="ROG Strix X670E-F Gaming WiFi", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "AM5", "chipset": "X670E", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6800, "m2Slots": 4, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="MPG X670E Carbon WiFi", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "AM5", "chipset": "X670E", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 6800, "m2Slots": 4, "sataSlots": 4, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="Prime B650M-A WiFi", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "AM5", "chipset": "B650", "ramType": "DDR5", "ramSlots": 2, "maxRamCapacity": 96, "maxRamSpeed": 6400, "m2Slots": 2, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="B760M DS3H DDR4", part_type="motherboard", brand="Gigabyte", specs={"motherboard": {"socket": "LGA1700", "chipset": "B760", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 5333, "m2Slots": 2, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="MAG B760 Tomahawk WiFi DDR4", part_type="motherboard", brand="MSI", specs={"motherboard": {"socket": "LGA1700", "chipset": "B760", "ramType": "DDR4", "ramSlots": 4, "maxRamCapacity": 128, "maxRamSpeed": 5333, "m2Slots": 3, "sataSlots": 6, "formFactor": "ATX"}}),
            Component(id=str(uuid.uuid4()), name="Prime H610M-E D4", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "LGA1700", "chipset": "H610", "ramType": "DDR4", "ramSlots": 2, "maxRamCapacity": 64, "maxRamSpeed": 4800, "m2Slots": 1, "sataSlots": 4, "formFactor": "MICRO_ATX"}}),
            Component(id=str(uuid.uuid4()), name="ProArt Z790-Creator WiFi", part_type="motherboard", brand="ASUS", specs={"motherboard": {"socket": "LGA1700", "chipset": "Z790", "ramType": "DDR5", "ramSlots": 4, "maxRamCapacity": 192, "maxRamSpeed": 7600, "m2Slots": 5, "sataSlots": 4, "formFactor": "ATX"}}),

            # -------------------------
            # GPUs (30)
            # -------------------------
            Component(id=str(uuid.uuid4()), name="GeForce GT 1030", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "GT 1030", "vram": 2, "tdp": 30, "length": 145, "powerConnectors": [], "recommendedPSU": 300}}),
            Component(id=str(uuid.uuid4()), name="GeForce GTX 1650", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "GTX 1650", "vram": 4, "tdp": 75, "length": 190, "powerConnectors": [], "recommendedPSU": 350}}),
            Component(id=str(uuid.uuid4()), name="GeForce GTX 1660 Super", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "GTX 1660 Super", "vram": 6, "tdp": 125, "length": 229, "powerConnectors": ["8-pin"], "recommendedPSU": 450}}),
            Component(id=str(uuid.uuid4()), name="GeForce GTX 1660 Ti", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "GTX 1660 Ti", "vram": 6, "tdp": 120, "length": 229, "powerConnectors": ["8-pin"], "recommendedPSU": 450}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 2060", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 2060", "vram": 6, "tdp": 160, "length": 229, "powerConnectors": ["8-pin"], "recommendedPSU": 500}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 3050", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 3050", "vram": 8, "tdp": 130, "length": 228, "powerConnectors": ["8-pin"], "recommendedPSU": 550}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 3060", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 3060", "vram": 12, "tdp": 170, "length": 242, "powerConnectors": ["8-pin"], "recommendedPSU": 550}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 3060 Ti", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 3060 Ti", "vram": 8, "tdp": 200, "length": 242, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 600}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 3070", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 3070", "vram": 8, "tdp": 220, "length": 242, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 650}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 3080", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 3080", "vram": 10, "tdp": 320, "length": 285, "powerConnectors": ["8-pin", "8-pin", "8-pin"], "recommendedPSU": 750}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 4060", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 4060", "vram": 8, "tdp": 115, "length": 240, "powerConnectors": ["8-pin"], "recommendedPSU": 550}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 4060 Ti", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 4060 Ti", "vram": 8, "tdp": 160, "length": 270, "powerConnectors": ["8-pin"], "recommendedPSU": 600}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 4060 Ti 16GB", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 4060 Ti", "vram": 16, "tdp": 165, "length": 270, "powerConnectors": ["8-pin"], "recommendedPSU": 600}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 4070", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 4070", "vram": 12, "tdp": 200, "length": 285, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 650}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 4070 Super", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 4070 Super", "vram": 12, "tdp": 220, "length": 285, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 700}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 4070 Ti", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 4070 Ti", "vram": 12, "tdp": 285, "length": 305, "powerConnectors": ["8-pin", "8-pin", "8-pin"], "recommendedPSU": 700}}),
            Component(id=str(uuid.uuid4()), name="GeForce RTX 4080", part_type="gpu", brand="NVIDIA", specs={"gpu": {"chipset": "RTX 4080", "vram": 16, "tdp": 320, "length": 336, "powerConnectors": ["8-pin", "8-pin", "8-pin"], "recommendedPSU": 750}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 6500 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 6500 XT", "vram": 4, "tdp": 107, "length": 190, "powerConnectors": ["8-pin"], "recommendedPSU": 400}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 6600", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 6600", "vram": 8, "tdp": 132, "length": 216, "powerConnectors": ["8-pin"], "recommendedPSU": 500}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 6600 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 6600 XT", "vram": 8, "tdp": 160, "length": 237, "powerConnectors": ["8-pin"], "recommendedPSU": 550}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 6650 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 6650 XT", "vram": 8, "tdp": 180, "length": 237, "powerConnectors": ["8-pin"], "recommendedPSU": 550}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 6700 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 6700 XT", "vram": 12, "tdp": 230, "length": 267, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 650}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 6750 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 6750 XT", "vram": 12, "tdp": 250, "length": 267, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 650}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 6800 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 6800 XT", "vram": 16, "tdp": 300, "length": 267, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 750}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 7600", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 7600", "vram": 8, "tdp": 165, "length": 230, "powerConnectors": ["8-pin"], "recommendedPSU": 550}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 7700 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 7700 XT", "vram": 12, "tdp": 245, "length": 267, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 650}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 7800 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 7800 XT", "vram": 16, "tdp": 263, "length": 267, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 700}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 7900 XT", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 7900 XT", "vram": 20, "tdp": 315, "length": 287, "powerConnectors": ["8-pin", "8-pin", "8-pin"], "recommendedPSU": 800}}),
            Component(id=str(uuid.uuid4()), name="Arc A750", part_type="gpu", brand="Intel", specs={"gpu": {"chipset": "Arc A750", "vram": 8, "tdp": 225, "length": 272, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 600}}),
            Component(id=str(uuid.uuid4()), name="Arc A770 16GB", part_type="gpu", brand="Intel", specs={"gpu": {"chipset": "Arc A770", "vram": 16, "tdp": 225, "length": 272, "powerConnectors": ["8-pin", "8-pin"], "recommendedPSU": 600}}),
            Component(id=str(uuid.uuid4()), name="Radeon RX 7900 XTX", part_type="gpu", brand="AMD", specs={"gpu": {"chipset": "RX 7900 XTX", "vram": 24, "tdp": 355, "length": 287, "powerConnectors": ["8-pin", "8-pin", "8-pin"], "recommendedPSU": 850}}),

            # -------------------------
            # RAMs (5)
            # -------------------------
            Component(id=str(uuid.uuid4()), name="Fury Beast DDR4 8GB 3200MHz", part_type="ram", brand="Kingston", specs={"ram": {"type": "DDR4", "capacity": 8, "speed": 3200, "modules": 1, "latency": "CL16", "voltage": 1.35}}),
            Component(id=str(uuid.uuid4()), name="Fury Beast DDR4 16GB 3200MHz", part_type="ram", brand="Kingston", specs={"ram": {"type": "DDR4", "capacity": 16, "speed": 3200, "modules": 2, "latency": "CL16", "voltage": 1.35}}),
            Component(id=str(uuid.uuid4()), name="Vengeance LPX DDR4 16GB 3200MHz", part_type="ram", brand="Corsair", specs={"ram": {"type": "DDR4", "capacity": 16, "speed": 3200, "modules": 2, "latency": "CL16", "voltage": 1.35}}),
            Component(id=str(uuid.uuid4()), name="Fury Beast DDR5 16GB 5200MHz", part_type="ram", brand="Kingston", specs={"ram": {"type": "DDR5", "capacity": 16, "speed": 5200, "modules": 2, "latency": "CL40", "voltage": 1.1}}),
            Component(id=str(uuid.uuid4()), name="Trident Z5 DDR5 32GB 6000MHz", part_type="ram", brand="G.Skill", specs={"ram": {"type": "DDR5", "capacity": 32, "speed": 6000, "modules": 2, "latency": "CL30", "voltage": 1.35}}),

            # -------------------------
            # Storage (5)
            # -------------------------
            Component(id=str(uuid.uuid4()), name="SSD SATA BX500 480GB", part_type="storage", brand="Crucial", specs={"storage": {"type": "SATA_SSD", "capacity": 480, "readSpeed": 540, "writeSpeed": 500, "interface": "SATA III", "formFactor": "2.5"}}),
            Component(id=str(uuid.uuid4()), name="SSD NVMe 970 EVO Plus 1TB", part_type="storage", brand="Samsung", specs={"storage": {"type": "NVME", "capacity": 1000, "readSpeed": 3500, "writeSpeed": 3300, "interface": "PCIe 3.0 x4", "formFactor": "M.2 2280"}}),
            Component(id=str(uuid.uuid4()), name="SSD NVMe SN770 1TB", part_type="storage", brand="WD", specs={"storage": {"type": "NVME", "capacity": 1000, "readSpeed": 5150, "writeSpeed": 4900, "interface": "PCIe 4.0 x4", "formFactor": "M.2 2280"}}),
            Component(id=str(uuid.uuid4()), name="SSD NVMe 990 Pro 1TB", part_type="storage", brand="Samsung", specs={"storage": {"type": "NVME", "capacity": 1000, "readSpeed": 7450, "writeSpeed": 6900, "interface": "PCIe 4.0 x4", "formFactor": "M.2 2280"}}),
            Component(id=str(uuid.uuid4()), name="HDD Barracuda 2TB 7200rpm", part_type="storage", brand="Seagate", specs={"storage": {"type": "HDD", "capacity": 2000, "readSpeed": 190, "writeSpeed": 190, "interface": "SATA III", "formFactor": "3.5"}}),

            # -------------------------
            # PSUs (5)
            # -------------------------
            Component(id=str(uuid.uuid4()), name="CV550 550W 80+ Bronze", part_type="psu", brand="Corsair", specs={"psu": {"wattage": 550, "certification": "80_PLUS_BRONZE", "modular": "NON", "pcie8pin": 2, "pcie6pin": 0}}),
            Component(id=str(uuid.uuid4()), name="CV650 650W 80+ Bronze", part_type="psu", brand="Corsair", specs={"psu": {"wattage": 650, "certification": "80_PLUS_BRONZE", "modular": "NON", "pcie8pin": 2, "pcie6pin": 2}}),
            Component(id=str(uuid.uuid4()), name="RM750e 750W 80+ Gold", part_type="psu", brand="Corsair", specs={"psu": {"wattage": 750, "certification": "80_PLUS_GOLD", "modular": "FULL", "pcie8pin": 4, "pcie6pin": 0}}),
            Component(id=str(uuid.uuid4()), name="Focus GX-650 650W 80+ Gold", part_type="psu", brand="Seasonic", specs={"psu": {"wattage": 650, "certification": "80_PLUS_GOLD", "modular": "FULL", "pcie8pin": 2, "pcie6pin": 2}}),
            Component(id=str(uuid.uuid4()), name="Focus GX-850 850W 80+ Gold", part_type="psu", brand="Seasonic", specs={"psu": {"wattage": 850, "certification": "80_PLUS_GOLD", "modular": "FULL", "pcie8pin": 4, "pcie6pin": 2}}),

            # -------------------------
            # Cases (5)
            # -------------------------
            Component(id=str(uuid.uuid4()), name="Versa H18", part_type="case", brand="Thermaltake", specs={"case": {"formFactor": "MICRO_ATX", "maxGPULength": 320, "maxCoolerHeight": 155, "maxPSULength": 140, "includedFans": 1, "maxFans": 3}}),
            Component(id=str(uuid.uuid4()), name="H510", part_type="case", brand="NZXT", specs={"case": {"formFactor": "ATX", "maxGPULength": 381, "maxCoolerHeight": 165, "maxPSULength": 210, "includedFans": 2, "maxFans": 4}}),
            Component(id=str(uuid.uuid4()), name="4000D Airflow", part_type="case", brand="Corsair", specs={"case": {"formFactor": "ATX", "maxGPULength": 360, "maxCoolerHeight": 170, "maxPSULength": 200, "includedFans": 2, "maxFans": 6}}),
            Component(id=str(uuid.uuid4()), name="Meshify 2", part_type="case", brand="Fractal Design", specs={"case": {"formFactor": "ATX", "maxGPULength": 461, "maxCoolerHeight": 185, "maxPSULength": 250, "includedFans": 3, "maxFans": 9}}),
            Component(id=str(uuid.uuid4()), name="O11 Dynamic EVO", part_type="case", brand="Lian Li", specs={"case": {"formFactor": "ATX", "maxGPULength": 420, "maxCoolerHeight": 167, "maxPSULength": 220, "includedFans": 0, "maxFans": 10}}),
        ]

        session.add_all(components)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed())
