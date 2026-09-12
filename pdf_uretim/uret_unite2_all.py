"""
2. Ünite — Temel Tasarım: Tüm PDF'leri Üret
Calistirir: python pdf_uretim/uret_unite2_all.py

Uretilen PDF'ler (units/7_sinif/unit2/ klasörüne kaydedilir):
  1.  Unite2_Ders_Plani.pdf
  2.  Unite2_On_Degerlendirme.pdf
  3.  Unite2_Kavram_Kartlari.pdf
  4.  Unite2_Calisma_Kagitlari.pdf
  5.  Unite2_Degerlendirme_Araclari.pdf
  6.  Unite2_Sinav_Ogrenci.pdf
  7.  Unite2_Sinav_Cevap_Anahtari.pdf
  8.  Unite2_Zenginlestirme_Paketi.pdf
  9.  Unite2_Destekleme_Paketi.pdf
  10. Unite2_Ogretmen_Yansitma_ve_Kapanis.pdf
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import *
from md_converter import build_pdf_from_md, read_md_file, extract_section
from config import unite_bilgisi

# ============================================================
# YAPILANDIRMA
# ============================================================

UNITE_NO = 2
UNITE = unite_bilgisi(UNITE_NO)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_DIR = os.path.join(ROOT, 'units', 'unit2')
PDF_DIR = os.path.join(ROOT, 'units', 'unit2')

os.makedirs(PDF_DIR, exist_ok=True)

def md(filename):
    return os.path.join(MD_DIR, filename)

def pdf(filename):
    return os.path.join(PDF_DIR, filename)

UI = UNITE['unite_info_string']  # "Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite"

# Ortak kapak meta bilgileri
KAPAK_META = {
    'Sınıf': '7',
    'Ders': 'Teknoloji ve Tasarım',
    'Ünite': '2. Ünite — Temel Tasarım',
    'Süre': '6 Ders Saati (6 × 40 dk)',
    'Süreç': '3 Hafta',
    'Kazanımlar': 'TT.7.2.1 – TT.7.2.4',
}

uretilen = []
hatalar = []

# ============================================================
# PDF 1 — DERS PLANI
# ============================================================

def uret_ders_plani():
    dosya = 'Unite2_Ders_Plani.md'
    cikti = 'Unite2_Ders_Plani.pdf'
    try:
        icerik = read_md_file(md(dosya))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='2. Ünite Ders Planı',
            subtitle='Temel Tasarım',
            meta_info=KAPAK_META,
            doc_type='Öğretmen Rehberi',
            add_cover=False,
            skip_top_title=False,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 2 — ÖN DEĞERLENDİRME
# ============================================================

def uret_on_degerlendirme():
    dosya = 'Unite2_On_Degerlendirme.md'
    cikti = 'Unite2_On_Degerlendirme.pdf'
    try:
        icerik = read_md_file(md(dosya))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='2. Ünite Ön Değerlendirme Araç Seti',
            subtitle='Temel Tasarım',
            meta_info=KAPAK_META,
            doc_type='Öğretmen Rehberi',
            add_cover=None,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 3 — KAVRAM KARTLARI
# ============================================================

def uret_kavram_kartlari():
    dosya = 'Unite2_Kavram_Kartlari.md'
    cikti = 'Unite2_Kavram_Kartlari.pdf'
    try:
        icerik = read_md_file(md(dosya))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='2. Ünite Kavram Kartları',
            subtitle='Temel Tasarım — 17 Anahtar Kavram',
            meta_info=KAPAK_META,
            doc_type='Sınıf Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 4 — ÇALIŞMA KÂĞITLARI
# ============================================================

def uret_calisma_kagitlari():
    dosya = 'Unite2_Calisma_Kagitlari.md'
    cikti = 'Unite2_Calisma_Kagitlari.pdf'
    try:
        icerik = read_md_file(md(dosya))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='2. Ünite Çalışma Kâğıtları',
            subtitle='Temel Tasarım — 6 Ders Saati',
            meta_info=KAPAK_META,
            doc_type='Öğrenci Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 5 — DEĞERLENDİRME ARAÇLARI (Sınav hariç)
# ============================================================

def uret_degerlendirme_araclari():
    dosya = 'Unite2_Degerlendirme_Araclari.md'
    cikti = 'Unite2_Degerlendirme_Araclari.pdf'
    try:
        icerik = read_md_file(md(dosya))
        # Sınav bölümlerini hariç tut (Araç 9 öğrenci + cevap anahtarı)
        sinav_ogr = '## ARAÇ 9: ÜNİTE SONU SINAVI (ÖĞRENCİ KOPYASI)'
        end_marker = '## ARAÇ 10:'
        # Sınav başına kadar olan kısım + Araç 10 sonrası
        lines = icerik.split('\n')
        filtered_lines = []
        skip = False
        for line in lines:
            if sinav_ogr in line:
                skip = True
            if end_marker in line:
                skip = False
            if not skip:
                filtered_lines.append(line)
        icerik_filtrelenmis = '\n'.join(filtered_lines)

        build_pdf_from_md(
            md_content=icerik_filtrelenmis,
            output_path=pdf(cikti),
            title='2. Ünite Değerlendirme Araçları',
            subtitle='Temel Tasarım — Süreç, Ürün ve Rubrikler',
            meta_info=KAPAK_META,
            doc_type='Öğretmen Rehberi',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 6 — SINAV (ÖĞRENCİ KOPYASI)
# ============================================================

def uret_sinav_ogrenci():
    cikti = 'Unite2_Sinav_Ogrenci.pdf'
    try:
        from uret_unite2_sinav_ogrenci import build as build_sinav
        build_sinav(output_path=pdf(cikti))
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 7 — SINAV CEVAP ANAHTARI (Ayrı PDF — Öğrenciye verilmez)
# ============================================================

def uret_sinav_cevap_anahtari():
    cikti = 'Unite2_Sinav_Cevap_Anahtari.pdf'
    try:
        from uret_unite2_sinav_cevap_anahtari import build as build_cevap
        build_cevap(output_path=pdf(cikti))
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 8 — ZENGİNLEŞTİRME PAKETİ
# ============================================================

def uret_zenginlestirme():
    dosya = 'Unite2_Zenginlestirme_Paketi.md'
    cikti = 'Unite2_Zenginlestirme_Paketi.pdf'
    try:
        icerik = read_md_file(md(dosya))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='2. Ünite Zenginleştirme Paketi',
            subtitle='Temel Tasarım — İleri Düzey Derinleştirme',
            meta_info=KAPAK_META,
            doc_type='Öğrenci Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 9 — DESTEKLEME PAKETİ
# ============================================================

def uret_destekleme():
    dosya = 'Unite2_Destekleme_Paketi.md'
    cikti = 'Unite2_Destekleme_Paketi.pdf'
    try:
        icerik = read_md_file(md(dosya))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='2. Ünite Destekleme Paketi',
            subtitle='Temel Tasarım — Yapılandırılmış Destek Materyalleri',
            meta_info=KAPAK_META,
            doc_type='Destekleme Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 10 — ÖĞRETMEN YANSITMA VE ÜNİTE KAPANIS
# ============================================================

def uret_yansitma():
    dosya = 'Unite2_Ogretmen_Yansitma_ve_Kapanis.md'
    cikti = 'Unite2_Ogretmen_Yansitma_ve_Kapanis.pdf'
    try:
        icerik = read_md_file(md(dosya))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='2. Ünite Öğretmen Yansıtma ve Kapanış',
            subtitle='Temel Tasarım',
            meta_info=KAPAK_META,
            doc_type='Öğretmen Rehberi',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 11 — CK6 ÖZ DEĞERLENDİRME (Ayrı öğrenci formu)
# ============================================================

def uret_ck6_oz_degerlendirme():
    cikti = 'Unite2_CK6_Oz_Degerlendirme.pdf'
    try:
        from uret_unite2_ck6_oz_degerlendirme import build as build_ck6
        build_ck6(output_path=pdf(cikti))
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# ANA ÇALIŞMA
# ============================================================

if __name__ == '__main__':
    gorevler = [
        ('1. Ders Plani',              uret_ders_plani),
        ('2. On Degerlendirme',         uret_on_degerlendirme),
        ('3. Kavram Kartlari',          uret_kavram_kartlari),
        ('4. Calisma Kagitlari',        uret_calisma_kagitlari),
        ('5. Degerlendirme Araclari',   uret_degerlendirme_araclari),
        ('6. Sinav (Ogrenci)',          uret_sinav_ogrenci),
        ('7. Sinav Cevap Anahtari',     uret_sinav_cevap_anahtari),
        ('8. Zenginlestirme Paketi',    uret_zenginlestirme),
        ('9. Destekleme Paketi',        uret_destekleme),
        ('10. Ogretmen Yansitma',       uret_yansitma),
        ('11. CK6 Oz Degerlendirme',   uret_ck6_oz_degerlendirme),
    ]

    print('\n2. Unite - Temel Tasarim: PDF Uretimi Basliyor')
    print(f'Cikti klasoru: {PDF_DIR}')
    print('=' * 60)

    uretilen_sayisi = 0
    hata_sayisi = 0

    for ad, fonksiyon in gorevler:
        print(f'  Uretiliyor: {ad} ... ', end='', flush=True)
        sonuc = fonksiyon()
        if isinstance(sonuc, tuple) and sonuc[0] == 'HATA':
            print(f'HATA - {sonuc[2]}')
            hata_sayisi += 1
        else:
            print(f'OK -> {sonuc}')
            uretilen_sayisi += 1

    print('=' * 60)
    print(f'Tamamlandi: {uretilen_sayisi} PDF uretildi, {hata_sayisi} hata.')
    if hata_sayisi == 0:
        print('Tum PDFler basariyla olusturuldu.')
    print()
