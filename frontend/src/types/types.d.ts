import type { JSX } from "react";

export type PartType =
    | "CPU"
    | "MOTHERBOARD"
    | "RAM"
    | "GPU"
    | "STORAGE"
    | "PSU"
    | "CASE"
    | "COOLER"
    | "MONITOR"
    | "KEYBOARD"
    | "MOUSE"
    | "HEADSET";

export type PartCategory = "ESSENTIAL" | "OPTIONAL";

export type Socket = "AM4" | "AM5" | "LGA1700" | "LGA1200" | "LGA1851";

export type RAMType = "DDR4" | "DDR5";

export type StorageType = "NVME" | "SATA_SSD" | "HDD";

export type PSUCertification =
    | "80_PLUS"
    | "80_PLUS_BRONZE"
    | "80_PLUS_SILVER"
    | "80_PLUS_GOLD"
    | "80_PLUS_PLATINUM"
    | "80_PLUS_TITANIUM";

export interface ComponentOffer {
    id: string;
    price: number;
    store: string;
    url: string;
    inStock: boolean;
    lastUpdated: Date;
}

export interface Component {
    id: string;
    name: string;
    partType: PartType;
    brand: string;
    imageUrl?: string;
    specs: ComponentSpecs;
    storeCount: number;
    bestOffer: ComponentOffer;
}

export type ComponentWithChosenOffer = Omit<Component, "offers"> & {
    offer: ComponentOffer;
};

export interface ComponentSpecs {
    cpu?: CPUSpecs;
    motherboard?: MotherboardSpecs;
    ram?: RAMSpecs;
    gpu?: GPUSpecs;
    storage?: StorageSpecs;
    psu?: PSUSpecs;
    case?: CaseSpecs;
    cooler?: CoolerSpecs;
    monitor?: MonitorSpecs;
}

export interface CPUSpecs {
    socket: Socket;
    tdp: number;
    cores: number;
    threads: number;
    baseClock: number;
    boostClock: number;
    integratedGraphics: boolean;
}

export interface MotherboardSpecs {
    socket: Socket;
    chipset: string;
    ramType: RAMType;
    ramSlots: number;
    maxRamCapacity: number;
    maxRamSpeed: number;
    m2Slots: number;
    sataSlots: number;
    formFactor: "ATX" | "MICRO_ATX" | "MINI_ITX" | "E-ATX";
}

export interface RAMSpecs {
    type: RAMType;
    capacity: number;
    speed: number;
    modules: number;
    latency: string;
    voltage: number;
}

export interface GPUSpecs {
    chipset: string;
    vram: number;
    tdp: number;
    length: number;
    powerConnectors: string[];
    recommendedPSU: number;
}

export interface StorageSpecs {
    type: StorageType;
    capacity: number;
    readSpeed?: number;
    writeSpeed?: number;
    interface: string;
    formFactor: string;
}

export interface PSUSpecs {
    wattage: number;
    certification: PSUCertification;
    modular: "FULL" | "SEMI" | "NON";
    pcie8pin: number;
    pcie6pin: number;
}

export interface CaseSpecs {
    formFactor: "ATX" | "MICRO_ATX" | "MINI_ITX" | "E-ATX";
    maxGPULength: number;
    maxCoolerHeight: number;
    maxPSULength: number;
    includedFans: number;
    maxFans: number;
}

export interface CoolerSpecs {
    type: "AIR" | "AIO";
    height?: number;
    radiatorSize?: number;
    tdpRating: number;
    compatibleSockets: Socket[];
}

export interface MonitorSpecs {
    size: number;
    resolution: string;
    refreshRate: number;
    panelType: "IPS" | "VA" | "TN" | "OLED";
    responseTime: number;
    adaptive: "GSYNC" | "FREESYNC" | "BOTH" | "NONE";
}

export interface Build {
    id: string;
    name?: string;
    components: {
        cpu?: ComponentWithChosenOffer;
        motherboard?: ComponentWithChosenOffer;
        ram?: ComponentWithChosenOffer;
        gpu?: ComponentWithChosenOffer;
        storage?: ComponentWithChosenOffer;
        psu?: ComponentWithChosenOffer;
        case?: ComponentWithChosenOffer;
        cooler?: ComponentWithChosenOffer;
        monitor?: ComponentWithChosenOffer;
        keyboard?: ComponentWithChosenOffer;
        mouse?: ComponentWithChosenOffer;
        headset?: ComponentWithChosenOffer;
    };
    createdAt: Date;
    updatedAt: Date;
}

export interface CompatibilityError {
    type: "ERROR" | "WARNING";
    message: string;
    affectedComponents: PartType[];
    details?: string;
}

export interface BuildValidation {
    isValid: boolean;
    errors: CompatibilityError[];
    warnings: CompatibilityError[];
    totalPrice: number;
    totalTDP: number;
    estimatedPerformance?: {
        game: string;
        avgFPS: number;
        resolution: string;
        settings: string;
    }[];
}

export interface PartInfo {
    type: PartType;
    label: string;
    icon: JSX.Component;
    category: PartCategory;
    description: string;
}

export const PARTS: Record<PartType, PartInfo> = {
    CPU: {
        type: "CPU",
        label: "Processador",
        icon: "🔧",
        category: "ESSENTIAL",
        description: "O cérebro do computador",
    },
    MOTHERBOARD: {
        type: "MOTHERBOARD",
        label: "Placa-Mãe",
        icon: "📟",
        category: "ESSENTIAL",
        description: "Conecta todos os componentes",
    },
    RAM: {
        type: "RAM",
        label: "Memória RAM",
        icon: "⚡",
        category: "ESSENTIAL",
        description: "Memória de acesso rápido",
    },
    GPU: {
        type: "GPU",
        label: "Placa de Vídeo",
        icon: "📊",
        category: "ESSENTIAL",
        description: "Processa gráficos e jogos",
    },
    STORAGE: {
        type: "STORAGE",
        label: "Armazenamento",
        icon: "💾",
        category: "ESSENTIAL",
        description: "SSD ou HD para guardar arquivos",
    },
    PSU: {
        type: "PSU",
        label: "Fonte",
        icon: "🔌",
        category: "ESSENTIAL",
        description: "Fornece energia para o sistema",
    },
    CASE: {
        type: "CASE",
        label: "Gabinete",
        icon: "📦",
        category: "ESSENTIAL",
        description: "Abriga todos os componentes",
    },
    COOLER: {
        type: "COOLER",
        label: "Cooler",
        icon: "❄️",
        category: "OPTIONAL",
        description: "Resfriamento extra para CPU",
    },
    MONITOR: {
        type: "MONITOR",
        label: "Monitor",
        icon: "🖥️",
        category: "OPTIONAL",
        description: "Tela para visualização",
    },
    KEYBOARD: {
        type: "KEYBOARD",
        label: "Teclado",
        icon: "⌨️",
        category: "OPTIONAL",
        description: "Periférico de entrada",
    },
    MOUSE: {
        type: "MOUSE",
        label: "Mouse",
        icon: "🖱️",
        category: "OPTIONAL",
        description: "Periférico de navegação",
    },
    HEADSET: {
        type: "HEADSET",
        label: "Headset",
        icon: "🎧",
        category: "OPTIONAL",
        description: "Áudio e comunicação",
    },
};
