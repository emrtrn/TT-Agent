"""
7. Unite - Enerjinin Donusumu ve Tasarim: Tum PDF'leri Uret
Calistirir: python pdf_uretim/uret_unite7_all.py

Uretilen PDF'ler (units/7_sinif/unit7/ klasorune kaydedilir):
  1.  Unite7_Ders_Plani.pdf
  2.  Unite7_On_Degerlendirme_Ogretmen.pdf
  3.  Unite7_On_Degerlendirme_Ogrenci_1.pdf
  4.  Unite7_On_Degerlendirme_Ogrenci_2.pdf
  5.  Unite7_Sunum_Icerigi.pdf
  6.  Unite7_Calisma_Kagitlari.pdf
  7.  Unite7_Degerlendirme_Araclari.pdf
  8.  Unite7_Zenginlestirme_Paketi.pdf
  9.  Unite7_Destekleme_Paketi.pdf
  10. Unite7_Ogretmen_Yansitma_ve_Kapanis.pdf
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)

from pdf_style import (
    register_fonts, add_page_number, create_doc,
    make_student_info_header,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, MindMapCanvas, HorizontalLine,
)
from md_converter import build_pdf_from_md, read_md_file

register_fonts()

# ============================================================
# YAPILANDIRMA
# ============================================================

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_DIR  = os.path.join(ROOT, 'units', 'unit7')
PDF_DIR = os.path.join(ROOT, 'units', 'unit7')

os.makedirs(PDF_DIR, exist_ok=True)

def md(filename):
    return os.path.join(MD_DIR, filename)

def pdf(filename):
    return os.path.join(PDF_DIR, filename)

UI = 'Teknoloji ve Tasarim - 7. Sinif - 7. Unite: Enerjinin Donusumu ve Tasarim'

KAPAK_META = {
    'Sinif': '7',
    'Ders': 'Teknoloji ve Tasarim',
    'Unite': '7. Unite - Enerjinin Donusumu ve Tasarim',
    'Sure': '8 Ders Saati (8 x 40 dk)',
    'Surec': '4 Hafta',
    'Kazanimlar': 'TT.7.7.1 - TT.7.7.5 (5 Kazanim)',
}

uretilen = []
hatalar  = []

# ============================================================
# PDF 1 - DERS PLANI
# ============================================================

def uret_ders_plani():
    cikti = 'Unite7_Ders_Plani.pdf'
    try:
        icerik = read_md_file(md('01_Ders_Plani.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite Ders Plani',
            subtitle='Enerjinin Donusumu ve Tasarim',
            meta_info=KAPAK_META,
            doc_type='Ogretmen Rehberi',
            add_cover=False,
            skip_top_title=False,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 2 - ON DEGERLENDIRME OGRETMEN REHBERI
# ============================================================

def uret_on_degerlendirme_ogretmen():
    cikti = 'Unite7_On_Degerlendirme_Ogretmen.pdf'
    try:
        icerik = read_md_file(md('02_On_Degerlendirme_Ogretmen_Rehberi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite On Degerlendirme',
            subtitle='Enerjinin Donusumu ve Tasarim - Ogretmen Rehberi',
            meta_info=KAPAK_META,
            doc_type='Ogretmen Rehberi',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 3 - ON DEGERLENDIRME OGRENCI 1 (Zihin Haritasi + Test)
# ============================================================

S_BAS  = ParagraphStyle('u7o_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u7o_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u7o_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u7o_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u7o_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u7o_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u7o_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u7o_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u7o_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)

SORULAR_O1 = [
    ('Bir nehirde akan su elektrik uretmek icin kullaniliyor. Suyun akarken sahip oldugu enerji turu asagidakilerden hangisidir?',
     ['A) Kimyasal enerji', 'B) Kinetik enerji', 'C) Potansiyel enerji', 'D) Ses enerjisi']),
    ('Bir termik santralde komur yakildiginda asagidaki enerji donusum zinciri hangi secenekte dogru verilmistir?',
     ['A) Elektrik enerjisi - Isi enerjisi - Kimyasal enerji',
      'B) Kinetik enerji - Isi enerjisi - Elektrik enerjisi',
      'C) Kimyasal enerji - Isi enerjisi - Elektrik enerjisi',
      'D) Potansiyel enerji - Kimyasal enerji - Isi enerjisi']),
    ('Asagidaki tanim lardan hangisi "yenilenebilir enerji kaynagi"ni dogru aciklar?',
     ['A) Dogada kendilginden yenilenen, kullanildikca tukenmeyen enerji kaynaklari',
      'B) Fabrikada uretilen ve satin alinan enerji turleri',
      'C) Yalnizca gunes ve ruzgardan elde edilen enerji',
      'D) Fosil yakitlardan daha pahali olan enerji kaynaklari']),
    ('Gunes enerjisi hakkinda asagidakilerden hangisi dogrudur?',
     ['A) Yalnizca sicak ulkelerde kullanilabilir',
      'B) Sadece elektrik uretmek icin kullanilir',
      'C) Uretimi sirasinda hic bakim gerektirmez',
      'D) Tukenme riski olmayan, temiz bir enerji kaynaqidir']),
    ('Kuresel isinmanin en onemli nedeni asagidakilerden hangisidir?',
     ['A) Gunesin giderek daha fazla enerji uretmesi',
      'B) Fosil yakitlarin yakilmasiyla atmosfere saliman sera gazlari',
      'C) Ozon tabakasindaki deligin buyumesi',
      'D) Ormanlarin cok hizli buyumesi']),
    ('Asagidakilerden hangisi fosil yakit degildir?',
     ['A) Komur', 'B) Petrol', 'C) Jeotermal enerji', 'D) Dogalgaz']),
    ('"Enerji verimliligi yuksek" bir urun ne anlama gelir?',
     ['A) Ayni isi daha az enerji tuketirek yapan urun',
      'B) Cok fazla enerji ureten cihaz',
      'C) Yalnizca gunes enerjisiyle calisan urun',
      'D) Tasarimi karmasik, ama dayanikli urun']),
    ('Bir tasarimci yeni bir ev aydinlatma sistemi tasarliyor. Surdurulebilirlik acisindan en dogru enerji kaynagi tercihi hangisi olur?',
     ['A) Komurle calisan termik santralden beslenen sistem',
      'B) Dogalgaz jeneratoru',
      'C) Aku depolama sistemi olmayan gunes paneli',
      'D) Gunes paneli + aku depolama sistemli, sebeke bagimsiz cozum']),
]


def uret_on_degerlendirme_ogrenci_1():
    cikti = 'Unite7_On_Degerlendirme_Ogrenci_1.pdf'
    try:
        doc = create_doc(pdf(cikti), title='On Degerlendirme - Ogrenci Formu 1', unite_info=UI)
        E   = []

        # --- SAYFA 1: Zihin Haritasi ---
        E.append(make_student_info_header())
        E.append(vsp(0.2))
        E.append(Paragraph(
            '<b>Not:</b> Bu calisma not icin degildir. Bildiklerini duerustce yaz - yanlis cevap olmaz!',
            S_NOT))
        E.append(vsp(0.15))
        E.append(sep())
        E.append(vsp(0.2))
        E.append(Paragraph('ARAC 1: ZIHIN HARITASI', S_BAS))
        E.append(Paragraph(
            '<b>Yonerge:</b> Asagida iki anahtar kelime var: <b>ENERJI</b> ve <b>TASARIM</b>. '
            'Bu kelimeleri duyduqunda aklina ne geliyor? Kavramlar, nesneler, ornekler, sorular... '
            'Aklina gelen her seyi yaz ve oklar cizerek baglandir. <b>Sure: 6 dakika</b>',
            S_YON))
        E.append(vsp(0.15))
        E.append(MindMapCanvas('ENERJI & TASARIM', width=17 * cm, height=9.5 * cm, num_branches=10))
        E.append(vsp(0.2))
        E.append(Paragraph('<b>Son soru:</b> Sence enerji ile tasarim birbiriyle baglantili mi? Neden?', S_SMBD))
        E.append(WritingLines(num_lines=2))
        E.append(vsp(0.15))
        E.append(Paragraph(
            'Ogretmenin bu kagidi toplayacak ve unite sonunda sana geri verecek. '
            'O zaman farkli renkli kalemle yeni ogrendiklerini ekleyeceksin!', S_NOT))
        E.append(sep())
        E.append(PageBreak())

        # --- SAYFA 2+: Tanilama Testi ---
        E.append(make_student_info_header())
        E.append(vsp(0.2))
        E.append(Paragraph('ARAC 2: IKI ASAMALI TANILAMA TESTI', S_BAS))
        E.append(Paragraph(
            '<b>Yonerge:</b> Her sorunun iki kismi var. Once dogru secenegi isaretle (A/B/C/D), '
            'sonra neden o secenegi sectigini acikla. Bilmiyorsan "Emin degilim ama..." diye basla. '
            '<b>Sure: 12 dakika</b>',
            S_YON))
        E.append(vsp(0.15))

        for i, (soru, secenekler) in enumerate(SORULAR_O1, 1):
            blok = []
            blok.append(Paragraph(f'<b>Soru {i}.</b> {soru}', S_SORU))
            for s in secenekler:
                blok.append(Paragraph(s, S_OPT))
            blok.append(vsp(0.1))
            blok.append(Paragraph('<b>Neden bu secenegi sectin?</b>', S_SMBD))
            blok.append(WritingLines(num_lines=1))
            blok.append(sep())
            blok.append(vsp(0.1))
            E.append(KeepTogether(blok))

        doc.build(E, onFirstPage=add_page_number, onLaterPages=add_page_number)
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 4 - ON DEGERLENDIRME OGRENCI 2
# ============================================================

def uret_on_degerlendirme_ogrenci_2():
    cikti = 'Unite7_On_Degerlendirme_Ogrenci_2.pdf'
    try:
        icerik = read_md_file(md('04_On_Degerlendirme_Ogrenci_2.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='On Degerlendirme - Ogrenci Formu 2',
            subtitle='Enerjinin Donusumu ve Tasarim',
            meta_info=None,
            doc_type='Ogrenci Materyali',
            add_cover=False,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 5 - SUNUM ICERIGI
# ============================================================

def uret_sunum_icerigi():
    cikti = 'Unite7_Sunum_Icerigi.pdf'
    try:
        icerik = read_md_file(md('05_Sunum_Icerigi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite Sunum Icerigi',
            subtitle='Enerjinin Donusumu ve Tasarim - 8 Ders',
            meta_info=KAPAK_META,
            doc_type='Ogretmen Rehberi',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 6 - CALISMA KAGITLARI
# ============================================================

def uret_calisma_kagitlari():
    cikti = 'Unite7_Calisma_Kagitlari.pdf'
    try:
        icerik = read_md_file(md('06_Calisma_Kagitlari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite Calisma Kagitlari',
            subtitle='Enerjinin Donusumu ve Tasarim - CK1 ile CK8',
            meta_info=KAPAK_META,
            doc_type='Ogrenci Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 7 - DEGERLENDIRME ARACLARI
# ============================================================

def uret_degerlendirme_araclari():
    cikti = 'Unite7_Degerlendirme_Araclari.pdf'
    try:
        icerik = read_md_file(md('07_Degerlendirme_Araclari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite Degerlendirme Araclari',
            subtitle='Enerjinin Donusumu ve Tasarim - 10 Arac',
            meta_info=KAPAK_META,
            doc_type='Ogretmen Rehberi',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 8 - ZENGINLESTIRME PAKETI
# ============================================================

def uret_zenginlestirme_paketi():
    cikti = 'Unite7_Zenginlestirme_Paketi.pdf'
    try:
        icerik = read_md_file(md('08_Zenginlestirme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite Zenginlestirme Paketi',
            subtitle='Enerjinin Donusumu ve Tasarim - Ileri Duzey Etkinlikler',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '7. Unite - Enerjinin Donusumu ve Tasarim',
                'Hedef': 'Ileri duzeyde ogrenmeye hazir ogrenciler',
                'Etkinlik Sayisi': '5 (Z1 - Z5)',
            },
            doc_type='Zenginlestirme Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 9 - DESTEKLEME PAKETI
# ============================================================

def uret_destekleme_paketi():
    cikti = 'Unite7_Destekleme_Paketi.pdf'
    try:
        icerik = read_md_file(md('09_Destekleme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite Destekleme Paketi',
            subtitle='Enerjinin Donusumu ve Tasarim - Destek Gerektiren Ogrenciler Icin',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '7. Unite - Enerjinin Donusumu ve Tasarim',
                'Hedef': 'Destekleme gerektiren ogrenciler',
                'Materyal Sayisi': '8 (D1 - D8)',
            },
            doc_type='Destekleme Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 10 - OGRETMEN YANSITMA VE KAPANIS
# ============================================================

def uret_yansitma_ve_kapanis():
    cikti = 'Unite7_Ogretmen_Yansitma_ve_Kapanis.pdf'
    try:
        icerik = read_md_file(md('10_Ogretmen_Yansitma_ve_Kapanis.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='7. Unite Ogretmen Yansitma ve Kapanis',
            subtitle='Enerjinin Donusumu ve Tasarim - 5 Arac',
            meta_info=KAPAK_META,
            doc_type='Ogretmen Rehberi',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# ANA CALISTIRICI
# ============================================================

if __name__ == '__main__':
    print('7. Unite PDF uretimi basliyor...')
    print()

    gorevler = [
        ('1. Ders Plani',                          uret_ders_plani),
        ('2. On Degerlendirme Ogretmen',            uret_on_degerlendirme_ogretmen),
        ('3. On Degerlendirme Ogrenci 1',           uret_on_degerlendirme_ogrenci_1),
        ('4. On Degerlendirme Ogrenci 2',           uret_on_degerlendirme_ogrenci_2),
        ('5. Sunum Icerigi',                        uret_sunum_icerigi),
        ('6. Calisma Kagitlari',                    uret_calisma_kagitlari),
        ('7. Degerlendirme Araclari',               uret_degerlendirme_araclari),
        ('8. Zenginlestirme Paketi',                uret_zenginlestirme_paketi),
        ('9. Destekleme Paketi',                    uret_destekleme_paketi),
        ('10. Ogretmen Yansitma ve Kapanis',        uret_yansitma_ve_kapanis),
    ]

    for isim, fonk in gorevler:
        sonuc = fonk()
        if isinstance(sonuc, tuple) and sonuc[0] == 'HATA':
            hatalar.append(sonuc)
            print(f'  HATA   [{isim}]  {sonuc[2]}')
        else:
            uretilen.append(sonuc)
            print(f'  OK     {sonuc}')

    print()
    print(f'Tamamlandi: {len(uretilen)} PDF uretildi, {len(hatalar)} hata.')
    if hatalar:
        print('Hatali dosyalar:')
        for h in hatalar:
            print(f'  - {h[1]}: {h[2]}')
