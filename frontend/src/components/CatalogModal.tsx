import { X } from "lucide-react";
import type { Component, PartInfo } from "../types/types";
import { SearchBar } from "./SearchBar";
import { ComponentCard } from "./ComponentCard";
import { useEffect, useState } from "react";
import apiClient from "../lib/apiClient";

interface CatalogModalProps {
    part: PartInfo;
    onClose: () => void;
}

export function CatalogModal({ part, onClose }: CatalogModalProps) {
    const [components, setComponents] = useState<Component[]>([]);
    const [loading, setLoading] = useState(true);

    const [searchTerm, setSearchTerm] = useState<string>("")

    useEffect(() => {
        (async () => {
            try {
                setLoading(true)
                const { data } = await apiClient.get<Component[]>("/components", {
                    params: {
                        part_type: part.type, search: searchTerm.trim() || undefined
                    }
                })
                setComponents(data)
            } catch (err) {
                console.error(err)
            } finally {
                setLoading(false)
            }
        })()
    }, [part.type, searchTerm]);

    return (
        <>
            <div className="fixed inset-0 bg-black/50 z-40" />
            <div className="fixed left-[50%] top-[50%] z-50 p-8 w-full translate-x-[-50%] translate-y-[-50%] gap-4 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg max-w-3xl border-2 bg-card/95 backdrop-blur-xl max-h-[90vh] flex flex-col overflow-y-auto">
                <div>
                    <h2 className="text-2xl font-black italic uppercase tracking-tighter">Catálogo de {part.label}</h2>
                    <p className="text-sm font-medium text-muted-foreground">Compare preços entre lojas nacionais e selecione o melhor hardware.</p>
                </div>
                <SearchBar partName={part.label} onSearch={(term) => setSearchTerm(term)} />
                <div className="flex flex-col gap-5 overflow-y-auto max-h-96">
                    {loading ? (
                        <p className="text-sm text-muted-foreground text-center py-8">Carregando componentes...</p>
                    ) : components.map((component: Component) => (
                        <ComponentCard key={component.id} component={component} icon={part.icon} onClose={onClose} />
                    ))}
                </div>
                <button className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground" onClick={onClose}>
                    <X />
                </button>
            </div>
        </>
    );
}
