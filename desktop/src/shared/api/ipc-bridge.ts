/**
 * IPC Bridge — thin re-export of the canonical implementation.
 *
 * This file exists for backward compatibility during FSD migration.
 * All new code should import directly from @/infrastructure/ipc/ipc-bridge.
 */
export {
  isTauri,
  IpcBridge,
  type IpcHandler,
  type IpcResponse,
  type IpcBridgeOptions,
} from "@/infrastructure/ipc/ipc-bridge";
