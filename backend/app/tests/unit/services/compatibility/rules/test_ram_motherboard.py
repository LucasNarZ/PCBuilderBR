from datetime import datetime
from app.schemas.build import BuildComponents, CompatibilityError
from app.schemas import ComponentWithChosenOffer, RAMSpecs, MotherboardSpecs, ComponentOffer
from app.services.compatibility.rules.ram_motherboard import RAMMotherboardRule


def make_offer():
    return ComponentOffer(
        id="offer-001",
        price=999.99,
        store="Kabum",
        url="https://kabum.com.br",
        in_stock=True,
        last_updated=datetime.now()
    )


def make_ram(ram_type: str = "DDR5", speed: int = 5200, capacity: int = 16, modules: int = 2):
    return ComponentWithChosenOffer(
        id="ram-001",
        name="Kingston Fury Beast 32GB",
        part_type="RAM",
        brand="Kingston",
        specs=RAMSpecs(
            type=ram_type,
            capacity=capacity,
            speed=speed,
            modules=modules,
            latency="CL40",
            voltage=1.1
        ),
        store_count=1,
        offer=make_offer()
    )


def make_motherboard(ram_type: str = "DDR5", max_ram_speed: int = 6400, max_ram_capacity: int = 128, ram_slots: int = 4):
    return ComponentWithChosenOffer(
        id="mb-001",
        name="ASUS Prime B650M-A",
        part_type="MOTHERBOARD",
        brand="ASUS",
        specs=MotherboardSpecs(
            socket="AM5",
            chipset="B650",
            ram_type=ram_type,
            ram_slots=ram_slots,
            max_ram_capacity=max_ram_capacity,
            max_ram_speed=max_ram_speed,
            m2_slots=2,
            sata_slots=4,
            form_factor="MICRO_ATX"
        ),
        store_count=1,
        offer=make_offer()
    )


rule = RAMMotherboardRule()


def test_no_ram_returns_no_errors():
    build = BuildComponents(ram=None, motherboard=make_motherboard())
    errors = rule.check(build)
    assert errors == []


def test_no_motherboard_returns_no_errors():
    build = BuildComponents(ram=make_ram(), motherboard=None)
    errors = rule.check(build)
    assert errors == []


def test_compatible_ram_and_motherboard():
    build = BuildComponents(ram=make_ram(), motherboard=make_motherboard())
    errors = rule.check(build)
    assert errors == []


def test_incompatible_ram_type():
    build = BuildComponents(ram=make_ram(ram_type="DDR4"), motherboard=make_motherboard(ram_type="DDR5"))
    errors = rule.check(build)
    assert any(e.type == "ERROR" and "RAM" in e.affected_components and "MOTHERBOARD" in e.affected_components for e in errors)


def test_ram_speed_above_max_is_warning():
    build = BuildComponents(ram=make_ram(speed=6800), motherboard=make_motherboard(max_ram_speed=6400))
    errors = rule.check(build)
    assert any(e.type == "WARNING" and "RAM" in e.affected_components for e in errors)


def test_ram_speed_at_max_no_warning():
    build = BuildComponents(ram=make_ram(speed=6400), motherboard=make_motherboard(max_ram_speed=6400))
    errors = rule.check(build)
    assert not any(e.type == "WARNING" for e in errors)


def test_ram_total_capacity_exceeds_max():
    build = BuildComponents(ram=make_ram(capacity=32, modules=4), motherboard=make_motherboard(max_ram_capacity=64))
    errors = rule.check(build)
    assert any(e.type == "ERROR" and "RAM" in e.affected_components for e in errors)


def test_ram_total_capacity_at_max_no_error():
    build = BuildComponents(ram=make_ram(capacity=16, modules=4), motherboard=make_motherboard(max_ram_capacity=64))
    errors = rule.check(build)
    assert not any("excede" in e.message for e in errors)


def test_ram_modules_exceed_slots():
    build = BuildComponents(ram=make_ram(modules=4), motherboard=make_motherboard(ram_slots=2))
    errors = rule.check(build)
    assert any(e.type == "ERROR" and "RAM" in e.affected_components for e in errors)


def test_ram_modules_equal_slots_no_error():
    build = BuildComponents(ram=make_ram(modules=2), motherboard=make_motherboard(ram_slots=2))
    errors = rule.check(build)
    assert not any("slots" in e.message for e in errors)


def test_multiple_errors_type_capacity_and_slots():
    build = BuildComponents(
        ram=make_ram(ram_type="DDR4", capacity=32, modules=4),
        motherboard=make_motherboard(ram_type="DDR5", max_ram_capacity=64, ram_slots=2)
    )
    errors = rule.check(build)
    assert len(errors) >= 3
