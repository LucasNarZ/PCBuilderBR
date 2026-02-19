import { Search } from "lucide-react";

interface SearchBarProps {
    partName: string;
}

export function SearchBar({ partName }: SearchBarProps) {
    return (
        <div className="relative">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground transition-colors group-focus-within:text-primary" />
            <input type="text" className="flex w-full rounded-md border-input px-3 py-1 shadow-sm file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm pl-12 h-14 bg-background border-2 text-lg font-bold placeholder:font-medium transition-all focus-visible:ring-offset-0 focus-visible:ring-primary/20" placeholder={`O que você esta procurando em ${partName}?`} />
        </div>
    )
}
