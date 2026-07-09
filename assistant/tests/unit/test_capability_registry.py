import tempfile
import yaml
from pathlib import Path
from app.capability.registry import CapabilityRegistry, CapabilityLifecycle


def test_capability_registry_lifecycle():
    # Test manual register
    manifest = {
        "id": "test_cap",
        "version": "1.2.3",
        "permissions": ["test"],
        "dependencies": []
    }
    CapabilityRegistry.register("test_cap", manifest)
    
    cap = CapabilityRegistry.get_capability("test_cap")
    assert cap is not None
    assert cap["status"] == CapabilityLifecycle.REGISTERED

    # Test update status
    CapabilityRegistry.update_status("test_cap", CapabilityLifecycle.HEALTHY)
    assert CapabilityRegistry.is_available("test_cap") is True

    # Test autodiscover from dynamic dir
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        sub_dir = tmp_path / "sub_cap"
        sub_dir.mkdir()
        
        manifest_file = sub_dir / "manifest.yaml"
        with open(manifest_file, "w", encoding="utf-8") as f:
            yaml.dump({
                "id": "autodiscovered_cap",
                "version": "2.0.0",
                "permissions": ["all"]
            }, f)
            
        CapabilityRegistry.autodiscover(tmp_path)
        
        discovered = CapabilityRegistry.get_capability("autodiscovered_cap")
        assert discovered is not None
        assert discovered["status"] == CapabilityLifecycle.INITIALIZED
        assert discovered["manifest"]["version"] == "2.0.0"
