"""
2. Ünite — Ön Değerlendirme Araç Seti PDF üretici
Çalıştır: python pdf_uretim/uret_02_on_degerlendirme.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH  = os.path.join(ROOT, 'units', 'unit2', 'Unite2_On_Degerlendirme.md')
PDF_PATH = os.path.join(ROOT, 'units', 'unit2', 'Unite2_On_Degerlendirme.pdf')

md = read_md_file(MD_PATH)

build_pdf_from_md(
    md_content=md,
    output_path=PDF_PATH,
    title='Ön Değerlendirme Araç Seti',
    subtitle='Temel Tasarım',
    meta_info=None,
    doc_type='Öğretmen Rehberi',
    add_cover=False,
    skip_top_title=False,
    unite_info='Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite',
)

print(f"PDF üretildi: {PDF_PATH}")
