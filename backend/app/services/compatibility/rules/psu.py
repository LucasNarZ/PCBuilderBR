from app.schemas.build import Build, CompatibilityError
from .base import CompatibilityRule

SAFETY_MARGIN = 1.25
SYSTEM_OVERHEAD_WATTS = 50

class PSURule(CompatibilityRule):
    def check(self, build: Build) -> list[CompatibilityError]:
        errors = []
        psu = build.psu
        cpu = build.cpu
        gpu = build.gpu

        if not psu:
            return errors

        psu_specs = psu.specs
        total_tdp = SYSTEM_OVERHEAD_WATTS

        if cpu:
            total_tdp += cpu.specs.tdp
        if gpu:
            total_tdp += gpu.specs.tdp

        recommended_wattage = int(total_tdp * SAFETY_MARGIN)

        if psu_specs.wattage < recommended_wattage:
            errors.append(CompatibilityError(
                type="ERROR",
                message=f"Fonte ({psu_specs.wattage}W) insuficiente. Consumo estimado com margem de segurança: {recommended_wattage}W",
                affected_components=["PSU", "CPU", "GPU"],
                details=f"CPU: {cpu.specs.tdp if cpu else 0}W + GPU: {gpu.specs.tdp if gpu else 0}W + sistema: {SYSTEM_OVERHEAD_WATTS}W",
            ))

        if gpu:
            gpu_connectors_needed = gpu.specs.power_connectors
            needed_8pin = sum(1 for c in gpu_connectors_needed if c == "8pin")
            needed_6pin = sum(1 for c in gpu_connectors_needed if c == "6pin")

            if needed_8pin > psu_specs.pcie_8pin:
                errors.append(CompatibilityError(
                    type="ERROR",
                    message=f"Fonte não tem conectores 8-pin suficientes: GPU precisa de {needed_8pin}, fonte tem {psu_specs.pcie_8pin}",
                    affected_components=["PSU", "GPU"],
                ))

            if needed_6pin > psu_specs.pcie_6pin:
                errors.append(CompatibilityError(
                    type="ERROR",
                    message=f"Fonte não tem conectores 6-pin suficientes: GPU precisa de {needed_6pin}, fonte tem {psu_specs.pcie_6pin}",
                    affected_components=["PSU", "GPU"],
                ))

        return errors
