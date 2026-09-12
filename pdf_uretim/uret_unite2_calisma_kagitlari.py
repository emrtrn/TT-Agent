"""
2. Ünite — Temel Tasarım: Çalışma Kâğıtları PDF Üretici
CK1–CK6 her biri ayrı PDF, tek sayfa hedefi.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    register_fonts, get_styles, add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, DrawingBox, Checkbox, HorizontalLine,
)
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import white

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit2')
UNITE_INFO = "2. Ünite: Temel Tasarım  •  Teknoloji ve Tasarım  •  7. Sınıf"

# ── Stil sabitleri ──────────────────────────────────────────────────────────

S_ADIM = ParagraphStyle('AdimH', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_SECONDARY, leading=12, spaceBefore=4, spaceAfter=2)
S_LABEL = ParagraphStyle('Label', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11, spaceAfter=1)
S_BOLUM = ParagraphStyle('Bolum', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_SECONDARY, leading=11, spaceAfter=2)
S_KUCUK = ParagraphStyle('Kucuk', fontName='TR-Regular', fontSize=7.5,
    textColor=COLOR_TEXT, leading=10, spaceAfter=1)
S_TH = ParagraphStyle('TH', fontName='TR-Bold', fontSize=7.5,
    textColor=white, alignment=TA_CENTER, leading=10)
S_TD = ParagraphStyle('TD', fontName='TR-Regular', fontSize=7.5,
    textColor=COLOR_TEXT, alignment=TA_LEFT, leading=10)
S_TD_C = ParagraphStyle('TDC', fontName='TR-Regular', fontSize=7.5,
    textColor=COLOR_TEXT, alignment=TA_CENTER, leading=10)

TABLE_STYLE_BASE = [
    ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
    ('LINEBELOW', (0, 0), (-1, 0), 1, COLOR_SECONDARY),
    ('GRID', (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
    ('TOPPADDING', (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]

# ── Yardımcı bileşenler ─────────────────────────────────────────────────────

def make_doc(filename, title):
    doc = SimpleDocTemplate(
        os.path.join(OUTPUT_DIR, filename),
        pagesize=A4,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        leftMargin=2*cm, rightMargin=2*cm,
        title=title,
    )
    doc.doc_title = title
    doc.unite_info = UNITE_INFO
    return doc


def sp(h=4):
    return Spacer(1, h)


def ck_baslik(ck_no, baslik, kazanim):
    data = [[
        Paragraph(f'<b>CK{ck_no} — {baslik}</b>',
            ParagraphStyle('CKT', fontName='TR-Bold', fontSize=12,
                textColor=COLOR_PRIMARY, leading=14)),
        Paragraph(kazanim,
            ParagraphStyle('CKK', fontName='TR-Italic', fontSize=7.5,
                textColor=COLOR_MUTED, alignment=TA_RIGHT, leading=10)),
    ]]
    t = Table(data, colWidths=[11*cm, 6*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEBELOW', (0, 0), (-1, 0), 1.5, COLOR_PRIMARY),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('RIGHTPADDING', (-1, 0), (-1, 0), 0),
    ]))
    return t


def ogrenci_header():
    data = [[
        Paragraph('<b>Adı Soyadı:</b>', S_LABEL), '',
        Paragraph('<b>Sınıf/No:</b>', S_LABEL), '',
        Paragraph('<b>Tarih:</b>', S_LABEL), '',
    ]]
    t = Table(data, colWidths=[2.7*cm, 5.1*cm, 2*cm, 2.8*cm, 1.5*cm, 2.9*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW', (1, 0), (1, 0), 0.8, COLOR_WRITING_LINE),
        ('LINEBELOW', (3, 0), (3, 0), 0.8, COLOR_WRITING_LINE),
        ('LINEBELOW', (5, 0), (5, 0), 0.8, COLOR_WRITING_LINE),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    return t


def yonerge_kutu(metin, sure):
    icerik = f'<b>Yönerge:</b> {metin}    <b>|    Süre:</b> {sure}'
    kutu = Table([[Paragraph(icerik, ParagraphStyle('Yn', fontName='TR-Regular',
        fontSize=8.5, textColor=COLOR_TEXT, leading=12))]], colWidths=[17*cm])
    kutu.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_VERY_LIGHT),
        ('BOX', (0, 0), (-1, -1), 0.5, COLOR_ACCENT),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return kutu


def adim(n, metin):
    return Paragraph(f'<b>Adım {n} — {metin}</b>', S_ADIM)


def satir_alani(*parcalar):
    """Yan yana etiket+WritingLines çiftleri → tek tablo satırı"""
    cells = []
    widths = []
    for etiket, genislik_cm, cizgi_sayisi in parcalar:
        cells.append(Paragraph(etiket, S_LABEL))
        cells.append(WritingLines(cizgi_sayisi, 15))
        widths.append(genislik_cm * cm)
        widths.append((17 / len(parcalar) - genislik_cm) * cm)
    t = Table([cells], colWidths=widths)
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
    ]))
    return t


def yonerge_tablo(basliklar, satirlar, genislikler):
    """Genel amaçlı sınıflandırma tablosu"""
    data = [[Paragraph(b, S_TH) for b in basliklar]]
    for satir in satirlar:
        data.append([Paragraph(h, S_TD) for h in satir])
    t = Table(data, colWidths=[g * cm for g in genislikler])
    t.setStyle(TableStyle(TABLE_STYLE_BASE))
    return t


def yansitma():
    ys = ParagraphStyle('YS', fontName='TR-Bold', fontSize=8,
        textColor=COLOR_SECONDARY, leading=10)
    yc = ParagraphStyle('YC', fontName='TR-Regular', fontSize=8,
        textColor=COLOR_TEXT, leading=10)
    data = [
        [Paragraph('<b>Yansıtma</b>', ys), ''],
        [Paragraph('En iyi yaptığım:', yc), WritingLines(1, 14)],
        [Paragraph('Zorlandığım:', yc), WritingLines(1, 14)],
    ]
    t = Table(data, colWidths=[3.5*cm, 13.5*cm])
    t.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_LIGHT),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def kontrol(maddeler):
    rows = [[Checkbox(size=8), Paragraph(m, ParagraphStyle('CB', fontName='TR-Regular',
        fontSize=8, textColor=COLOR_TEXT, leading=11))] for m in maddeler]
    t = Table(rows, colWidths=[0.6*cm, 16.4*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return t


def iki_sutun(sol_el, sag_el, sol_cm=8.4, sag_cm=8.6):
    t = Table([[sol_el, sag_el]], colWidths=[sol_cm*cm, sag_cm*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LINEBEFORE', (1, 0), (1, -1), 0.5, COLOR_LIGHT_GREY),
    ]))
    return t


# ── CK1 — Eleman Avı ────────────────────────────────────────────────────────

def build_ck1():
    el = []
    el += [ck_baslik(1, "Eleman Avı", "TT.7.2.1.a  •  1. Ders  •  8 dk"), sp(4)]
    el += [ogrenci_header(), sp(5)]
    el += [yonerge_kutu(
        "Önündeki nesneyi ya da sınıftan seçtiğin bir ürünü incele. "
        "Tasarım elemanlarını ara ve tabloyu doldur.",
        "8 dakika"), sp(6)]

    el.append(adim(1, "İnceleyeceğim Nesne"))
    el.append(satir_alani(("İncelediğim nesne:", 4.5, 1), ("Seçme nedenim:", 3.5, 1)))
    el.append(sp(6))

    el.append(adim(2, "Elemanları Bul"))
    elemanlar = [
        ("Nokta", "( ) Evet   ( ) Hayır"), ("Çizgi", "( ) Evet   ( ) Hayır"),
        ("Renk", "( ) Evet   ( ) Hayır"), ("Doku", "( ) Evet   ( ) Hayır"),
        ("Şekil", "( ) Evet   ( ) Hayır"), ("Ton / Valör", "( ) Evet   ( ) Hayır"),
        ("Mekân (Uzam)", "( ) Evet   ( ) Hayır"), ("Biçim / Form", "( ) Evet   ( ) Hayır"),
    ]
    data2 = [[Paragraph(b, S_TH) for b in ["Tasarım Elemanı", "Var mı?", "Bu üründe nasıl kullanılmış?"]]]
    for e, v in elemanlar:
        data2.append([Paragraph(e, S_TD), Paragraph(v, S_TD_C), Paragraph('', S_TD)])
    t2 = Table(data2, colWidths=[3*cm, 3.2*cm, 10.8*cm])
    t2.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    el += [t2, sp(6)]

    el.append(adim(3, "En Belirgin 3 Eleman"))
    for i in range(1, 4):
        el.append(satir_alani((f"{i}. Eleman:", 2.5, 1), ("Neden belirgin?", 3.5, 1)))
    el.append(sp(6))

    el.append(adim(4, "Çizimle Göster — Nesneyi eskizle, elemanları ok + etiketle işaretle"))
    el += [DrawingBox(height=4.2*cm, caption="Eskiz + etiket alanı"), sp(6)]

    el += [yansitma(), sp(4)]
    el.append(kontrol([
        "Seçtiğim nesneyi yazdım",
        "Tabloyu doldurdum (en az 5 satır)",
        "En belirgin 3 elemanı açıkladım",
        "Çizimde etiketleri yazdım",
    ]))

    doc = make_doc("Unite2_CK1_Eleman_Avi.pdf", "CK1 — Eleman Avı")
    doc.build(el, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("  CK1 uretildi: Unite2_CK1_Eleman_Avi.pdf")


# ── CK2 — Tasarım İlkelerini Karşılaştırıyorum ──────────────────────────────

def build_ck2():
    el = []
    el += [ck_baslik(2, "Tasarım İlkelerini Karşılaştırıyorum", "TT.7.2.1.b  •  2. Ders  •  8 dk"), sp(4)]
    el += [ogrenci_header(), sp(5)]
    el += [yonerge_kutu(
        "Öğretmenin gösterdiği çağdaş afiş ile geleneksel Türk sanat eserini karşılaştır. "
        "Tasarım ilkelerini her ikisinde de bul, tabloyu doldur.",
        "8 dakika"), sp(5)]

    el.append(satir_alani(("Afiş:", 2, 1), ("Geleneksel eser:", 3.5, 1)))
    el.append(sp(5))

    el.append(adim(1, "İlkeleri İşaretle"))
    ilkeler = ["Denge", "Ritim", "Vurgu", "Hareket", "Birlik", "Çeşitlilik", "Zıtlık (Kontrast)", "Oran-Orantı"]
    data1 = [[Paragraph(b, S_TH) for b in ["Tasarım İlkesi", "Afişte var mı?", "Geleneksel eserde var mı?"]]]
    for ilke in ilkeler:
        data1.append([Paragraph(ilke, S_TD),
                      Paragraph("( ) Evet   ( ) Hayır", S_TD_C),
                      Paragraph("( ) Evet   ( ) Hayır", S_TD_C)])
    t1 = Table(data1, colWidths=[4.5*cm, 3.5*cm, 9*cm])
    t1.setStyle(TableStyle([*TABLE_STYLE_BASE, ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    el += [t1, sp(6)]

    el.append(adim(2, "Ortak İlkeler"))
    for i in range(1, 3):
        el.append(satir_alani(
            (f"Ortak ilke {i}:", 2.8, 1), ("Afişte:", 1.8, 1), ("Eserde:", 1.8, 1)))
    el.append(sp(5))

    el.append(adim(3, "Sadece birinde olan / çok farklı uygulanan ilke:"))
    el += [WritingLines(2, 16), sp(5)]

    el.append(adim(4, "Yüzyıllar önce yapılan eser ile bugünün afişinin ortak dili var mı?"))
    el += [WritingLines(2, 16), sp(6)]

    el += [yansitma(), sp(4)]
    el.append(kontrol([
        "Her iki eseri yazdım",
        "Tabloyu eksiksiz doldurdum",
        "En az 2 ortak ilkeyi açıkladım",
        "Yorum bölümünü yazdım",
    ]))

    doc = make_doc("Unite2_CK2_Ilkeler_Karsilastirma.pdf", "CK2 — Tasarım İlkelerini Karşılaştırıyorum")
    doc.build(el, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("  CK2 uretildi: Unite2_CK2_Ilkeler_Karsilastirma.pdf")


# ── CK3 — Eseri İnceliyorum ─────────────────────────────────────────────────

def build_ck3():
    el = []
    el += [ck_baslik(3, "Eseri İnceliyorum", "TT.7.2.2  •  3. Ders  •  8 dk"), sp(4)]
    el += [ogrenci_header(), sp(5)]
    el += [yonerge_kutu(
        "Seçtiğin sanat eseri veya tasarım ürününü incele. "
        "Her adımı sırayla tamamla — yorum için zemin hazırlıyorsun.",
        "8 dakika"), sp(5)]

    el.append(satir_alani(("Eserin adı / tanımı:", 4, 1), ("Sanatçı (biliniyorsa):", 3.5, 1)))
    el.append(sp(5))

    el.append(adim(1, "Ne Var? — Gördüğün her şeyi listele (renk, şekil, nesne, doku...)"))
    el += [WritingLines(2, 16), sp(4)]

    el.append(adim(2, "Ne Anlatıyor? — Eserin konusu veya mesajı nedir?"))
    el += [WritingLines(2, 16), sp(4)]

    el.append(adim(3, "Hangi Eleman ve İlke Baskın?"))
    el.append(satir_alani(("Baskın eleman:", 3, 1), ("Neden?", 2, 1)))
    el.append(satir_alani(("Baskın ilke:", 3, 1), ("Neden?", 2, 1)))
    el.append(sp(4))

    el.append(adim(4, "Hangi Duyguyu Uyandırıyor?"))
    el += [WritingLines(2, 16), sp(4)]

    el.append(adim(5, "Yeniden Yorumlama Hazırlığı"))
    el.append(satir_alani(("Değiştireceğim:", 3.5, 1), ("Anlamı korumak için:", 3.5, 1)))
    el.append(Paragraph("Nedenin:", S_LABEL))
    el += [WritingLines(1, 16), sp(6)]

    el += [yansitma(), sp(4)]
    el.append(kontrol([
        "Eserin adını yazdım",
        "'Ne var?' bölümünü detaylı doldurdum",
        "1 eleman + 1 ilke seçip açıkladım",
        "Değiştirmek istediğim şeyi yazdım",
    ]))

    doc = make_doc("Unite2_CK3_Eseri_Inceliyorum.pdf", "CK3 — Eseri İnceliyorum")
    doc.build(el, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("  CK3 uretildi: Unite2_CK3_Eseri_Inceliyorum.pdf")


# ── CK4 — Dörtlü Analoji (2 sütun) ─────────────────────────────────────────

def build_ck4():
    el = []
    el += [ck_baslik(4, "Dörtlü Analoji", "TT.7.2.3  •  4. Ders  •  18 dk"), sp(4)]
    el += [ogrenci_header(), sp(5)]
    el += [yonerge_kutu(
        "Seçtiğin tasarım konusunu 4 farklı yolla yansıt: sözel slogan (A), "
        "görsel eskiz (B), soyut renk/doku (C), nesnel örnek (D).",
        "18 dakika"), sp(5)]

    el.append(satir_alani(("Tasarım konum:", 3.5, 1), ("Kısaca açıkla:", 3, 1)))
    el.append(sp(6))

    # Sol sütun: A (Slogan) + B (Eskiz)
    sol = []
    sol.append(Paragraph('<b>A — Sözel Analoji: Slogan</b>', S_BOLUM))
    sol.append(Paragraph('Konunu bir slogana dönüştür (benzetme içermeli):', S_KUCUK))
    sol.append(WritingLines(2, 16))
    sol.append(sp(3))
    sol.append(Paragraph('Hangi benzetmeyi kullandın?', S_KUCUK))
    sol.append(WritingLines(1, 15))
    sol.append(sp(7))
    sol.append(Paragraph('<b>B — Görsel Analoji: Eskiz</b>', S_BOLUM))
    sol.append(Paragraph('Konuna benzeyen nesne/formu çiz ve etiketle:', S_KUCUK))
    sol.append(DrawingBox(height=4.5*cm, caption="Eskiz alanı"))
    sol.append(sp(3))
    sol.append(Paragraph('Konuyu andıran nesne: _______________   Neden: _______________', S_KUCUK))

    # Sağ sütun: C (Renk/Doku) + D (Nesnel)
    sag = []
    sag.append(Paragraph('<b>C — Soyut Analoji: Renk ve Doku</b>', S_BOLUM))
    sag.append(Paragraph('Konunu bir renk veya dokuyla ifade et. Boyayarak ya da yazarak doldur:', S_KUCUK))
    sag.append(DrawingBox(height=3.5*cm, caption="Boyama / doldurma alanı"))
    sag.append(sp(3))
    sag.append(Paragraph('Renk(ler): _______________   Doku: _______________', S_KUCUK))
    sag.append(WritingLines(1, 15))
    sag.append(sp(7))
    sag.append(Paragraph('<b>D — Nesnel Analoji: Gerçek Örnek</b>', S_BOLUM))
    sag.append(Paragraph('Çevrenden konunla benzerlik taşıyan bir nesne seç:', S_KUCUK))
    sag.append(Paragraph('Nesne: _______________________________________________', S_KUCUK))
    sag.append(WritingLines(2, 15))

    el.append(iki_sutun(sol, sag))
    el.append(sp(6))

    el.append(adim(5, "En Güçlü Analoji — Dört bölümün hangisi en güçlü? Neden?"))
    el += [WritingLines(2, 16), sp(5)]

    el += [yansitma(), sp(4)]
    el.append(kontrol([
        "Tasarım konumu yazdım",
        "Slogan bölümünü (A) doldurdum",
        "Eskizi çizdim ve etiketledim (B)",
        "Renk/doku (C) + nesnel örnek (D) bölümlerini doldurdum",
    ]))

    doc = make_doc("Unite2_CK4_Dortlu_Analoji.pdf", "CK4 — Dörtlü Analoji")
    doc.build(el, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("  CK4 uretildi: Unite2_CK4_Dortlu_Analoji.pdf")


# ── CK5 — Tasarım Planım (2 sütunlu tablo düzeni) ───────────────────────────

def build_ck5():
    el = []
    el += [ck_baslik(5, "Tasarım Planım", "TT.7.2.4.a  •  5. Ders  •  16 dk"), sp(4)]
    el += [ogrenci_header(), sp(5)]
    el += [yonerge_kutu(
        "Tasarımını planla. Problemi tanımla, eleman/ilke/malzemeleri seç. "
        "A3 kâğıdına 3 taslak çizerken bu plana bak.",
        "16 dakika"), sp(5)]

    el.append(adim(1, "Tasarım Problemim"))
    el.append(Paragraph(
        '<b>"Ben</b> ________________________________ <b>için</b> ________________________________ <b>tasarlayacağım."</b>',
        ParagraphStyle('Cumle', fontName='TR-Regular', fontSize=9, textColor=COLOR_TEXT, leading=13, spaceAfter=2)))
    el.append(Paragraph("Açıklama (kim için, neden, hangi problemi çözecek?):", S_LABEL))
    el += [WritingLines(2, 16), sp(6)]

    # Adım 2 (sol) + Adım 3 (sağ) → yan yana
    eleman_data = [[Paragraph(b, S_TH) for b in ["Kategori", "Seçimim", "Nasıl kullanacağım?"]]]
    for kat in ["Tasarım Elemanı 1", "Tasarım Elemanı 2", "Tasarım Elemanı 3",
                "Tasarım İlkesi 1", "Tasarım İlkesi 2"]:
        eleman_data.append([Paragraph(kat, S_TD), Paragraph('', S_TD), Paragraph('', S_TD)])

    t_eleman = Table(eleman_data, colWidths=[3.2*cm, 2.2*cm, 2.6*cm])
    t_eleman.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('BOTTOMPADDING', (0, 1), (-1, -1), 9),
    ]))

    mal_data = [[Paragraph(b, S_TH) for b in ["Malzeme", "Var?", "Nereden?"]]]
    for _ in range(4):
        mal_data.append([Paragraph('', S_TD), Paragraph('( ) E  ( ) H', S_TD_C), Paragraph('', S_TD)])

    t_mal = Table(mal_data, colWidths=[3*cm, 2*cm, 3*cm])
    t_mal.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('BOTTOMPADDING', (0, 1), (-1, -1), 9),
    ]))

    sol_adim2 = [Paragraph('<b>Adım 2 — Eleman ve İlkeler</b>', S_BOLUM), t_eleman]
    sag_adim3 = [Paragraph('<b>Adım 3 — Malzeme Listesi</b>', S_BOLUM), t_mal]

    el.append(iki_sutun(sol_adim2, sag_adim3, sol_cm=8.4, sag_cm=8.6))
    el.append(sp(6))

    el.append(adim(4, "A3 Taslak Planı — Üç farklı taslak fikri:"))
    for i in range(1, 4):
        el.append(satir_alani((f"{i}. Taslak fikri:", 3.5, 1)))
    el.append(satir_alani(("En çok işleyeceğim taslak:", 5, 1), ("Neden:", 2.5, 1)))
    el.append(sp(5))

    el.append(adim(5, "Akran Geri Dönütü"))
    el.append(satir_alani(("Akranın adı:", 2.8, 1), ("Geri dönütü:", 3, 1)))
    el.append(sp(6))

    el += [yansitma(), sp(4)]
    el.append(kontrol([
        "Tasarım problemimi tam cümleyle yazdım",
        "En az 3 eleman + 2 ilke seçip açıkladım",
        "Malzeme listesi hazır",
        "3 taslak fikrini yazdım ve akran geri dönütü aldım",
    ]))

    doc = make_doc("Unite2_CK5_Tasarim_Plani.pdf", "CK5 — Tasarım Planım")
    doc.build(el, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("  CK5 uretildi: Unite2_CK5_Tasarim_Plani.pdf")


# ── CK6 — Galeri Öz Değerlendirmesi ─────────────────────────────────────────

def build_ck6():
    el = []
    el += [ck_baslik(6, "Galeri Öz Değerlendirmesi", "TT.7.2.4.b  •  6. Ders  •  8 dk"), sp(4)]
    el += [ogrenci_header(), sp(5)]
    el += [yonerge_kutu(
        "Galeri turunu tamamladıktan sonra hem kendi tasarımını "
        "hem de ünite boyunca yaptıklarını değerlendir.",
        "8 dakika"), sp(5)]

    el.append(adim(0, "Tasarımımı Değerlendiriyorum"))
    olcut_data = [
        ["Ölçüt", "Harika", "İyi", "Gelişiyor", "Henüz Değil"],
        ["Tasarım elemanlarını bilinçli kullandım", "( )", "( )", "( )", "( )"],
        ["Tasarım ilkelerini uyguladım", "( )", "( )", "( )", "( )"],
        ["Konu/problem ile tasarım uyumluydu", "( )", "( )", "( )", "( )"],
        ["Özgün bir fikir ortaya koydum", "( )", "( )", "( )", "( )"],
        ["Süreci planlayarak ilerledim", "( )", "( )", "( )", "( )"],
    ]
    olcut_fmt = []
    for r_idx, row in enumerate(olcut_data):
        new_row = []
        for c_idx, cell in enumerate(row):
            if r_idx == 0:
                new_row.append(Paragraph(cell, S_TH))
            elif c_idx == 0:
                new_row.append(Paragraph(cell, S_TD))
            else:
                new_row.append(Paragraph(cell, S_TD_C))
        olcut_fmt.append(new_row)
    t_olcut = Table(olcut_fmt, colWidths=[7*cm, 2.2*cm, 1.8*cm, 2.5*cm, 3.5*cm])
    t_olcut.setStyle(TableStyle([
        *TABLE_STYLE_BASE,
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
    ]))
    el += [t_olcut, sp(6)]

    # Güçlü yan + Farklı yapacak → yan yana
    sol_b2 = [
        Paragraph('<b>Tasarımımın En Güçlü Yanı</b>', S_BOLUM),
        WritingLines(2, 16),
    ]
    sag_b3 = [
        Paragraph('<b>Bir Sonra Farklı Yapacaklarım</b>', S_BOLUM),
        WritingLines(2, 16),
    ]
    el.append(iki_sutun(sol_b2, sag_b3))
    el.append(sp(6))

    el.append(adim(0, "Galeriden İzlenimler"))
    el.append(satir_alani(("En dikkat çeken ürün:", 4.5, 1), ("Öne çıkan özelliği:", 3.5, 1)))
    el.append(Paragraph("Post-it'lerden öğrendiğim:", S_LABEL))
    el += [WritingLines(2, 16), sp(6)]

    el.append(adim(0, "Ünite Sonu"))
    el.append(Paragraph(
        '"Bu üniteden önce eleman ve ilkeler hakkında _________________________ düşünüyordum. '
        'Şimdi ise _________________________ biliyorum."',
        ParagraphStyle('USon', fontName='TR-Regular', fontSize=8.5,
            textColor=COLOR_TEXT, leading=12, spaceAfter=3)))
    el.append(satir_alani(("En sevdiğim ders:", 3.5, 1), ("Neden:", 2.5, 1)))
    el.append(sp(6))

    el += [yansitma(), sp(4)]
    el.append(kontrol([
        "Öz değerlendirme tablosunu doldurdum",
        "Tasarımımın güçlü yanını yazdım",
        "Galeri izlenimlerimi yazdım",
        "Ünite sonu cümlesini tamamladım",
    ]))

    doc = make_doc("Unite2_CK6_Galeri_Oz_Degerlendirme.pdf", "CK6 — Galeri Öz Değerlendirmesi")
    doc.build(el, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("  CK6 uretildi: Unite2_CK6_Galeri_Oz_Degerlendirme.pdf")


# ── Ana giriş ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Unite 2 Calisma Kagitlari PDF uretimi basliyor...\n")
    build_ck1()
    build_ck2()
    build_ck3()
    build_ck4()
    build_ck5()
    build_ck6()
    print("\nTum CK PDF'leri uretildi!")
