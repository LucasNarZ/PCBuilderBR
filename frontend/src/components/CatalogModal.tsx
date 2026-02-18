import { X } from "lucide-react";
import type { PartInfo } from "../types/types";

interface CatalogModalProps {
    part: PartInfo;
    onClose: () => void;
}

export function CatalogModal({ part, onClose }: CatalogModalProps) {
    return (
        <div className="fixed left-[50%] top-[50%] z-50 w-full translate-x-[-50%] translate-y-[-50%] gap-4 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg max-w-3xl border-2 bg-card/95 backdrop-blur-xl max-h-[90vh] flex flex-col p-0 overflow-hidden">
            <div>
                <h2>Catálogo de {part.label}</h2>
                <p>Compare preços entre lojas nacionais e selecione o melhor hardware.</p>
            </div>
            <button className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground" onClick={onClose}>
                <X />
            </button>
        </div>
    )

}
