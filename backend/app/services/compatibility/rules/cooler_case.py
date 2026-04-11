from app.schemas.build import Build, CompatibilityError
from .base import CompatibilityRule

class CoolerCaseRule(CompatibilityRule):
    def check(self, build: Build) -> list[CompatibilityError]:
        errors = []
        cooler = build.cooler
        case = build.case
        cpu = build.cpu

        if not cooler:
            return errors

        cooler_specs = cooler.specs

        if case and cooler_specs.type == "AIR" and cooler_specs.height:
            max_height = case.specs.max_cooler_height
            if cooler_specs.height > max_height:
                errors.append(CompatibilityError(
                    type="ERROR",
                    message=f"Cooler ({cooler_specs.height}mm) não cabe no gabinete (máx {max_height}mm)",
                    affected_components=["COOLER", "CASE"],
                ))

        if cpu:
            cpu_socket = cpu.specs.socket
            if cpu_socket not in cooler_specs.compatible_sockets:
                errors.append(CompatibilityError(
                    type="ERROR",
                    message=f"Cooler não suporta o socket {cpu_socket}",
                    affected_components=["COOLER", "CPU"],
                ))

        return errors
