import { ChevronDown, Store, Zap } from "lucide-react";
import { useContext, useState } from "react";
import type { Component, ComponentOffer, CPUSpecs, MotherboardSpecs, RAMSpecs, GPUSpecs, StorageSpecs, PSUSpecs, CaseSpecs, CoolerSpecs, MonitorSpecs } from "../types/types";
import { BuildContext } from "../context/buildContext";
import { OfferCard } from "./OfferCard";
import apiClient from "../lib/apiClient";

interface ComponentCardProps {
    component: Component;
    icon: any;
    onClose: () => void;
}

function getMainSpec(component: Component): string | null {
    const { partType, specs } = component;
    switch (partType) {
        case 'CPU': {
            const s = specs as CPUSpecs;
            return `${s.cores}C/${s.threads}T · ${s.socket}`;
        }
        case 'MOTHERBOARD': {
            const s = specs as MotherboardSpecs;
            return `${s.socket} · ${s.chipset}`;
        }
        case 'RAM': {
            const s = specs as RAMSpecs;
            return `${s.capacity}GB ${s.type} ${s.speed}MHz`;
        }
        case 'GPU': {
            const s = specs as GPUSpecs;
            return `${s.vram}GB VRAM · ${s.chipset}`;
        }
        case 'STORAGE': {
            const s = specs as StorageSpecs;
            return `${s.capacity}GB ${s.type}`;
        }
        case 'PSU': {
            const s = specs as PSUSpecs;
            return `${s.wattage}W · ${s.certification.replace(/_/g, ' ')}`;
        }
        case 'CASE': {
            const s = specs as CaseSpecs;
            return `${s.formFactor} · GPU até ${s.maxGPULength}mm`;
        }
        case 'COOLER': {
            const s = specs as CoolerSpecs;
            return `${s.type} · ${s.tdpRating}W TDP`;
        }
        case 'MONITOR': {
            const s = specs as MonitorSpecs;
            return `${s.size}" ${s.resolution} ${s.refreshRate}Hz`;
        }
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
    const [offers, setOffers] = useState<ComponentOffer[]>([]);
    const [loadingOffers, setLoadingOffers] = useState(false);
    const [build, setBuild] = useContext(BuildContext);

    const toggleOffers = async () => {
        if (!offersOpen && offers.length === 0) {
            setLoadingOffers(true);
            const { data } = await apiClient.get(`/components/${component.name}/offers/`);
            setOffers(data);
            setLoadingOffers(false);
        }
        setOffersOpen(prev => !prev);
    };

    const selectOffer = (offer: ComponentOffer) => {
        const key = component.partType.toLowerCase() as keyof typeof build;
        setBuild(prev => ({
            ...prev,
            [key]: { ...component, offer }
        }));
        onClose();
    };

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
                        {component.bestOffer?.price ? `R$ ${component.bestOffer.price.toLocaleString('pt-BR')}` : '—'}
                    </p>
                </div>
            </div>
            <button
                className="w-full flex items-center justify-between py-2 px-2 hover:bg-muted/50 rounded-lg text-xs font-bold uppercase tracking-widest text-muted-foreground transition-colors"
                onClick={toggleOffers}
            >
                <div className="flex items-center gap-2">
                    <Store className="h-3 w-3" />
                    {loadingOffers
                        ? 'Carregando ofertas...'
                        : `Disponível em ${component.storeCount} ${offers.length === 1 ? 'loja' : 'lojas'}`
                    }
                </div>
                <ChevronDown className={`h-3 w-3 transition-transform duration-200 ${offersOpen ? 'rotate-180' : ''}`} />
            </button>
            {offersOpen && (
                <div className="mt-2 space-y-2">
                    {offers.map((offer) => (
                        <OfferCard key={offer.store} offer={offer} index={0} onSelect={selectOffer} />
                    ))}
                </div>
            )}
            <button
                className="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground border border-primary-border hover-elevate active-elevate-2 px-4 py-2 w-full mt-4 h-12 font-black uppercase italic tracking-tighter transition-all"
                onClick={() => selectOffer(component.bestOffer)}
                disabled={!component.bestOffer}
            >
                <Zap size={16} className="stroke-3" />
                ESCOLHER MELHOR OFERTA
            </button>
        </div>
    );
}
