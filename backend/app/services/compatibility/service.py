from app.schemas import BuildComponents, BuildValidation, CompatibilityError
from app.services.compatibility.rules.cpu_motherboard import CPUMotherboardRule
from app.services.compatibility.rules.ram_motherboard import RAMMotherboardRule
from app.services.compatibility.rules.gpu_case import GPUCaseRule
from app.services.compatibility.rules.psu import PSURule
from app.services.compatibility.rules.cooler_case import CoolerCaseRule

SYSTEM_OVERHEAD_WATTS = 50

class CompatibilityService:
    def __init__(self):
        self._rules = [
            CPUMotherboardRule(),
            RAMMotherboardRule(),
            GPUCaseRule(),
            PSURule(),
            CoolerCaseRule(),
        ]

    def test_compatibility(self, build: BuildComponents) -> BuildValidation:
        all_issues: list[CompatibilityError] = []

        for rule in self._rules:
            all_issues.extend(rule.check(build))

        errors = [i for i in all_issues if i.type == "ERROR"]
        warnings = [i for i in all_issues if i.type == "WARNING"]

        total_price = sum(
            getattr(build, field).offer.price
            for field in build.model_fields
            if getattr(build, field) is not None
        )

        total_tdp = SYSTEM_OVERHEAD_WATTS
        if build.cpu:
            total_tdp += build.cpu.specs.tdp
        if build.gpu:
            total_tdp += build.gpu.specs.tdp

        return BuildValidation(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            total_price=total_price,
            total_tdp=total_tdp,
        )
