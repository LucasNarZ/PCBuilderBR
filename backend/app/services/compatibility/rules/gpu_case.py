from app.schemas.build import Build, CompatibilityError
from .base import CompatibilityRule

class GPUCaseRule(CompatibilityRule):
    WARNING_THRESHOLD_MM = 20

    def check(self, build: Build) -> list[CompatibilityError]:
        errors = []
        gpu = build.gpu
        case = build.case

        if not gpu or not case:
            return errors

        gpu_length = gpu.specs.length
        max_length = case.specs.max_gpu_length

        if gpu_length > max_length:
            errors.append(CompatibilityError(
                type="ERROR",
                message=f"GPU ({gpu_length}mm) não cabe no gabinete (máx {max_length}mm)",
                affected_components=["GPU", "CASE"],
            ))
        elif (max_length - gpu_length) < self.WARNING_THRESHOLD_MM:
            errors.append(CompatibilityError(
                type="WARNING",
                message=f"GPU ({gpu_length}mm) cabe no gabinete, mas com folga mínima de {max_length - gpu_length}mm — verifique o cabo de alimentação",
                affected_components=["GPU", "CASE"],
            ))

        return errors
