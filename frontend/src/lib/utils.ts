import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatNumber(num: number): string {
  if (num >= 1000000) return (num / 1000000).toFixed(1) + "M"
  if (num >= 1000) return (num / 1000).toFixed(1) + "K"
  return num.toString()
}

export function getScoreColor(score: number): string {
  if (score >= 0.8) return "text-emerald-400"
  if (score >= 0.6) return "text-cyan-400"
  if (score >= 0.4) return "text-amber-400"
  return "text-red-400"
}

export function getStatusColor(status: string): string {
  switch (status) {
    case "active": case "running": case "completed": case "hot": case "viral": return "text-emerald-400"
    case "growing": case "rising": case "pending": return "text-cyan-400"
    case "paused": case "stable": return "text-amber-400"
    case "declining": case "failed": return "text-red-400"
    default: return "text-slate-400"
  }
}

export function getGlowClass(score: number): string {
  if (score >= 0.8) return "shadow-emerald-500/20 shadow-lg"
  if (score >= 0.6) return "shadow-cyan-500/20 shadow-lg"
  if (score >= 0.4) return "shadow-amber-500/20 shadow-lg"
  return "shadow-red-500/20 shadow-lg"
}
