import pytest
from app.services.compatibility.rules.cpu_motherboard import CPUMotherboardRule
from app.schemas import BuildComponents, ComponentWithChosenOffer, CPUSpecs, MotherboardSpecs, ComponentOffer
from datetime import datetime

def make_offer():
    return ComponentOffer(
        id="offer-001",
        price=999.99,
        store="Kabum",
        url="https://kabum.com.br",
        in_stock=True,
        last_updated=datetime.now()
    )

def make_cpu(socket: str):
    return ComponentWithChosenOffer(
        id="cpu-001",
        name="Ryzen 5 7600X",
        part_type="CPU",
        brand="AMD",
        specs=CPUSpecs(
            socket=socket,
            tdp=105,
            cores=6,
            threads=12,
            base_clock=4.7,
            boost_clock=5.3,
            integrated_graphics=True
        ),
        store_count=1,
        offer=make_offer()
    )

def make_motherboard(socket: str):
    return ComponentWithChosenOffer(
        id="mb-001",
        name="ASUS Prime B650M",
        part_type="MOTHERBOARD",
        brand="ASUS",
        specs=MotherboardSpecs(
            socket=socket,
            chipset="B650",
            ram_type="DDR5",
            ram_slots=4,
            max_ram_capacity=128,
            max_ram_speed=6400,
            m2_slots=2,
            sata_slots=4,
            form_factor="MICRO_ATX"
        ),
        store_count=1,
        offer=make_offer()
    )

rule = CPUMotherboardRule()

def test_compatible_sockets():
    build = BuildComponents(cpu=make_cpu("AM5"), motherboard=make_motherboard("AM5"))
    errors = rule.check(build)
    assert errors == []

def test_incompatible_sockets():
    build = BuildComponents(cpu=make_cpu("AM5"), motherboard=make_motherboard("AM4"))
    errors = rule.check(build)
    assert len(errors) == 1
    assert errors[0].type == "ERROR"

def test_missing_cpu():
    build = BuildComponents(cpu=None, motherboard=make_motherboard("AM5"))
    errors = rule.check(build)
    assert errors == []

def test_missing_motherboard():
    build = BuildComponents(cpu=make_cpu("AM5"), motherboard=None)
    errors = rule.check(build)
    assert errors == []
