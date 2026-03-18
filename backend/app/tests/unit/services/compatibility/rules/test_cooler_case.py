import pytest
from datetime import datetime
from app.schemas.build import BuildComponents, CompatibilityError
from app.schemas import ComponentWithChosenOffer, CoolerSpecs, CaseSpecs, CPUSpecs, ComponentOffer
from app.services.compatibility.rules.cooler_case import CoolerCaseRule


def make_offer():
    return ComponentOffer(
        id="offer-001",
        price=999.99,
        store="Kabum",
        url="https://kabum.com.br",
        in_stock=True,
        last_updated=datetime.now()
    )


def make_cooler(cooler_type: str = "AIR", height: int = 150, compatible_sockets: list[str] = None):
    return ComponentWithChosenOffer(
        id="cooler-001",
        name="Cooler Master Hyper 212",
        part_type="COOLER",
        brand="Cooler Master",
        specs=CoolerSpecs(
            type=cooler_type,
            height=height,
            tdp_rating=150,
            compatible_sockets=compatible_sockets or ["AM5", "LGA1700"]
        ),
        store_count=1,
        offer=make_offer()
    )


def make_case(max_cooler_height: int = 160):
    return ComponentWithChosenOffer(
        id="case-001",
        name="Cooler Master Q300L",
        part_type="CASE",
        brand="Cooler Master",
        specs=CaseSpecs(
            form_factor="MICRO_ATX",
            max_gpu_length=360,
            max_cooler_height=max_cooler_height,
            max_psu_length=180,
            included_fans=1,
            max_fans=5
        ),
        store_count=1,
        offer=make_offer()
    )


def make_cpu(socket: str = "AM5"):
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


rule = CoolerCaseRule()


def test_no_cooler_returns_no_errors():
    build = BuildComponents(cooler=None, case=make_case(), cpu=make_cpu())
    errors = rule.check(build)
    assert errors == []


def test_air_cooler_fits_in_case():
    build = BuildComponents(cooler=make_cooler(height=150), case=make_case(max_cooler_height=160), cpu=make_cpu())
    errors = rule.check(build)
    assert errors == []


def test_air_cooler_too_tall_for_case():
    build = BuildComponents(cooler=make_cooler(height=170), case=make_case(max_cooler_height=160), cpu=make_cpu())
    errors = rule.check(build)
    assert len(errors) == 1
    assert errors[0].type == "ERROR"
    assert "COOLER" in errors[0].affected_components
    assert "CASE" in errors[0].affected_components


def test_air_cooler_exact_max_height_fits():
    build = BuildComponents(cooler=make_cooler(height=160), case=make_case(max_cooler_height=160), cpu=make_cpu())
    errors = rule.check(build)
    assert errors == []


def test_aio_cooler_height_not_checked():
    build = BuildComponents(cooler=make_cooler(cooler_type="AIO", height=170), case=make_case(max_cooler_height=160), cpu=make_cpu())
    errors = rule.check(build)
    assert not any("CASE" in e.affected_components for e in errors)


def test_cooler_compatible_socket():
    build = BuildComponents(cooler=make_cooler(compatible_sockets=["AM5"]), cpu=make_cpu(socket="AM5"), case=None)
    errors = rule.check(build)
    assert errors == []


def test_cooler_incompatible_socket():
    build = BuildComponents(cooler=make_cooler(compatible_sockets=["LGA1700"]), cpu=make_cpu(socket="AM5"), case=None)
    errors = rule.check(build)
    assert len(errors) == 1
    assert errors[0].type == "ERROR"
    assert "COOLER" in errors[0].affected_components
    assert "CPU" in errors[0].affected_components


def test_cooler_no_cpu_skips_socket_check():
    build = BuildComponents(cooler=make_cooler(), cpu=None, case=None)
    errors = rule.check(build)
    assert errors == []


def test_cooler_no_case_skips_height_check():
    build = BuildComponents(cooler=make_cooler(height=999), cpu=make_cpu(), case=None)
    errors = rule.check(build)
    assert not any("CASE" in e.affected_components for e in errors)


def test_multiple_errors_height_and_socket():
    build = BuildComponents(
        cooler=make_cooler(height=200, compatible_sockets=["LGA1700"]),
        case=make_case(max_cooler_height=160),
        cpu=make_cpu(socket="AM5")
    )
    errors = rule.check(build)
    assert len(errors) == 2
