import { Cpu, Plus } from "lucide-react";
import type { PartInfo } from "../types"

interface PartCardProps {
    part: PartInfo;
}

export function PartCard({ part }: PartCardProps) {
    return (
        <div className="flex h-24 border-2 rounded-xl p-5 items-center bg-card text-card-foreground shadow overflow-hidden transition-all duration-300 border-border/40 hover:border-primary/30 hover:bg-muted/30">
            <div className="bg-border p-3 mr-5 rounded-xl">
                {part.icon}
            </div>
            <div className="flex flex-col">
                <div className="flex items-center gap-3">
                    <p className="font-bold text-muted-foreground/80 font-xs uppercase">{part.label}</p>
                    <div className="whitespace-nowrap inline-flex items-center rounded-md border py-0.5 transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 hover-elevate border-transparent bg-secondary text-secondary-foreground text-[10px] h-4 px-1.5 font-black uppercase tracking-tighter">{part.category === "ESSENTIAL" ? "Obrigatório" : "Opcional"}</div>
                </div>
                <div className="text-muted-foreground/60 font-medium italic">Nenhum item selecionado na categoria {part.label}</div>

            </div>
            <button className="ml-auto mr-5 shrink-0 p-2 w-32 inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 hover-elevate active-elevate-2 bg-primary text-primary-foreground border border-primary-border min-h-10 h-12 px-6 font-black tracking-tighter rounded-xl group-hover:scale-105 transition-transform active:scale-95 hover:scale-105 shadow-lg shadow-primary/20">
                <Plus color="#ffffff" size={24} />
                <p>ADICIONAR</p>
            </button>

        </div >
    )
}
