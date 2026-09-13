"""Normalize title/subject properties for the 7-01 editable DOCX source set.

This intentionally changes only docProps/core.xml in each DOCX archive. It does
not open/save the document through Word or python-docx, so visible document
content and layout parts are copied unchanged. Existing PDFs are left untouched;
they receive the new properties when the teacher exports the revised DOCX files.
"""

from __future__ import annotations

import argparse
import os
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(r"C:\Users\emret\Desktop\Documents\7-01")
DOCUMENTS = {
    "U1_00_Ogretmen_Hazirlik.docx": (
        "1. ÜNİTE — ÖĞRETMEN HAZIRLIK REHBERİ",
        "7. Sınıf Teknoloji ve Tasarım - Ünite 1 Öğretmen Hazırlık Rehberi",
    ),
    "U1_01_Ders_Plani.docx": (
        "ÜNİTE DERS PLANI — Teknoloji ve Tasarım Öğreniyorum",
        "7. Sınıf Teknoloji ve Tasarım - Ünite 1 Ders Planı",
    ),
    "U1_02_On_Degerlendirme.docx": (
        "ÖN DEĞERLENDİRME — Teknoloji ve Tasarım Öğreniyorum",
        "7. Sınıf Teknoloji ve Tasarım - Ünite 1 Ön Değerlendirme",
    ),
    "U1_03_Bireysel_Calisma_Kagitlari.docx": (
        "BİREYSEL ÇALIŞMA KÂĞITLARI — Teknoloji ve Tasarım Öğreniyorum",
        "7. Sınıf Teknoloji ve Tasarım - Ünite 1 Bireysel Çalışma Kâğıtları",
    ),
    "U1_04_Grup_Calisma_Kagitlari.docx": (
        "GRUP ÇALIŞMA KÂĞITLARI — Teknoloji ve Tasarım Öğreniyorum",
        "7. Sınıf Teknoloji ve Tasarım - Ünite 1 Grup Çalışma Kâğıtları",
    ),
    "U1_05_Oz_Degerlendirme.docx": (
        "ÖZ DEĞERLENDİRME — Teknoloji ve Tasarım Öğreniyorum",
        "7. Sınıf Teknoloji ve Tasarım - Ünite 1 Öz Değerlendirme",
    ),
    "U1_06_Degerlendirme.docx": (
        "ÜNİTE SONU DEĞERLENDİRME — Teknoloji ve Tasarım Öğreniyorum",
        "7. Sınıf Teknoloji ve Tasarım - Ünite 1 Ünite Sonu Değerlendirme",
    ),
}

NS = {
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
}
ET.register_namespace("cp", NS["cp"])
ET.register_namespace("dc", NS["dc"])


def set_text(root: ET.Element, tag: str, value: str) -> None:
    node = root.find(tag, NS)
    if node is None:
        node = ET.SubElement(root, tag)
    node.text = value


def read_properties(path: Path) -> tuple[str | None, str | None]:
    with zipfile.ZipFile(path) as archive:
        core = ET.fromstring(archive.read("docProps/core.xml"))
    return core.findtext("dc:title", namespaces=NS), core.findtext("dc:subject", namespaces=NS)


def rewrite_properties(path: Path, title: str, subject: str) -> None:
    with zipfile.ZipFile(path, "r") as source:
        core = ET.fromstring(source.read("docProps/core.xml"))
        set_text(core, "dc:title", title)
        set_text(core, "dc:subject", subject)
        core_bytes = ET.tostring(core, encoding="utf-8", xml_declaration=True)
        fd, temporary_name = tempfile.mkstemp(prefix=f".{path.stem}-", suffix=".docx", dir=path.parent)
        os.close(fd)
        temporary_path = Path(temporary_name)
        try:
            with zipfile.ZipFile(temporary_path, "w", zipfile.ZIP_DEFLATED) as target:
                for member in source.infolist():
                    payload = core_bytes if member.filename == "docProps/core.xml" else source.read(member.filename)
                    target.writestr(member, payload)
            os.replace(temporary_path, path)
        finally:
            if temporary_path.exists():
                temporary_path.unlink()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write properties; omit for a dry run.")
    args = parser.parse_args()

    for name, (title, subject) in DOCUMENTS.items():
        path = ROOT / name
        if not path.is_file():
            raise FileNotFoundError(path)
        before = read_properties(path)
        print(f"{name}\n  before: title={before[0]!r}; subject={before[1]!r}\n  target: title={title!r}; subject={subject!r}")
        if args.apply:
            rewrite_properties(path, title, subject)
            after = read_properties(path)
            if after != (title, subject):
                raise RuntimeError(f"Verification failed for {path}")
            print("  result: verified")


if __name__ == "__main__":
    main()
