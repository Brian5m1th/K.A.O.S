// ---- Barrel de compatibilidade retroativa ----
// As stores foram migradas para application/stores/
// Mantido para backward compatibility durante a transicao.
// Novos imports devem usar @/application diretamente.
export {
  useAgentStore, useAuthStore, useChatStore,
  useConversationStore, useSystemStore,
  useThemeStore, useUpdateStore, useUIStore
} from "@/application/stores";
export type {
  AgentStatus, AgentConfig, AgentInstance,
  ConversationSession
} from "@/application/stores";