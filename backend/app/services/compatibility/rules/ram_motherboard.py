from app.schemas.build import Build, CompatibilityError
from .base import CompatibilityRule

class RAMMotherboardRule(CompatibilityRule):
    def check(self, build: Build) -> list[CompatibilityError]:
        errors = []
        ram = build.ram
        mb = build.motherboard

        if not ram or not mb:
            return errors

        mb_specs = mb.specs
        ram_specs = ram.specs

        if ram_specs.type != mb_specs.ram_type:
            errors.append(CompatibilityError(
                type="ERROR",
                message=f"Tipo de RAM incompatível: RAM é {ram_specs.type}, placa-mãe suporta {mb_specs.ram_type}",
                affected_components=["RAM", "MOTHERBOARD"],
            ))

        if ram_specs.speed > mb_specs.max_ram_speed:
            errors.append(CompatibilityError(
                type="WARNING",
                message=f"RAM {ram_specs.speed}MHz excede o máximo suportado ({mb_specs.max_ram_speed}MHz), irá operar na velocidade máxima da placa",
                affected_components=["RAM", "MOTHERBOARD"],
            ))

        total_capacity = ram_specs.capacity * ram_specs.modules
        if total_capacity > mb_specs.max_ram_capacity:
            errors.append(CompatibilityError(
                type="ERROR",
                message=f"Capacidade total de RAM ({total_capacity}GB) excede o máximo suportado ({mb_specs.max_ram_capacity}GB)",
                affected_components=["RAM", "MOTHERBOARD"],
            ))

        if ram_specs.modules > mb_specs.ram_slots:
            errors.append(CompatibilityError(
                type="ERROR",
                message=f"RAM possui {ram_specs.modules} módulos, mas a placa-mãe tem apenas {mb_specs.ram_slots} slots",
                affected_components=["RAM", "MOTHERBOARD"],
            ))

        return errors
