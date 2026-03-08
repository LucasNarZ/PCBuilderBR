from dataclasses import dataclass, field
from app.clients.base import StoreClientProtocol
from app.clients.kabum import KabumClient

@dataclass
class StoreClients:
    kabum: KabumClient = field(default_factory=KabumClient)
    # amazon: AmazonClient = field(default_factory=AmazonClient)

    def all(self) -> list[StoreClientProtocol]:
        return [self.kabum]
