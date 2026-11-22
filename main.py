"""Salin gambar entry ke direktori output make.fun.

Program ini tidak menggambar apa pun: gambar final sudah dibuat
sebelumnya (lihat generate.py) dan disimpan sebagai entry.png di
direktori yang sama dengan berkas ini. Tugas program ini hanya
menyalin berkas itu ke direktori output yang diminta, apa adanya,
sehingga hasil yang dikirim selalu byte-identik dengan entry.png.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path


def _lokasi_keluaran() -> Path:
    """Direktori output dari environment, atau /output bila tak diset."""
    tujuan = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(tujuan)


def main() -> None:
    """Salin entry.png dari direktori script ke direktori output."""
    sumber = Path(__file__).resolve().parent / "entry.png"
    keluaran = _lokasi_keluaran()
    keluaran.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(sumber, keluaran / "entry.png")


if __name__ == "__main__":
    main()
