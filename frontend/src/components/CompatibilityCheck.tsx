import { CircleAlert, CircleCheck, CircleX } from "lucide-react";
import type { CompatibilityError } from "../types/types";

interface CompatibilityCheckProps {
    compatibilityError: CompatibilityError;
}

export function CompatibilityCheck({ compatibilityError }: CompatibilityCheckProps) {
    return (
        <div className="flex items-center gap-3 p-3 rounded-xl bg-green-500/5 border border-green-500/10 transition-colors hover:bg-green-500/10">
            {compatibilityError.type == "ERROR" ? <CircleX color="#ff0328" size={40} /> : <CircleAlert color="#ffaf03" size={40} />}
            <p className="text-xs font-bold uppercase tracking-tight">{compatibilityError.message}</p>
        </div>
    )
}
