"""
6. Unite - Dogadan Tasarima: Tum PDF'leri Uret
Calistir: python pdf_uretim/uret_unite6_all.py

Uretilen PDF'ler (units/7_sinif/unit6/ klasorune kaydedilir):
  1.  Unite6_Ders_Plani.pdf
  2.  Unite6_On_Degerlendirme_Ogretmen.pdf
  3.  Unite6_On_Degerlendirme_Ogrenci_1.pdf
  4.  Unite6_On_Degerlendirme_Ogrenci_2.pdf
  5.  Unite6_Biyomimikri_Ornek_Kartlari.pdf
  6.  Unite6_Calisma_Kagitlari.pdf           (CK1-CK6 birlestirme)
  7.  Unite6_Degerlendirme_Araclari.pdf      (13+14+15 birlestirme)
  8.  Unite6_Sinav_Ogrenci.pdf
  9.  Unite6_Sinav_Cevap_Anahtari.pdf        (AYRI DOSYA)
  10. Unite6_Genel_Degerlendirme_Tablosu.pdf
  11. Unite6_Zenginlestirme_Paketi.pdf
  12. Unite6_Destekleme_Paketi.pdf
  13. Unite6_Yansitma_ve_Kapanis.pdf
  Not: 06_Sunum_Icerigi.md PDF uretilmez (slayt uygulamasina aktarilir)
"""

import sys
import os
import re

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
    register_fonts, add_page_number, create_doc, make_cover,
    make_student_info_header,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, MindMapCanvas, DrawingBox, HorizontalLine,
)
from md_converter import (
    build_pdf_from_md, read_md_file, md_to_flowables, clean_emojis,
)

register_fonts()

# ============================================================
# YAPILANDIRMA
# ============================================================

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_DIR  = os.path.join(ROOT, 'units', 'unit6')
PDF_DIR = os.path.join(ROOT, 'units', 'unit6')

os.makedirs(PDF_DIR, exist_ok=True)

def md(filename):
    return os.path.join(MD_DIR, filename)

def pdf(filename):
    return os.path.join(PDF_DIR, filename)

UI = 'Teknoloji ve Tasarim - 7. Sinif - 6. Unite: Dogadan Tasarima'

KAPAK_META = {
    'Sinif': '7',
    'Ders': 'Teknoloji ve Tasarim',
    'Unite': '6. Unite - Dogadan Tasarima',
    'Sure': '8 Ders Saati (8 x 40 dk)',
    'Surec': '4 Hafta',
    'Kazanimlar': 'TT.7.6.1 - TT.7.6.2 - TT.7.6.3 (3 Kazanim)',
}

uretilen = []
hatalar  = []

# ============================================================
# YARDIMCI: CK dosyalari icin on/son isleme
# ============================================================

_DB_RE = re.compile(
    r'\[(Cizim Alani|Eskiz Alani|Alan|Çizim Alanı|Eskiz Alanı)[^\]]*:'
    r'\s*~?(\d+(?:[.,]\d+)?)\s*cm\s*[xX×]\s*(\d+(?:[.,]\d+)?)\s*cm[^\]]*\]',
    re.IGNORECASE | re.UNICODE,
)


def preprocess_ck_md(content):
    """Basit notasyonlari isaretcilere donustur (tablo satirlari atlanir)."""
    lines = content.split('\n')
    result = []
    for line in lines:
        if line.strip().startswith('|'):
            result.append(line)
        else:
            line = _DB_RE.sub(
                lambda m: f'UNIT6_DB_{m.group(2).replace(",",".")}_{m.group(3).replace(",",".")}',
                line,
            )
            result.append(line)
    return '\n'.join(result)


def postprocess_unit6_flowables(flowables):
    """Isaretci paragraflarini gercek cizim elemanlarina donustur."""
    result = []
    for fl in flowables:
        if isinstance(fl, KeepTogether):
            inner = postprocess_unit6_flowables(fl._content)
            result.append(KeepTogether(inner) if len(inner) > 1 else (inner[0] if inner else fl))
            continue
        if isinstance(fl, Paragraph):
            txt = getattr(fl, 'text', '')
            m = re.match(r'UNIT6_DB_(\d+(?:\.\d+)?)_(\d+(?:\.\d+)?)', txt)
            if m:
                result.append(DrawingBox(height=float(m.group(2)) * cm))
                continue
        result.append(fl)
    return result


def build_ck_pdf(output_path, md_filenames, title, subtitle, meta_info):
    """CK dosyalarini birlestirip ozel notasyon destekli PDF uret."""
    doc = create_doc(output_path, title=title, unite_info=UI)
    elements = []
    elements.extend(make_cover(title, subtitle, meta_info, 'Ogrenci Materyali'))

    for i, fname in enumerate(md_filenames):
        raw = read_md_file(md(fname))
        raw = clean_emojis(raw)
        raw = preprocess_ck_md(raw)
        flowables = md_to_flowables(raw, skip_top_title=True, compact_mode=True)
        flowables = postprocess_unit6_flowables(flowables)
        elements.extend(flowables)
        if i < len(md_filenames) - 1:
            elements.append(PageBreak())

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return output_path


# ============================================================
# PDF 1 - DERS PLANI
# ============================================================

def uret_ders_plani():
    cikti = 'Unite6_Ders_Plani.pdf'
    try:
        icerik = read_md_file(md('01_Ders_Plani.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Ders Plani',
            subtitle='Dogadan Tasarima',
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
    cikti = 'Unite6_On_Degerlendirme_Ogretmen.pdf'
    try:
        icerik = read_md_file(md('02_On_Degerlendirme_Ogretmen_Rehberi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite On Degerlendirme',
            subtitle='Dogadan Tasarima - Ogretmen Rehberi',
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
# PDF 3 - ON DEGERLENDIRME OGRENCI 1 (Zihin Haritasi + Tanilama Testi)
# ============================================================

S_BAS  = ParagraphStyle('u6_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u6_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u6_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u6_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u6_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u6_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u6_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u6_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u6_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)


def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)


SORULAR_O1 = [
    (
        'Biyomimikri kavraminin en dogru tanimi hangisidir?',
        [
            'A) Hayvanlari taklit eden robot yapimi teknolojisi',
            'B) Dogadaki canlilarin ozelliklerini tasarima uyarlama yaklasimi',
            'C) Dogal malzemeleri kullanarak urun yapma yontemi',
            'D) Biyoloji ile mimariyi birlestiren bir sanat akimi',
        ]
    ),
    (
        'Geko kertenkeleleri duvara kolayca yapişabilir çünkü ayaklarinda milyonlarca ince nano tüy bulunur. '
        'Bu özelligi taklit eden ürün hangisidir?',
        [
            'A) Su geçirmez çizme',
            'B) Yüzücü gözlügü',
            'C) Yapişkanli nano yüzey bandi',
            'D) Isi yalitim malzemesi',
        ]
    ),
    (
        'Lotus çiçeginin yapraklarindaki özellik sayesinde su yüzeyde tutunmaz, damlalar yuvarlanip gider. '
        'Bu "lotus etkisi" hangi tasarima ilham kaynagi olmustur?',
        [
            'A) Günes enerjisi toplayan panel yapimi',
            'B) Su geçirmez ve kendiliğinden temizlenen kumas üretimi',
            'C) Hafif ama dayanikli çati kirisi tasarimi',
            'D) Hizli yüzücü kiyafeti yapimi',
        ]
    ),
    (
        'Biyomorfizm nedir?',
        [
            'A) Canlilarin islevsel özelliklerini birebir taklit etme',
            'B) Dogal formlari estetik amaçla tasarima yansitma',
            'C) Biyolojik malzemeleri doğrudan ürünlerde kullanma',
            'D) Ekosistemi koruma odakli tasarim yapma',
        ]
    ),
    (
        'Köpek baliğinin deri yapisindaki küçük disimsi çikintilir suyu verimli biçimde keser. '
        'Bu özellik hangi alanda kullanilmak üzere arastirilmistir?',
        [
            'A) Hava araci gövde tasarimi',
            'B) Tibbi implant kaplamalar',
            'C) Yüzücü kiyafeti tasarimi',
            'D) Günes paneli yüzeyi',
        ]
    ),
    (
        'Biyofili kavramini en iyi açiklayan ifade hangisidir?',
        [
            'A) Biyoçesitliligi koruma çabasi',
            'B) Insanin dogayla olan içgüdüsel bagi ve dogaya yönelik eğilimi',
            'C) Bitkileri dekoratif tasarim ögesi olarak kullanma',
            'D) Dogal malzemeleri geri dönüstürme anlayisi',
        ]
    ),
    (
        "Afrika'daki termit tepeleri içinde kendi sicakliklarini kontrol eden dogal bir havalandirma sistemi çalişir. "
        'Bu sistem hangi yapiya ilham vermistir?',
        [
            'A) Günes paneli çiftligi',
            'B) Yesil çati (teras bahçe)',
            'C) Eastgate Centre ofis binasi',
            'D) Köprü kirisi tasarimi',
        ]
    ),
    (
        'Bir tasarimci biyomimetik yaklasimi kullanirken en temel olarak hangi soruya odaklanir?',
        [
            'A) Bu ürünün maliyeti nedir?',
            'B) Bu problemi doga nasil çözmüş?',
            'C) Bu formu kim daha önce çizmis?',
            'D) Bu ürünü kimler satin alir?',
        ]
    ),
]


def uret_on_degerlendirme_ogrenci_1():
    cikti = 'Unite6_On_Degerlendirme_Ogrenci_1.pdf'
    try:
        doc = create_doc(pdf(cikti), title='On Degerlendirme - Ogrenci Formu 1', unite_info=UI)
        E   = []

        # --- SAYFA 1: Zihin Haritasi ---
        E.append(make_student_info_header())
        E.append(vsp(0.2))
        E.append(Paragraph(
            '<b>Not:</b> Bu calisma not icin degildir. Dogru ya da yanlis cevap yoktur. '
            'Aklina geleni ictenlikle yaz!',
            S_NOT))
        E.append(vsp(0.15))
        E.append(sep())
        E.append(vsp(0.2))
        E.append(Paragraph('ARAC 1: ZIHIN HARITASI', S_BAS))
        E.append(Paragraph(
            '<b>Yonerge:</b> Asagida iki anahtar kelime var: <b>DOGA</b> ve <b>TASARIM</b>. '
            'Bu kelimeleri duyduğunda aklina gelen her seyi oklar ve kelimelerle bagla. '
            'Canli adlari, ürünler, kavramlar, her sey olabilir! <b>Sure: 5-7 dakika</b>',
            S_YON))
        E.append(vsp(0.15))
        E.append(MindMapCanvas('DOGA  TASARIM', width=17 * cm, height=9.5 * cm, num_branches=8))
        E.append(vsp(0.2))
        E.append(Paragraph(
            '<b>Son soru:</b> Sence DOGA ve TASARIM birbiriyle nasil iliskili? Kisaca açikla:',
            S_SMBD))
        E.append(WritingLines(num_lines=2))
        E.append(vsp(0.15))
        E.append(Paragraph(
            'Ogretmenin bu kagidi toplayacak ve unite sonunda sana geri verecek. '
            'O zaman farkli renkli kalemle yeni ogrendiklerini ekleyeceksin!',
            S_NOT))
        E.append(sep())
        E.append(PageBreak())

        # --- SAYFA 2+: Tanilama Testi ---
        E.append(make_student_info_header())
        E.append(vsp(0.2))
        E.append(Paragraph('ARAC 2: IKI ASAMALI TANILAMA TESTI', S_BAS))
        E.append(Paragraph(
            '<b>Yonerge:</b> Her sorunun iki kismi var. Once dogru secenegi isaretleyin (A/B/C/D), '
            'sonra neden o secenegi sectiginizi açiklayin. Bilmiyorsan "Emin degilim ama..." diye basla. '
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
    cikti = 'Unite6_On_Degerlendirme_Ogrenci_2.pdf'
    try:
        icerik = read_md_file(md('04_On_Degerlendirme_Ogrenci_2.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='On Degerlendirme - Ogrenci Formu 2',
            subtitle='Dogadan Tasarima',
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
# PDF 5 - BIYOMIMIKRI ORNEK KARTLARI
# ============================================================

def uret_biyomimikri_kartlari():
    cikti = 'Unite6_Biyomimikri_Ornek_Kartlari.pdf'
    try:
        icerik = read_md_file(md('05_Biyomimikri_Ornek_Kartlari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Biyomimikri Ornek Kartlari',
            subtitle='Dogadan Tasarima - 10 Cift Yuzlu Kart',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '6. Unite - Dogadan Tasarima',
                'Kapsam': '10 Kart: Geko, Lotus, Termit, Balina, Papatyagillan, Kartal, Kirpi, Zambak Caligi, Kus Tuyü, Agac Kabugu',
                'Kullanim': 'Laminasyon onerilen ogretmen materyali',
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
# PDF 6 - CALISMA KAGITLARI (CK1-CK6 birlestirme)
# ============================================================

def uret_calisma_kagitlari():
    cikti = 'Unite6_Calisma_Kagitlari.pdf'
    try:
        build_ck_pdf(
            output_path=pdf(cikti),
            md_filenames=[
                '07_CK1_Biyomimikri_Kesif_Tablosu.md',
                '08_CK2_Biyomimetik_Derinlik_Analizi.md',
                '09_CK3_Doga_Formu_Gozlem_ve_Cizim.md',
                '10_CK4_Biyomimikri_Tasarim_Kartim.md',
                '11_CK5_Disiplinler_Arasi_Problem_Cozum_Haritasi.md',
                '12_CK6_Biyomimikri_Tasarim_Gelistirme_Formu.md',
            ],
            title='6. Unite Calisma Kagitlari',
            subtitle='Dogadan Tasarima - CK1-CK6',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '6. Unite - Dogadan Tasarima',
                'Kapsam': 'CK1: Kesif Tablosu · CK2: Derinlik Analizi · CK3: Gozlem&Cizim · '
                          'CK4: Tasarim Kartim · CK5: Disiplinlerarasi Harita · CK6: Gelistirme Formu',
                'Toplam': '6 Calisma Kagidi (Ders 1-6)',
            },
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))


# ============================================================
# PDF 7 - DEGERLENDIRME ARACLARI (13 + 14 + 15 birlestirme)
# ============================================================

def uret_degerlendirme_araclari():
    cikti = 'Unite6_Degerlendirme_Araclari.pdf'
    try:
        icerik_13 = read_md_file(md('13_Surec_Gozlem_Formu.md'))
        icerik_14 = read_md_file(md('14_Urun_Degerlendirme_Rubrik.md'))
        icerik_15 = read_md_file(md('15_Ogrenci_Oz_ve_Akran_Degerlendirme.md'))
        combined  = (icerik_13
                     + '\n\n<!-- PAGEBREAK -->\n\n'
                     + icerik_14
                     + '\n\n<!-- PAGEBREAK -->\n\n'
                     + icerik_15)
        build_pdf_from_md(
            md_content=combined,
            output_path=pdf(cikti),
            title='6. Unite Degerlendirme Araclari',
            subtitle='Dogadan Tasarima - 3 Degerlendirme Araci',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '6. Unite - Dogadan Tasarima',
                'Araclar': 'Surec Gozlem Formu · Urun Degerlendirme Rubrik · Oz & Akran Degerlendirme',
                'Ag.': 'Surec %20 + Urun Rubrik %40 + Sinav %40 = %100',
            },
            doc_type='Ogretmen Rehberi',
            add_cover=True,
            skip_top_title=False,
            unite_info=UI,
            compact_mode=True,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))


# ============================================================
# PDF 8 - SINAV OGRENCI
# ============================================================

def uret_sinav_ogrenci():
    cikti = 'Unite6_Sinav_Ogrenci.pdf'
    try:
        icerik = read_md_file(md('16_Unite6_Sinav_Ogrenci.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Sinav - Ogrenci Formu',
            subtitle='Dogadan Tasarima',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '6. Unite - Dogadan Tasarima',
                'Puan Dagilimi': 'A: Coktan Secmeli · B: Kisa Cevap · C: Performans',
                'Sure': '40 dakika',
            },
            doc_type='Ogrenci Materyali',
            add_cover=True,
            skip_top_title=True,
            unite_info=UI,
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))


# ============================================================
# PDF 9 - SINAV CEVAP ANAHTARI (AYRI DOSYA)
# ============================================================

def uret_sinav_cevap_anahtari():
    cikti = 'Unite6_Sinav_Cevap_Anahtari.pdf'
    try:
        icerik = read_md_file(md('17_Unite6_Sinav_Cevap_Anahtari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Sinav Cevap Anahtari',
            subtitle='Dogadan Tasarima - OGRETMEN ICIN',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Uyari': 'Bu belge ogrencilere dagitilmaz - yalnizca ogretmen kullanimi',
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
# PDF 10 - GENEL DEGERLENDIRME TABLOSU
# ============================================================

def uret_genel_degerlendirme_tablosu():
    cikti = 'Unite6_Genel_Degerlendirme_Tablosu.pdf'
    try:
        icerik = read_md_file(md('18_Genel_Degerlendirme_Tablosu.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Genel Degerlendirme Tablosu',
            subtitle='Dogadan Tasarima - Sinif Listesi',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '6. Unite - Dogadan Tasarima',
                'Kapsam': 'Tum ogrenciler icin unite sonu notlama tablosu',
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
# PDF 11 - ZENGINLESTIRME PAKETI
# ============================================================

def uret_zenginlestirme_paketi():
    cikti = 'Unite6_Zenginlestirme_Paketi.pdf'
    try:
        icerik = read_md_file(md('19_Zenginlestirme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Zenginlestirme Paketi',
            subtitle='Dogadan Tasarima - Ileri Duzey Etkinlikler',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '6. Unite - Dogadan Tasarima',
                'Hedef': 'Ileri duzeyde ogrenmeye hazir ogrenciler',
                'Etkinlik Sayisi': '7 Etkinlik (Z1-Z7)',
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
# PDF 12 - DESTEKLEME PAKETI
# ============================================================

def uret_destekleme_paketi():
    cikti = 'Unite6_Destekleme_Paketi.pdf'
    try:
        icerik = read_md_file(md('20_Destekleme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Destekleme Paketi',
            subtitle='Dogadan Tasarima - Destek Gerektiren Ogrenciler Icin',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '6. Unite - Dogadan Tasarima',
                'Hedef': 'Destekleme gerektiren ogrenciler',
                'Materyal Sayisi': '5 Materyal (D1-D5)',
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
# PDF 13 - YANSITMA VE KAPANIS
# ============================================================

def uret_yansitma_ve_kapanis():
    cikti = 'Unite6_Yansitma_ve_Kapanis.pdf'
    try:
        icerik = read_md_file(md('21_Ogretmen_Yansitma_ve_Kapanis.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='6. Unite Ogretmen Yansitma ve Kapanis',
            subtitle='Dogadan Tasarima - Ogretmen Gunlugu + Ogrenci Anketi + Zumre Sablonu',
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
    print('6. Unite PDF uretimi basliyor...')
    print()

    gorevler = [
        ('1.  Ders Plani',                              uret_ders_plani),
        ('2.  On Degerlendirme Ogretmen',               uret_on_degerlendirme_ogretmen),
        ('3.  On Degerlendirme Ogrenci 1',              uret_on_degerlendirme_ogrenci_1),
        ('4.  On Degerlendirme Ogrenci 2',              uret_on_degerlendirme_ogrenci_2),
        ('5.  Biyomimikri Ornek Kartlari',              uret_biyomimikri_kartlari),
        ('6.  Calisma Kagitlari (CK1-CK6)',             uret_calisma_kagitlari),
        ('7.  Degerlendirme Araclari',                  uret_degerlendirme_araclari),
        ('8.  Sinav Ogrenci',                           uret_sinav_ogrenci),
        ('9.  Sinav Cevap Anahtari',                    uret_sinav_cevap_anahtari),
        ('10. Genel Degerlendirme Tablosu',             uret_genel_degerlendirme_tablosu),
        ('11. Zenginlestirme Paketi',                   uret_zenginlestirme_paketi),
        ('12. Destekleme Paketi',                       uret_destekleme_paketi),
        ('13. Yansitma ve Kapanis',                     uret_yansitma_ve_kapanis),
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
