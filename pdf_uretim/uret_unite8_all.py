"""
8. Unite - Butunlesik Ogrenme: STEAM: Tum PDF'leri Uret
Calistirir: python pdf_uretim/uret_unite8_all.py

Uretilen PDF'ler (units/7_sinif/unit8/ klasorune kaydedilir):
  1.  Unite8_Ders_Plani.pdf
  2.  Unite8_On_Degerlendirme_Ogretmen.pdf
  3.  Unite8_On_Degerlendirme_Ogrenci_1.pdf
  4.  Unite8_On_Degerlendirme_Ogrenci_2.pdf
  5.  Unite8_Sunum_Icerigi.pdf
  6.  Unite8_STEAM_Surec_Posteri.pdf
  7.  Unite8_Calisma_Kagitlari.pdf
  8.  Unite8_Degerlendirme_Araclari.pdf
  9.  Unite8_Sinav_Cevap_Anahtari.pdf
  10. Unite8_Zenginlestirme_Paketi.pdf
  11. Unite8_Destekleme_Paketi.pdf
  12. Unite8_Ogretmen_Yansitma_ve_Kapanis.pdf
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
MD_DIR  = os.path.join(ROOT, 'units', 'unit8')
PDF_DIR = os.path.join(ROOT, 'units', 'unit8')

os.makedirs(PDF_DIR, exist_ok=True)

def md(filename):
    return os.path.join(MD_DIR, filename)

def pdf(filename):
    return os.path.join(PDF_DIR, filename)

UI = 'Teknoloji ve Tasarim - 7. Sinif - 8. Unite: Butunlesik Ogrenme: STEAM'

KAPAK_META = {
    'Sinif': '7',
    'Ders': 'Teknoloji ve Tasarim',
    'Unite': '8. Unite - Butunlesik Ogrenme: STEAM',
    'Sure': '10 Ders Saati (10 x 40 dk)',
    'Surec': '5 Hafta',
    'Kazanimlar': 'TT.7.8.1 - TT.7.8.6 (6 Kazanim)',
}

uretilen = []
hatalar  = []

# ============================================================
# PDF 1 - DERS PLANI
# ============================================================

def uret_ders_plani():
    cikti = 'Unite8_Ders_Plani.pdf'
    try:
        icerik = read_md_file(md('01_Ders_Plani.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Ders Plani',
            subtitle='Butunlesik Ogrenme: STEAM',
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
    cikti = 'Unite8_On_Degerlendirme_Ogretmen.pdf'
    try:
        icerik = read_md_file(md('02_On_Degerlendirme_Ogretmen_Rehberi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite On Degerlendirme',
            subtitle='Butunlesik Ogrenme: STEAM - Ogretmen Rehberi',
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

S_BAS  = ParagraphStyle('u8o_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u8o_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u8o_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u8o_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u8o_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u8o_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u8o_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u8o_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u8o_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)

SORULAR_O1 = [
    ('STEAM kisaltmasindaki "E" harfi hangi disiplini temsil eder?',
     ['A) Ekoloji', 'B) Ekonomi', 'C) Muhendislik', 'D) Elektronik']),
    ('Bir grup ogrenci okullarindaki su israfini onlemek icin bir sistem tasarliyor. Bu proje STEAM\'in hangi ozelligini en iyi gostermektedir?',
     ['A) Tek bir disiplin yeterlidir',
      'B) Sanat bileseni gereksizdir',
      'C) Birden fazla disiplin birlikte calisir',
      'D) Matematik bileseni yoktur']),
    ('Muhendislik tasarim surecinin ilk adimi hangisidir?',
     ['A) Malzeme secmek', 'B) Problem belirlemek', 'C) Prototip uretmek', 'D) Sunum yapmak']),
    ('Bir projede "paydas" kimdir?',
     ['A) Projeyi degerlendiren ogretmen',
      'B) Problemden etkilenen veya cozumunden yararlanan kisi/grup',
      'C) Proje ekibinin lideri',
      'D) Yalnizca problemi yaratan kisi']),
    ('"Prototip" kavrami icin en dogru aciklama hangisidir?',
     ['A) Satisa hazir final urun',
      'B) Yalnizca bilgisayarda yapilan cizim',
      'C) Bir tasarimin test edilmek uzere yapilan ilk deneme modeli',
      'D) Yalnizca profesyonellerin yapabilecegi model']),
    ('STEAM yaklasiminda Sanat (Arts) bileseni tasarimda ne saglar?',
     ['A) Sarki soyleme ve dans etme',
      'B) Yalnizca resim cizmek',
      'C) Sanat tarihi arastirmak',
      'D) Estetik, tasarim ve yaraticilik']),
    ('Grup calismalarinda gorev dagitiminin temel amaci nedir?',
     ['A) Bazi ogrencilerin daha az calismasi',
      'B) Her uyenin sorumluluğunu netlestirerek verimliligi artirmak',
      'C) Ogretmenin isini kolaylastirmak',
      'D) Projeyi bireysel calismaya donusturmek']),
    ('Asagidakilerden hangisi gercek bir STEAM projesine en iyi ornek olabilir?',
     ['A) Matematik testi cozmek',
      'B) Siir ezberlemek',
      'C) Tek basina bir resim cizmek',
      'D) Gunes enerjisiyle calisan bir bahce sulama sistemi tasarlamak']),
]


def uret_on_degerlendirme_ogrenci_1():
    cikti = 'Unite8_On_Degerlendirme_Ogrenci_1.pdf'
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
            '<b>Yonerge:</b> Asagida merkez kutuya bak: <b>STEAM</b>. '
            'Bu kelimeyi duyduğunda aklina hangi sozcukler, kavramlar, ornekler, dersler geliyor? '
            'Her birini oklarla merkeze baglayarak yaz. Istedigin kadar dal ekleyebilirsin. <b>Sure: 5 dakika</b>',
            S_YON))
        E.append(vsp(0.15))
        E.append(MindMapCanvas('STEAM', width=17 * cm, height=9.5 * cm, num_branches=10))
        E.append(vsp(0.2))
        E.append(Paragraph('<b>Son soru:</b> Sence STEAM\'deki bes disiplin birbiriyle iliskili midir? Neden?', S_SMBD))
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
            '<b>Sure: 10-12 dakika</b>',
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
    cikti = 'Unite8_On_Degerlendirme_Ogrenci_2.pdf'
    try:
        icerik = read_md_file(md('04_On_Degerlendirme_Ogrenci_2.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='On Degerlendirme - Ogrenci Formu 2',
            subtitle='Butunlesik Ogrenme: STEAM',
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
    cikti = 'Unite8_Sunum_Icerigi.pdf'
    try:
        icerik = read_md_file(md('05_Sunum_Icerigi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Sunum Icerigi',
            subtitle='Butunlesik Ogrenme: STEAM - 10 Ders',
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
# PDF 6 - STEAM SUREC POSTERI
# ============================================================

def uret_steam_surec_posteri():
    cikti = 'Unite8_STEAM_Surec_Posteri.pdf'
    try:
        icerik = read_md_file(md('06_STEAM_Surec_Posteri.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='STEAM Proje Dongusu',
            subtitle='Gercek Bir Problemden Gercek Bir Cozume',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '8. Unite - Butunlesik Ogrenme: STEAM',
                'Format': 'A3 Sinif Posteri (A4\'te basilmis referans kopya)',
                'Kullanim': 'Sinif duvarina asilir; ders baslarinda referans gosterilir',
            },
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
# PDF 7 - CALISMA KAGITLARI
# ============================================================

def uret_calisma_kagitlari():
    cikti = 'Unite8_Calisma_Kagitlari.pdf'
    try:
        icerik = read_md_file(md('07_Calisma_Kagitlari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Calisma Kagitlari',
            subtitle='Butunlesik Ogrenme: STEAM - CK1 ile CK5',
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
# PDF 8 - DEGERLENDIRME ARACLARI
# ============================================================

def uret_degerlendirme_araclari():
    cikti = 'Unite8_Degerlendirme_Araclari.pdf'
    try:
        icerik = read_md_file(md('08_Degerlendirme_Araclari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Degerlendirme Araclari',
            subtitle='Butunlesik Ogrenme: STEAM - 10 Arac',
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
# PDF 9 - SINAV CEVAP ANAHTARI (ayri PDF)
# ============================================================

def uret_sinav_cevap_anahtari():
    cikti = 'Unite8_Sinav_Cevap_Anahtari.pdf'
    try:
        icerik = read_md_file(md('09_Sinav_Cevap_Anahtari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Sinav Cevap Anahtari',
            subtitle='Butunlesik Ogrenme: STEAM - Ogretmen Icin',
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
# PDF 10 - ZENGINLESTIRME PAKETI
# ============================================================

def uret_zenginlestirme_paketi():
    cikti = 'Unite8_Zenginlestirme_Paketi.pdf'
    try:
        icerik = read_md_file(md('10_Zenginlestirme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Zenginlestirme Paketi',
            subtitle='Butunlesik Ogrenme: STEAM - Ileri Duzey Etkinlikler',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '8. Unite - Butunlesik Ogrenme: STEAM',
                'Hedef': 'Ileri duzeyde ogrenmeye hazir ogrenciler',
                'Etkinlik Sayisi': '7 (Z1 - Z7)',
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
# PDF 11 - DESTEKLEME PAKETI
# ============================================================

def uret_destekleme_paketi():
    cikti = 'Unite8_Destekleme_Paketi.pdf'
    try:
        icerik = read_md_file(md('11_Destekleme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Destekleme Paketi',
            subtitle='Butunlesik Ogrenme: STEAM - Destek Gerektiren Ogrenciler Icin',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '8. Unite - Butunlesik Ogrenme: STEAM',
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
# PDF 12 - OGRETMEN YANSITMA VE KAPANIS
# ============================================================

def uret_yansitma_ve_kapanis():
    cikti = 'Unite8_Ogretmen_Yansitma_ve_Kapanis.pdf'
    try:
        icerik = read_md_file(md('12_Ogretmen_Yansitma_ve_Kapanis.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='8. Unite Ogretmen Yansitma ve Kapanis',
            subtitle='Butunlesik Ogrenme: STEAM',
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
    print('8. Unite PDF uretimi basliyor...')
    print()

    gorevler = [
        ('1.  Ders Plani',                           uret_ders_plani),
        ('2.  On Degerlendirme Ogretmen',             uret_on_degerlendirme_ogretmen),
        ('3.  On Degerlendirme Ogrenci 1',            uret_on_degerlendirme_ogrenci_1),
        ('4.  On Degerlendirme Ogrenci 2',            uret_on_degerlendirme_ogrenci_2),
        ('5.  Sunum Icerigi',                         uret_sunum_icerigi),
        ('6.  STEAM Surec Posteri',                   uret_steam_surec_posteri),
        ('7.  Calisma Kagitlari',                     uret_calisma_kagitlari),
        ('8.  Degerlendirme Araclari',                uret_degerlendirme_araclari),
        ('9.  Sinav Cevap Anahtari',                  uret_sinav_cevap_anahtari),
        ('10. Zenginlestirme Paketi',                 uret_zenginlestirme_paketi),
        ('11. Destekleme Paketi',                     uret_destekleme_paketi),
        ('12. Ogretmen Yansitma ve Kapanis',          uret_yansitma_ve_kapanis),
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
