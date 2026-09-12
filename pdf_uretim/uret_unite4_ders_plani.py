"""
4. Unite -- Ders Plani PDF ureticisi
Calistir: python pdf_uretim/uret_unite4_ders_plani.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH  = os.path.join(ROOT, 'units', 'unit4', 'U4_MD_01_Ders_Plani.md')
PDF_PATH = os.path.join(ROOT, 'units', 'unit4', 'U4_PDF_01_Ders_Plani.pdf')

md = read_md_file(MD_PATH)

build_pdf_from_md(
    md_content=md,
    output_path=PDF_PATH,
    title='4. Unite Ders Plani',
    subtitle='Bilgisayar Destekli Tasarim',
    meta_info=None,
    doc_type='Ogretmen Rehberi',
    add_cover=False,
    skip_top_title=False,
    unite_info='Teknoloji ve Tasarim - 7. Sinif - 4. Unite',
)

print(f"PDF uretildi: {PDF_PATH}")
