from datetime import datetime
from app.schemas.build import BuildComponents, CompatibilityError
from app.schemas import ComponentWithChosenOffer, GPUSpecs, CaseSpecs, ComponentOffer
from app.services.compatibility.rules.gpu_case import GPUCaseRule


def make_offer():
    return ComponentOffer(
        id="offer-001",
        price=999.99,
        store="Kabum",
        url="https://kabum.com.br",
        in_stock=True,
        last_updated=datetime.now()
    )


def make_gpu(length: int = 295):
    return ComponentWithChosenOffer(
        id="gpu-001",
        name="RTX 4060 Ti",
        part_type="GPU",
        brand="NVIDIA",
        specs=GPUSpecs(
            chipset="AD106",
            vram=16,
            tdp=165,
            length=length,
            power_connectors=["8pin"],
            recommended_psu=550
        ),
        store_count=1,
        offer=make_offer()
    )


def make_case(max_gpu_length: int = 360):
    return ComponentWithChosenOffer(
        id="case-001",
        name="Cooler Master Q300L",
        part_type="CASE",
        brand="Cooler Master",
        specs=CaseSpecs(
            form_factor="MICRO_ATX",
            max_gpu_length=max_gpu_length,
            max_cooler_height=160,
            max_psu_length=180,
            included_fans=1,
            max_fans=5
        ),
        store_count=1,
        offer=make_offer()
    )


rule = GPUCaseRule()


def test_no_gpu_returns_no_errors():
    build = BuildComponents(gpu=None, case=make_case())
    errors = rule.check(build)
    assert errors == []


def test_no_case_returns_no_errors():
    build = BuildComponents(gpu=make_gpu(), case=None)
    errors = rule.check(build)
    assert errors == []


def test_gpu_fits_with_plenty_of_space():
    build = BuildComponents(gpu=make_gpu(length=295), case=make_case(max_gpu_length=360))
    errors = rule.check(build)
    assert errors == []


def test_gpu_does_not_fit():
    build = BuildComponents(gpu=make_gpu(length=380), case=make_case(max_gpu_length=360))
    errors = rule.check(build)
    assert len(errors) == 1
    assert errors[0].type == "ERROR"
    assert "GPU" in errors[0].affected_components
    assert "CASE" in errors[0].affected_components


def test_gpu_exactly_at_max_length_no_error():
    build = BuildComponents(gpu=make_gpu(length=340), case=make_case(max_gpu_length=360))
    errors = rule.check(build)
    assert errors == []


def test_gpu_fits_but_below_warning_threshold():
    build = BuildComponents(gpu=make_gpu(length=345), case=make_case(max_gpu_length=360))
    errors = rule.check(build)
    assert len(errors) == 1
    assert errors[0].type == "WARNING"
    assert "GPU" in errors[0].affected_components
    assert "CASE" in errors[0].affected_components


def test_gpu_fits_exactly_at_warning_threshold():
    build = BuildComponents(gpu=make_gpu(length=340), case=make_case(max_gpu_length=360))
    errors = rule.check(build)
    assert errors == []


def test_gpu_one_mm_above_warning_threshold_no_warning():
    build = BuildComponents(gpu=make_gpu(length=339), case=make_case(max_gpu_length=360))
    errors = rule.check(build)
    assert errors == []


def test_gpu_one_mm_too_long_is_error_not_warning():
    build = BuildComponents(gpu=make_gpu(length=361), case=make_case(max_gpu_length=360))
    errors = rule.check(build)
    assert errors[0].type == "ERROR"
