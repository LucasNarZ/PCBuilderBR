import { CircleCheck, ExternalLink } from "lucide-react";
import { CompatibilityCheck } from "./CompatibilityCheck";

export function Summary() {
    const checks: Check[] = [
        {
            level: "CORRECT",
            message: "nothing wrong"
        }
    ]
    return (
        <div className="flex flex-col p-7 rounded-xl bg-card text-card-foreground sticky top-24 border-2 shadow-[0_10px_40px_-15px_rgba(0,0,0,0.1)] overflow-hidden">
            <div className="flex justify-between">
                <h2 className="font-extrabold italic text-2xl">SUMÁRIO GERAL</h2>
                <div className="whitespace-nowrap inline-flex items-center border px-2.5 py-0.5 text-xs transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 hover-elevate border-transparent text-primary-foreground shadow-xs bg-green-500 hover:bg-green-500 font-black italic tracking-tighter gap-1 rounded-sm"><CircleCheck size={16} /> OK</div>
            </div>
            <p className="font-bold text-xs uppercase tracking-widest text-muted-foreground/60">Análise de Performance & Custo</p>
            <div className="p-6 bg-muted/40 rounded-2xl border-2 border-border/50 flex flex-col items-center justify-center text-center gap-1 group transition-colors hover:bg-muted/60 mt-5">
                <h2 className="text-xs font-black uppercase tracking-[0.2em] text-muted-foreground/70">INVESTIMENTO TOTAL</h2>
                <h1 className="text-5xl font-black text-primary tracking-tighter italic">R$20.00</h1>
            </div>
            <div className="my-8">
                {checks.map((check: Check) => <CompatibilityCheck {...check} />)}
            </div>
            <button className="inline-flex items-center justify-center gap-2 whitespace-nowrap focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 hover-elevate active-elevate-2 bg-primary text-primary-foreground border border-primary-border min-h-9 px-4 py-2 w-full h-16 text-lg font-black uppercase italic tracking-tighter rounded-2xl shadow-xl shadow-primary/20 hover:scale-[1.02] active:scale-[0.98] transition-all">
                COMPRAR SETUP COMPLETO
                <ExternalLink />
            </button>

        </div>
    )
}
