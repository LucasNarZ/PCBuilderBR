import type { Component } from "../types/types";

interface ComponentCardProps {
    component: Component;
    icon: any;
}

function getMainSpec(component: Component): string | null {
    const { partType, specs } = component;
    switch (partType) {
        case 'CPU':
            return specs.cpu ? `${specs.cpu.cores}C/${specs.cpu.threads}T · ${specs.cpu.socket}` : null;
        case 'MOTHERBOARD':
            return specs.motherboard ? `${specs.motherboard.socket} · ${specs.motherboard.chipset}` : null;
        case 'RAM':
            return specs.ram ? `${specs.ram.capacity}GB ${specs.ram.type} ${specs.ram.speed}MHz` : null;
        case 'GPU':
            return specs.gpu ? `${specs.gpu.vram}GB VRAM · ${specs.gpu.chipset}` : null;
        case 'STORAGE':
            return specs.storage ? `${specs.storage.capacity}GB ${specs.storage.type}` : null;
        case 'PSU':
            return specs.psu ? `${specs.psu.wattage}W · ${specs.psu.certification.replace(/_/g, ' ')}` : null;
        case 'CASE':
            return specs.case ? `${specs.case.formFactor} · GPU até ${specs.case.maxGPULength}mm` : null;
        case 'COOLER':
            return specs.cooler ? `${specs.cooler.type} · ${specs.cooler.tdpRating}W TDP` : null;
        case 'MONITOR':
            return specs.monitor ? `${specs.monitor.size}" ${specs.monitor.resolution} ${specs.monitor.refreshRate}Hz` : null;
        case 'KEYBOARD':
        case 'MOUSE':
        case 'HEADSET':
            return component.brand;
        default:
            return null;
    }
}

export function ComponentCard({ component, icon }: ComponentCardProps) {
    const mainSpec = getMainSpec(component);
    const lowestPrice = component.offers.length > 0
        ? Math.min(...component.offers.map(o => o.price))
        : null;

    return (
        <div className="p-4 bg-white rounded-xl">
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-4">
                    <div className="h-12 w-12 rounded-lg bg-muted flex items-center justify-center group-hover/item:bg-primary group-hover/item:text-primary-foreground transition-colors">
                        {icon}
                    </div>
                    <div>
                        <p className="font-black text-lg tracking-tight leading-none mb-1">{component.name}</p>
                        {mainSpec && (
                            <div className="whitespace-nowrap inline-flex items-center rounded-md px-2.5 transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 hover-elevate text-foreground border [border-color:var(--badge-outline)] text-[10px] font-bold uppercase py-0">
                                {mainSpec}
                            </div>
                        )}
                    </div>
                </div>
                <div className="text-right">
                    <p className="text-[10px] font-bold text-muted-foreground uppercase mb-1">Menor Preço</p>
                    <p className="font-black text-2xl text-primary leading-none tracking-tighter italic">
                        {lowestPrice != null ? `R$ ${lowestPrice.toLocaleString('pt-BR')}` : '—'}
                    </p>
                </div>
            </div>
            <button className="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 hover-elevate active-elevate-2 bg-primary text-primary-foreground border border-primary-border min-h-9 px-4 py-2 w-full mt-4 h-12 font-black uppercase italic tracking-tighter">
                SELECIONAR PARA BUILD
            </button>
        </div>
    );
}
