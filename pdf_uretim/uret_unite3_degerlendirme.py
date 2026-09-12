"""
3. Ünite — Değerlendirme Araçları PDF Üreticisi
8 ayrı PDF üretir (units/7_sinif/unit3/ klasörüne kaydeder).

Çalıştır: python pdf_uretim/uret_unite3_degerlendirme.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether,
)

from pdf_style import (
    register_fonts, add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, DrawingBox, HorizontalLine,
)

register_fonts()

OUT        = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit3')
UNITE_INFO = '3. Ünite: Tasarım Odaklı Süreç  •  Teknoloji ve Tasarım  •  7. Sınıf'
TW         = 17 * cm

# ── Stiller ─────────────────────────────────────────────────────────────────

S_BAS  = ParagraphStyle('u3d_BAS',  fontName='TR-Bold',    fontSize=13, textColor=COLOR_PRIMARY,   leading=16)
S_ALT  = ParagraphStyle('u3d_ALT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     alignment=TA_RIGHT, leading=10)
S_BLM  = ParagraphStyle('u3d_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=6, spaceAfter=2)
S_LBL  = ParagraphStyle('u3d_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11, spaceAfter=1)
S_SML  = ParagraphStyle('u3d_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SML7 = ParagraphStyle('u3d_SML7', fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      leading=9.5)
S_SMBD = ParagraphStyle('u3d_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMIT = ParagraphStyle('u3d_SMIT', fontName='TR-Italic',  fontSize=7.5,textColor=COLOR_MUTED,     leading=10)
S_TH   = ParagraphStyle('u3d_TH',   fontName='TR-Bold',    fontSize=7.5,textColor=white,           alignment=TA_CENTER, leading=10)
S_TH7  = ParagraphStyle('u3d_TH7',  fontName='TR-Bold',    fontSize=7,  textColor=white,           alignment=TA_CENTER, leading=9.5)
S_TD   = ParagraphStyle('u3d_TD',   fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10.5)
S_TD7  = ParagraphStyle('u3d_TD7',  fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=9.5)
S_TDC  = ParagraphStyle('u3d_TDC',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=10.5)
S_TDC7 = ParagraphStyle('u3d_TDC7', fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=9.5)
S_YON  = ParagraphStyle('u3d_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12)
S_KAZ  = ParagraphStyle('u3d_KAZ',  fontName='TR-Bold',    fontSize=8,  textColor=COLOR_PRIMARY,   leading=11, spaceBefore=4)
S_SORU = ParagraphStyle('u3d_SORU', fontName='TR-Bold',    fontSize=8.5,textColor=COLOR_TEXT,      leading=12, spaceAfter=2)
S_OPT  = ParagraphStyle('u3d_OPT',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11, spaceAfter=0, leftIndent=6)

TABLE_BASE = [
    ('BACKGROUND',     (0, 0), (-1, 0),  COLOR_PRIMARY),
    ('LINEBELOW',      (0, 0), (-1, 0),  1, COLOR_SECONDARY),
    ('GRID',           (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
    ('TOPPADDING',     (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING',  (0, 0), (-1, 0),  3),
    ('BOTTOMPADDING',  (0, 1), (-1, -1), 5),
    ('LEFTPADDING',    (0, 0), (-1, -1), 4),
    ('RIGHTPADDING',   (0, 0), (-1, -1), 4),
    ('VALIGN',         (0, 0), (-1, -1), 'TOP'),
]

# ── Yardımcı Fonksiyonlar ────────────────────────────────────────────────────

def make_doc(fname, title):
    doc = SimpleDocTemplate(
        os.path.join(OUT, fname),
        pagesize=A4,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        leftMargin=2*cm,  rightMargin=2*cm,
        title=title,
    )
    doc.doc_title  = title
    doc.unite_info = UNITE_INFO
    return doc

def sp(n=4):
    return Spacer(1, n)

def blm(text):
    return Paragraph(text, S_BLM)

def araç_baslik(no_str, ad, alt_bilgi=''):
    t = Table([[
        Paragraph(f'<b>{no_str} — {ad}</b>', S_BAS),
        Paragraph(alt_bilgi, S_ALT),
    ]], colWidths=[11*cm, 6*cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (0,0),(-1,0),  1.5, COLOR_PRIMARY),
        ('TOPPADDING',    (0,0),(-1,-1), 0),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(0,0),   0),
        ('RIGHTPADDING',  (-1,0),(-1,0), 0),
    ]))
    return t

def ogrenci_satiri():
    t = Table([[
        Paragraph('<b>Adı Soyadı:</b>', S_LBL), '',
        Paragraph('<b>Sınıf/No:</b>',   S_LBL), '',
        Paragraph('<b>Tarih:</b>',       S_LBL), '',
    ]], colWidths=[2.7*cm, 5.1*cm, 2*cm, 2.8*cm, 1.5*cm, 2.9*cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (5,0),(5,0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 2),
        ('LEFTPADDING',   (0,0),(-1,-1), 2),
        ('RIGHTPADDING',  (0,0),(-1,-1), 4),
    ]))
    return t

def degerlendiren_satiri():
    t = Table([[
        Paragraph('<b>Değerlendiren:</b>', S_LBL), '',
        Paragraph('<b>Değerlendirilen:</b>', S_LBL), '',
    ]], colWidths=[3*cm, 5.5*cm, 3.5*cm, 5*cm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 2),
        ('LEFTPADDING',   (0,0),(-1,-1), 2),
        ('RIGHTPADDING',  (0,0),(-1,-1), 4),
    ]))
    return t

def yon_kutu(metin):
    t = Table([[Paragraph(metin, S_YON)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND',   (0,0),(-1,-1), COLOR_VERY_LIGHT),
        ('BOX',          (0,0),(-1,-1), 0.5, COLOR_ACCENT),
        ('LEFTPADDING',  (0,0),(-1,-1), 8),
        ('RIGHTPADDING', (0,0),(-1,-1), 8),
        ('TOPPADDING',   (0,0),(-1,-1), 5),
        ('BOTTOMPADDING',(0,0),(-1,-1), 5),
    ]))
    return t

def alan(etiket, n=2):
    return [Paragraph(etiket, S_LBL), WritingLines(n, 15)]

def puan_tablosu(toplam, aralik_rows):
    """
    toplam: '20'
    aralik_rows: [(aralik_str, duzey_str), ...]
    """
    hdr = [Paragraph('Toplam Puan', S_TH), Paragraph('Performans Düzeyi', S_TH)]
    data = [hdr]
    for i, (aralik, duzey) in enumerate(aralik_rows):
        data.append([
            Paragraph(aralik, S_TDC),
            Paragraph(duzey,  S_TD),
        ])
    t = Table(data, colWidths=[4*cm, 13*cm])
    st = [
        ('BACKGROUND',    (0,0),(-1,0),  COLOR_PRIMARY),
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0,1),(-1,-1), [white, COLOR_VERY_LIGHT_GREY]),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(-1,-1), 4),
        ('RIGHTPADDING',  (0,0),(-1,-1), 4),
        ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
    ]
    # Hücre birleştirme — Toplam Puan satırı (2. satır) sol kolonu birleştir
    t.setStyle(TableStyle(st))
    return t

def donut_alan(etiket, n=1):
    return [Paragraph(f'<b>{etiket}:</b>', S_LBL), WritingLines(n, 15)]

def rubrik_tablo(satirlar):
    """
    satirlar: list of (olcut, ustun, yeterli, gelisiyor, destek)
    Döner rubrik tablosu, toplam puan satırı dahil.
    Sütun genişlikleri: [3.2, 3.3, 3.3, 3.3, 3.3, 0.6] = 17cm
    """
    col_w = [3.2*cm, 3.3*cm, 3.3*cm, 3.3*cm, 3.3*cm, 0.6*cm]
    hdr = [
        Paragraph('Ölçüt', S_TH7),
        Paragraph('4 — Üstün', S_TH7),
        Paragraph('3 — Yeterli', S_TH7),
        Paragraph('2 — Gelişiyor', S_TH7),
        Paragraph('1 — Destek Gerekli', S_TH7),
        Paragraph('P', S_TH7),
    ]
    data = [hdr]
    for olcut, ustun, yeterli, gelisiyor, destek in satirlar:
        data.append([
            Paragraph(f'<b>{olcut}</b>', S_TD7),
            Paragraph(ustun,    S_TD7),
            Paragraph(yeterli,  S_TD7),
            Paragraph(gelisiyor,S_TD7),
            Paragraph(destek,   S_TD7),
            Paragraph('',       S_TDC7),
        ])
    data.append([
        Paragraph('<b>Toplam Puan</b>', S_SMBD),
        Paragraph('', S_TD7), Paragraph('', S_TD7),
        Paragraph('', S_TD7), Paragraph('', S_TD7),
        Paragraph('', S_TDC7),
    ])
    t = Table(data, colWidths=col_w)
    st = [
        ('BACKGROUND',    (0,0),(-1,0),  COLOR_PRIMARY),
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0,1),(-1,-2), [white, COLOR_VERY_LIGHT_GREY]),
        ('BACKGROUND',    (0,-1),(-1,-1),COLOR_VERY_LIGHT),
        ('LINEABOVE',     (0,-1),(-1,-1),1, COLOR_PRIMARY),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(-1,-1), 3),
        ('RIGHTPADDING',  (0,0),(-1,-1), 3),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        # Son satırda colspan simulasyonu — sol 5 hücreyi birleştir
        ('SPAN',          (0,-1),(4,-1)),
        ('ALIGN',         (0,-1),(4,-1),'LEFT'),
        ('ALIGN',         (5,-1),(5,-1),'CENTER'),
    ]
    t.setStyle(TableStyle(st))
    return t

def donüt_alan(n=3):
    return [Paragraph('<b>Öğretmen Dönütü:</b>', S_LBL), WritingLines(n, 15)]

DUZEYER = [
    ('17–20', 'Üstün'),
    ('13–16', 'Yeterli'),
    ('8–12',  'Gelişiyor'),
    ('0–7',   'Destek Gerekli'),
]


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 1 — Süreç Gözlem Formu (Sayfa 1: Ders 1–5)
# ═══════════════════════════════════════════════════════════════════════════

def arac1():
    e = []

    # Sayfa 1 — Ders 1–5
    e.append(araç_baslik('Araç 1', 'Süreç Gözlem Formu',
                         'TT.7.3.1  •  10 Ders Saati  •  20 Öğrenci'))
    e.append(ogrenci_satiri())
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(4))
    e.append(yon_kutu(
        'Bu form, 10 ders saati boyunca her öğrencinin süreç katılımını izlemek için kullanılır. '
        'Her ders sonunda doldurulur. Not vermek için değil, öğrenme sürecini takip etmek için hazırlanmıştır. '
        'Form iki bölümdür: Ders 1–5 (bu sayfa) ve Ders 6–10 (arkası).'
    ))
    e.append(sp(6))

    # Ölçek tablosu
    e.append(blm('Değerlendirme Ölçeği'))
    olcek_data = [
        [Paragraph('Simge', S_TH), Paragraph('Anlamı', S_TH)],
        [Paragraph('A', S_TDC), Paragraph('Çok İyi — beklentinin üzerinde, bağımsız ve özgün katılım', S_TD)],
        [Paragraph('B', S_TDC), Paragraph('İyi — beklenen düzeyde, etkin katılım', S_TD)],
        [Paragraph('C', S_TDC), Paragraph('Gelişiyor — katılım var ancak yönlendirme gerekiyor', S_TD)],
        [Paragraph('D', S_TDC), Paragraph('Destek Gerekli — sınırlı katılım, birebir destek şart', S_TD)],
        [Paragraph('—', S_TDC), Paragraph('Gözlenmedi — o gün devamsız veya değerlendirme yapılamadı', S_TD)],
    ]
    olcek_t = Table(olcek_data, colWidths=[1.5*cm, 15.5*cm])
    olcek_t.setStyle(TableStyle(TABLE_BASE))
    e.append(olcek_t)
    e.append(sp(6))

    # Beceriler 1–5
    e.append(blm('Gözlenen Beceriler — Ders 1–5'))
    bec_data = [
        [Paragraph('Ders', S_TH), Paragraph('Odak', S_TH),
         Paragraph('Gözlenen Ana Beceri', S_TH), Paragraph('Kazanım', S_TH)],
        [Paragraph('1', S_TDC), Paragraph('Tasarım nedir?', S_TD),
         Paragraph('Design Thinking döngüsünü kavrama, ilgi gösterme', S_TD),
         Paragraph('TT.7.3.1', S_TDC)],
        [Paragraph('2', S_TDC), Paragraph('Problem tespiti', S_TD),
         Paragraph('Gerçek bir problemi gözlem yoluyla tanımlama', S_TD),
         Paragraph('TT.7.3.1.a', S_TDC)],
        [Paragraph('3', S_TDC), Paragraph('Analiz / Empati', S_TD),
         Paragraph('Kullanıcı perspektifini benimseme, empati haritası doldurma', S_TD),
         Paragraph('TT.7.3.1.b', S_TDC)],
        [Paragraph('4', S_TDC), Paragraph('Fikir üretimi', S_TD),
         Paragraph('Beyin fırtınası etkinliğine katılım, fikir çeşitliliği', S_TD),
         Paragraph('TT.7.3.1.c', S_TDC)],
        [Paragraph('5', S_TDC), Paragraph('Eskiz / Taslak', S_TD),
         Paragraph('Fikri görselleştirme, malzeme planlama', S_TD),
         Paragraph('TT.7.3.1.d', S_TDC)],
    ]
    bec_t = Table(bec_data, colWidths=[1.2*cm, 3.3*cm, 9.5*cm, 3*cm])
    bec_t.setStyle(TableStyle(TABLE_BASE))
    e.append(bec_t)
    e.append(sp(6))

    # Gözlem tablosu 1–5
    e.append(blm('Gözlem Tablosu — Ders 1–5'))
    col_no   = 0.7*cm
    col_ad   = 4.7*cm
    col_ders = (TW - col_no - col_ad) / 5
    goz_hdr = [
        Paragraph('No', S_TH), Paragraph('Adı Soyadı', S_TH),
        Paragraph('1.', S_TH), Paragraph('2.', S_TH),
        Paragraph('3.', S_TH), Paragraph('4.', S_TH), Paragraph('5.', S_TH),
    ]
    goz_data = [goz_hdr]
    for i in range(1, 21):
        goz_data.append([
            Paragraph(str(i), S_TDC), Paragraph('', S_TD),
            Paragraph('', S_TDC), Paragraph('', S_TDC),
            Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC),
        ])
    goz_t = Table(goz_data, colWidths=[col_no, col_ad] + [col_ders]*5,
                  rowHeights=[0.55*cm] + [0.48*cm]*20)
    goz_t.setStyle(TableStyle([
        *TABLE_BASE,
        ('BOTTOMPADDING', (0,1),(-1,-1), 3),
    ]))
    e.append(goz_t)

    # Sayfa 2 — Ders 6–10
    e.append(PageBreak())
    e.append(araç_baslik('Araç 1 (devam)', 'Süreç Gözlem Formu — Ders 6–10',
                         'TT.7.3.1  •  TT.7.3.2'))
    e.append(sp(6))

    bec_data2 = [
        [Paragraph('Ders', S_TH), Paragraph('Odak', S_TH),
         Paragraph('Gözlenen Ana Beceri', S_TH), Paragraph('Kazanım', S_TH)],
        [Paragraph('6', S_TDC), Paragraph('Uygulama', S_TD),
         Paragraph('Prototip üretim sürecine katılım, malzeme kullanımı', S_TD),
         Paragraph('TT.7.3.1.e', S_TDC)],
        [Paragraph('7', S_TDC), Paragraph('Uygulama', S_TD),
         Paragraph('Prototip tamamlama, detay çalışması', S_TD),
         Paragraph('TT.7.3.1.e', S_TDC)],
        [Paragraph('8', S_TDC), Paragraph('Test / Geri Bildirim', S_TD),
         Paragraph('Kullanıcıya test ettirme, yapıcı geri bildirim alma/verme', S_TD),
         Paragraph('TT.7.3.1.f', S_TDC)],
        [Paragraph('9', S_TDC), Paragraph('Revize', S_TD),
         Paragraph('Geri bildirimleri tasarıma yansıtma, ergonomi/sürdürülebilirlik farkındalığı', S_TD),
         Paragraph('TT.7.3.1.g', S_TDC)],
        [Paragraph('10', S_TDC), Paragraph('Sunum', S_TD),
         Paragraph('Tasarım sürecini yapılandırarak sunma, öz değerlendirme', S_TD),
         Paragraph('TT.7.3.2', S_TDC)],
    ]
    bec_t2 = Table(bec_data2, colWidths=[1.2*cm, 3.3*cm, 9.5*cm, 3*cm])
    bec_t2.setStyle(TableStyle(TABLE_BASE))
    e.append(bec_t2)
    e.append(sp(6))

    e.append(blm('Gözlem Tablosu — Ders 6–10 + Genel'))
    col_ders2 = (TW - col_no - col_ad) / 6
    goz_hdr2 = [
        Paragraph('No', S_TH), Paragraph('Adı Soyadı', S_TH),
        Paragraph('6.', S_TH), Paragraph('7.', S_TH),
        Paragraph('8.', S_TH), Paragraph('9.', S_TH),
        Paragraph('10.', S_TH), Paragraph('Genel', S_TH),
    ]
    goz_data2 = [goz_hdr2]
    for i in range(1, 21):
        goz_data2.append([
            Paragraph(str(i), S_TDC), Paragraph('', S_TD),
            Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC),
            Paragraph('', S_TDC), Paragraph('', S_TDC), Paragraph('', S_TDC),
        ])
    goz_t2 = Table(goz_data2, colWidths=[col_no, col_ad] + [col_ders2]*6,
                   rowHeights=[0.55*cm] + [0.48*cm]*20)
    goz_t2.setStyle(TableStyle([
        *TABLE_BASE,
        ('BOTTOMPADDING', (0,1),(-1,-1), 3),
    ]))
    e.append(goz_t2)
    e.append(sp(8))

    # Notlar
    e.append(blm('Öğretmen Notları'))
    e += alan('Ek destek gereksinimi olan öğrenciler:', 2)
    e.append(sp(3))
    e += alan('Zenginleştirme adayı öğrenciler:', 2)
    e.append(sp(3))
    e += alan('Sınıf geneline ilişkin gözlemler:', 2)

    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 2 — Eskiz Rubriği (ÇK6 + ÇK7)
# ═══════════════════════════════════════════════════════════════════════════

def arac2():
    e = []
    e.append(araç_baslik('Araç 2', 'Eskiz Rubriği',
                         'TT.7.3.1.d  •  5. Ders  •  ÇK6 + ÇK7'))
    e.append(ogrenci_satiri())
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(4))
    e.append(yon_kutu(
        'Bu rubrik, ÇK6 (Tasarım Eskizi Sayfası) ve ÇK7 (Malzeme Planlama Tablosu) birlikte değerlendirilir. '
        'Kazanım: TT.7.3.1.d — Tasarım fikrinin görsel taslağını oluşturur; malzeme ve ihtiyaçları planlar.'
    ))
    e.append(sp(6))
    e.append(rubrik_tablo([
        (
            'Problem–Tasarım Uyumu',
            'Eskiz, tanımlanan probleme doğrudan yanıt veriyor; kullanıcı ve kullanım bağlamı yansıtılmış.',
            'Eskiz problemle ilişkili, bağlantı büyük ölçüde kurulmuş.',
            'Eskiz çizilmiş fakat problemle bağlantısı zayıf ya da belirsiz.',
            'Eskiz ile problem arasında bağ kurulamıyor.',
        ),
        (
            'Eskiz Netliği ve Okunabilirliği',
            'Çizim açık ve anlaşılır; farklı açılardan gösterim (ön/üst/detay) yapılmış.',
            'Ana görünüm net, bir-iki ek açı eklenmiş.',
            'Tek görünüm var, okunabilir ancak yetersiz detay.',
            'Eskiz karmaşık ya da anlaşılmaz.',
        ),
        (
            'Ölçü ve Boyut Belirtme',
            'Tüm kritik ölçüler ve boyutlar belirtilmiş; gerçekçi oran-orantı gözetilmiş.',
            'Çoğu ölçü belirtilmiş, küçük eksikler var.',
            'Birkaç ölçü belirtilmiş ama yetersiz.',
            'Ölçü / boyut bilgisi yok.',
        ),
        (
            'Malzeme Planlama (ÇK7)',
            'Malzeme listesi eksiksiz; her malzemenin neden seçildiği gerekçelendirilmiş, alternatifler düşünülmüş.',
            'Malzeme listesi tamamlanmış, gerekçe büyük ölçüde verilmiş.',
            'Malzeme listesi kısmen tamamlanmış.',
            'Malzeme listesi boş ya da gerçekçi değil.',
        ),
        (
            'Sürdürülebilirlik Farkındalığı',
            'Seçilen malzemelerin çevre etkisi değerlendirilmiş; geri dönüştürülebilir seçenekler önerilmiş.',
            'Sürdürülebilirlik düşünülmüş, bir-iki öneri yapılmış.',
            'Sürdürülebilirliğe değinilmiş ama yüzeysel.',
            'Sürdürülebilirlik göz ardı edilmiş.',
        ),
    ]))
    e.append(sp(8))
    e.append(puan_tablosu('20', DUZEYER))
    e.append(sp(8))
    e += donüt_alan(3)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 3 — Prototip Rubriği (ÇK8)
# ═══════════════════════════════════════════════════════════════════════════

def arac3():
    e = []
    e.append(araç_baslik('Araç 3', 'Prototip Rubriği',
                         'TT.7.3.1.e  •  7. Ders  •  ÇK8'))
    e.append(ogrenci_satiri())
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(4))
    e.append(yon_kutu(
        'Bu rubrik, ÇK8 (Prototip Süreç Günlüğü) ve üretilen fiziksel prototip birlikte değerlendirilir. '
        'Kazanım: TT.7.3.1.e — Tasarım eskizini üç boyutlu bir prototipe / makete dönüştürür.'
    ))
    e.append(sp(6))
    e.append(rubrik_tablo([
        (
            'Eskiz–Prototip Uyumu',
            'Prototip, eskizdeki tasarım fikrine sadık biçimde üretilmiş; plan ile uygulama örtüşüyor.',
            'Büyük ölçüde uyumlu, küçük sapmalar var.',
            'Eskizden belirgin sapma var ancak temel fikir korunmuş.',
            'Prototip eskizle örtüşmüyor.',
        ),
        (
            'İşçilik Kalitesi',
            'Malzemeler özenle kullanılmış; yapı sağlam, detaylara dikkat edilmiş.',
            'Genel olarak özenli, küçük işçilik hataları var.',
            'Prototip tamamlanmış ama kaba ya da dağınık.',
            'Prototip tamamlanmamış ya da işlevsiz.',
        ),
        (
            'Süreç Günlüğü Tutarlılığı (ÇK8)',
            'Her ders için adımlar, güçlükler ve çözümler düzenli biçimde kayıt altına alınmış.',
            'Süreç büyük ölçüde kayıt altına alınmış.',
            'Kısmi kayıt; bazı alanlar boş bırakılmış.',
            'Günlük doldurmamış.',
        ),
        (
            'Ergonomi Farkındalığı',
            'Prototipin kullanıcıya uygunluğu düşünülmüş; boyut, tutuş veya kullanım kolaylığı değerlendirilmiş.',
            'Ergonomi düşünülmüş, bir-iki örnek verilmiş.',
            'Ergonomiye değinilmiş ama yüzeysel.',
            'Ergonomi göz ardı edilmiş.',
        ),
        (
            'Sorun Çözme Yetkinliği',
            'Üretim sırasında karşılaşılan güçlükler bağımsız biçimde çözülmüş; alternatif yollar denenmiş.',
            'Güçlükler genellikle çözülmüş, zaman zaman destek alınmış.',
            'Güçlükleri çözmek için sürekli yönlendirmeye ihtiyaç duyulmuş.',
            'Güçlükler çözülememiş, üretim tamamlanamamış.',
        ),
    ]))
    e.append(sp(8))
    e.append(puan_tablosu('20', DUZEYER))
    e.append(sp(8))
    e += donüt_alan(3)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 4 — Sunum Rubriği (ÇK11)
# ═══════════════════════════════════════════════════════════════════════════

def arac4():
    e = []
    e.append(araç_baslik('Araç 4', 'Sunum Rubriği',
                         'TT.7.3.2  •  10. Ders  •  ÇK11'))
    e.append(ogrenci_satiri())
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(4))
    e.append(yon_kutu(
        'Bu rubrik, ÇK11 (Tasarım Süreci Sunum Şablonu) ve sözlü / görsel sunum birlikte değerlendirilir. '
        'Kazanım: TT.7.3.2 — Tasarım sürecini ve ürününü yapılandırarak sınıfa sunar; öz değerlendirme yapar.'
    ))
    e.append(sp(6))
    e.append(rubrik_tablo([
        (
            'Sürecin Tamamlanmış Aktarımı',
            '7 adımın tamamını kendi deneyimiyle ilişkilendirerek anlamlı biçimde aktarmış.',
            'Çoğu adımı aktarmış, bir-iki adım eksik ya da yüzeysel.',
            '3–4 adımı aktarabilmiş.',
            '2 veya daha az adımı aktarabilmiş.',
        ),
        (
            'Problemi ve Çözümü Netleştirme',
            'Problemi, hedef kullanıcıyı ve tasarımının nasıl bir çözüm sunduğunu açıkça ifade etmiş.',
            'Problem ve çözüm anlatılmış, kullanıcı bağlantısı kısmen kurulmuş.',
            'Problem anlatılmış fakat çözüm bağlantısı zayıf.',
            'Problemi veya çözümü netleştirememiş.',
        ),
        (
            'Geri Bildirim–Revize Yansıması',
            'Test aşamasında aldığı geri bildirimleri ve bunlara göre yaptığı değişiklikleri somut örneklerle açıklamış.',
            'Geri bildirim–revize ilişkisini kurmuş, örnekler kısmen somut.',
            'Revize yaptığını belirtmiş ama geri bildirimle bağlantısı belirsiz.',
            'Geri bildirim ve revizeye değinmemiş.',
        ),
        (
            'Öz Değerlendirme Derinliği',
            'Neyin iyi gittiğini ve neyi değiştireceğini gerçekçi ve özgün bir bakışla değerlendirmiş.',
            'Öz değerlendirme yapılmış, büyük ölçüde gerçekçi.',
            'Yüzeysel; yalnızca güçlü ya da yalnızca zayıf yan belirtilmiş.',
            'Öz değerlendirme yapılmamış.',
        ),
        (
            'Sözlü İfade ve Tasarım Dili',
            'Akıcı ve özgüvenli konuşmuş; prototip, empati, inovasyon, ergonomi gibi terimleri doğru kullanmış.',
            'Kavramları büyük ölçüde doğru kullanmış, hafif tereddütler var.',
            'Kavramları az ya da hatalı kullanmış.',
            'Tasarım dili kullanmamış, ezber ya da okunmuş gibi.',
        ),
    ]))
    e.append(sp(8))
    e.append(puan_tablosu('20', DUZEYER))
    e.append(sp(8))
    e += donüt_alan(3)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 5 — Akran Değerlendirme Formu
# ═══════════════════════════════════════════════════════════════════════════

def arac5():
    e = []
    e.append(araç_baslik('Araç 5', 'Akran Değerlendirme Formu',
                         'TT.7.3.1.f  •  8. Ders — Test Aşaması'))
    e.append(degerlendiren_satiri())
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(4))
    e.append(yon_kutu(
        'Bu form, test aşamasında (8. Ders) arkadaşının prototipini inceleyen öğrenci tarafından doldurulur. '
        'Kullanıcı gibi düşün — tasarımcı değil, kullanan biri olarak değerlendir. '
        'Dürüst ol, nazik ol. Eleştiri tasarımın en iyi arkadaşıdır.'
    ))
    e.append(sp(6))

    # Kullanım değerlendirme tablosu
    e.append(blm('Kullanım Değerlendirmesi'))
    e.append(Paragraph('3 = Çok iyi  •  2 = Yeterli  •  1 = Geliştirilebilir', S_SMIT))
    e.append(sp(3))
    alan_data = [
        [Paragraph('Değerlendirme Alanı', S_TH),
         Paragraph('3', S_TH), Paragraph('2', S_TH), Paragraph('1', S_TH)],
        [Paragraph('Tasarım, tanımlanan problemi gerçekten çözüyor', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Kullanımı kolay ve anlaşılır', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Dayanıklı ve sağlam görünüyor', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Elime / vücuduma uygun hissettiriyor (ergonomi)', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Genel olarak özgün bir fikir taşıyor', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
    ]
    alan_t = Table(alan_data, colWidths=[12.5*cm, 1.5*cm, 1.5*cm, 1.5*cm])
    alan_t.setStyle(TableStyle(TABLE_BASE))
    e.append(alan_t)
    e.append(sp(8))

    e.append(blm('Arkadaşımın Tasarımında Güçlü Bulduğum 2 Şey'))
    e += alan('1.', 2)
    e.append(sp(3))
    e += alan('2.', 2)
    e.append(sp(8))

    e.append(blm('Geliştirilebilir Bir Öneri (Nazikçe ve Somut)'))
    e.append(Paragraph('"Bence ... yapılabilir çünkü ..." kalıbını kullanmayı dene.', S_SMIT))
    e += alan('', 2)
    e.append(sp(8))

    e.append(blm('Tasarımı Kullanan Biri Olarak Sorum'))
    e.append(Paragraph('Bu tasarımı gerçekten hayatımda kullansaydım hangi soruyu sorardım?', S_SMIT))
    e += alan('', 2)

    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 6 — Ünite Sonu Sınavı (Öğrenci Kopyası)
# ═══════════════════════════════════════════════════════════════════════════

MCQ_SORULAR = [
    (
        '1. Tasarım Odaklı Düşünme sürecinde "empati" adımının temel amacı nedir?',
        ['A) Fikir üretmek için beyin fırtınası yapmak',
         'B) Problemi yaşayan kişinin yerine geçerek ihtiyaçlarını ve duygularını anlamak',
         'C) Tasarımı test etmek ve geri bildirim almak',
         'D) Prototip üretmek için malzeme seçmek'],
    ),
    (
        '2. Aşağıdakilerden hangisi "prototip"i en doğru tanımlar?',
        ['A) Satışa hazır son ürün',
         'B) Tasarımın bilgisayarda çizilmiş görseli',
         'C) Tasarım fikrinin test edilmesi için yapılan deneme modeli',
         'D) Bir ürünün fabrikada üretilen ilk kopyası'],
    ),
    (
        '3. Design Thinking döngüsünde "Nasıl çözebiliriz?" sorusu hangi adımda sorulur?',
        ['A) Problem Tespiti',
         'B) Empati',
         'C) Fikir Üretimi',
         'D) Test / Geri Bildirim'],
    ),
    (
        '4. Ergonomi kavramı tasarımda neyi ifade eder?',
        ['A) Ürünün görsel açıdan güzel olması',
         'B) Ürünün ucuz malzemeyle üretilmesi',
         'C) Ürünün insan vücuduna, hareketlerine ve kullanım alışkanlıklarına uygun tasarlanması',
         'D) Ürünün çevre dostu olması'],
    ),
    (
        '5. Aşağıdakilerden hangisi "sürdürülebilir tasarım" için en doğru tanımdır?',
        ['A) Her yıl güncellenen, moda olan ürünler tasarlamak',
         'B) Geleceği düşünerek az kaynak harcayan, geri dönüştürülebilir, uzun ömürlü ürünler tasarlamak',
         'C) Yalnızca doğal malzeme kullanan ürünler tasarlamak',
         'D) Tasarım sürecini mümkün olduğunca kısa tutmak'],
    ),
    (
        '6. "Crazy 8" etkinliği Design Thinking\'in hangi adımında kullanılır ve amacı nedir?',
        ['A) Problem Tespiti — problemi 8 farklı açıdan incelemek',
         'B) Fikir Üretimi — 8 dakikada 8 farklı fikir çizmek',
         'C) Test Aşaması — 8 kullanıcıyla ürünü denemek',
         'D) Revize — tasarımda 8 değişiklik yapmak'],
    ),
    (
        '7. Bir tasarım prototipi test edilirken kullanıcıdan gelen eleştiri nasıl değerlendirilmelidir?',
        ['A) Tasarımın başarısız olduğu anlamına gelir; sıfırdan başlanmalıdır',
         'B) Görmezden gelinmeli; tasarımcı kendi kararında ısrar etmelidir',
         'C) Tasarımı geliştirme fırsatı olarak görülmeli ve revize aşamasına taşınmalıdır',
         'D) Yalnızca çok sayıda kişi aynı eleştiriyi yapıyorsa dikkate alınmalıdır'],
    ),
    (
        '8. Tasarım Odaklı Düşünme döngüsü "revize" adımıyla neden bitmez?',
        ['A) Çünkü revize yapmak çok zaman alır',
         'B) Çünkü tasarım mükemmele ulaştığında döngü otomatik olarak durur',
         'C) Çünkü revize edilen ürün yeni bir döngünün başlangıcıdır; tasarım sürekli gelişir',
         'D) Çünkü revize adımından sonra sunum zorunludur'],
    ),
]

def arac6_ogrenci():
    e = []
    # Başlık ve öğrenci bilgisi
    e.append(araç_baslik('Araç 6', 'Ünite Sonu Sınavı — Öğrenci Kopyası',
                         'TT.7.3.1  •  TT.7.3.2  •  35 Dakika  •  100 Puan'))
    e.append(ogrenci_satiri())
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(4))
    e.append(yon_kutu(
        'Bu sınav 3 bölümden oluşur: Çoktan Seçmeli (40 puan) + Kısa Cevaplı (30 puan) + Performans Görevi (30 puan). '
        'Toplam süre: 35 dakika. Kurşun kalem kullan. Yanıtını değiştirmek istersen üzerini çiz ve yanına yaz.'
    ))
    e.append(sp(6))

    # ── Bölüm 1: MCQ ───────────────────────────────────────────────
    e.append(blm('BÖLÜM 1 — ÇOKTAN SEÇMELİ  (8 soru × 5 puan = 40 puan)'))
    for soru_txt, secenekler in MCQ_SORULAR:
        blok = [
            Paragraph(soru_txt, S_SORU),
            *[Paragraph(s, S_OPT) for s in secenekler],
            sp(4),
            HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.4),
            sp(4),
        ]
        e += blok

    # Bölüm 1 puanlama tablosu
    e.append(blm('Bölüm 1 — Puanlama Tablosu'))
    p1_hdr = [Paragraph('Soru', S_TH)] + [Paragraph(str(i), S_TH) for i in range(1, 9)] + [Paragraph('Toplam', S_TH)]
    p1_cvp = [Paragraph('Cevap', S_SMBD)] + [Paragraph('', S_TDC)]*8 + [Paragraph('', S_TDC)]
    p1_puan = [Paragraph('Puan', S_SMBD)] + [Paragraph('', S_TDC)]*8 + [Paragraph('____ / 40', S_TDC)]
    p1_t = Table([p1_hdr, p1_cvp, p1_puan],
                 colWidths=[1.7*cm] + [1.7*cm]*8 + [2.1*cm])
    p1_t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0),  COLOR_PRIMARY),
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0,1),(-1,-1), [white, COLOR_VERY_LIGHT_GREY]),
        ('TOPPADDING',    (0,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(-1,-1), 3),
        ('RIGHTPADDING',  (0,0),(-1,-1), 3),
        ('ALIGN',         (0,0),(-1,-1), 'CENTER'),
        ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
    ]))
    e.append(p1_t)
    e.append(sp(8))

    # ── Bölüm 2: Kısa Cevaplı ──────────────────────────────────────
    e.append(blm('BÖLÜM 2 — KISA CEVAPLI SORULAR  (3 soru × 10 puan = 30 puan)'))
    e.append(Paragraph('<b>Soru 9.</b>  Tasarım Odaklı Düşünme sürecinin <b>7 adımını</b> '
                       'sırasıyla yazınız ve her adımı <b>bir cümleyle</b> açıklayınız.', S_SORU))
    e.append(sp(3))
    adim_hdr = [Paragraph('Adım', S_TH), Paragraph('Adın', S_TH), Paragraph('Açıklama (bir cümle)', S_TH)]
    adim_data = [adim_hdr]
    for i in range(1, 8):
        adim_data.append([
            Paragraph(str(i), S_TDC),
            Paragraph('', S_TD),
            Paragraph('', S_TD),
        ])
    adim_t = Table(adim_data, colWidths=[1.2*cm, 4*cm, 11.8*cm],
                   rowHeights=[0.55*cm] + [0.65*cm]*7)
    adim_t.setStyle(TableStyle([
        *TABLE_BASE,
        ('BOTTOMPADDING', (0,1),(-1,-1), 3),
    ]))
    e.append(adim_t)
    e.append(sp(8))

    e.append(Paragraph('<b>Soru 10.</b>  <b>"Empati"</b> ile <b>"sempati"</b> arasındaki farkı açıklayınız. '
                       'Tasarım sürecinde empati neden sempati yerine tercih edilir? '
                       'Kendi tasarım sürecinizden <b>bir örnek</b> vererek açıklayınız.', S_SORU))
    e += alan('', 3)
    e.append(sp(8))

    e.append(Paragraph('<b>Soru 11.</b>  Bir prototip neden <b>mükemmel olmak zorunda değildir?</b> '
                       'Prototip yapmanın asıl amacını açıklayınız. Bu ünite boyunca kendi prototipi̇ni̇zi̇ '
                       'yaparken hangi güçlükleri yaşadınız ve bunları nasıl çözdünüz?', S_SORU))
    e += alan('', 3)
    e.append(sp(8))

    # ── Bölüm 3: Performans Görevi ─────────────────────────────────
    e.append(blm('BÖLÜM 3 — PERFORMANS GÖREVİ  (30 puan)'))
    e.append(Paragraph(
        '<b>Soru 12.</b>  Aşağıdaki senaryoyu okuyunuz ve görevleri tamamlayınız.',
        S_SORU))
    e.append(sp(3))
    e.append(yon_kutu(
        'Mahallenizdeki yaşlı bir komşunuz, pazardan getirdiği ağır poşetleri '
        'merdiven çıkarken taşımakta zorlanıyor.'
    ))
    e.append(sp(6))

    # a) Empati analizi
    e.append(Paragraph('<b>a)</b> Bu problemi yaşayan kişi için kısa bir '
                       '<b>empati analizi</b> yapınız. (10 puan)', S_SORU))
    e.append(sp(3))
    emp_hdr  = [Paragraph('Empati Boyutu', S_TH), Paragraph('Notlarım', S_TH)]
    emp_data = [emp_hdr]
    for boyut in ['Ne hissediyor?', 'Ne düşünüyor?',
                  'Ne istiyor / ihtiyacı ne?', 'Önündeki engeller neler?']:
        emp_data.append([Paragraph(boyut, S_TD), Paragraph('', S_TD)])
    emp_t = Table(emp_data, colWidths=[4.5*cm, 12.5*cm],
                  rowHeights=[0.55*cm] + [1.1*cm]*4)
    emp_t.setStyle(TableStyle(TABLE_BASE))
    e.append(emp_t)
    e.append(sp(6))

    # b) Fikir üretimi
    e.append(Paragraph('<b>b)</b> Bu problemi çözmek için <b>en az 3 farklı fikir</b> '
                       'üretiniz. Her fikri bir cümleyle açıklayınız. (10 puan)', S_SORU))
    e.append(sp(3))
    fikir_hdr  = [Paragraph('Fikir', S_TH), Paragraph('Açıklama', S_TH)]
    fikir_data = [fikir_hdr]
    for i in range(1, 4):
        fikir_data.append([Paragraph(str(i), S_TDC), Paragraph('', S_TD)])
    fikir_t = Table(fikir_data, colWidths=[1.2*cm, 15.8*cm],
                    rowHeights=[0.55*cm] + [1.1*cm]*3)
    fikir_t.setStyle(TableStyle(TABLE_BASE))
    e.append(fikir_t)
    e.append(sp(6))

    # c) Taslak
    e.append(Paragraph('<b>c)</b> En iyi bulduğunuz fikrin <b>taslak eskizini</b> aşağıya çiziniz. '
                       'Ergonomi ve sürdürülebilirlik açısından birer özelliğini belirtiniz. (10 puan)', S_SORU))
    e.append(sp(3))
    e.append(DrawingBox(height=7.5*cm, caption='Taslak Çizim Alanı'))
    e.append(sp(5))
    e += alan('Ergonomi özelliği:', 1)
    e.append(sp(3))
    e += alan('Sürdürülebilirlik özelliği:', 1)
    e.append(sp(8))

    # Genel puanlama
    e.append(blm('Genel Puanlama'))
    gp_data = [
        [Paragraph('Bölüm', S_TH), Paragraph('Puan', S_TH)],
        [Paragraph('Bölüm 1 — Çoktan Seçmeli (1–8)', S_TD),  Paragraph('____ / 40', S_TDC)],
        [Paragraph('Bölüm 2 — Kısa Cevaplı (9–11)', S_TD),   Paragraph('____ / 30', S_TDC)],
        [Paragraph('Bölüm 3 — Performans Görevi (12)', S_TD), Paragraph('____ / 30', S_TDC)],
        [Paragraph('<b>TOPLAM</b>', S_SMBD),                   Paragraph('<b>____ / 100</b>', S_TDC)],
    ]
    gp_t = Table(gp_data, colWidths=[13*cm, 4*cm])
    gp_t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0),  COLOR_PRIMARY),
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0,1),(-1,-2), [white, COLOR_VERY_LIGHT_GREY]),
        ('BACKGROUND',    (0,-1),(-1,-1),COLOR_LIGHT),
        ('LINEABOVE',     (0,-1),(-1,-1),1, COLOR_PRIMARY),
        ('TOPPADDING',    (0,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
        ('LEFTPADDING',   (0,0),(-1,-1), 6),
        ('RIGHTPADDING',  (0,0),(-1,-1), 6),
        ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
    ]))
    e.append(gp_t)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 6 — Cevap Anahtarı (Yalnızca Öğretmen)
# ═══════════════════════════════════════════════════════════════════════════

def arac6_cevap():
    e = []
    e.append(araç_baslik('Araç 6 — Cevap Anahtarı',
                         'Ünite Sonu Sınavı (Yalnızca Öğretmen Kullanımı)',
                         'Bu sayfa öğrencilere dağıtılmaz'))
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(6))

    # Bölüm 1 cevaplar
    e.append(blm('Bölüm 1 — Çoktan Seçmeli Cevaplar'))
    cv_hdr  = [Paragraph('Soru', S_TH), Paragraph('Cevap', S_TH), Paragraph('Kazanım', S_TH)]
    cv_data = [cv_hdr] + [
        [Paragraph(str(n), S_TDC), Paragraph(c, S_TDC), Paragraph(k, S_TD)]
        for n, c, k in [
            (1, 'B', 'TT.7.3.1.b'),
            (2, 'C', 'TT.7.3.1.e'),
            (3, 'C', 'TT.7.3.1.c'),
            (4, 'C', 'TT.7.3.1.d / genel'),
            (5, 'B', 'TT.7.3.1.g'),
            (6, 'B', 'TT.7.3.1.c'),
            (7, 'C', 'TT.7.3.1.f–g'),
            (8, 'C', 'TT.7.3.1 genel'),
        ]
    ]
    cv_t = Table(cv_data, colWidths=[2*cm, 2*cm, 13*cm])
    cv_t.setStyle(TableStyle(TABLE_BASE))
    e.append(cv_t)
    e.append(sp(8))

    # Bölüm 2 kılavuz
    e.append(blm('Bölüm 2 — Kısa Cevaplı Puanlama Kılavuzu'))

    kilavuz = [
        ('<b>Soru 9 (10 puan)</b>',
         'Her doğru adım adı: 0,5 puan × 7 = 3,5 puan. '
         'Her anlamlı açıklama: ≈1 puan × 7 = en fazla 6,5 puan (toplam 10). '
         'Beklenen sıra: Problem Tespiti — Analiz/Empati — Fikir Üretimi — Eskiz/Taslak — Uygulama/Prototip — Test/Geri Bildirim — Revize. '
         'Sıralama hatası varsa ve açıklama doğruysa tam puan; hem isim hem açıklama yanlışsa 0 puan.'),
        ('<b>Soru 10 (10 puan)</b>',
         'Farkı doğru tanımlamış (4p): Empati = kişinin yerine geçmek, hissettiklerini anlamak; Sempati = acımak, kendi penceresinden yaklaşmak. '
         'Tasarımda neden empati gerektiğini açıklamış (3p): Tasarımcı kullanıcının gerçek ihtiyacını ancak empatiyle keşfedebilir. '
         'Kendi tasarım sürecinden makul örnek vermiş (3p).'),
        ('<b>Soru 11 (10 puan)</b>',
         'Prototip amacını doğru açıklamış (4p): hızlı test etmek, hata yakalamak, kullanıcıya göstermek; mükemmellik değil işe yararlık. '
         '"Mükemmel olmak zorunda değil" gerekçesi (3p): zaman kısıtı, fikrin denemesi, revize için açık olma. '
         'Kişisel güçlük ve çözüm örneği (3p): özgün ve tutarlı deneyim aktarımı.'),
    ]
    for baslik, aciklama in kilavuz:
        t = Table([[Paragraph(baslik, S_SMBD), Paragraph(aciklama, S_SML)]],
                  colWidths=[3.5*cm, 13.5*cm])
        t.setStyle(TableStyle([
            ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
            ('BACKGROUND',    (0,0),(0,0),   COLOR_VERY_LIGHT),
            ('TOPPADDING',    (0,0),(-1,-1), 4),
            ('BOTTOMPADDING', (0,0),(-1,-1), 6),
            ('LEFTPADDING',   (0,0),(-1,-1), 5),
            ('RIGHTPADDING',  (0,0),(-1,-1), 5),
            ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ]))
        e.append(t)
        e.append(sp(3))

    e.append(sp(6))

    # Bölüm 3 kılavuz
    e.append(blm('Bölüm 3 — Performans Görevi Puanlama Kılavuzu  (30 puan)'))
    p3_hdr  = [Paragraph('Alt Görev', S_TH), Paragraph('Puan', S_TH), Paragraph('Değerlendirme Kriteri', S_TH)]
    p3_data = [p3_hdr,
        [Paragraph('a) Empati Analizi', S_TD), Paragraph('0–10', S_TDC),
         Paragraph('4 boyutun tamamı dolu (4p) + kullanıcı perspektifinden yazılmış (3p) + somut ve senaryoya özgü (3p)', S_TD)],
        [Paragraph('b) Fikir Üretimi', S_TD), Paragraph('0–10', S_TDC),
         Paragraph('En az 3 farklı fikir (3p) + fikirler birbirinden belirgin biçimde farklı (4p) + açıklayıcı cümle (3p)', S_TD)],
        [Paragraph('c) Taslak + Ergonomi / Sürdürülebilirlik', S_TD), Paragraph('0–10', S_TDC),
         Paragraph('Taslak çizilmiş ve problemi çözüyor (4p) + ergonomi özelliği belirtilmiş (3p) + sürdürülebilirlik özelliği (3p)', S_TD)],
    ]
    p3_t = Table(p3_data, colWidths=[4.5*cm, 1.5*cm, 11*cm])
    p3_t.setStyle(TableStyle(TABLE_BASE))
    e.append(p3_t)
    e.append(sp(8))

    # Kazanım dağılımı
    e.append(blm('Kazanım Bazlı Dağılım'))
    kaz_hdr  = [Paragraph('Kazanım', S_TH), Paragraph('İlgili Sorular', S_TH), Paragraph('Max Puan', S_TH)]
    kaz_data = [kaz_hdr] + [
        [Paragraph(k, S_TD), Paragraph(s, S_TDC), Paragraph(str(p), S_TDC)]
        for k, s, p in [
            ('TT.7.3.1.a — Problem tespiti',           '1, 9, 12a',     15),
            ('TT.7.3.1.b — Empati',                    '1, 10, 12a',    20),
            ('TT.7.3.1.c — Fikir üretimi',             '3, 6, 12b',     20),
            ('TT.7.3.1.d–e — Eskiz ve Prototip',       '2, 4, 12c',     20),
            ('TT.7.3.1.f–g — Test, Revize, Sürdürülebilirlik', '5, 7, 8, 11, 12c', 25),
        ]
    ]
    kaz_t = Table(kaz_data, colWidths=[9*cm, 4*cm, 4*cm])
    kaz_t.setStyle(TableStyle(TABLE_BASE))
    e.append(kaz_t)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ARAÇ 7 — Genel Değerlendirme Tablosu
# ═══════════════════════════════════════════════════════════════════════════

def arac7():
    e = []
    e.append(araç_baslik('Araç 7', 'Genel Değerlendirme Tablosu',
                         'TT.7.3.1  •  TT.7.3.2  •  Ünite Sonu'))
    e.append(ogrenci_satiri())
    e.append(HorizontalLine(color=COLOR_PRIMARY, thickness=1.5))
    e.append(sp(6))

    # Ağırlıklı puanlama
    e.append(blm('Ağırlıklı Puanlama'))
    ag_hdr  = [Paragraph('Değerlendirme Aracı', S_TH),
               Paragraph('Ham Puan', S_TH), Paragraph('Ağırlık', S_TH), Paragraph('Ağırlıklı Puan', S_TH)]
    ag_data = [ag_hdr] + [
        [Paragraph(a, S_TD), Paragraph(hp, S_TDC), Paragraph(w, S_TDC), Paragraph('____', S_TDC)]
        for a, hp, w in [
            ('Süreç Gözlem Formu  (A=4, B=3, C=2, D=1 ortalaması)', '____ / 4',   '× 0,20'),
            ('Ürün Rubrikleri  (Eskiz + Prototip ortalaması)',        '____ / 20',  '× 0,25'),
            ('Akran Değerlendirme',                                   '____ / 15',  '× 0,10'),
            ('Öz Değerlendirme  (ÇK11)',                              '____ / 20',  '× 0,10'),
            ('Ünite Sonu Sınavı',                                     '____ / 100', '× 0,20'),
            ('Sunum Rubriği  (ÇK11 + sözlü sunum)',                  '____ / 20',  '× 0,15'),
        ]
    ]
    ag_data.append([Paragraph('<b>TOPLAM</b>', S_SMBD), Paragraph('', S_TDC),
                    Paragraph('<b>%100</b>', S_TDC), Paragraph('<b>____ / 100</b>', S_TDC)])
    ag_t = Table(ag_data, colWidths=[9*cm, 2.5*cm, 2.5*cm, 3*cm])
    ag_t.setStyle(TableStyle([
        *TABLE_BASE,
        ('BACKGROUND',  (0,-1),(-1,-1), COLOR_LIGHT),
        ('LINEABOVE',   (0,-1),(-1,-1), 1, COLOR_PRIMARY),
    ]))
    e.append(ag_t)
    e.append(sp(8))

    # Kazanım karnesi
    e.append(blm('Kazanım Düzeyi Karnesi'))
    kaz_hdr  = [Paragraph('Kazanım', S_TH), Paragraph('Düzey', S_TH)]
    kaz_data = [kaz_hdr] + [
        [Paragraph(k, S_TD), Paragraph('( ) Üstün  ( ) Yeterli  ( ) Gelişiyor  ( ) Destek', S_TD)]
        for k in [
            'TT.7.3.1.a — Problemi gözlem yoluyla tanımlar',
            'TT.7.3.1.b — Kullanıcı perspektifini benimser (empati)',
            'TT.7.3.1.c — Özgün fikirler üretir',
            'TT.7.3.1.d — Tasarım eskizi oluşturur ve planlar',
            'TT.7.3.1.e — Prototip / maket üretir',
            'TT.7.3.1.f — Prototipi test eder, geri bildirim alır',
            'TT.7.3.1.g — Geri bildirimlere göre revize eder',
            'TT.7.3.2 — Tasarım sürecini yapılandırarak sunar',
        ]
    ]
    kaz_t = Table(kaz_data, colWidths=[9*cm, 8*cm])
    kaz_t.setStyle(TableStyle(TABLE_BASE))
    e.append(kaz_t)
    e.append(sp(8))

    # Programlar arası bileşenler
    e.append(blm('Programlar Arası Bileşenler Gözlemi'))
    biles_hdr  = [Paragraph('Bileşen', S_TH), Paragraph('Gelişim Düzeyi', S_TH)]
    biles_data = [biles_hdr] + [
        [Paragraph(b, S_TD), Paragraph('( ) Üstün  ( ) Yeterli  ( ) Gelişiyor', S_TD)]
        for b in [
            'KB2 — Eleştirel ve Yaratıcı Düşünme',
            'OB3 — Problem Çözme',
            'SDB2 — İletişim ve İşbirliği',
            'D7 — Estetik ve Tasarım Duyarlılığı',
            'E3 — Girişimcilik / İnovasyon',
        ]
    ]
    biles_t = Table(biles_data, colWidths=[9*cm, 8*cm])
    biles_t.setStyle(TableStyle(TABLE_BASE))
    e.append(biles_t)
    e.append(sp(8))

    # Öğretmen yorumu
    e.append(blm('Öğretmen Genel Yorumu'))
    e += alan('Öğrencinin güçlü yönleri:', 2)
    e.append(sp(3))
    e += alan('Gelişmesi gereken alanlar:', 2)
    e.append(sp(3))
    e += alan('Bir sonraki üniteye yönelik öneriler:', 2)
    e.append(sp(3))
    e += alan('Veliye paylaşılacak özet not:', 2)
    e.append(sp(8))

    # Zaman çizelgesi
    e.append(blm('Öğretmen İçin Zaman Çizelgesi — Hangi Araç, Ne Zaman?'))
    zc_hdr  = [Paragraph('Ders', S_TH), Paragraph('Sırasında', S_TH), Paragraph('Ders Sonrası', S_TH)]
    zc_data = [zc_hdr] + [
        [Paragraph(d, S_TDC), Paragraph(s, S_TD), Paragraph(p, S_TD)]
        for d, s, p in [
            ('1',  'Süreç Gözlem Formu', '—'),
            ('2',  'Süreç Gözlem Formu', 'ÇK1 inceleme'),
            ('3',  'Süreç Gözlem Formu', 'ÇK2–ÇK3 inceleme'),
            ('4',  'Süreç Gözlem Formu', 'ÇK4–ÇK5 inceleme'),
            ('5',  'Süreç Gözlem Formu', 'Eskiz Rubriği (ÇK6 + ÇK7)'),
            ('6',  'Süreç Gözlem Formu', 'ÇK8 (Ders 6 sayfası) inceleme'),
            ('7',  'Süreç Gözlem Formu', 'Prototip Rubriği (ÇK8 tamamı)'),
            ('8',  'Süreç Gözlem Formu + Akran Değerlendirme', 'ÇK9 inceleme'),
            ('9',  'Süreç Gözlem Formu', 'ÇK10 inceleme'),
            ('10', 'Süreç Gözlem Formu', 'Sunum Rubriği + ÇK11'),
            ('Ünite Sonu', '—', 'Sınav + Genel Değerlendirme Tablosu'),
        ]
    ]
    zc_t = Table(zc_data, colWidths=[2*cm, 6.5*cm, 8.5*cm])
    zc_t.setStyle(TableStyle(TABLE_BASE))
    e.append(zc_t)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  PDF ÜRETİMİ
# ═══════════════════════════════════════════════════════════════════════════

ARACLAR = [
    ('Arac1_Surec_Gozlem_Formu.pdf',     'Arac 1 - Surec Gozlem Formu',   arac1),
    ('Arac2_Eskiz_Rubrigi.pdf',          'Arac 2 - Eskiz Rubrigi',        arac2),
    ('Arac3_Prototip_Rubrigi.pdf',       'Arac 3 - Prototip Rubrigi',     arac3),
    ('Arac4_Sunum_Rubrigi.pdf',          'Arac 4 - Sunum Rubrigi',        arac4),
    ('Arac5_Akran_Degerlendirme.pdf',    'Arac 5 - Akran Degerlendirme',  arac5),
    ('Arac6_Sinav_Ogrenci.pdf',          'Arac 6 - Sinav Ogrenci',        arac6_ogrenci),
    ('Arac6_Sinav_Cevap_Anahtari.pdf',   'Arac 6 - Cevap Anahtari',       arac6_cevap),
    ('Arac7_Genel_Degerlendirme.pdf',    'Arac 7 - Genel Degerlendirme',  arac7),
]

try:
    from pypdf import PdfReader
    def sayfa_sayisi(p): return len(PdfReader(p).pages)
except ImportError:
    def sayfa_sayisi(p): return '?'

print('\n3. Unite - Degerlendirme Araclari PDF Uretimi\n' + '-' * 50)
for fname, title, builder in ARACLAR:
    path = os.path.join(OUT, fname)
    doc  = make_doc(fname, title)
    doc.build(builder(), onFirstPage=add_page_number, onLaterPages=add_page_number)
    n    = sayfa_sayisi(path)
    print(f'  {fname:<48} -> {n} sayfa')
print('-' * 50)
print(f'Tum dosyalar: {OUT}')
