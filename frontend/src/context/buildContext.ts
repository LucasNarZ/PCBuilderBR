import { createContext } from "react";
import type { Build } from "../types/types";

export const BuildContext = createContext<
  [
    Partial<Build["components"]>,
    React.Dispatch<React.SetStateAction<Partial<Build["components"]>>>,
  ]
>([{}, () => {}]);
