import type { ComponentOffer } from "../types/types";

interface OfferCardProps {
    offer: ComponentOffer;
    index: number;
    onSelect: (offer: ComponentOffer) => void;
}

export function OfferCard({ offer, index, onSelect }: OfferCardProps) {
    const isCheapest = index === 0;
    return (
        <div className={`flex items-center justify-between p-3 rounded-xl border ${isCheapest ? 'bg-primary/5 border-primary/20 shadow-sm' : 'bg-background border-border/50'}`}>
            <div className="flex items-center gap-3">
                <div className="h-8 w-8 rounded bg-muted flex items-center justify-center font-bold text-[10px]">
                    {offer.store[0]}
                </div>
                <span className={`font-bold text-sm ${isCheapest ? 'text-primary' : 'text-foreground'}`}>
                    {offer.store}
                </span>
            </div>
            <div className="flex items-center gap-2">
                <span className={`font-black tracking-tight ${isCheapest ? 'text-primary text-lg' : 'text-muted-foreground text-sm'}`}>
                    R$ {offer.price.toLocaleString('pt-BR')}
                </span>
                <a
                    href={offer.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center justify-center h-8 px-3 font-bold text-[10px] uppercase rounded-md border border-border bg-background hover:bg-muted transition-colors"
                >
                    Ver
                </a>
                <button
                    onClick={() => onSelect(offer)}
                    className={`inline-flex items-center justify-center h-8 px-3 font-bold text-[10px] uppercase rounded-md border transition-colors ${isCheapest ? 'bg-primary text-primary-foreground border-primary-border hover:bg-primary/90' : 'bg-background border-border hover:bg-muted'}`}
                >
                    Selecionar
                </button>
            </div>
        </div>
    );
}
