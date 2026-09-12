# -*- coding: utf-8 -*-
"""
2. Unite - Calisma Kagitlari (Kombine, tek PDF)
Calistirir: python pdf_uretim/uret_unite2_calisma_kagitlari_kombine.py
Uretilen PDF: units/7_sinif/unit2/U2_PDF_03_Calisma_Kagitlari.pdf
- Kapak sayfasi YOK
- 6 calisma kagidi, her biri bir sayfada
- Baslik formati: "Calisma Kagidi N - Baslik" (Unit 1 uyumlu)
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak,
)
from pdf_style import (
    register_fonts, add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, DrawingBox,
)

register_fonts()

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, 'units', 'unit2')
os.makedirs(PDF_DIR, exist_ok=True)

CIKTI     = os.path.join(PDF_DIR, 'U2_PDF_03_Calisma_Kagitlari.pdf')
UNITE_ADI = 'Teknoloji ve Tasarım — 7. Sınıf — 2. Ünite: Temel Tasarım'

# ============================================================
# STİLLER
# ============================================================

S_CK    = ParagraphStyle('ck2_CK',   fontName='TR-Bold',    fontSize=10.5, textColor=white,
                          leading=13, alignment=TA_LEFT,
                          backColor=COLOR_PRIMARY, borderPad=5,
                          spaceBefore=0, spaceAfter=3)
S_META  = ParagraphStyle('ck2_META', fontName='TR-Regular', fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=3)
S_ADIM  = ParagraphStyle('ck2_ADIM', fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=11, spaceBefore=4, spaceAfter=2)
S_GOV   = ParagraphStyle('ck2_GOV',  fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,
                          leading=11, spaceAfter=3,
                          backColor=COLOR_VERY_LIGHT, leftIndent=5, rightIndent=5, borderPad=4)
S_BODY  = ParagraphStyle('ck2_BODY', fontName='TR-Regular', fontSize=8,   textColor=COLOR_TEXT,
                          leading=11, spaceAfter=2)
S_NOTE  = ParagraphStyle('ck2_NOTE', fontName='TR-Italic',  fontSize=7.5, textColor=COLOR_MUTED,
                          leading=10, spaceAfter=2)
S_LABEL = ParagraphStyle('ck2_LBL',  fontName='TR-Bold',    fontSize=8,   textColor=COLOR_TEXT,
                          leading=11, spaceAfter=1)
S_BOLUM = ParagraphStyle('ck2_BLM',  fontName='TR-Bold',    fontSize=8.5, textColor=COLOR_SECONDARY,
                          leading=11, spaceAfter=2)
S_KUCUK = ParagraphStyle('ck2_KCK',  fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,
                          leading=10, spaceAfter=1)
S_TH    = ParagraphStyle('ck2_TH',   fontName='TR-Bold',    fontSize=7.5, textColor=white,
                          alignment=TA_CENTER, leading=10)
S_TD    = ParagraphStyle('ck2_TD',   fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,
                          alignment=TA_LEFT,   leading=10)
S_TD_C  = ParagraphStyle('ck2_TDC',  fontName='TR-Regular', fontSize=7.5, textColor=COLOR_TEXT,
                          alignment=TA_CENTER, leading=10)

TABLE_STYLE_BASE = [
    ('BACKGROUND',    (0, 0), (-1, 0), COLOR_PRIMARY),
    ('LINEBELOW',     (0, 0), (-1, 0), 1,   COLOR_SECONDARY),
    ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
    ('TOPPADDING',    (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, 0),  3),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ('LEFTPADDING',   (0, 0), (-1, -1), 4),
    ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
    ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
]


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def vsp(h=0.15):
    return Spacer(1, h * cm)


def ck_baslik(no, baslik, kazanim):
    """Unit 1 uyumlu renkli başlık bandı + meta satır."""
    blok = []
    blok.append(Paragraph(f'Çalışma Kâğıdı {no} — {baslik}', S_CK))
    blok.append(Paragraph(f'Kazanım: {kazanim}', S_META))
    return blok


def ad_satiri():
    cols = [
        Paragraph('Ad Soyad: ______________________', S_LABEL),
        Paragraph('Sınıf/No: _________', S_LABEL),
        Paragraph('Tarih: ____________', S_LABEL),
    ]
    t = Table([cols], colWidths=[8.5 * cm, 4.25 * cm, 4.25 * cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
    ]))
    return t


def yonerge_kutu(metin, sure):
    icerik = f'<b>Yönerge:</b> {metin}    <b>|    Süre:</b> {sure}'
    t = Table([[Paragraph(icerik, S_GOV)]], colWidths=[17 * cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, -1), COLOR_VERY_LIGHT),
        ('BOX',           (0, 0), (-1, -1), 0.5, COLOR_ACCENT),
        ('LEFTPADDING',   (0, 0), (-1, -1), 8),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 8),
        ('TOPPADDING',    (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t


def adim(n, metin):
    return Paragraph(f'<b>Adım {n} — {metin}</b>', S_ADIM)


def satir_alani(*parcalar):
    """Yan yana etiket + yazı çizgisi."""
    cells, widths = [], []
    for etiket, gen_cm, cizgi_n in parcalar:
        cells.append(Paragraph(etiket, S_LABEL))
        cells.append(WritingLines(cizgi_n, 15))
        widths.append(gen_cm * cm)
        widths.append((17.0 / len(parcalar) - gen_cm) * cm)
    t = Table([cells], colWidths=widths)
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'BOTTOM'),
        ('TOPPADDING',    (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 3),
    ]))
    return t


def iki_sutun(sol, sag, sol_cm=8.4, sag_cm=8.6):
    t = Table([[sol, sag]], colWidths=[sol_cm * cm, sag_cm * cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LINEBEFORE',    (1, 0), (1, -1), 0.5, COLOR_LIGHT_GREY),
    ]))
    return t


def yansitma():
    ys = ParagraphStyle('ys_h', fontName='TR-Bold',    fontSize=8, textColor=COLOR_SECONDARY, leading=10)
    yc = ParagraphStyle('ys_c', fontName='TR-Regular', fontSize=8, textColor=COLOR_TEXT,       leading=10)
    data = [
        [Paragraph('<b>Yansıtma</b>', ys), ''],
        [Paragraph('En iyi yaptığım:', yc), WritingLines(1, 14)],
        [Paragraph('Zorlandığım:', yc),     WritingLines(1, 14)],
    ]
    t = Table(data, colWidths=[3.5 * cm, 13.5 * cm])
    t.setStyle(TableStyle([
        ('SPAN',          (0, 0), (1, 0)),
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_LIGHT),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def kontrol(maddeler):
    rows = [[Paragraph('[ ]', S_BODY), Paragraph(m, S_BODY)] for m in maddeler]
    t = Table(rows, colWidths=[0.6 * cm, 16.4 * cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
    ]))
    return t


# ============================================================
# SAYFA 1: ELEMAN AVI
# ============================================================

def ck1():
    e = []
    e += ck_baslik(1, 'ELEMAN AVI', 'TT.7.2.1.a  —  1. Ders  —  8 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Önündeki nesneyi ya da sınıftan seçtiğin bir ürünü incele. '
        'Tasarım elemanlarını ara ve tabloyu doldur. Yanlış cevap yoktur — gözlemlediğini yaz.',
        '8 dakika'))
    e.append(vsp(0.1))

    e.append(adim(1, 'İnceleyeceğim Nesne'))
    e.append(satir_alani(('İncelediğim nesne:', 4.5, 1), ('Seçme nedenim:', 3.5, 1)))
    e.append(vsp(0.1))

    e.append(adim(2, 'Elemanları Bul'))
    elemanlar = [
        ('Nokta',       '( ) Evet   ( ) Hayır'),
        ('Çizgi',       '( ) Evet   ( ) Hayır'),
        ('Renk',        '( ) Evet   ( ) Hayır'),
        ('Doku',        '( ) Evet   ( ) Hayır'),
        ('Şekil',       '( ) Evet   ( ) Hayır'),
        ('Ton / Valör', '( ) Evet   ( ) Hayır'),
        ('Mekân (Uzam)','( ) Evet   ( ) Hayır'),
        ('Biçim / Form','( ) Evet   ( ) Hayır'),
    ]
    data = [[Paragraph(b, S_TH) for b in ['Tasarım Elemanı', 'Var mı?', 'Bu üründe nasıl kullanılmış?']]]
    for el, v in elemanlar:
        data.append([Paragraph(el, S_TD), Paragraph(v, S_TD_C), Paragraph('', S_TD)])
    t = Table(data, colWidths=[3 * cm, 3.2 * cm, 10.8 * cm])
    t.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    e.append(t)
    e.append(vsp(0.1))

    e.append(adim(3, 'En Belirgin 3 Eleman'))
    for i in range(1, 4):
        e.append(satir_alani((f'{i}. Eleman:', 2.5, 1), ('Neden belirgin?', 3.5, 1)))
    e.append(vsp(0.1))

    e.append(adim(4, 'Çizimle Göster — Nesneyi eskizle, elemanları ok + etiketle işaretle'))
    e.append(DrawingBox(height=3.8 * cm, caption='Eskiz + etiket alanı'))
    e.append(vsp(0.1))

    e.append(yansitma())
    e.append(vsp(0.06))
    e.append(kontrol([
        'Seçtiğim nesneyi yazdım',
        'Tabloyu doldurdum (en az 5 satır)',
        'En belirgin 3 elemanı açıkladım',
        'Çizimde etiketleri yazdım',
    ]))
    return e


# ============================================================
# SAYFA 2: TASARIM İLKELERİNİ KARŞILAŞTIRIYORUM
# ============================================================

def ck2():
    e = []
    e += ck_baslik(2, 'TASARIM İLKELERİNİ KARŞILAŞTIRIYORUM',
                   'TT.7.2.1.b  —  2. Ders  —  8 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Öğretmenin gösterdiği çağdaş afiş ile geleneksel Türk sanat eserini karşılaştır. '
        'Tasarım ilkelerini her ikisinde de bul, tabloyu doldur.',
        '8 dakika'))
    e.append(vsp(0.1))

    e.append(satir_alani(('Afiş:', 2, 1), ('Geleneksel eser:', 3.5, 1)))
    e.append(vsp(0.1))

    e.append(adim(1, 'İlkeleri İşaretle'))
    ilkeler = ['Denge', 'Ritim', 'Vurgu', 'Hareket', 'Birlik', 'Çeşitlilik', 'Zıtlık (Kontrast)', 'Oran-Orantı']
    data = [[Paragraph(b, S_TH) for b in ['Tasarım İlkesi', 'Afişte var mı?', 'Geleneksel eserde var mı?']]]
    for ilke in ilkeler:
        data.append([Paragraph(ilke, S_TD),
                     Paragraph('( ) Evet   ( ) Hayır', S_TD_C),
                     Paragraph('( ) Evet   ( ) Hayır', S_TD_C)])
    t = Table(data, colWidths=[4.5 * cm, 4 * cm, 8.5 * cm])
    t.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    e.append(t)
    e.append(vsp(0.1))

    e.append(adim(2, 'Ortak İlkeler'))
    for i in range(1, 3):
        e.append(satir_alani(
            (f'Ortak ilke {i}:', 2.8, 1), ('Afişte:', 1.8, 1), ('Eserde:', 1.8, 1)))
    e.append(vsp(0.1))

    e.append(adim(3, 'Sadece birinde olan ya da çok farklı uygulanan ilke:'))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.1))

    e.append(adim(4, 'Yüzyıllar önce yapılan eser ile bugünün afişinin ortak dili var mı?'))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.1))

    e.append(yansitma())
    e.append(vsp(0.06))
    e.append(kontrol([
        'Her iki eseri yazdım',
        'Tabloyu eksiksiz doldurdum',
        'En az 2 ortak ilkeyi açıkladım',
        'Yorum bölümünü yazdım',
    ]))
    return e


# ============================================================
# SAYFA 3: ESERİ İNCELİYORUM
# ============================================================

def ck3():
    e = []
    e += ck_baslik(3, 'ESERİ İNCELİYORUM', 'TT.7.2.2  —  3. Ders  —  8 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Seçtiğin sanat eseri veya tasarım ürününü incele. '
        'Her adımı sırayla tamamla — yorum için zemin hazırlıyorsun.',
        '8 dakika'))
    e.append(vsp(0.1))

    e.append(satir_alani(('Eserin adı / tanımı:', 4, 1), ('Sanatçı (biliniyorsa):', 3.5, 1)))
    e.append(vsp(0.1))

    e.append(adim(1, 'Ne Var? — Gördüğün her şeyi listele (renk, şekil, nesne, doku...)'))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.08))

    e.append(adim(2, 'Ne Anlatıyor? — Eserin konusu veya mesajı nedir?'))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.08))

    e.append(adim(3, 'Hangi Eleman ve İlke Baskın?'))
    e.append(satir_alani(('Baskın eleman:', 3, 1), ('Neden?', 2, 1)))
    e.append(satir_alani(('Baskın ilke:', 3, 1), ('Neden?', 2, 1)))
    e.append(vsp(0.08))

    e.append(adim(4, 'Hangi Duyguyu Uyandırıyor?'))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.08))

    e.append(adim(5, 'Yeniden Yorumlama Hazırlığı'))
    e.append(satir_alani(('Değiştireceğim:', 3.5, 1), ('Anlamı korumak için:', 3.5, 1)))
    e.append(Paragraph('Nedenin:', S_LABEL))
    e.append(WritingLines(1, 16))
    e.append(vsp(0.1))

    e.append(yansitma())
    e.append(vsp(0.06))
    e.append(kontrol([
        'Eserin adını yazdım',
        '"Ne var?" bölümünü detaylı doldurdum',
        '1 eleman + 1 ilke seçip açıkladım',
        'Değiştirmek istediğim şeyi yazdım',
    ]))
    return e


# ============================================================
# SAYFA 4: DÖRTLÜ ANALOJİ
# ============================================================

def ck4():
    e = []
    e += ck_baslik(4, 'DÖRTLÜ ANALOJİ', 'TT.7.2.3  —  4. Ders  —  18 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Seçtiğin tasarım konusunu 4 farklı yolla yansıt: sözel slogan (A), '
        'görsel eskiz (B), soyut renk/doku (C), nesnel örnek (D).',
        '18 dakika'))
    e.append(vsp(0.1))

    e.append(satir_alani(('Tasarım konum:', 3.5, 1), ('Kısaca açıkla:', 3, 1)))
    e.append(vsp(0.1))

    # Sol: A + B
    sol = []
    sol.append(Paragraph('<b>A — Sözel Analoji: Slogan</b>', S_BOLUM))
    sol.append(Paragraph('Konunu bir slogana dönüştür (benzetme içermeli):', S_KUCUK))
    sol.append(WritingLines(2, 16))
    sol.append(vsp(0.06))
    sol.append(Paragraph('Hangi benzetmeyi kullandın?', S_KUCUK))
    sol.append(WritingLines(1, 15))
    sol.append(vsp(0.1))
    sol.append(Paragraph('<b>B — Görsel Analoji: Eskiz</b>', S_BOLUM))
    sol.append(Paragraph('Konuna benzeyen nesne/formu çiz ve etiketle:', S_KUCUK))
    sol.append(DrawingBox(height=4.2 * cm, caption='Eskiz alanı'))
    sol.append(vsp(0.04))
    sol.append(Paragraph('Konuyu andıran nesne: ___________   Neden: ___________', S_KUCUK))

    # Sağ: C + D
    sag = []
    sag.append(Paragraph('<b>C — Soyut Analoji: Renk ve Doku</b>', S_BOLUM))
    sag.append(Paragraph('Konunu bir renk veya dokuyla ifade et:', S_KUCUK))
    sag.append(DrawingBox(height=3.2 * cm, caption='Boyama / doldurma alanı'))
    sag.append(vsp(0.04))
    sag.append(Paragraph('Renk(ler): ___________   Doku: ___________', S_KUCUK))
    sag.append(WritingLines(1, 15))
    sag.append(vsp(0.1))
    sag.append(Paragraph('<b>D — Nesnel Analoji: Gerçek Örnek</b>', S_BOLUM))
    sag.append(Paragraph('Çevrenden konunla benzerlik taşıyan bir nesne seç:', S_KUCUK))
    sag.append(Paragraph('Nesne: _______________________________', S_KUCUK))
    sag.append(WritingLines(2, 15))

    e.append(iki_sutun(sol, sag))
    e.append(vsp(0.1))

    e.append(adim(5, 'En Güçlü Analoji — Dört bölümün hangisi en güçlü? Neden?'))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.1))

    e.append(yansitma())
    e.append(vsp(0.06))
    e.append(kontrol([
        'Tasarım konumu yazdım',
        'Slogan bölümünü (A) doldurdum',
        'Eskizi çizdim ve etiketledim (B)',
        'Renk/doku (C) + nesnel örnek (D) bölümlerini doldurdum',
    ]))
    return e


# ============================================================
# SAYFA 5: TASARIM PLANIM
# ============================================================

def ck5():
    e = []
    e += ck_baslik(5, 'TASARIM PLANIM', 'TT.7.2.4.a  —  5. Ders  —  16 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Tasarımını planla. Problemi tanımla, eleman/ilke/malzemeleri seç. '
        'A3 kâğıdına 3 taslak çizerken bu plana bak.',
        '16 dakika'))
    e.append(vsp(0.1))

    e.append(adim(1, 'Tasarım Problemim'))
    e.append(Paragraph(
        '<b>"Ben</b> _________________________ '
        '<b>için</b> _________________________ '
        '<b>tasarlayacağım."</b>',
        ParagraphStyle('cumle', fontName='TR-Regular', fontSize=9,
                       textColor=COLOR_TEXT, leading=13, spaceAfter=2)))
    e.append(Paragraph('Açıklama (kim için, neden, hangi problemi çözecek?):', S_LABEL))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.1))

    # Adım 2 (sol) + Adım 3 (sağ) yan yana
    eleman_data = [[Paragraph(b, S_TH) for b in ['Kategori', 'Seçimim', 'Nasıl kullanacağım?']]]
    for kat in ['Tasarım Elemanı 1', 'Tasarım Elemanı 2', 'Tasarım Elemanı 3',
                'Tasarım İlkesi 1', 'Tasarım İlkesi 2']:
        eleman_data.append([Paragraph(kat, S_TD), '', ''])
    t_el = Table(eleman_data, colWidths=[3.2 * cm, 2.2 * cm, 2.6 * cm])
    t_el.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 9)]))

    mal_data = [[Paragraph(b, S_TH) for b in ['Malzeme', 'Var?', 'Nereden?']]]
    for _ in range(4):
        mal_data.append([Paragraph('', S_TD), Paragraph('( ) E  ( ) H', S_TD_C), Paragraph('', S_TD)])
    t_mal = Table(mal_data, colWidths=[3 * cm, 2 * cm, 3 * cm])
    t_mal.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 9)]))

    sol2 = [Paragraph('<b>Adım 2 — Eleman ve İlkeler</b>', S_BOLUM), t_el]
    sag3 = [Paragraph('<b>Adım 3 — Malzeme Listesi</b>',   S_BOLUM), t_mal]
    e.append(iki_sutun(sol2, sag3))
    e.append(vsp(0.1))

    e.append(adim(4, 'A3 Taslak Planı — Üç farklı taslak fikri:'))
    for i in range(1, 4):
        e.append(satir_alani((f'{i}. Taslak fikri:', 3.5, 1)))
    e.append(satir_alani(('En çok işleyeceğim taslak:', 5, 1), ('Neden:', 2.5, 1)))
    e.append(vsp(0.08))

    e.append(adim(5, 'Akran Geri Dönütü'))
    e.append(satir_alani(('Akranın adı:', 2.8, 1), ('Geri dönütü:', 3, 1)))
    e.append(vsp(0.1))

    e.append(yansitma())
    e.append(vsp(0.06))
    e.append(kontrol([
        'Tasarım problemimi tam cümleyle yazdım',
        'En az 3 eleman + 2 ilke seçip açıkladım',
        'Malzeme listesi hazır',
        '3 taslak fikrini yazdım ve akran geri dönütü aldım',
    ]))
    return e


# ============================================================
# SAYFA 6: GALERİ ÖZ DEĞERLENDİRMESİ
# ============================================================

def ck6():
    e = []
    e += ck_baslik(6, 'GALERİ ÖZ DEĞERLENDİRMESİ', 'TT.7.2.4.b  —  6. Ders  —  8 dk')
    e.append(ad_satiri())
    e.append(vsp(0.1))
    e.append(yonerge_kutu(
        'Galeri turunu tamamladıktan sonra hem kendi tasarımını '
        'hem de ünite boyunca yaptıklarını değerlendir.',
        '8 dakika'))
    e.append(vsp(0.1))

    e.append(adim(1, 'Tasarımımı Değerlendiriyorum'))
    olcut_data = [
        ['Ölçüt', 'Harika', 'İyi', 'Gelişiyor', 'Henüz Değil'],
        ['Tasarım elemanlarını bilinçli kullandım', '( )', '( )', '( )', '( )'],
        ['Tasarım ilkelerini uyguladım',            '( )', '( )', '( )', '( )'],
        ['Konu/problem ile tasarım uyumluydu',      '( )', '( )', '( )', '( )'],
        ['Özgün bir fikir ortaya koydum',           '( )', '( )', '( )', '( )'],
        ['Süreci planlayarak ilerledim',            '( )', '( )', '( )', '( )'],
    ]
    fmt_data = []
    for r, row in enumerate(olcut_data):
        new_row = []
        for c, cell in enumerate(row):
            if r == 0:
                new_row.append(Paragraph(cell, S_TH))
            elif c == 0:
                new_row.append(Paragraph(cell, S_TD))
            else:
                new_row.append(Paragraph(cell, S_TD_C))
        fmt_data.append(new_row)
    t_olcut = Table(fmt_data, colWidths=[7 * cm, 2.2 * cm, 1.8 * cm, 2.5 * cm, 3.5 * cm])
    t_olcut.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 5)]))
    e.append(t_olcut)
    e.append(vsp(0.1))

    sol_b2 = [Paragraph('<b>Tasarımımın En Güçlü Yanı</b>', S_BOLUM), WritingLines(2, 16)]
    sag_b3 = [Paragraph('<b>Bir Sonra Farklı Yapacaklarım</b>', S_BOLUM), WritingLines(2, 16)]
    e.append(iki_sutun(sol_b2, sag_b3))
    e.append(vsp(0.1))

    e.append(adim(2, 'Galeriden İzlenimler'))
    e.append(satir_alani(('En dikkat çeken ürün:', 4.5, 1), ('Öne çıkan özelliği:', 3.5, 1)))
    e.append(Paragraph("Post-it'lerden öğrendiğim:", S_LABEL))
    e.append(WritingLines(2, 16))
    e.append(vsp(0.1))

    e.append(adim(3, 'Ünite Sonu'))
    e.append(Paragraph(
        '"Bu üniteden önce eleman ve ilkeler hakkında _________________________ düşünüyordum. '
        'Şimdi ise _________________________ biliyorum."',
        ParagraphStyle('uson', fontName='TR-Regular', fontSize=8.5,
                       textColor=COLOR_TEXT, leading=12, spaceAfter=3)))
    e.append(satir_alani(('En sevdiğim ders:', 3.5, 1), ('Neden:', 2.5, 1)))
    e.append(vsp(0.1))

    e.append(yansitma())
    e.append(vsp(0.06))
    e.append(kontrol([
        'Öz değerlendirme tablosunu doldurdum',
        'Tasarımımın güçlü yanını yazdım',
        'Galeri izlenimlerimi yazdım',
        'Ünite sonu cümlesini tamamladım',
    ]))
    return e


# ============================================================
# ANA BLOK
# ============================================================

def main():
    doc = SimpleDocTemplate(
        CIKTI,
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=1.8 * cm, bottomMargin=1.8 * cm,
        title='2. Ünite — Temel Tasarım: Çalışma Kâğıtları',
    )
    doc.unite_info = UNITE_ADI

    story = []
    sayfalar = [ck1, ck2, ck3, ck4, ck5, ck6]
    for i, ck in enumerate(sayfalar):
        story += ck()
        if i < len(sayfalar) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print('OK  U2_PDF_03_Calisma_Kagitlari.pdf  (6 sayfa)')


if __name__ == '__main__':
    main()
