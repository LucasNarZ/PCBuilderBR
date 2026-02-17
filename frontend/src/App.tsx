import { Box, Cpu, HardDrive, Headset, Keyboard, Monitor, Mouse, Power, Snowflake, Wallpaper, Zap } from 'lucide-react';
import { PartCard } from './components/PartCard';
import { Summary } from './components/Summary';
import type { PartInfo } from './types.d';

export const PARTS_DATA: PartInfo[] = [
    {
        type: 'CPU',
        label: 'Processador',
        icon: <Cpu size={24} color="#3d3846" />,
        category: 'ESSENTIAL',
        description: 'O cérebro do computador',
        components: [
            {
                id: 'cpu-001',
                name: 'AMD Ryzen 5 7600',
                partType: 'CPU',
                brand: 'AMD',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/385927/processador-amd-ryzen-5-7600-3-8ghz-5-1ghz-turbo-6-cores-12-threads-cooler-wraith-stealth-am5-100-100000927box_1663685523_g.jpg',
                specs: {
                    cpu: {
                        socket: 'AM5',
                        tdp: 65,
                        cores: 6,
                        threads: 12,
                        baseClock: 3.8,
                        boostClock: 5.1,
                        integratedGraphics: true
                    }
                },
                offers: [
                    {
                        id: 'cpu-001-kabum',
                        price: 1199,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/385927',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'cpu-001-pichau',
                        price: 1189,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/ryzen-5-7600',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'cpu-001-terabyte',
                        price: 1210,
                        store: 'Terabyte',
                        url: 'https://terabyte.com.br/ryzen-7600',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'cpu-002',
                name: 'AMD Ryzen 7 7800X3D',
                partType: 'CPU',
                brand: 'AMD',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/437094/processador-amd-ryzen-7-7800x3d-4-2ghz-5-0ghz-turbo-8-cores-16-threads-am5-100-100000910wof_1680713298_g.jpg',
                specs: {
                    cpu: {
                        socket: 'AM5',
                        tdp: 120,
                        cores: 8,
                        threads: 16,
                        baseClock: 4.2,
                        boostClock: 5.0,
                        integratedGraphics: true
                    }
                },
                offers: [
                    {
                        id: 'cpu-002-kabum',
                        price: 2899,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/437094',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'cpu-002-pichau',
                        price: 2849,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/ryzen-7-7800x3d',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'cpu-003',
                name: 'Intel Core i5-14600K',
                partType: 'CPU',
                brand: 'Intel',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/505990/processador-intel-core-i5-14600k-14-geracao-3-5ghz-5-3ghz-turbo-14-cores-20-threads-lga1700-bx8071514600k_1697050630_g.jpg',
                specs: {
                    cpu: {
                        socket: 'LGA1700',
                        tdp: 125,
                        cores: 14,
                        threads: 20,
                        baseClock: 3.5,
                        boostClock: 5.3,
                        integratedGraphics: true
                    }
                },
                offers: [
                    {
                        id: 'cpu-003-kabum',
                        price: 1799,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/505990',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'cpu-003-pichau',
                        price: 1750,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/i5-14600k',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            }
        ]
    },
    {
        type: 'MOTHERBOARD',
        label: 'Placa-Mãe',
        icon: <Box size={24} color="#3d3846" />,
        category: 'ESSENTIAL',
        description: 'Conecta todos os componentes',
        components: [
            {
                id: 'mobo-001',
                name: 'ASUS TUF Gaming B650-PLUS',
                partType: 'MOTHERBOARD',
                brand: 'ASUS',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/385711/placa-mae-asus-tuf-gaming-b650-plus-wi-fi-amd-am5-atx-ddr5-90mb1d70-m0eay0_1663343556_g.jpg',
                specs: {
                    motherboard: {
                        socket: 'AM5',
                        chipset: 'B650',
                        ramType: 'DDR5',
                        ramSlots: 4,
                        maxRamCapacity: 128,
                        maxRamSpeed: 6400,
                        m2Slots: 2,
                        sataSlots: 4,
                        formFactor: 'ATX'
                    }
                },
                offers: [
                    {
                        id: 'mobo-001-kabum',
                        price: 1299,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/385711',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'mobo-001-pichau',
                        price: 1250,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/tuf-b650-plus',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'mobo-002',
                name: 'Gigabyte B760M AORUS ELITE',
                partType: 'MOTHERBOARD',
                brand: 'Gigabyte',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/432953/placa-mae-gigabyte-b760m-aorus-elite-intel-lga-1700-micro-atx-ddr5-b760m-aorus-elite_1677865846_g.jpg',
                specs: {
                    motherboard: {
                        socket: 'LGA1700',
                        chipset: 'B760',
                        ramType: 'DDR5',
                        ramSlots: 4,
                        maxRamCapacity: 128,
                        maxRamSpeed: 7600,
                        m2Slots: 3,
                        sataSlots: 4,
                        formFactor: 'MICRO_ATX'
                    }
                },
                offers: [
                    {
                        id: 'mobo-002-kabum',
                        price: 999,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/432953',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'mobo-002-pichau',
                        price: 949,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/b760m-elite',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            }
        ]
    },
    {
        type: 'RAM',
        label: 'Memória RAM',
        icon: <Zap size={24} color="#3d3846" />,
        category: 'ESSENTIAL',
        description: 'Memória de acesso rápido',
        components: [
            {
                id: 'ram-001',
                name: 'Kingston Fury Beast 32GB (2x16GB) DDR5 6000MHz',
                partType: 'RAM',
                brand: 'Kingston',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/385245/memoria-kingston-fury-beast-rgb-32gb-2x16gb-ddr5-6000mhz-cl36-preto-kf560c36bbeak2-32_1663083113_g.jpg',
                specs: {
                    ram: {
                        type: 'DDR5',
                        capacity: 32,
                        speed: 6000,
                        modules: 2,
                        latency: 'CL36',
                        voltage: 1.35
                    }
                },
                offers: [
                    {
                        id: 'ram-001-kabum',
                        price: 890,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/385245',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'ram-001-pichau',
                        price: 870,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/fury-32gb-6000',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'ram-002',
                name: 'Corsair Vengeance 16GB (2x8GB) DDR5 5600MHz',
                partType: 'RAM',
                brand: 'Corsair',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/sync_mirakl/384537/Mem-ria-RAM-Corsair-Vengeance-RGB-16GB-2x8GB-DDR5-5600MHz-CMH16GX5M2B5600C40_1718304668_g.jpg',
                specs: {
                    ram: {
                        type: 'DDR5',
                        capacity: 16,
                        speed: 5600,
                        modules: 2,
                        latency: 'CL40',
                        voltage: 1.25
                    }
                },
                offers: [
                    {
                        id: 'ram-002-kabum',
                        price: 520,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/384537',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'ram-002-pichau',
                        price: 499,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/vengeance-16gb',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            }
        ]
    },
    {
        type: 'GPU',
        label: 'Placa de Vídeo',
        icon: <Wallpaper size={24} color="#3d3846" />,
        category: 'ESSENTIAL',
        description: 'Processa gráficos e jogos',
        components: [
            {
                id: 'gpu-001',
                name: 'NVIDIA GeForce RTX 4060 8GB',
                partType: 'GPU',
                brand: 'NVIDIA',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/486451/placa-de-video-rtx-4060-ventus-2x-black-8g-oc-nvidia-geforce-8-gb-gddr6-dlss-ray-tracing-912-v516-001_1687284817_g.jpg',
                specs: {
                    gpu: {
                        chipset: 'RTX 4060',
                        vram: 8,
                        tdp: 115,
                        length: 199,
                        powerConnectors: ['8-pin'],
                        recommendedPSU: 550
                    }
                },
                offers: [
                    {
                        id: 'gpu-001-kabum',
                        price: 1850,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/486451',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'gpu-001-pichau',
                        price: 1799,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/rtx-4060',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'gpu-002',
                name: 'AMD Radeon RX 7600 8GB',
                partType: 'GPU',
                brand: 'AMD',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/468293/placa-de-video-asrock-amd-radeon-rx-7600-challenger-8gb-gddr6-fsr-ray-tracing-90-ga3rzz-00uanf_1684943327_g.jpg',
                specs: {
                    gpu: {
                        chipset: 'RX 7600',
                        vram: 8,
                        tdp: 165,
                        length: 204,
                        powerConnectors: ['8-pin'],
                        recommendedPSU: 550
                    }
                },
                offers: [
                    {
                        id: 'gpu-002-kabum',
                        price: 1699,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/468293',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'gpu-002-pichau',
                        price: 1650,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/rx-7600',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'gpu-003',
                name: 'NVIDIA GeForce RTX 4070 SUPER 12GB',
                partType: 'GPU',
                brand: 'NVIDIA',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/531890/placa-de-video-asus-dual-geforce-rtx-4070-super-oc-edition-12gb-gddr6x-dlss-3-ray-tracing-90yv0jc0-m0na00_1706124717_g.jpg',
                specs: {
                    gpu: {
                        chipset: 'RTX 4070 SUPER',
                        vram: 12,
                        tdp: 220,
                        length: 267,
                        powerConnectors: ['16-pin'],
                        recommendedPSU: 700
                    }
                },
                offers: [
                    {
                        id: 'gpu-003-kabum',
                        price: 4299,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/531890',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'gpu-003-pichau',
                        price: 4199,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/rtx-4070-super',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            }
        ]
    },
    {
        type: 'STORAGE',
        label: 'Armazenamento',
        icon: <HardDrive size={24} color="#3d3846" />,
        category: 'ESSENTIAL',
        description: 'SSD ou HD para guardar arquivos',
        components: [
            {
                id: 'storage-001',
                name: 'SSD Kingston NV2 1TB M.2 NVMe',
                partType: 'STORAGE',
                brand: 'Kingston',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/289668/ssd-kingston-nv2-1tb-m-2-2280-nvme-pcie-4-0-leitura-3500mb-s-e-gravacao-2100mb-s-snv2s-1000g_1659703310_g.jpg',
                specs: {
                    storage: {
                        type: 'NVME',
                        capacity: 1000,
                        readSpeed: 3500,
                        writeSpeed: 2100,
                        interface: 'PCIe 4.0',
                        formFactor: 'M.2 2280'
                    }
                },
                offers: [
                    {
                        id: 'storage-001-kabum',
                        price: 450,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/289668',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'storage-001-pichau',
                        price: 439,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/kingston-nv2-1tb',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'storage-002',
                name: 'SSD Samsung 980 PRO 2TB M.2 NVMe',
                partType: 'STORAGE',
                brand: 'Samsung',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/289429/ssd-samsung-980-pro-2tb-m-2-nvme-2280-leitura-7000mb-s-gravacao-5100mb-s-mz-v8p2t0b-am_1659544175_g.jpg',
                specs: {
                    storage: {
                        type: 'NVME',
                        capacity: 2000,
                        readSpeed: 7000,
                        writeSpeed: 5100,
                        interface: 'PCIe 4.0',
                        formFactor: 'M.2 2280'
                    }
                },
                offers: [
                    {
                        id: 'storage-002-kabum',
                        price: 899,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/289429',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'storage-002-pichau',
                        price: 870,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/980-pro-2tb',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            }
        ]
    },
    {
        type: 'PSU',
        label: 'Fonte',
        icon: <Power size={24} color="#3d3846" />,
        category: 'ESSENTIAL',
        description: 'Fornece energia para o sistema',
        components: [
            {
                id: 'psu-001',
                name: 'Corsair CV650 650W 80 Plus Bronze',
                partType: 'PSU',
                brand: 'Corsair',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/112596/fonte-corsair-650w-80-plus-bronze-cv650-cp-9020236-br_1598460793_g.jpg',
                specs: {
                    psu: {
                        wattage: 650,
                        certification: '80_PLUS_BRONZE',
                        modular: 'NON',
                        pcie8pin: 2,
                        pcie6pin: 2
                    }
                },
                offers: [
                    {
                        id: 'psu-001-kabum',
                        price: 420,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/112596',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'psu-001-pichau',
                        price: 399,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/cv650',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            },
            {
                id: 'psu-002',
                name: 'Corsair RM850x 850W 80 Plus Gold Modular',
                partType: 'PSU',
                brand: 'Corsair',
                imageUrl: 'https://images.kabum.com.br/produtos/fotos/sync_mirakl/468811/Fonte-Corsair-RM850x-SHIFT-850W-80-Plus-Gold-Full-Modular-CP-9020255-WW_1718304667_g.jpg',
                specs: {
                    psu: {
                        wattage: 850,
                        certification: '80_PLUS_GOLD',
                        modular: 'FULL',
                        pcie8pin: 4,
                        pcie6pin: 2
                    }
                },
                offers: [
                    {
                        id: 'psu-002-kabum',
                        price: 780,
                        store: 'Kabum',
                        url: 'https://kabum.com.br/produto/468811',
                        inStock: true,
                        lastUpdated: new Date()
                    },
                    {
                        id: 'psu-002-pichau',
                        price: 750,
                        store: 'Pichau',
                        url: 'https://pichau.com.br/rm850x',
                        inStock: true,
                        lastUpdated: new Date()
                    }
                ]
            }
        ]
    },
    // {
    //     type: 'CASE',
    //     label: 'Gabinete',
    //     icon: <Box size={24} color="#3d3846" />,
    //     category: 'ESSENTIAL',
    //     description: 'Abriga todos os componentes',
    //     components: [
    //         {
    //             id: 'case-001',
    //             name: 'Lian Li O11 Dynamic EVO',
    //             partType: 'CASE',
    //             brand: 'Lian Li',
    //             imageUrl: 'https://images.kabum.com.br/produtos/fotos/284691/gabinete-gamer-lian-li-o11-dynamic-evo-mid-tower-atx-vidro-temperado-branco-o11dew_1657046054_g.jpg',
    //             specs: {
    //                 case: {
    //                     formFactor: 'ATX',
    //                     maxGPULength: 420,
    //                     maxCoolerHeight: 167,
    //                     maxPSULength: 225,
    //                     includedFans: 0,
    //                     maxFans: 13
    //                 }
    //             },
    //             offers: [
    //                 {
    //                     id: 'case-001-kabum',
    //                     price: 950,
    //                     store: 'Kabum',
    //                     url: 'https://kabum.com.br/produto/284691',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 },
    //                 {
    //                     id: 'case-001-pichau',
    //                     price: 920,
    //                     store: 'Pichau',
    //                     url: 'https://pichau.com.br/o11-dynamic-evo',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 }
    //             ]
    //         },
    //         {
    //             id: 'case-002',
    //             name: 'NZXT H510 Flow',
    //             partType: 'CASE',
    //             brand: 'NZXT',
    //             imageUrl: 'https://images.kabum.com.br/produtos/fotos/368058/gabinete-gamer-nzxt-h510-flow-mid-tower-atx-lateral-em-vidro-preto-com-fundo-branco-ca-h52fw-01_1654716059_g.jpg',
    //             specs: {
    //                 case: {
    //                     formFactor: 'ATX',
    //                     maxGPULength: 381,
    //                     maxCoolerHeight: 165,
    //                     maxPSULength: 180,
    //                     includedFans: 2,
    //                     maxFans: 7
    //                 }
    //             },
    //             offers: [
    //                 {
    //                     id: 'case-002-kabum',
    //                     price: 599,
    //                     store: 'Kabum',
    //                     url: 'https://kabum.com.br/produto/368058',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 },
    //                 {
    //                     id: 'case-002-pichau',
    //                     price: 580,
    //                     store: 'Pichau',
    //                     url: 'https://pichau.com.br/h510-flow',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 }
    //             ]
    //         }
    //     ]
    // },
    // {
    //     type: 'COOLER',
    //     label: 'Cooler',
    //     icon: <Snowflake size={24} color="#3d3846" />,
    //     category: 'OPTIONAL',
    //     description: 'Resfriamento extra para CPU',
    //     components: [
    //         {
    //             id: 'cooler-001',
    //             name: 'DeepCool AK400',
    //             partType: 'COOLER',
    //             brand: 'DeepCool',
    //             imageUrl: 'https://images.kabum.com.br/produtos/fotos/289690/cooler-para-processador-deepcool-ak400-preto-r-ak400-bknnmn-g-1_1659704831_g.jpg',
    //             specs: {
    //                 cooler: {
    //                     type: 'AIR',
    //                     height: 155,
    //                     tdpRating: 220,
    //                     compatibleSockets: ['AM4', 'AM5', 'LGA1700', 'LGA1200']
    //                 }
    //             },
    //             offers: [
    //                 {
    //                     id: 'cooler-001-kabum',
    //                     price: 199,
    //                     store: 'Kabum',
    //                     url: 'https://kabum.com.br/produto/289690',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 },
    //                 {
    //                     id: 'cooler-001-pichau',
    //                     price: 189,
    //                     store: 'Pichau',
    //                     url: 'https://pichau.com.br/ak400',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 }
    //             ]
    //         },
    //         {
    //             id: 'cooler-002',
    //             name: 'Corsair iCUE H100i RGB Elite 240mm',
    //             partType: 'COOLER',
    //             brand: 'Corsair',
    //             imageUrl: 'https://images.kabum.com.br/produtos/fotos/377098/water-cooler-corsair-icue-h100i-rgb-elite-240mm-cw-9060065-ww_1658507951_g.jpg',
    //             specs: {
    //                 cooler: {
    //                     type: 'AIO',
    //                     radiatorSize: 240,
    //                     tdpRating: 250,
    //                     compatibleSockets: ['AM4', 'AM5', 'LGA1700', 'LGA1200']
    //                 }
    //             },
    //             offers: [
    //                 {
    //                     id: 'cooler-002-kabum',
    //                     price: 699,
    //                     store: 'Kabum',
    //                     url: 'https://kabum.com.br/produto/377098',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 },
    //                 {
    //                     id: 'cooler-002-pichau',
    //                     price: 680,
    //                     store: 'Pichau',
    //                     url: 'https://pichau.com.br/h100i-elite',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 }
    //             ]
    //         }
    //     ]
    // },
    // {
    //     type: 'MONITOR',
    //     label: 'Monitor',
    //     icon: <Monitor size={24} color="#3d3846" />,
    //     category: 'OPTIONAL',
    //     description: 'Tela para visualização',
    //     components: [
    //         {
    //             id: 'monitor-001',
    //             name: 'AOC Hero 27" 165Hz IPS QHD',
    //             partType: 'MONITOR',
    //             brand: 'AOC',
    //             imageUrl: 'https://images.kabum.com.br/produtos/fotos/400830/monitor-gamer-aoc-hero-27-165hz-1ms-ips-qhd-2560x1440-hdmi-displayport-ajuste-de-altura-freesync-premium-27g2z_1669913849_g.jpg',
    //             specs: {
    //                 monitor: {
    //                     size: 27,
    //                     resolution: '2560x1440',
    //                     refreshRate: 165,
    //                     panelType: 'IPS',
    //                     responseTime: 1,
    //                     adaptive: 'FREESYNC'
    //                 }
    //             },
    //             offers: [
    //                 {
    //                     id: 'monitor-001-kabum',
    //                     price: 1299,
    //                     store: 'Kabum',
    //                     url: 'https://kabum.com.br/produto/400830',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 },
    //                 {
    //                     id: 'monitor-001-pichau',
    //                     price: 1250,
    //                     store: 'Pichau',
    //                     url: 'https://pichau.com.br/aoc-hero-27',
    //                     inStock: true,
    //                     lastUpdated: new Date()
    //                 }
    //             ]
    //         }
    //     ]
    // },
    // {
    //     type: 'KEYBOARD',
    //     label: 'Teclado',
    //     icon: <Keyboard size={24} color="#3d3846" />,
    //     category: 'OPTIONAL',
    //     description: 'Periférico de entrada',
    //     components: []
    // },
    // {
    //     type: 'MOUSE',
    //     label: 'Mouse',
    //     icon: <Mouse size={24} color="#3d3846" />,
    //     category: 'OPTIONAL',
    //     description: 'Periférico de navegação',
    //     components: []
    // },
    // {
    //     type: 'HEADSET',
    //     label: 'Headset',
    //     icon: <Headset size={24} color="#3d3846" />,
    //     category: 'OPTIONAL',
    //     description: 'Áudio e comunicação',
    //     components: []
    // }
];

function App() {
    return (
        <>
            <nav className='p-4'>PCBuilderBR</nav>
            <div className="w-full h-full p-8 grid grid-cols-1 lg:grid-cols-[1fr_400px] gap-8">
                <main className="flex flex-col gap-6" >
                    <div className='mb-4'>
                        <h1 className='text-3xl font-extrabold italic'>SIMULADOR DE MONTAGEM</h1>
                        <p className='text-muted-foreground'>Confira seu setup com validação de montagem em tempo real</p>
                    </div>
                    <div className="flex flex-col gap-6">
                        {PARTS_DATA.map((part: PartInfo) => <PartCard part={part} />)}
                    </div>
                </main>
                <aside className="bg-amber-200 ">
                    <Summary />
                </aside>
            </ div >
        </>
    )
}

export default App
