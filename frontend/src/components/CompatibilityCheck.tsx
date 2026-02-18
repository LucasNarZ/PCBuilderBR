import { CircleAlert, CircleCheck, CircleX } from "lucide-react";

export function CompatibilityCheck({ level, message }: Check) {
    return (
        <div className="flex items-center gap-3 p-3 rounded-xl bg-green-500/5 border border-green-500/10 transition-colors hover:bg-green-500/10">
            {level == "CORRECT" ? <CircleCheck color="#00c950" /> : level == "ERROR" ? <CircleX color="#ff0328" /> : <CircleAlert color="#ffaf03" />}
            <p className="text-xs font-bold uppercase tracking-tight">{message}</p>
        </div>
    )
}
