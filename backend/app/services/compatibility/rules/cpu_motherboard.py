from app.schemas.build import Build, CompatibilityError
from .base import CompatibilityRule

class CPUMotherboardRule(CompatibilityRule):
    def check(self, build: Build) -> list[CompatibilityError]:
        errors = []
        cpu = build.cpu
        mb = build.motherboard

        if not cpu or not mb:
            return errors

        if cpu.specs.socket != mb.specs.socket:
            errors.append(CompatibilityError(
                type="ERROR",
                message=f"Socket incompatível: CPU usa {cpu.specs.socket}, placa-mãe suporta {mb.specs.socket}",
                affected_components=["CPU", "MOTHERBOARD"],
            ))

        return errors
