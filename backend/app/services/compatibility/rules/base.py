from abc import ABC, abstractmethod
from app.schemas.build import Build, CompatibilityError

class CompatibilityRule(ABC):
    @abstractmethod
    def check(self, build: Build) -> list[CompatibilityError]:
        ...
