#!/usr/bin/env python3
"""
Gera update-proxy.json para tauri-plugin-updater v2.

Uso:
    python3 gen_update_proxy.py --version 0.5.0 --date 2026-06-23T00:00:00Z \\
        --tag v0.5.0 --artifacts-dir ./dist

G-07: usa glob recursivo para capturar todos os arquivos .sig
"""

import argparse
import glob
import json
import os
import sys

REPO = "Brian5m1th/K.A.O.S"

PLATFORM_MAP = {
    ".msi": "windows-x86_64",
    ".exe": "windows-x86_64",
    ".AppImage": "linux-x86_64",
    ".deb": "linux-x86_64",
    ".rpm": "linux-x86_64",
    ".dmg": "darwin-aarch64",
    ".tar.gz": "darwin-aarch64",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera update-proxy.json para Tauri updater v2")
    parser.add_argument("--version", required=True, help="Versão semantica (ex: 0.5.0)")
    parser.add_argument("--date", required=True, help="Data ISO 8601 (ex: 2026-06-23T00:00:00Z)")
    parser.add_argument("--tag", required=True, help="Tag git (ex: v0.5.0)")
    parser.add_argument(
        "--artifacts-dir",
        default=".",
        help="Diretorio contendo os artefatos de build e arquivos .sig",
    )
    args = parser.parse_args()

    # G-07: buscar TODOS os .sig recursivamente (msi.sig, exe.sig, dmg.sig, AppImage.sig, etc.)
    sig_files = glob.glob(os.path.join(args.artifacts_dir, "**", "*.sig"), recursive=True)
    sig_map: dict[str, str] = {}

    for sig_path in sig_files:
        sig_name = os.path.basename(sig_path)
        for ext in PLATFORM_MAP:
            if sig_name.endswith(ext + ".sig"):
                platform = PLATFORM_MAP[ext]
                with open(sig_path, encoding="utf-8") as f:
                    sig_map[platform] = f.read().strip()
                break

    platforms: dict[str, dict[str, str]] = {}
    seen_platforms: set[str] = set()

    for ext, platform in PLATFORM_MAP.items():
        if platform in seen_platforms:
            continue
        seen_platforms.add(platform)

        sig = sig_map.get(platform, "")
        # Monta URL do asset baseada na plataforma
        if platform == "windows-x86_64":
            url = (
                f"https://github.com/{REPO}/releases/download/"
                f"{args.tag}/KAOS_{args.version}_x64_en-US.msi"
            )
        elif platform == "darwin-aarch64":
            url = (
                f"https://github.com/{REPO}/releases/download/"
                f"{args.tag}/KAOS_{args.version}_aarch64.dmg"
            )
        else:  # linux-x86_64
            url = (
                f"https://github.com/{REPO}/releases/download/"
                f"{args.tag}/KAOS_{args.version}_amd64.AppImage"
            )

        platforms[platform] = {"url": url, "signature": sig}

    output = {
        "version": args.version,
        "pub_date": args.date,
        "notes": "",
        "platforms": platforms,
    }

    json.dump(output, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
