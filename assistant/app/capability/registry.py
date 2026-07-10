"""Capability Registry with Lifecycle control.

SDD-KAOS-EVOLUTION-001: Dynamic discoverability of Capabilities based on manifests
                       and lifecycle states.
"""
import yaml
from pathlib import Path
from typing import Any, Dict, List
from loguru import logger


class CapabilityLifecycle:
    CREATED = "CREATED"
    REGISTERED = "REGISTERED"
    INITIALIZED = "INITIALIZED"
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"
    RECOVERING = "RECOVERING"
    DISABLED = "DISABLED"


class CapabilityRegistry:
    """Registry to load, manage lifecycle, and query K.A.O.S capabilities."""

    _capabilities: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def register(cls, cap_id: str, manifest: Dict[str, Any]) -> None:
        """Register a new capability with its manifest."""
        cls._capabilities[cap_id] = {
            "manifest": manifest,
            "status": CapabilityLifecycle.REGISTERED,
            "error_message": None,
            "health_score": 1.0,
        }
        logger.info(f"[CapabilityRegistry] Registered: '{cap_id}' (version {manifest.get('version', '1.0')})")

    @classmethod
    def update_status(cls, cap_id: str, status: str, error_message: str | None = None) -> None:
        """Update the capability's current lifecycle state."""
        if cap_id in cls._capabilities:
            cls._capabilities[cap_id]["status"] = status
            cls._capabilities[cap_id]["error_message"] = error_message
            logger.info(f"[CapabilityRegistry] Capability '{cap_id}' lifecycle state changed to: {status}")

    @classmethod
    def get_capability(cls, cap_id: str) -> Dict[str, Any] | None:
        """Get the full capability info."""
        return cls._capabilities.get(cap_id)

    @classmethod
    def list_all(cls) -> List[Dict[str, Any]]:
        """List all capabilities with their status and manifest data."""
        return [
            {
                "id": cap_id,
                "status": val["status"],
                "error_message": val["error_message"],
                "manifest": val["manifest"],
            }
            for cap_id, val in cls._capabilities.items()
        ]

    @classmethod
    def is_available(cls, cap_id: str) -> bool:
        """Checks if a capability is registered and in a functional/healthy state."""
        cap = cls.get_capability(cap_id)
        if not cap:
            return False
        return cap["status"] in (
            CapabilityLifecycle.INITIALIZED,
            CapabilityLifecycle.HEALTHY,
            CapabilityLifecycle.DEGRADED,
        )

    @classmethod
    def autodiscover(cls, base_dir: Path) -> None:
        """Autodiscovers capabilities by scanning the base directory for yaml manifests."""
        if not base_dir.exists():
            logger.warning(f"[CapabilityRegistry] Autodiscover base_dir does not exist: {base_dir}")
            return
        logger.info(f"[CapabilityRegistry] Starting autodiscover in: {base_dir}")
        for sub in base_dir.iterdir():
            if sub.is_dir():
                manifest_file = sub / "manifest.yaml"
                if manifest_file.exists():
                    try:
                        with open(manifest_file, "r", encoding="utf-8") as f:
                            manifest = yaml.safe_load(f)
                            if manifest and "id" in manifest:
                                cap_id = manifest["id"]
                                cls.register(cap_id, manifest)
                                cls.update_status(cap_id, CapabilityLifecycle.INITIALIZED)
                    except Exception as e:
                        logger.error(f"[CapabilityRegistry] Error loading manifest from {manifest_file}: {e}")
