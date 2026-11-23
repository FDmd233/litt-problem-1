#!/usr/bin/env python3
"""Verify SHA256SUMS from the repository root."""
from hashlib import sha256
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
manifest = root / "SHA256SUMS"
failures = []
for line in manifest.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    expected, relpath = line.split("  ", 1)
    path = root / relpath
    if not path.is_file():
        failures.append(f"missing: {relpath}")
        continue
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        failures.append(f"hash mismatch: {relpath}")
if failures:
    print("\n".join(failures))
    sys.exit(1)
print("SHA-256 manifest: OK")
