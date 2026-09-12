"""
2. Ünite — Sunum Notları (Ders 1) PDF üretici
Slayt 1-11: Giriş + 1. Ders (Tasarımın Alfabesi: Elemanlar)
Çalıştır: python pdf_uretim/uret_02_sunum_ders1.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH  = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Sunum_Icerigi.md')
PDF_PATH = os.path.join(ROOT, 'units', 'unit2', 'Unite2_Sunum_Ders1.pdf')

full_md = read_md_file(MD_PATH)

# Slayt 12 başlığına kadar olan bölümü çıkar (Slayt 1-11)
lines = full_md.split('\n')
end_idx = None
for i, line in enumerate(lines):
    if '## SLAYT 12' in line:
        end_idx = i
        break

md = '\n'.join(lines[:end_idx]) if end_idx else full_md

build_pdf_from_md(
    md_content=md,
    output_path=PDF_PATH,
    title='Sunum Notları — 1. Ders',
    subtitle='Tasarımın Alfabesi: Elemanlar',
    meta_info={
        'Sınıf': '7. Sınıf',
        'Ünite': '2. Temel Tasarım',
        'Kapsam': 'Slayt 1–11 (Giriş + Ders 1)',
        'Süre': '40 dakika',
    },
    doc_type='Sunum Notları',
    add_cover=None,
    skip_top_title=False,
    unite_info='Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite: Temel Tasarım',
)

print(f"PDF üretildi: {PDF_PATH}")
