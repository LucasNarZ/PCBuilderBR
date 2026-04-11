from datetime import datetime
from app.schemas.build import BuildComponents, CompatibilityError
from app.schemas import ComponentWithChosenOffer, PSUSpecs, CPUSpecs, GPUSpecs, ComponentOffer
from app.services.compatibility.rules.psu import PSURule, SAFETY_MARGIN, SYSTEM_OVERHEAD_WATTS


def make_offer():
    return ComponentOffer(
        id="offer-001",
        price=999.99,
        store="Kabum",
        url="https://kabum.com.br",
        in_stock=True,
        last_updated=datetime.now()
    )


def make_psu(wattage: int = 650, pcie_8pin: int = 2, pcie_6pin: int = 0):
    return ComponentWithChosenOffer(
        id="psu-001",
        name="Corsair RM650",
        part_type="PSU",
        brand="Corsair",
        specs=PSUSpecs(
            wattage=wattage,
            certification="80_PLUS_GOLD",
            modular="FULL",
            pcie_8pin=pcie_8pin,
            pcie_6pin=pcie_6pin
        ),
        store_count=1,
        offer=make_offer()
    )


def make_cpu(tdp: int = 105):
    return ComponentWithChosenOffer(
        id="cpu-001",
        name="Ryzen 5 7600X",
        part_type="CPU",
        brand="AMD",
        specs=CPUSpecs(
            socket="AM5",
            tdp=tdp,
            cores=6,
            threads=12,
            base_clock=4.7,
            boost_clock=5.3,
            integrated_graphics=True
        ),
        store_count=1,
        offer=make_offer()
    )


def make_gpu(tdp: int = 165, power_connectors: list[str] = None):
    return ComponentWithChosenOffer(
        id="gpu-001",
        name="RTX 4060 Ti",
        part_type="GPU",
        brand="NVIDIA",
        specs=GPUSpecs(
            chipset="AD106",
            vram=16,
            tdp=tdp,
            length=295,
            power_connectors=power_connectors or ["8pin"],
            recommended_psu=550
        ),
        store_count=1,
        offer=make_offer()
    )


rule = PSURule()


def test_no_psu_returns_no_errors():
    build = BuildComponents(psu=None, cpu=make_cpu(), gpu=make_gpu())
    errors = rule.check(build)
    assert errors == []


def test_sufficient_psu_no_errors():
    build = BuildComponents(psu=make_psu(wattage=650), cpu=make_cpu(tdp=105), gpu=make_gpu(tdp=165))
    errors = rule.check(build)
    assert errors == []


def test_insufficient_psu_wattage():
    cpu_tdp = 105
    gpu_tdp = 165
    recommended = int((SYSTEM_OVERHEAD_WATTS + cpu_tdp + gpu_tdp) * SAFETY_MARGIN)
    build = BuildComponents(psu=make_psu(wattage=recommended - 1), cpu=make_cpu(tdp=cpu_tdp), gpu=make_gpu(tdp=gpu_tdp))
    errors = rule.check(build)
    assert any(e.type == "ERROR" and "PSU" in e.affected_components for e in errors)


def test_psu_wattage_exactly_at_recommended_no_error():
    cpu_tdp = 105
    gpu_tdp = 165
    recommended = int((SYSTEM_OVERHEAD_WATTS + cpu_tdp + gpu_tdp) * SAFETY_MARGIN)
    build = BuildComponents(psu=make_psu(wattage=recommended), cpu=make_cpu(tdp=cpu_tdp), gpu=make_gpu(tdp=gpu_tdp))
    errors = rule.check(build)
    assert not any("insuficiente" in e.message for e in errors)


def test_no_cpu_no_gpu_only_overhead():
    recommended = int(SYSTEM_OVERHEAD_WATTS * SAFETY_MARGIN)
    build = BuildComponents(psu=make_psu(wattage=recommended - 1), cpu=None, gpu=None)
    errors = rule.check(build)
    assert any(e.type == "ERROR" and "PSU" in e.affected_components for e in errors)


def test_no_gpu_skips_connector_check():
    build = BuildComponents(psu=make_psu(pcie_8pin=0), cpu=make_cpu(), gpu=None)
    errors = rule.check(build)
    assert not any("8-pin" in e.message for e in errors)


def test_insufficient_8pin_connectors():
    build = BuildComponents(
        psu=make_psu(wattage=850, pcie_8pin=1),
        cpu=make_cpu(),
        gpu=make_gpu(tdp=300, power_connectors=["8pin", "8pin", "8pin"])
    )
    errors = rule.check(build)
    assert any("8-pin" in e.message and "PSU" in e.affected_components for e in errors)


def test_sufficient_8pin_connectors():
    build = BuildComponents(
        psu=make_psu(wattage=850, pcie_8pin=2),
        cpu=make_cpu(),
        gpu=make_gpu(power_connectors=["8pin", "8pin"])
    )
    errors = rule.check(build)
    assert not any("8-pin" in e.message for e in errors)


def test_insufficient_6pin_connectors():
    build = BuildComponents(
        psu=make_psu(wattage=850, pcie_6pin=0),
        cpu=make_cpu(),
        gpu=make_gpu(tdp=200, power_connectors=["6pin"])
    )
    errors = rule.check(build)
    assert any("6-pin" in e.message and "PSU" in e.affected_components for e in errors)


def test_sufficient_6pin_connectors():
    build = BuildComponents(
        psu=make_psu(wattage=850, pcie_6pin=2),
        cpu=make_cpu(),
        gpu=make_gpu(power_connectors=["6pin", "6pin"])
    )
    errors = rule.check(build)
    assert not any("6-pin" in e.message for e in errors)


def test_multiple_errors_wattage_and_connectors():
    build = BuildComponents(
        psu=make_psu(wattage=300, pcie_8pin=0, pcie_6pin=0),
        cpu=make_cpu(tdp=125),
        gpu=make_gpu(tdp=450, power_connectors=["8pin", "8pin", "8pin"])
    )
    errors = rule.check(build)
    assert len(errors) >= 2
