"""
3. Ünite — Ders Planı PDF üretici
Çalıştır: python pdf_uretim/uret_03_ders_plani.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH  = os.path.join(ROOT, 'units', 'unit3', '01_Ders_Plani.md')
PDF_PATH = os.path.join(ROOT, 'units', 'unit3', '01_Ders_Plani.pdf')

md = read_md_file(MD_PATH)

build_pdf_from_md(
    md_content=md,
    output_path=PDF_PATH,
    title='3. Ünite Ders Planı',
    subtitle='Tasarım Odaklı Süreç',
    meta_info=None,
    doc_type='Öğretmen Rehberi',
    add_cover=False,
    skip_top_title=False,
    unite_info='Teknoloji ve Tasarım • 7. Sınıf • 3. Ünite',
)

print(f"PDF üretildi: {PDF_PATH}")
