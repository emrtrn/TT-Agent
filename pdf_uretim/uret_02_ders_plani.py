"""
2. Ünite — Ders Planı PDF üretici
Çalıştır: python pdf_uretim/uret_02_ders_plani.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file
from config import unite_bilgisi, kapak_meta

UNITE_NO = 2
UNITE = unite_bilgisi(UNITE_NO)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH  = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Ders_Plani.md')
PDF_PATH = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Ders_Plani.pdf')

md = read_md_file(MD_PATH)

META = kapak_meta(
    saat_sayisi=UNITE['saat'],
    Kazanımlar='TT.7.2.1 – TT.7.2.4 (4 Öğrenme Çıktısı)',
)

build_pdf_from_md(
    md_content=md,
    output_path=PDF_PATH,
    title='2. Ünite Ders Planı',
    subtitle=UNITE['ad'],
    meta_info=None,
    doc_type='Öğretmen Rehberi',
    add_cover=False,
    skip_top_title=False,
    unite_info=UNITE['unite_info_string'],
)

print(f"PDF üretildi: {PDF_PATH}")
