# -*- coding: utf-8 -*-
"""
5. Unite - Mimari Tasarim: Tum PDF'leri Uret
Calistirir: python pdf_uretim/uret_unite5_all.py

Uretilen PDF'ler (units/7_sinif/unit5/ klasorune kaydedilir):
  1. U5_PDF_01_Ders_Plani.pdf
  2. U5_PDF_02_On_Degerlendirme.pdf
  3. U5_PDF_03_Calisma_Kagitlari.pdf
  4. U5_PDF_04_Degerlendirme.pdf
  5. U5_PDF_05_Destekleme.pdf
  6. U5_PDF_06_Zenginlestirme.pdf
  7. U5_PDF_Kavram_Kartlari.pdf
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
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
MD_DIR  = os.path.join(ROOT, 'units', 'unit5')
PDF_DIR = os.path.join(ROOT, 'units', 'unit5')

os.makedirs(PDF_DIR, exist_ok=True)

def md(filename):
    return os.path.join(MD_DIR, filename)

def pdf(filename):
    return os.path.join(PDF_DIR, filename)

UI = 'Teknoloji ve Tasarim - 7. Sinif - 5. Unite: Mimari Tasarim'

KAPAK_META = {
    'Sinif': '7',
    'Ders': 'Teknoloji ve Tasarim',
    'Unite': '5. Unite - Mimari Tasarim',
    'Sure': '8 Ders Saati (8 x 40 dk)',
    'Surec': '4 Hafta',
    'Kazanimlar': 'TT.7.5.1 - TT.7.5.4 (4 Kazanim)',
}

uretilen = []
hatalar  = []

# ============================================================
# PAYLAŞILAN STILLER
# ============================================================

S_BAS  = ParagraphStyle('u5_BAS',  fontName='TR-Bold',    fontSize=11, textColor=COLOR_PRIMARY,   leading=14, spaceBefore=6, spaceAfter=3)
S_SMBD = ParagraphStyle('u5_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SORU = ParagraphStyle('u5_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=4, spaceAfter=2)
S_OPT  = ParagraphStyle('u5_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, leftIndent=6)
S_YON  = ParagraphStyle('u5_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12,
                         backColor=COLOR_VERY_LIGHT, borderPad=6, borderColor=COLOR_ACCENT, borderWidth=0.8,
                         leftIndent=6, rightIndent=6, spaceBefore=4, spaceAfter=4)
S_NOT  = ParagraphStyle('u5_NOT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11, spaceBefore=2)
S_AU3  = ParagraphStyle('u5_AU3',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceBefore=3)

# Degerlendirme icin kompakt stiller
S_DEG_SORU = ParagraphStyle('u5_DEG_SORU', fontName='TR-Bold',    fontSize=8,   textColor=COLOR_TEXT, leading=10, spaceBefore=5)
S_DEG_OPT  = ParagraphStyle('u5_DEG_OPT',  fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT, leading=10, leftIndent=8)
S_DEG_YON  = ParagraphStyle('u5_DEG_YON',  fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT, leading=11,
                              backColor=COLOR_VERY_LIGHT, borderPad=5, borderColor=COLOR_ACCENT, borderWidth=0.8,
                              leftIndent=6, rightIndent=6, spaceBefore=3, spaceAfter=3)
S_DEG_META = ParagraphStyle('u5_DEG_META', fontName='TR-Regular', fontSize=8,   textColor=COLOR_MUTED, leading=11, spaceBefore=2)

def sep():
    return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)

def vsp(h=0.2):
    return Spacer(1, h * cm)

# ============================================================
# PDF 1 - DERS PLANI
# ============================================================

def uret_ders_plani():
    cikti = 'U5_PDF_01_Ders_Plani.pdf'
    try:
        icerik = read_md_file(md('U5_MD_01_Ders_Plani.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='5. Unite Ders Plani',
            subtitle='Mimari Tasarim',
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
# PDF 2 - ON DEGERLENDIRME (birlesik, maks 2 sayfa)
# ============================================================

SORULAR_OD = [
    (
        '“Antropometri” kavramı ne anlama gelir?',
        [
            'A) Arazinin eğimini ve yüzeyini inceleyen bilim dalı',
            'B) İnsan bedeninin ölçülerini ve oranlarını inceleyen bilim dalı',
            'C) Yapıların depreme dayanıklılığını hesaplayan alan',
            'D) Binalarda enerji tasarrufu sağlayan yöntemler',
        ]
    ),
    (
        'Çok yağış alan ve karlı kış geçiren bir bölgede evlerin çatıları genellikle nasıl olur?',
        [
            'A) Düz ve geniş',
            'B) Dik ve yüksek',
            'C) Cam kaplı',
            'D) Açık avlulu',
        ]
    ),
    (
        'Aşağıdakilerden hangisi “sürdürülebilir mimari” için en iyi örnektir?',
        [
            'A) Binanın her odasına ayrı klima takılması',
            'B) Çatıya güneş paneli yerleştirilerek enerji üretilmesi',
            'C) Binanın yüksek tavanlı yapılması',
            'D) Dış cephenin parlak renklerle boyanması',
        ]
    ),
    (
        '“Kat planı” nedir?',
        [
            'A) Binanın dışından çekilen fotoğraf',
            'B) Yapının yan duvarının görünüşü',
            'C) Yapının bir katının yukarıdan çizilen yatay kesit planı',
            'D) Binanın temelinin derinliğini gösteren çizim',
        ]
    ),
    (
        '“Topografya” kavramı mimarlık açısından ne anlama gelir?',
        [
            'A) Binanın renk ve cephe tasarımı',
            'B) Kullanılan yapı malzemelerinin listesi',
            'C) Yapının iç mekan düzenlenmesi',
            'D) Arazinin yüzey biçimi, eğimi ve yükseklik özellikleri',
        ]
    ),
]

ACIK_UCLU_OD = [
    (
        'Yaşadığın yerdeki evler nasıl görünüyor? '
        'Çatıları ne şekilde, malzemeleri ne? '
        'Sence bu evler neden böyle yapılmış olabilir?',
        3
    ),
    (
        'Bir ev tasar larken nelere dikkat edilmeli? En önemli gördüğün 3 şeyi yaz.',
        3
    ),
]


def uret_on_degerlendirme():
    cikti = 'U5_PDF_02_On_Degerlendirme.pdf'
    try:
        doc = create_doc(pdf(cikti), title='On Degerlendirme - Mimari Tasarim', unite_info=UI)
        E   = []

        E.append(make_student_info_header())
        E.append(vsp(0.15))
        E.append(Paragraph(
            '<b>\xd6ğretmen Notu:</b> Bu araçlar notla ölçülmez. '
            '1. ders saatinin ilk 20 dakikasında uygulanır. '
            'Zihin haritası toplanır ve ünite sonunda iade edilir.',
            S_NOT))
        E.append(Paragraph(
            'Bu çalışma <b>not için değildir.</b> '
            'Doğru ya da yanlış cevap yoktur — içinden geldiği gibi yaz!',
            S_NOT))
        E.append(vsp(0.1))
        E.append(sep())

        E.append(vsp(0.15))
        E.append(Paragraph('ARAÇ 1: ZİHİN HARİTASI', S_BAS))
        E.append(Paragraph(
            '<b>Yönerge:</b> <b>MİMARLIK</b> ve <b>BİNA</b> sözcüklerini duyunca '
            'aklına neler geliyor? Kavramları, örnekleri, meslekleri — '
            'aklına gelen her şeyi yaz; oklar çizerek birbiriyle bağla. '
            '<b>Süre: 5 dakika</b>',
            S_YON))
        E.append(vsp(0.1))
        E.append(MindMapCanvas('MİMARLIK / BİNA', width=17 * cm, height=7.0 * cm, num_branches=8))
        E.append(vsp(0.15))
        E.append(Paragraph(
            '<b>Son soru:</b> Sence “mimari” ile “tasarım” arasında nasıl bir ilişki var?',
            S_SMBD))
        E.append(WritingLines(num_lines=2))
        E.append(vsp(0.1))
        E.append(sep())

        E.append(vsp(0.1))
        E.append(Paragraph('ARAÇ 2: İKİ AŞAMALI TANILAMA TESTİ', S_BAS))
        E.append(Paragraph(
            '<b>Yönerge:</b> Her soruda önce seçeneği işaretle (A/B/C/D), '
            'sonra neden o seçeneği seçtiğini kısaca açıkla. '
            'Emin değilsen “Emin değilim ama...” diye başla. '
            '<b>Süre: 10 dakika</b>',
            S_YON))
        E.append(vsp(0.1))

        for i, (soru, secenekler) in enumerate(SORULAR_OD, 1):
            blok = []
            blok.append(Paragraph(f'<b>Soru {i}.</b> {soru}', S_SORU))
            for s in secenekler:
                blok.append(Paragraph(s, S_OPT))
            blok.append(vsp(0.08))
            blok.append(Paragraph('<b>Neden bu seçeneği seçtiniz?</b>', S_SMBD))
            blok.append(WritingLines(num_lines=1))
            blok.append(sep())
            blok.append(vsp(0.08))
            E.append(KeepTogether(blok))

        E.append(vsp(0.1))
        E.append(Paragraph('ARAÇ 3: AÇIK UÇLU SORULAR', S_BAS))
        E.append(Paragraph('<b>Süre: 5 dakika</b> — 1-2 cümle yeterli.', S_YON))
        E.append(vsp(0.1))

        for j, (soru, satirsayisi) in enumerate(ACIK_UCLU_OD, 1):
            blok = []
            blok.append(Paragraph(f'<b>Soru {j}.</b> {soru}', S_AU3))
            blok.append(WritingLines(num_lines=satirsayisi))
            E.append(KeepTogether(blok))

        doc.build(E, onFirstPage=add_page_number, onLaterPages=add_page_number)
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# ============================================================
# PDF 3 - CALISMA KAGITLARI
# ============================================================

def uret_calisma_kagitlari():
    cikti = 'U5_PDF_03_Calisma_Kagitlari.pdf'
    try:
        icerik = read_md_file(md('U5_MD_03_Calisma_Kagitlari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='5. Unite Calisma Kagitlari',
            subtitle='Mimari Tasarim - CK1 ile CK6',
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
# PDF 4 - DEGERLENDIRME SINAVI (10 soru, tek sayfa)
# ============================================================

SORULAR_DEG = [
    (
        '“Antropometri” kavramı neyi inceler?',
        [
            'A) Arazinin yüzey biçimini ve eğimini',
            'B) Binaların depreme dayanıklılığını',
            'C) İnsan bedeninin ölçülerini ve oranlarını',
            'D) Güneş ışınlarının binalara etkisini',
        ]
    ),
    (
        'Kuzey yarımkürede (Türkiye’de) bir evin oturma odası gün boyu en fazla güneş ışığı almak için hangi yöne bakmalıdır?',
        [
            'A) Kuzey',
            'B) Doğu',
            'C) Batı',
            'D) Güney',
        ]
    ),
    (
        'Çok kar yağan dağlık bir bölgede ev çatıları neden dik ve yüksek yapılır?',
        [
            'A) Güneş ışığından daha fazla yararlanmak için',
            'B) Karın birikmeden kaymasını sağlamak için',
            'C) Hava sirkülasyonunu artırmak için',
            'D) Binanın görünümünü güzelleştirmek için',
        ]
    ),
    (
        '”Sürdürülebilir mimari” için en iyi örnek hangisidir?',
        [
            'A) Her kata ayrı ısıtma sistemi kurulması',
            'B) Dış cephenin her yıl boyanması',
            'C) Çatıya güneş paneli ile yenilenebilir enerji üretilmesi',
            'D) Binaya mümkün olduğunca fazla pencere eklenmesi',
        ]
    ),
    (
        '“Kat planı” nasıl elde edilir?',
        [
            'A) Binanın dışından fotoğraf çekilerek',
            'B) Yapının bir katının yukarıdan yatay olarak çizilmesiyle',
            'C) Binanın yan duvarının görünüşü çizilerek',
            'D) Yapının temel derinliği hesaplanarak',
        ]
    ),
    (
        'Mardin ve çevresindeki geleneksel evler neden taş ve yassı çatılıdır?',
        [
            'A) Ahşap malzeme bulunamadığı için',
            'B) Sıcak ve kurak iklimde aşırı yağış olmadığı için',
            'C) Deprem riskine karşı daha dayanıklı olduğu için',
            'D) Uzak görüntü sağlaması için',
        ]
    ),
    (
        'UNESCO Dünya Mirası listesindeki geleneksel Osmanlı sivil mimarisinin en iyi korunmuş örnekleri hangi şehirdedir?',
        [
            'A) Nevşehir',
            'B) Edirne',
            'C) Safranbolu',
            'D) Trabzon',
        ]
    ),
    (
        '“Erişilebilirlik” ilkesi mimari açıdan ne anlama gelir?',
        [
            'A) Binanın şehir merkezine yakın konumlandırılması',
            'B) Engelli ve yaşlı bireyler dahil herkesin yapıya ulaşabilmesi',
            'C) Binanın birden fazla girişe sahip olması',
            'D) Yapıya araçla ulaşılabilmesi',
        ]
    ),
    (
        '1:50 ölçekli bir kat planında 4 cm’lik çizgi gerçekte kaç metreye karşılık gelir?',
        [
            'A) 4 m',
            'B) 50 m',
            'C) 2 m',
            'D) 0,4 m',
        ]
    ),
    (
        '“Topografya” kavramını doğru tanımlayan ifade hangisidir?',
        [
            'A) Binanın renk ve cephe tasarımı',
            'B) Arazinin yüzey biçimi, eğimi ve yükseklik özellikleri',
            'C) Yapıda kullanılan malzemelerin listesi',
            'D) Binanın iç mekan düzenlenmesi',
        ]
    ),
]


def uret_degerlendirme():
    cikti = 'U5_PDF_04_Degerlendirme.pdf'
    try:
        doc = create_doc(pdf(cikti), title='Unite Sonu Degerlendirme - Mimari Tasarim', unite_info=UI)
        E   = []

        E.append(make_student_info_header())
        E.append(vsp(0.1))
        E.append(Paragraph(
            '<b>Ders:</b> Teknoloji ve Tasarım  |  '
            '<b>Ünite:</b> 5 — Mimari Tasarım  |  '
            '<b>Süre:</b> 35 dakika  |  '
            '<b>Puan:</b> 100',
            S_DEG_META))
        E.append(vsp(0.08))
        E.append(Paragraph(
            'Her sorunun yalnızca bir doğru cevabı vardır. '
            'Doğru seçeneği daire içine alın. '
            '<b>(Her soru 10 puan)</b>',
            S_DEG_YON))
        E.append(vsp(0.1))
        E.append(sep())
        E.append(vsp(0.1))

        for i, (soru, secenekler) in enumerate(SORULAR_DEG, 1):
            blok = []
            blok.append(Paragraph(f'<b>{i}.</b> {soru}', S_DEG_SORU))
            for s in secenekler:
                blok.append(Paragraph(s, S_DEG_OPT))
            E.append(KeepTogether(blok))

        # ---- SAYFA 2: CEVAP ANAHTARI ----
        E.append(PageBreak())

        E.append(Paragraph(
            'Öğretmen İçin — Cevap Anahtarı',
            S_BAS))
        E.append(Paragraph(
            'Ünite 5: Mimari Tasarım — Ünite Sonu Değerlendirme Sınavı',
            S_DEG_META))
        E.append(vsp(0.1))
        E.append(Paragraph(
            'Bu sayfa öğrencilerle paylaşılmaz — yalnızca öğretmen kullanımı içindir.',
            S_CA_NOT))
        E.append(vsp(0.2))
        E.append(sep())
        E.append(vsp(0.2))

        col_w = [1.3 * cm, 3.2 * cm, 12.5 * cm]
        tablo_veri = [[
            Paragraph('<b>Soru</b>', S_CA_HDR),
            Paragraph('<b>Doğru Cevap</b>', S_CA_HDR),
            Paragraph('<b>Ölçülen Kavram</b>', S_CA_HDR),
        ]]
        for no, cevap, kavram in CEVAP_ANAHTARI:
            tablo_veri.append([
                Paragraph(str(no), S_CA_NO),
                Paragraph(f'<b>{cevap}</b>', S_CA_ANS),
                Paragraph(kavram, S_CA_CELL),
            ])

        tablo = Table(tablo_veri, colWidths=col_w, repeatRows=1)
        tablo.setStyle(TableStyle([
            ('BACKGROUND',     (0, 0), (-1, 0),  COLOR_VERY_LIGHT),
            ('LINEBELOW',      (0, 0), (-1, 0),  1.2, COLOR_PRIMARY),
            ('GRID',           (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_VERY_LIGHT_GREY, None]),
            ('VALIGN',         (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING',     (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING',  (0, 0), (-1, -1), 4),
            ('LEFTPADDING',    (0, 0), (-1, -1), 6),
            ('RIGHTPADDING',   (0, 0), (-1, -1), 6),
        ]))
        E.append(tablo)
        E.append(vsp(0.45))

        E.append(Paragraph(
            '<b>Not:</b> Yalnızca yanlış cevabı cezalandırmayın. '
            'Mantıklı gerekçe sunan öğrencilere kısmi puan verilebilir.',
            S_CA_NOT))

        doc.build(E, onFirstPage=add_page_number, onLaterPages=add_page_number)
        return cikti
    except Exception as e:
        return ('HATA', cikti, str(e))

# Cevap anahtari stilleri ve sabitleri
S_CA_HDR  = ParagraphStyle('u5_CA_HDR',  fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_PRIMARY,   leading=11)
S_CA_CELL = ParagraphStyle('u5_CA_CELL', fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,      leading=11)
S_CA_NO   = ParagraphStyle('u5_CA_NO',   fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_PRIMARY,   leading=11, alignment=1)
S_CA_ANS  = ParagraphStyle('u5_CA_ANS',  fontName='TR-Bold',    fontSize=9,   textColor=COLOR_SECONDARY, leading=11, alignment=1)
S_CA_NOT  = ParagraphStyle('u5_CA_NOT',  fontName='TR-Italic',  fontSize=8,   textColor=COLOR_MUTED,     leading=11)

CEVAP_ANAHTARI = [
    (1,  'C', 'Antropometri — insan bedeni ölçüleri ve oranları'),
    (2,  'D', 'Güneş yönü — kuzey yarımkürede güney cephe'),
    (3,  'B', 'İklim-çatı ilişkisi — karlı bölgede dik ve yüksek çatı'),
    (4,  'C', 'Sürdürülebilir mimari — güneş paneli / yenilenebilir enerji'),
    (5,  'B', 'Kat planı — bir katın yukarıdan yatay kesit çizimi'),
    (6,  'B', 'Bölgesel mimari — Mardin; sıcak ve kurak iklim, yassı çatı'),
    (7,  'C', 'UNESCO mirası — Safranbolu; geleneksel Osmanlı sivil mimarisi'),
    (8,  'B', 'Erişilebilirlik — engelli ve yaşlı dahil herkesin yapıya ulaşması'),
    (9,  'C', 'Ölçek hesabı — 1:50 ölçeğinde 4 cm = 200 cm = 2 m'),
    (10, 'B', 'Topografya — arazinin yüzey biçimi, eğimi ve yükseklik özellikleri'),
]

# ============================================================
# PDF 5 - DESTEKLEME
# ============================================================

def uret_destekleme():
    cikti = 'U5_PDF_05_Destekleme.pdf'
    try:
        icerik = read_md_file(md('U5_MD_05_Destekleme.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='5. Unite Destekleme',
            subtitle='Mimari Tasarim - Destek Gerektiren Ogrenciler Icin',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '5. Unite - Mimari Tasarim',
                'Hedef': 'Destekleme gerektiren ogrenciler',
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
# PDF 6 - ZENGINLESTIRME
# ============================================================

def uret_zenginlestirme():
    cikti = 'U5_PDF_06_Zenginlestirme.pdf'
    try:
        icerik = read_md_file(md('U5_MD_06_Zenginlestirme.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='5. Unite Zenginlestirme',
            subtitle='Mimari Tasarim - Ileri Duzey Etkinlikler',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '5. Unite - Mimari Tasarim',
                'Hedef': 'Ileri duzeyde ogrenmeye hazir ogrenciler',
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
# PDF 7 - KAVRAM KARTLARI
# ============================================================

def uret_kavram_kartlari():
    cikti = 'U5_PDF_Kavram_Kartlari.pdf'
    try:
        icerik = read_md_file(md('U5_MD_Kavram_Kartlari.md'))
        build_pdf_from_md(
            md_content=icerik,
            output_path=pdf(cikti),
            title='5. Unite Kavram Kartlari',
            subtitle='Mimari Tasarim - 17 Anahtar Kavram',
            meta_info={
                'Sinif': '7',
                'Ders': 'Teknoloji ve Tasarim',
                'Unite': '5. Unite - Mimari Tasarim',
                'Kapsam': '17 Kavram: 4 Renk Grubu',
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
# ANA CALISTIRICI
# ============================================================

if __name__ == '__main__':
    print('5. Unite PDF uretimi basliyor...')
    print()

    gorevler = [
        ('1. Ders Plani',        uret_ders_plani),
        ('2. On Degerlendirme',  uret_on_degerlendirme),
        ('3. Calisma Kagitlari', uret_calisma_kagitlari),
        ('4. Degerlendirme',     uret_degerlendirme),
        ('5. Destekleme',        uret_destekleme),
        ('6. Zenginlestirme',    uret_zenginlestirme),
        ('7. Kavram Kartlari',   uret_kavram_kartlari),
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
            print(f'  {h[1]}: {h[2]}')
