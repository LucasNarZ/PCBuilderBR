from datetime import datetime
from enum import Enum
from typing import Generic, Optional, TypeVar
from .base import BaseSchema


class PartType(str, Enum):
    CPU = "CPU"
    MOTHERBOARD = "MOTHERBOARD"
    RAM = "RAM"
    GPU = "GPU"
    STORAGE = "STORAGE"
    PSU = "PSU"
    CASE = "CASE"
    COOLER = "COOLER"
    MONITOR = "MONITOR"
    KEYBOARD = "KEYBOARD"
    MOUSE = "MOUSE"
    HEADSET = "HEADSET"


class PartCategory(str, Enum):
    ESSENTIAL = "ESSENTIAL"
    OPTIONAL = "OPTIONAL"


class Socket(str, Enum):
    AM4 = "AM4"
    AM5 = "AM5"
    LGA1700 = "LGA1700"
    LGA1200 = "LGA1200"
    LGA1851 = "LGA1851"


class RAMType(str, Enum):
    DDR4 = "DDR4"
    DDR5 = "DDR5"


class StorageType(str, Enum):
    NVME = "NVME"
    SATA_SSD = "SATA_SSD"
    HDD = "HDD"


class PSUCertification(str, Enum):
    PLUS_80 = "80_PLUS"
    PLUS_80_BRONZE = "80_PLUS_BRONZE"
    PLUS_80_SILVER = "80_PLUS_SILVER"
    PLUS_80_GOLD = "80_PLUS_GOLD"
    PLUS_80_PLATINUM = "80_PLUS_PLATINUM"
    PLUS_80_TITANIUM = "80_PLUS_TITANIUM"


class FormFactor(str, Enum):
    ATX = "ATX"
    MICRO_ATX = "MICRO_ATX"
    MINI_ITX = "MINI_ITX"
    E_ATX = "E-ATX"


class ModularType(str, Enum):
    FULL = "FULL"
    SEMI = "SEMI"
    NON = "NON"


class CoolerType(str, Enum):
    AIR = "AIR"
    AIO = "AIO"


class PanelType(str, Enum):
    IPS = "IPS"
    VA = "VA"
    TN = "TN"
    OLED = "OLED"


class AdaptiveSync(str, Enum):
    GSYNC = "GSYNC"
    FREESYNC = "FREESYNC"
    BOTH = "BOTH"
    NONE = "NONE"


class CompatibilityErrorType(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"


class ComponentOffer(BaseSchema):
    id: str
    price: float
    store: str
    url: str
    in_stock: bool


class CPUSpecs(BaseSchema):
    socket: Socket
    tdp: int
    cores: int
    threads: int
    base_clock: float
    boost_clock: float
    integrated_graphics: bool


class MotherboardSpecs(BaseSchema):
    socket: Socket
    chipset: str
    ram_type: RAMType
    ram_slots: int
    max_ram_capacity: int
    max_ram_speed: int
    m2_slots: int
    sata_slots: int
    form_factor: FormFactor


class RAMSpecs(BaseSchema):
    type: RAMType
    capacity: int
    speed: int
    modules: int
    latency: str
    voltage: float


class GPUSpecs(BaseSchema):
    chipset: str
    vram: int
    tdp: int
    length: int
    power_connectors: list[str]
    recommended_psu: int


class StorageSpecs(BaseSchema):
    type: StorageType
    capacity: int
    read_speed: Optional[int] = None
    write_speed: Optional[int] = None
    interface: str
    form_factor: str


class PSUSpecs(BaseSchema):
    wattage: int
    certification: PSUCertification
    modular: ModularType
    pcie_8pin: int
    pcie_6pin: int


class CaseSpecs(BaseSchema):
    form_factor: FormFactor
    max_gpu_length: int
    max_cooler_height: int
    max_psu_length: int
    included_fans: int
    max_fans: int


class CoolerSpecs(BaseSchema):
    type: CoolerType
    height: Optional[int] = None
    radiator_size: Optional[int] = None
    tdp_rating: int
    compatible_sockets: list[Socket]


class MonitorSpecs(BaseSchema):
    size: float
    resolution: str
    refresh_rate: int
    panel_type: PanelType
    response_time: float
    adaptive: AdaptiveSync


SpecT = TypeVar("SpecT")


class Component(BaseSchema, Generic[SpecT]):
    id: str
    name: str
    part_type: PartType
    brand: str
    image_url: Optional[str] = None
    specs: SpecT
    store_count: int
    best_offer: ComponentOffer


class ComponentWithChosenOffer(BaseSchema, Generic[SpecT]):
    id: str
    name: str
    part_type: PartType
    brand: str
    image_url: Optional[str] = None
    specs: SpecT
    store_count: int
    offer: ComponentOffer


class BuildComponents(BaseSchema):
    cpu: Optional[ComponentWithChosenOffer[CPUSpecs]] = None
    motherboard: Optional[ComponentWithChosenOffer[MotherboardSpecs]] = None
    ram: Optional[ComponentWithChosenOffer[RAMSpecs]] = None
    gpu: Optional[ComponentWithChosenOffer[GPUSpecs]] = None
    storage: Optional[ComponentWithChosenOffer[StorageSpecs]] = None
    psu: Optional[ComponentWithChosenOffer[PSUSpecs]] = None
    case: Optional[ComponentWithChosenOffer[CaseSpecs]] = None
    cooler: Optional[ComponentWithChosenOffer[CoolerSpecs]] = None
    monitor: Optional[ComponentWithChosenOffer[MonitorSpecs]] = None
    keyboard: Optional[ComponentWithChosenOffer[None]] = None
    mouse: Optional[ComponentWithChosenOffer[None]] = None
    headset: Optional[ComponentWithChosenOffer[None]] = None


class Build(BaseSchema):
    id: str
    name: Optional[str] = None
    components: BuildComponents
    created_at: datetime
    updated_at: datetime


class CompatibilityError(BaseSchema):
    type: CompatibilityErrorType
    message: str
    affected_components: list[PartType]
    details: Optional[str] = None


class EstimatedPerformance(BaseSchema):
    game: str
    avg_fps: float
    resolution: str
    settings: str


class BuildValidation(BaseSchema):
    is_valid: bool
    errors: list[CompatibilityError]
    warnings: list[CompatibilityError]
    total_price: float
    total_tdp: int
    estimated_performance: Optional[list[EstimatedPerformance]] = None


class PartInfo(BaseSchema):
    type: PartType
    label: str
    icon: str
    category: PartCategory
    description: str
