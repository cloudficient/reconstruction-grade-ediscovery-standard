"""MkDocs hook: copy standard/*.md into the website/ docs_dir before build.

On Linux/macOS, creates symlinks. On Windows (or if symlinks fail),
falls back to file copies. Copied/linked files are cleaned up after build.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

_linked_files: list[Path] = []


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    standard_dir = docs_dir.parent / "standard"

    if not standard_dir.is_dir():
        return

    for src in sorted(standard_dir.glob("*.md")):
        if src.name.lower() == "readme.md":
            continue
        dest = docs_dir / src.name
        if dest.exists() or dest.is_symlink():
            dest.unlink()
        try:
            os.symlink(src.resolve(), dest)
        except OSError:
            shutil.copy2(src, dest)
        _linked_files.append(dest)


def on_post_build(config, **kwargs):
    for path in _linked_files:
        try:
            path.unlink()
        except FileNotFoundError:
            pass
    _linked_files.clear()
