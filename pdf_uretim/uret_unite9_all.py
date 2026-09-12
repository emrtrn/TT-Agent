"""
9. Unite - Yapay Zeka ve Akilli Urunler: Tum PDF'leri Uret
Calistir: python pdf_uretim/uret_unite9_all.py

Uretilen PDF'ler (units/7_sinif/unit9/ klasorune kaydedilir):
  1.  Unite9_Ders_Plani.pdf
  2.  Unite9_On_Degerlendirme_Ogretmen.pdf
  3.  Unite9_On_Degerlendirme_Ogrenci_1.pdf
  4.  Unite9_On_Degerlendirme_Ogrenci_2.pdf
  5.  Unite9_Kavram_Kartlari.pdf
  6.  Unite9_Calisma_Kagitlari.pdf           (CK1-CK4 birlestirme)
  7.  Unite9_Degerlendirme_Araclari.pdf      (11+12+15 birlestirme)
  8.  Unite9_Sinav_Ogrenci.pdf
  9.  Unite9_Sinav_Cevap_Anahtari.pdf        (AYRI DOSYA)
  10. Unite9_Zenginlestirme_Paketi.pdf
  11. Unite9_Destekleme_Paketi.pdf
  12. Unite9_Ogretmen_Yansitma_ve_Kapanis.pdf
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
MD_DIR  = os.path.join(ROOT, 'units', 'unit9')
PDF_DIR = os.path.join(ROOT, 'units', 'unit9')

os.makedirs(PDF_DIR, exist_ok=True)

def md(filename):
    return os.path.join(MD_DIR, filename)

def pdf(filename):
    return os.path.join(PDF_DIR, filename)

UI = 'Teknoloji ve Tasarim - 7. Sinif - 9. Unite: Yapay Zeka ve Akilli Urunler'

KAPAK_META = {
    'Sinif': '7',
    'Ders': 'Teknoloji ve Tasarim',
    'Unite': '9. Unite - Yapay Zeka ve Akilli Urunler',
    'Sure': '8 Ders Saati (8 x 40 dk)',
    'Surec': '4 Hafta',
    'Kazanimlar': 'TT.7.9.1 - TT.7.9.4 (4 Kazanim)',
}

uretilen = []
hatalar  = []

# ============================================================
# YARDIMCI: Ozel notasyon on ve son isleme (CK dosyalari icin)
# ============================================================

_WL_RE  = re.compile(r'\[Yazma alanı için (\d+) satır\]')
_DB_RE  = re.compile(
    r'\[Çizim Alanı:\s*(\d+(?:[.,]\d+)?)\s*cm\s*[x×X]\s*(\d+(?:[.,]\d+)?)\s*cm[^\]]*\]'
)
_MM_RE  = re.compile(r'\[MindMapCanvas:[^\]]*\]')


def preprocess_ck_md(content):
    """Ozel notasyonlari benzersiz isaretcilere donustur."""
    content = _WL_RE.sub(lambda m: f'UNIT9_WL_{m.group(1)}', content)
    content = _DB_RE.sub(
        lambda m: f'UNIT9_DB_{m.group(1).replace(",",".")}_{m.group(2).replace(",",".")}',
        content
    )
    content = _MM_RE.sub('UNIT9_MINDMAP', content)
    return content


def postprocess_unit9_flowables(flowables):
    """Isaretci paragraflarini gercek cizim elemanlarina donustur."""
    result = []
    for fl in flowables:
        if isinstance(fl, KeepTogether):
            inner = postprocess_unit9_flowables(fl._content)
            result.append(KeepTogether(inner) if len(inner) > 1 else inner[0] if inner else fl)
            continue
        if isinstance(fl, Paragraph):
            txt = getattr(fl, 'text', '')
            m = re.match(r'UNIT9_WL_(\d+)', txt)
            if m:
                result.append(WritingLines(num_lines=int(m.group(1))))
                continue
            m = re.match(r'UNIT9_DB_(\d+(?:\.\d+)?)_(\d+(?:\.\d+)?)', txt)
            if m:
                result.append(DrawingBox(height=float(m.group(2)) * cm))
                continue
            if txt.strip() == 'UNIT9_MINDMAP':
                result.append(MindMapCanvas(
                    'YAPAY ZEKA & AKILLI URUN', height=9 * cm, num_branches=8))
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
        flowables = postprocess_unit9_flowables(flowables)
        elements.extend(flowables)
        if i < len(md_filenames) - 1:
            elements.append(PageBreak())

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return output_path


# ============================================================
# PDF 1 - DERS PLANI
# ============================================================

def uret_ders_plani():
    cikti = 'Unite9_Ders_Plani.pdf'
    try:
        icerik = read_md_file(md('01_Ders_Plani.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite Ders Plani',
            subtitle='Yapay Zeka ve Akilli Urunler',
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
    cikti = 'Unite9_On_Degerlendirme_Ogretmen.pdf'
    try:
        icerik = read_md_file(md('02_On_Degerlendirme_Ogretmen_Rehberi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite On Degerlendirme',
            subtitle='Yapay Zeka ve Akilli Urunler - Ogretmen Rehberi',
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

S_BAS  = ParagraphStyle('u9_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_BLM  = ParagraphStyle('u9_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LBL  = ParagraphStyle('u9_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11)
S_SML  = ParagraphStyle('u9_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u9_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u9_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u9_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u9_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u9_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)


def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)


SORULAR_O1 = [
    ('Yapay zeka (YZ) kavramini en iyi aciklayan ifade hangisidir?',
     ['A) Insanlara benzeyen fiziksel robotlarin genel adi',
      'B) Bilgisayar programlarinin ogrenme, anlama ve karar verme gibi insan ozelliklerini taklit etmesini saglayan teknoloji',
      'C) Internet baglantisi gerektiren her tur mobil uygulama',
      'D) Sosyal medya platformlarinin yonetim sistemi']),
    ('Makine ogrenmesi ne anlama gelir?',
     ['A) Fabrika makinelerinin birbirini otomatik olarak tamir etmesi',
      'B) Bilgisayarin buyuk miktarda veriden oruntu cikararek belirli gorevlerde kendi kendine gelismesi',
      'C) Insanlarin bilgisayara geleneksel ders anlatimi yontemiyle bilgi aktarmasi',
      'D) Makinelerin calisma hizlarini optimize etmesi']),
    ('Derin ogrenme (deep learning) ile ilgili hangisi dogrudur?',
     ['A) Derin ogrenme, kitap okuyarak gerceklesen bir ogrenme sureicidir',
      'B) Derin ogrenme, katmanli yapay sinir aglarini kullanarak buyuk verilerden anlam cikaran bir makine ogrenmesi yaklasımidir',
      'C) Derin ogrenme yalnizca matematik problemleri icin kullanilir',
      'D) Derin ogrenme, robotlarin hareket etmesini saglayan mekanik bir sistemdir']),
    ('Asagidakilerden hangisi yapay zeka kullanan bir uygulama ornegi dir?',
     ['A) Toplama, cikarma islemi yapan basit bir hesap makinesi uygulamasi',
      'B) Belge olusturmak icin kullanilan bir metin duzenleyici program',
      "C) Muzik uygulamasinin dinleme gecmisine gore 'Sana Ozel' calma listesi olusturmasi",
      'D) Saati gosteren dijital bir alarmli saat uygulamasi']),
    ("'Istem muhendisligi' (prompt engineering) ne anlama gelir?",
     ['A) Bir yapay zeka modelini sifirdan yazilim kodlariyla programlama',
      'B) Yapay zekadan dogru ve ise yarar sonuclar elde etmek icin etkili talimatlar (istemler) yazma becerisi',
      'C) Bir bilgisayarin donanim bilesenlerini tasarlama ve uretme sureci',
      'D) Yapay zeka araclarini yalnizca Ingilizce dilinde kullanma zorunlulugu']),
    ("Yapay zekanin 'halusinasyon' yapmasi ne demektir?",
     ['A) Yapay zekanin ekran goruntusу alamamasi ve goruntu isleme hatasi vermesi',
      'B) Yapay zekanin cok fazla veri isleydiginde asiri yavashlamasi',
      'C) Yapay zekanin var olmayan, yanlis veya uydurulmus bilgileri gercékmis gibi guvenle sunmasi',
      'D) Yapay zekanin internet baglantisi kesildiginde calismаyi durdurması']),
    ('Yapay zekanin insanlara gore en belirgin avantaji nedir?',
     ['A) Her konuda insan gibi ozgun ve yaratici dusunebilmesi',
      'B) Buyuk veri kumelerini cok hizla isleyerek belirli oruntuleri insandan daha hizli bulabilmesi',
      'C) Duygusal zekasinin insandan ustun olmasi',
      'D) Her kosulda her zaman dogru ve guvenilir sonuc uretmesi']),
    ("'Akilli urun' kavramini en iyi tanimlayan ifade hangisidir?",
     ['A) Pahali ve modern bir gorunume sahip olan her teknolojik urun',
      'B) Yalnizca internete baglanabilen her elektronik cihaz',
      'C) Algilayicilar (sensorler) araciligiyla cevresini algilayan, bu veriyi isleyen ve duruma gore tepki veren urun',
      'D) Siyah renkte tasarlanmis ve minimum malzeme kullanan urunler']),
]


def uret_on_degerlendirme_ogrenci_1():
    cikti = 'Unite9_On_Degerlendirme_Ogrenci_1.pdf'
    try:
        doc = create_doc(pdf(cikti), title='On Degerlendirme - Ogrenci Formu 1', unite_info=UI)
        E   = []

        # --- SAYFA 1: Zihin Haritasi ---
        E.append(make_student_info_header())
        E.append(vsp(0.2))
        E.append(Paragraph(
            '<b>Not:</b> Bu calisma not icin degildir. Bildiklerini durustce yaz - yanlis cevap olmaz!',
            S_NOT))
        E.append(vsp(0.15))
        E.append(sep())
        E.append(vsp(0.2))
        E.append(Paragraph('ARAC 1: ZIHIN HARITASI', S_BAS))
        E.append(Paragraph(
            '<b>Yonerge:</b> Asagida iki anahtar kelime var: <b>YAPAY ZEKA</b> ve <b>AKILLI URUN</b>. '
            'Bu kelimeleri duyduqunda aklina hangi kelimeler, kavramlar, nesneler, ornekler geliyor? '
            'Aklina gelen her seyi oklarla baglayarak yaz. <b>Sure: 5 dakika</b>',
            S_YON))
        E.append(vsp(0.15))
        E.append(MindMapCanvas('YAPAY ZEKA & AKILLI URUN', width=17 * cm, height=9.5 * cm, num_branches=8))
        E.append(vsp(0.2))
        E.append(Paragraph('<b>Son soru:</b> Sence yapay zeka ile akilli urun birbiriyle nasil ilisкilidir?', S_SMBD))
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
            '<b>Yonerge:</b> Her sorunun iki kismi var. Once dogru secenegi daire icine al, '
            'sonra neden o secenegi sectigini acikla. Bilmiyorsan "Tahminim su:" diye basla. '
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
    cikti = 'Unite9_On_Degerlendirme_Ogrenci_2.pdf'
    try:
        icerik = read_md_file(md('04_On_Degerlendirme_Ogrenci_2.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='On Degerlendirme - Ogrenci Formu 2',
            subtitle='Yapay Zeka ve Akilli Urunler',
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
# PDF 5 - KAVRAM KARTLARI
# ============================================================

def uret_kavram_kartlari():
    cikti = 'Unite9_Kavram_Kartlari.pdf'
    try:
        icerik = read_md_file(md('05_Kavram_Kartlari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite Kavram Kartlari',
            subtitle='Yapay Zeka ve Akilli Urunler - 12 Kart, 4 Renk Grubu',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '9. Unite - Yapay Zeka ve Akilli Urunler',
                'Kart Sayisi': '12 Kart (Mavi / Turuncu / Yesil / Mor)',
                'Kullanim': 'Laminasyon ile kalici kullanim onerilir',
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
# PDF 6 - CALISMA KAGITLARI (CK1-CK4 birlestirme)
# ============================================================

def uret_calisma_kagitlari():
    cikti = 'Unite9_Calisma_Kagitlari.pdf'
    try:
        build_ck_pdf(
            output_path=pdf(cikti),
            md_filenames=[
                '07_CK1_YZ_Kavram_Siniflandirma.md',
                '08_CK2_Prompt_Deney.md',
                '09_CK3_Model_Egitimi_Halusinasyon.md',
                '10_CK4_Akilli_Urun_Tasarim.md',
            ],
            title='9. Unite Calisma Kagitlari',
            subtitle='Yapay Zeka ve Akilli Urunler - CK1-CK4',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '9. Unite - Yapay Zeka ve Akilli Urunler',
                'Kapsam': 'CK1: Kavram Siniflandirma · CK2: Prompt Deney · CK3: Model Egitimi · CK4: Akilli Urun Tasarim',
                'Not': 'CK3 icin halusinasyon ornekleri baski oncesi eklenmelidir.',
            },
        )
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 7 - DEGERLENDIRME ARACLARI (11 + 12 + 15 birlestirme)
# ============================================================

def uret_degerlendirme_araclari():
    cikti = 'Unite9_Degerlendirme_Araclari.pdf'
    try:
        icerik_11 = read_md_file(md('11_Surec_Gozlem_Formu.md'))
        icerik_12 = read_md_file(md('12_Urun_Degerlendirme_Rubrik.md'))
        icerik_15 = read_md_file(md('15_Akran_Oz_Degerlendirme.md'))
        combined  = (icerik_11
                     + '\n\n<!-- PAGEBREAK -->\n\n'
                     + icerik_12
                     + '\n\n<!-- PAGEBREAK -->\n\n'
                     + icerik_15)
        build_pdf_from_md(
            md_content=combined,
            output_path=pdf(cikti),
            title='9. Unite Degerlendirme Araclari',
            subtitle='Yapay Zeka ve Akilli Urunler - 3 Degerlendirme Araci',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '9. Unite - Yapay Zeka ve Akilli Urunler',
                'Araclar': 'Surec Gozlem Formu (%20) · Urun Degerlendirme Rubrik · Akran/Oz Degerlendirme',
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
    cikti = 'Unite9_Sinav_Ogrenci.pdf'
    try:
        icerik = read_md_file(md('13_Sinav_Ogrenci.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite Sinav - Ogrenci Formu',
            subtitle='Yapay Zeka ve Akilli Urunler',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '9. Unite - Yapay Zeka ve Akilli Urunler',
                'Puan Dagilimi': 'A: Coktan Secmeli 8x5=40 · B: Kisa Cevap 3x10=30 · C: Performans 30',
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
    cikti = 'Unite9_Sinav_Cevap_Anahtari.pdf'
    try:
        icerik = read_md_file(md('14_Sinav_Cevap_Anahtari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite Sinav Cevap Anahtari',
            subtitle='Yapay Zeka ve Akilli Urunler - OGRETMEN ICIN',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Uyari': 'Bu belge ogrencilere dagitilmaz — yalnizca ogretmen kullanimi',
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
# PDF 10 - ZENGINLESTIRME PAKETI
# ============================================================

def uret_zenginlestirme_paketi():
    cikti = 'Unite9_Zenginlestirme_Paketi.pdf'
    try:
        icerik = read_md_file(md('16_Unite9_Zenginlestirme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite Zenginlestirme Paketi',
            subtitle='Yapay Zeka ve Akilli Urunler - Ileri Duzey Etkinlikler',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '9. Unite - Yapay Zeka ve Akilli Urunler',
                'Hedef': 'Ileri duzeyde ogrenmeye hazir ogrenciler',
                'Etkinlik Sayisi': '6 Etkinlik',
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
    cikti = 'Unite9_Destekleme_Paketi.pdf'
    try:
        icerik = read_md_file(md('17_Unite9_Destekleme_Paketi.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite Destekleme Paketi',
            subtitle='Yapay Zeka ve Akilli Urunler - Destek Gerektiren Ogrenciler',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '9. Unite - Yapay Zeka ve Akilli Urunler',
                'Hedef': 'Destekleme gerektiren ogrenciler',
                'Materyal Sayisi': '5 Materyal',
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
    cikti = 'Unite9_Ogretmen_Yansitma_ve_Kapanis.pdf'
    try:
        icerik = read_md_file(md('18_Unite9_Ogretmen_Yansitma_ve_Kapanis.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='9. Unite Ogretmen Yansitma ve Kapanis',
            subtitle='Yapay Zeka ve Akilli Urunler - 5 Arac + 8. Sinif Koprusu',
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
    print('9. Unite PDF uretimi basliyor...')
    print()

    gorevler = [
        ('1.  Ders Plani',                         uret_ders_plani),
        ('2.  On Degerlendirme Ogretmen',            uret_on_degerlendirme_ogretmen),
        ('3.  On Degerlendirme Ogrenci 1',           uret_on_degerlendirme_ogrenci_1),
        ('4.  On Degerlendirme Ogrenci 2',           uret_on_degerlendirme_ogrenci_2),
        ('5.  Kavram Kartlari',                      uret_kavram_kartlari),
        ('6.  Calisma Kagitlari (CK1-CK4)',          uret_calisma_kagitlari),
        ('7.  Degerlendirme Araclari',               uret_degerlendirme_araclari),
        ('8.  Sinav Ogrenci',                        uret_sinav_ogrenci),
        ('9.  Sinav Cevap Anahtari',                 uret_sinav_cevap_anahtari),
        ('10. Zenginlestirme Paketi',                uret_zenginlestirme_paketi),
        ('11. Destekleme Paketi',                    uret_destekleme_paketi),
        ('12. Ogretmen Yansitma ve Kapanis',         uret_yansitma_ve_kapanis),
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
