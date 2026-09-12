"""
1. Ünite — Ders Planı PDF üretici
Çalıştır: python pdf_uretim/uret_01_ders_plani.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file
from config import unite_bilgisi

UNITE_NO = 1
UNITE = unite_bilgisi(UNITE_NO)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH  = os.path.join(ROOT, 'units', 'unit1', '01_Ders_Plani.md')
PDF_PATH = os.path.join(ROOT, 'units', 'unit1', '01_Ders_Plani_v2.pdf')

md = read_md_file(MD_PATH)

build_pdf_from_md(
    md_content=md,
    output_path=PDF_PATH,
    title='1. Ünite Ders Planı',
    subtitle=UNITE['ad'],
    meta_info=None,
    doc_type='Öğretmen Rehberi',
    add_cover=False,
    skip_top_title=False,
    unite_info=UNITE['unite_info_string'],
)

print(f"PDF üretildi: {PDF_PATH}")
