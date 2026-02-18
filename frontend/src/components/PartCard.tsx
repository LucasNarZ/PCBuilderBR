import { Plus } from "lucide-react";
import type { PartInfo } from "../types/types"

interface PartCardProps {
    part: PartInfo;
    onSelect: (part: PartInfo) => void;
}

export function PartCard({ part, onSelect }: PartCardProps) {
    return (
        <div className="flex flex-col sm:flex-row border-2 rounded-xl p-3 sm:p-5 sm:items-center bg-card text-card-foreground shadow transition-all duration-300 border-border/40 hover:border-primary/30 hover:bg-muted/30 gap-3 sm:gap-0">

            <div className="flex items-center gap-3 flex-1 min-w-0">
                <div className="bg-border p-2 sm:p-3 rounded-lg sm:rounded-xl shrink-0">
                    <div className="w-5 h-5 sm:w-6 sm:h-6 flex items-center justify-center">
                        {part.icon}
                    </div>
                </div>

                <div className="flex flex-col gap-1 min-w-0 flex-1">
                    <div className="flex items-center gap-2 flex-wrap">
                        <p className="font-bold text-muted-foreground/80 text-xs sm:text-sm uppercase">
                            {part.label}
                        </p>
                        <div className="whitespace-nowrap inline-flex items-center rounded-md border py-0.5 px-1.5 bg-secondary text-secondary-foreground text-[9px] sm:text-[10px] h-4 font-black uppercase tracking-tighter">
                            {part.category === "ESSENTIAL" ? "Obrigatório" : "Opcional"}
                        </div>
                    </div>

                    <div className="text-muted-foreground/60 font-medium italic text-xs sm:text-sm leading-tight">
                        Nenhum item selecionado na categoria {part.label.toLowerCase()}
                    </div>
                </div>
            </div>

            <button className="w-full sm:w-auto sm:ml-5 shrink-0 inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground border border-primary-border h-10 sm:h-12 px-4 sm:px-6 font-black tracking-tighter rounded-lg sm:rounded-xl transition-transform active:scale-95 hover:scale-105 shadow-lg shadow-primary/20" onClick={() => onSelect(part)}>
                <Plus size={18} className="sm:w-6 sm:h-6" />
                <span className="text-xs sm:text-sm">ADICIONAR</span>
            </button>
        </div>
    )
}
