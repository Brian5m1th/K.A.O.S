// ---- Barrel de compatibilidade retroativa ----
// Servicos migrados para infrastructure/
export { kaosFetch, setAccessTokenProvider, setServerUrlProvider } from "@/infrastructure/http";
export { isTauri, invokeIpc, listenIpc } from "@/infrastructure/ipc";
export { TauriStoreService } from "@/infrastructure/storage";