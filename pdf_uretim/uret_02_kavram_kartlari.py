"""
2. Ünite — Kavram Kartları PDF üretici
Çalıştır: python pdf_uretim/uret_02_kavram_kartlari.py
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
MD_PATH  = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Kavram_Kartlari.md')
PDF_PATH = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Kavram_Kartlari.pdf')

md = read_md_file(MD_PATH)

META = kapak_meta(
    saat_sayisi=UNITE['saat'],
    Kapsam='17 Kavram: 9 Tasarim Elemani + 8 Tasarim Ilkesi',
)

build_pdf_from_md(
    md_content=md,
    output_path=PDF_PATH,
    title='2. Unite Kavram Kartlari',
    subtitle=UNITE['ad'],
    meta_info=META,
    doc_type='Ogretmen Rehberi',
    add_cover=True,
    skip_top_title=True,
    unite_info=UNITE['unite_info_string'],
)

from pypdf import PdfReader
r = PdfReader(PDF_PATH)
print(f"PDF uretildi: {PDF_PATH}")
print(f"Toplam sayfa: {len(r.pages)}")
