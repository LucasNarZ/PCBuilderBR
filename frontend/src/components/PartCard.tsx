import { Plus, Trash2 } from "lucide-react";
import type { PartInfo } from "../types/types"
import { useContext } from "react";
import { BuildContext } from "../context/buildContext";

interface PartCardProps {
    part: PartInfo;
    onSelect: (part: PartInfo) => void;
}

export function PartCard({ part, onSelect }: PartCardProps) {
    const [build, setBuild] = useContext(BuildContext)
    const key = part.type.toLowerCase() as keyof typeof build
    const selectedComponent = build[key]

    const handleRemove = () => {
        setBuild(prev => {
            const next = { ...prev }
            delete next[key]
            return next
        })
    }

    return (
        <div className={`flex flex-col sm:flex-row border-2 rounded-xl p-3 sm:p-5 sm:items-center bg-card text-card-foreground shadow transition-all duration-300 gap-3 sm:gap-0 ${selectedComponent ? 'border-primary/50 bg-primary/5 shadow-[0_0_15px_-5px_rgba(34,197,94,0.3)]' : 'border-border/40 hover:border-primary/30 hover:bg-muted/30'}`}>
            <div className="flex items-center gap-3 flex-1 min-w-0">
                <div className={`p-2 sm:p-3 rounded-lg sm:rounded-xl shrink-0 transition-all duration-300 ${selectedComponent ? 'bg-primary text-white scale-110 shadow-lg' : 'bg-border text-muted-foreground'}`}>
                    <div className="w-5 h-5 sm:w-6 sm:h-6 flex items-center justify-center [&>svg]:w-full [&>svg]:h-full [&>svg]:text-inherit">
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

                    {selectedComponent ? (
                        <div className="flex flex-col">
                            <h3 className="font-black text-base sm:text-xl truncate tracking-tight">{selectedComponent.name}</h3>
                            <div className="flex items-center gap-3 mt-1">
                                <span className="text-xs font-mono text-muted-foreground uppercase">{selectedComponent.brand}</span>
                                <div className="h-1 w-1 rounded-full bg-border" />
                                <div className="flex items-center gap-1.5">
                                    <span className="text-sm font-black text-primary">
                                        R$ {selectedComponent.offer.price.toLocaleString('pt-BR')}
                                    </span>
                                    <a href={selectedComponent.offer.url}
                                        target="_blank"
                                        rel="noopener noreferrer" className="text-[9px] border border-primary/20 text-primary font-bold px-1 rounded">
                                        {selectedComponent.offer.store} ↗
                                    </a>
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div className="text-muted-foreground/60 font-medium italic text-xs sm:text-sm leading-tight">
                            {`Nenhum item selecionado na categoria ${part.label.toLowerCase()}`}
                        </div>
                    )}
                </div>
            </div>

            {
                selectedComponent ? (
                    <button
                        className="w-full sm:w-auto sm:ml-5 shrink-0 inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm h-10 sm:h-12 px-4 sm:px-6 rounded-lg sm:rounded-xl transition-all text-muted-foreground hover:text-destructive hover:bg-destructive/10"
                        onClick={handleRemove}
                    >
                        <Trash2 size={18} />
                    </button>
                ) : (
                    <button
                        className="w-full sm:w-auto sm:ml-5 shrink-0 inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground border border-primary-border h-10 sm:h-12 px-4 sm:px-6 font-black tracking-tighter rounded-lg sm:rounded-xl transition-transform active:scale-95 hover:scale-105 shadow-lg shadow-primary/20"
                        onClick={() => onSelect(part)}
                    >
                        <Plus size={18} className="sm:w-6 sm:h-6" />
                        <span className="text-xs sm:text-sm">ADICIONAR</span>
                    </button>
                )
            }
        </div >
    )
}
