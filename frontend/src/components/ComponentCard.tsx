import { ChevronDown, Store, Zap } from "lucide-react";
import { useContext, useState } from "react";
import type { Component, ComponentOffer } from "../types/types";
import { BuildContext } from "../context/buildContext";
import { OfferCard } from "./OfferCard";

interface ComponentCardProps {
    component: Component;
    icon: any;
    onClose: () => void;
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

export function ComponentCard({ component, icon, onClose }: ComponentCardProps) {
    const mainSpec = getMainSpec(component);
    const [offersOpen, setOffersOpen] = useState(false);
    const sortedOffers = [...component.offers].sort((a, b) => a.price - b.price);
    const cheapestOffer = sortedOffers[0];

    const [build, setBuild] = useContext(BuildContext)

    const selectOffer = (offer: ComponentOffer) => {
        const { offers, ...componentWithoutOffers } = component
        const key = component.partType.toLowerCase() as keyof typeof build
        setBuild(prev => ({
            ...prev,
            [key]: {
                ...componentWithoutOffers,
                offer
            }
        }))
        onClose();
    }

    return (
        <div className="p-4 bg-card rounded-xl border-2 border-border/40 hover:border-primary/50 transition-all group/item">
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-4">
                    <div className="h-12 w-12 rounded-lg bg-muted flex items-center justify-center group-hover/item:bg-primary group-hover/item:text-primary-foreground transition-colors">
                        {icon}
                    </div>
                    <div>
                        <p className="font-black text-lg tracking-tight leading-none mb-1">{component.name}</p>
                        {mainSpec && (
                            <div className="whitespace-nowrap inline-flex items-center rounded-md px-2.5 border text-[10px] font-bold uppercase py-0">
                                {mainSpec}
                            </div>
                        )}
                    </div>
                </div>
                <div className="text-right">
                    <p className="text-[10px] font-bold text-muted-foreground uppercase mb-1">Menor Preço</p>
                    <p className="font-black text-2xl text-primary leading-none tracking-tighter italic">
                        {cheapestOffer ? `R$ ${cheapestOffer.price.toLocaleString('pt-BR')}` : '—'}
                    </p>
                </div>
            </div>

            <button
                className="w-full flex items-center justify-between py-2 px-2 hover:bg-muted/50 rounded-lg text-xs font-bold uppercase tracking-widest text-muted-foreground transition-colors"
                onClick={() => setOffersOpen(prev => !prev)}
            >
                <div className="flex items-center gap-2">
                    <Store className="h-3 w-3" />
                    Disponível em {component.offers.length} {component.offers.length === 1 ? 'loja' : 'lojas'}
                </div>
                <ChevronDown className={`h-3 w-3 transition-transform duration-200 ${offersOpen ? 'rotate-180' : ''}`} />
            </button>

            {offersOpen && (
                <div className="mt-2 space-y-2">
                    {sortedOffers.map((offer, idx) => (
                        <OfferCard key={offer.store} offer={offer} index={idx} onSelect={selectOffer} />
                    ))}
                </div>
            )}

            <button
                className="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground border border-primary-border hover-elevate active-elevate-2 px-4 py-2 w-full mt-4 h-12 font-black uppercase italic tracking-tighter transition-all"
                onClick={() => selectOffer(cheapestOffer)}
            >
                <Zap size={16} className="stroke-3" />
                ESCOLHER MELHOR OFERTA
            </button>
        </div>
    );
}
