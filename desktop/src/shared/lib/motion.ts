import type { Transition } from "framer-motion";

export const spring: Record<string, Transition> = {
  panel: { type: "spring", stiffness: 380, damping: 35 },
  palette: { type: "spring", stiffness: 450, damping: 28 },
  tokenStream: { type: "tween", duration: 0.08, ease: "linear" },
};
