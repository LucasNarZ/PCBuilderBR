import { Box, Cpu, HardDrive, Power, Wallpaper, Zap } from 'lucide-react';
import { PartCard } from './components/PartCard';
import { Summary } from './components/Summary';
import type { Build, CompatibilityError, PartInfo } from './types/types.d';
import { useEffect, useState } from 'react';
import { CatalogModal } from './components/CatalogModal';
import { BuildContext } from './context/buildContext';
import apiClient from './lib/apiClient';

export const PARTS_DATA: PartInfo[] = [
    {
        type: 'CPU',
        label: 'Processador',
        icon: <Cpu size={24} />,
        category: 'ESSENTIAL',
        description: 'O cérebro do computador',
    },
    {
        type: 'MOTHERBOARD',
        label: 'Placa-Mãe',
        icon: <Box size={24} />,
        category: 'ESSENTIAL',
        description: 'Conecta todos os componentes',
    },
    {
        type: 'RAM',
        label: 'Memória RAM',
        icon: <Zap size={24} />,
        category: 'ESSENTIAL',
        description: 'Memória de acesso rápido',
    },
    {
        type: 'GPU',
        label: 'Placa de Vídeo',
        icon: <Wallpaper size={24} />,
        category: 'ESSENTIAL',
        description: 'Processa gráficos e jogos',
    },
    {
        type: 'STORAGE',
        label: 'Armazenamento',
        icon: <HardDrive size={24} />,
        category: 'ESSENTIAL',
        description: 'SSD ou HD para guardar arquivos',
    },
    {
        type: 'PSU',
        label: 'Fonte',
        icon: <Power size={24} />,
        category: 'ESSENTIAL',
        description: 'Fornece energia para o sistema',
    },
    {
        type: 'CASE',
        label: 'Gabinete',
        icon: <Box size={24} />,
        category: 'ESSENTIAL',
        description: 'Abriga todos os componentes',
    },
];

function App() {
    const [selectedPart, setSelectedPart] = useState<PartInfo | null>(null)
    const [build, setBuild] = useState<Partial<Build['components']>>({})
    const [compatibilityErrors, setCompatibilityErrors] = useState<CompatibilityError[]>([])

    useEffect(() => {
        (async () => {
            const { data } = await apiClient.post("/compatibility/", build)
            console.log(data)

            setCompatibilityErrors([...data.errors, ...data.warnings])
        })()
    }, [build])

    return (
        <>
            <BuildContext value={[build, setBuild]}>
                <nav className="fixed top-0 left-0 right-0 z-30 bg-background/95 backdrop-blur-md border-b">
                    <div className="container mx-auto px-4 md:px-8 py-4 flex items-center justify-between max-w-screen-2xl">
                        <div className="flex items-center gap-3">
                            <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
                                <Cpu size={20} color="#ffffff" />
                            </div>
                            <div>
                                <h1 className="text-lg font-bold leading-none">PC Builder BR</h1>
                                <p className="hidden sm:block text-[10px] text-muted-foreground font-medium">Monte seu PC ideal</p>
                            </div>
                        </div>
                    </div>
                </nav>
                <div className="w-full h-full p-8 pt-24 grid grid-cols-1 lg:grid-cols-[1fr_400px] gap-8 container px-4 md:px-8 py-8 mx-auto max-w-screen-2xl">
                    <main className="flex flex-col gap-6" >
                        <div className='mb-4'>
                            <div className='flex gap-2'>
                                <div className="h-8 w-2 bg-primary rounded-full"></div>
                                <p className='text-3xl italic font-extrabold'>SIMULADOR DE MONTAGEM</p>
                            </div>
                            <p className='text-muted-foreground font-medium'>Confira seu setup com validação de montagem em tempo real</p>
                        </div>
                        <div className="flex flex-col gap-6">
                            {PARTS_DATA.map((part: PartInfo) => <PartCard part={part} onSelect={(part: PartInfo) => setSelectedPart(part)} />)}
                        </div>
                    </main>
                    <aside className="space-y-6">
                        <Summary compatibilityErrors={compatibilityErrors} />
                    </aside>
                </div>
                {selectedPart && <CatalogModal part={selectedPart} onClose={() => setSelectedPart(null)} />}
            </BuildContext >
        </>
    )
}

export default App
