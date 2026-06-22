import type { Transition, Variants } from "framer-motion";

export const spring: Record<string, Transition> = {
  panel: { type: "spring", stiffness: 380, damping: 35 },
  palette: { type: "spring", stiffness: 450, damping: 28 },
  tokenStream: { type: "tween", duration: 0.08, ease: "linear" },
};

export const hover = {
  whileHover: { scale: 1.02 },
  whileTap: { scale: 0.98 },
};

export const fadeSlide: Variants = {
  initial: { opacity: 0, y: 8 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -4 },
};

export const fade: Variants = {
  initial: { opacity: 0 },
  animate: { opacity: 1 },
  exit: { opacity: 0 },
};
