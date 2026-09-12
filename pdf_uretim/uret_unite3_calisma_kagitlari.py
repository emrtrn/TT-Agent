"""
3. Ünite — Öğrenci Çalışma Kâğıtları PDF Üreticisi
ÇK1–ÇK11: her biri ayrı A4 PDF.
Çalıştır: python pdf_uretim/uret_unite3_calisma_kagitlari.py
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
)

from pdf_style import (
    add_page_number,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_TEXT, COLOR_MUTED,
    COLOR_LIGHT_GREY, COLOR_VERY_LIGHT_GREY, COLOR_WRITING_LINE,
    WritingLines, DrawingBox, HorizontalLine,
)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit3')
UNITE_INFO = '3. Ünite: Tasarım Odaklı Süreç  •  Teknoloji ve Tasarım  •  7. Sınıf'
TW = 17 * cm

# ── Stiller ─────────────────────────────────────────────────────────────────
S_CKT  = ParagraphStyle('u3_CKT',  fontName='TR-Bold',    fontSize=12, textColor=COLOR_PRIMARY,   leading=14)
S_KAZ  = ParagraphStyle('u3_KAZ',  fontName='TR-Italic',  fontSize=7.5,textColor=COLOR_MUTED,     alignment=TA_RIGHT, leading=10)
S_BLM  = ParagraphStyle('u3_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=6, spaceAfter=2)
S_LBL  = ParagraphStyle('u3_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11, spaceAfter=1)
S_SML  = ParagraphStyle('u3_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMBD = ParagraphStyle('u3_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMMT = ParagraphStyle('u3_SMMT', fontName='TR-Italic',  fontSize=7.5,textColor=COLOR_MUTED,     leading=10)
S_TH   = ParagraphStyle('u3_TH',   fontName='TR-Bold',    fontSize=7.5,textColor=white,           alignment=TA_CENTER, leading=10)
S_TD   = ParagraphStyle('u3_TD',   fontName='TR-Regular', fontSize=7.5,textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10)
S_TDC  = ParagraphStyle('u3_TDC',  fontName='TR-Regular', fontSize=7.5,textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=10)
S_NUM  = ParagraphStyle('u3_NUM',  fontName='TR-Bold',    fontSize=10, textColor=COLOR_PRIMARY,   alignment=TA_LEFT,   leading=13)
S_YON  = ParagraphStyle('u3_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12)
S_QUAD = ParagraphStyle('u3_QUAD', fontName='TR-Bold',    fontSize=8.5,textColor=white,           alignment=TA_CENTER, leading=11)
S_TMPL = ParagraphStyle('u3_TMPL', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11)
S_CUMLE= ParagraphStyle('u3_CUMLE',fontName='TR-Regular', fontSize=9,  textColor=COLOR_TEXT,      leading=14,
                         backColor=COLOR_VERY_LIGHT, borderPadding=6)

TABLE_BASE = [
    ('BACKGROUND',     (0, 0), (-1, 0),  COLOR_PRIMARY),
    ('LINEBELOW',      (0, 0), (-1, 0),  1, COLOR_SECONDARY),
    ('GRID',           (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
    ('TOPPADDING',     (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING',  (0, 0), (-1, 0),  3),
    ('BOTTOMPADDING',  (0, 1), (-1, -1), 7),
    ('LEFTPADDING',    (0, 0), (-1, -1), 4),
    ('RIGHTPADDING',   (0, 0), (-1, -1), 4),
    ('VALIGN',         (0, 0), (-1, -1), 'TOP'),
]

# ── Yardımcı Bileşenler ──────────────────────────────────────────────────────

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

def ck_baslik(no, ad, kazanim, ders, sure):
    t = Table([[
        Paragraph(f'<b>ÇK{no} — {ad}</b>', S_CKT),
        Paragraph(f'{kazanim}  •  Ders {ders}  •  {sure}', S_KAZ),
    ]], colWidths=[11*cm, 6*cm])
    t.setStyle(TableStyle([
        ('VALIGN',       (0,0),(-1,-1), 'MIDDLE'),
        ('LINEBELOW',    (0,0),(-1,0),  1.5, COLOR_PRIMARY),
        ('TOPPADDING',   (0,0),(-1,-1), 0),
        ('BOTTOMPADDING',(0,0),(-1,-1), 4),
        ('LEFTPADDING',  (0,0),(0,0),   0),
        ('RIGHTPADDING', (-1,0),(-1,0), 0),
    ]))
    return t

def ogrenci_satiri():
    t = Table([[
        Paragraph('<b>Adı Soyadı:</b>', S_LBL), '',
        Paragraph('<b>Sınıf/No:</b>', S_LBL),   '',
        Paragraph('<b>Tarih:</b>', S_LBL),       '',
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

def yon_kutu(metin, sure):
    t = Table([[
        Paragraph(f'<b>Yönerge:</b> {metin}    <b>|    Süre:</b> {sure}', S_YON)
    ]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), COLOR_VERY_LIGHT),
        ('BOX',           (0,0),(-1,-1), 0.5, COLOR_ACCENT),
        ('LEFTPADDING',   (0,0),(-1,-1), 8),
        ('RIGHTPADDING',  (0,0),(-1,-1), 8),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
    ]))
    return t

def bolum(text):
    return Paragraph(text, S_BLM)

def alan(etiket, n=2):
    """Etiket paragrafı + n satırlık yazı alanı; list döndürür."""
    return [Paragraph(etiket, S_LBL), WritingLines(n, 15)]

def kontrol_tablo(maddeler):
    data = [[Paragraph(b, S_TH) for b in
             ['Kontrol Maddesi', 'Tamam', 'Geliştirilmeli', 'Uygulanamaz']]]
    for m in maddeler:
        data.append([
            Paragraph(m, S_TD),
            Paragraph('( )', S_TDC),
            Paragraph('( )', S_TDC),
            Paragraph('( )', S_TDC),
        ])
    t = Table(data, colWidths=[9.5*cm, 2.5*cm, 2.5*cm, 2.5*cm])
    t.setStyle(TableStyle([
        *TABLE_BASE,
        ('BOTTOMPADDING', (0,1),(-1,-1), 4),
    ]))
    return t

def bilgi_kutu(icerik):
    t = Table([[Paragraph(icerik, S_SML)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), COLOR_VERY_LIGHT),
        ('BOX',           (0,0),(-1,-1), 0.5, COLOR_PRIMARY),
        ('LEFTPADDING',   (0,0),(-1,-1), 8),
        ('TOPPADDING',    (0,0),(-1,-1), 6),
        ('BOTTOMPADDING', (0,0),(-1,-1), 6),
    ]))
    return t

def header_blok(no, ad, kazanim, ders, sure, yon_metin, yon_sure):
    return [
        ck_baslik(no, ad, kazanim, ders, sure),
        ogrenci_satiri(),
        HorizontalLine(color=COLOR_PRIMARY, thickness=1.5),
        sp(4),
        yon_kutu(yon_metin, yon_sure),
        sp(5),
    ]


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK1 — Problem Tespiti Formu
# ═══════════════════════════════════════════════════════════════════════════
def ck1():
    e = header_blok(1, 'Problem Tespiti Formu', 'TT.7.3.1', '2', '~15 dk',
        'Günlük hayatında seni rahatsız eden ya da zorlandığını gördüğün gerçek bir sorunu '
        'gözlemle ve bu formu doldur.', '15 dakika')
    e += [bolum('Adım 1 — Problem Gözlemi')]
    e += alan('Problemi ne zaman / nerede fark ettin?', 2)
    e += [sp(3)]
    e += alan('Bu problemi KİM yaşıyor? (kişiyi veya grubu tanımla)', 2)
    e += [sp(3)]
    e += alan('Problem tam olarak NE? (ne oluyor, ne zorlanıyorlar?)', 3)
    e += [sp(3), bolum('Adım 2 — Problemi Bir Cümleyle Tanımla'),
          Paragraph('[Kişi/grup] , [durum/bağlam] içindeyken [sorun] yaşıyor çünkü [neden].', S_TMPL)]
    e += alan('Cevabını yaz:', 3)
    e += [sp(3), bolum('Adım 3 — Problemi Değerlendir')]
    chk_data = [
        [Paragraph(b, S_TH) for b in ['Soru', 'Evet', 'Hayır', 'Emin Değilim']],
        [Paragraph('Bu problemi gerçek bir kişi yaşıyor mu?',      S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Problem gözlemlenebilir mi?',                   S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Bir ürün veya araç bu problemi çözebilir mi?',  S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Yaşım ve imkânlarımla çözüm üretebilir miyim?', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
    ]
    chk_t = Table(chk_data, colWidths=[9.5*cm, 2.5*cm, 2.5*cm, 2.5*cm])
    chk_t.setStyle(TableStyle([*TABLE_BASE, ('BOTTOMPADDING',(0,1),(-1,-1), 8)]))
    e += [chk_t, sp(4), bolum('Adım 4 — Önem Ölçeği'),
          Paragraph('Bu problem kaç kişiyi etkiliyor?', S_LBL)]
    olcek = Table([[
        Paragraph('Sadece bir kişi\n( ) 1', S_TDC),
        Paragraph('Az kişi\n( ) 2', S_TDC),
        Paragraph('Birçok kişi\n( ) 3', S_TDC),
        Paragraph('Çok fazla kişi\n( ) 4', S_TDC),
    ]], colWidths=[4.25*cm]*4)
    olcek.setStyle(TableStyle([
        ('GRID',           (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('ALIGN',          (0,0),(-1,-1), 'CENTER'),
        ('VALIGN',         (0,0),(-1,-1), 'MIDDLE'),
        ('TOPPADDING',     (0,0),(-1,-1), 6),
        ('BOTTOMPADDING',  (0,0),(-1,-1), 6),
        ('ROWBACKGROUNDS', (0,0),(-1,-1), [COLOR_VERY_LIGHT_GREY]),
    ]))
    e += [olcek, sp(4), bolum('Yansıtma')]
    e += alan('Bu problemle çalışmak istememin nedeni:', 2)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK2 — Empati Haritası
# ═══════════════════════════════════════════════════════════════════════════
def ck2():
    e = header_blok(2, 'Empati Haritası', 'TT.7.3.1', '3', '~15 dk',
        'Problemini yaşayan kişiyi gözlemle ya da hayal et. Onun yerine geç; '
        'ne düşündüğünü, hissettiğini, söylediğini ve yaptığını yaz.', '15 dakika')
    e += [bolum('Kullanıcı Profili')]
    profil = Table([[
        Paragraph('<b>Adı / Takma Adı:</b>', S_SML), '',
        Paragraph('<b>Yaşı:</b>', S_SML), '',
        Paragraph('<b>Rolü / Mesleği:</b>', S_SML), '',
    ]], colWidths=[3.2*cm, 3*cm, 1.4*cm, 1.8*cm, 3*cm, 4.6*cm])
    profil.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (5,0),(5,0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0,0),(-1,-1), 1),
        ('BOTTOMPADDING', (0,0),(-1,-1), 1),
        ('LEFTPADDING',   (0,0),(-1,-1), 2),
        ('RIGHTPADDING',  (0,0),(-1,-1), 2),
    ]))
    e += [profil, sp(5)]
    quad = Table([
        [Paragraph('DÜŞÜNÜYOR', S_QUAD),
         Paragraph('HİSSEDİYOR', S_QUAD)],
        [Paragraph('(Kafasında neler dönüyor? Endişeleri neler?)', S_SMMT),
         Paragraph('(Hangi duygu? Mutlu mu, hayal kırıklığı mı?)', S_SMMT)],
        [Paragraph('SÖYLÜYOR', S_QUAD),
         Paragraph('YAPIYOR', S_QUAD)],
        [Paragraph('(Başkalarına ne söylüyor? Şikâyetleri?)', S_SMMT),
         Paragraph('(Bu problem için günlük hayatta ne yapıyor?)', S_SMMT)],
    ], colWidths=[8.4*cm, 8.4*cm],
       rowHeights=[0.65*cm, 5.2*cm, 0.65*cm, 5.2*cm])
    quad.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0),  COLOR_PRIMARY),
        ('BACKGROUND',    (0,2),(-1,2),  COLOR_PRIMARY),
        ('TEXTCOLOR',     (0,0),(-1,0),  white),
        ('TEXTCOLOR',     (0,2),(-1,2),  white),
        ('BACKGROUND',    (0,1),(-1,1),  white),
        ('BACKGROUND',    (0,3),(-1,3),  white),
        ('BOX',           (0,0),(-1,-1), 1, COLOR_PRIMARY),
        ('GRID',          (0,0),(-1,-1), 0.5, COLOR_LIGHT_GREY),
        ('ALIGN',         (0,0),(-1,0),  'CENTER'),
        ('ALIGN',         (0,2),(-1,2),  'CENTER'),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ('ALIGN',         (0,1),(-1,3),  'LEFT'),
        ('TOPPADDING',    (0,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,0),(-1,-1), 3),
        ('LEFTPADDING',   (0,0),(-1,-1), 5),
        ('RIGHTPADDING',  (0,0),(-1,-1), 5),
    ]))
    e += [quad, sp(4), bolum('Temel Bulgular')]
    e += alan('En büyük acı noktası (pain point):', 1)
    e += [sp(2)]
    e += alan('En çok ihtiyaç duyduğu şey:', 1)
    e += [sp(2)]
    e += alan('Tasarımımın ona sağlaması gereken fayda:', 1)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK3 — Kullanıcı Analiz Tablosu
# ═══════════════════════════════════════════════════════════════════════════
def ck3():
    e = header_blok(3, 'Kullanıcı Analiz Tablosu', 'TT.7.3.1', '3', '~10 dk',
        'ÇK2\'deki empati haritanı kullanarak kullanıcını daha derinlemesine analiz et.',
        '10 dakika')
    e += [bolum('Kullanıcı Özeti')]
    ozet = Table([
        [Paragraph('<b>Kategori</b>', S_TH), Paragraph('<b>Bilgi</b>', S_TH)],
        [Paragraph('Kullanıcı kim?', S_TD), ''],
        [Paragraph('Yaşı / Grubu', S_TD), ''],
        [Paragraph('Problemi nerede yaşıyor?', S_TD), ''],
        [Paragraph('Problemi ne zaman yaşıyor?', S_TD), ''],
        [Paragraph('Şu an nasıl çözüyor? (varsa)', S_TD), ''],
        [Paragraph('Mevcut çözümün eksikleri', S_TD), ''],
    ], colWidths=[5*cm, 12*cm])
    ozet.setStyle(TableStyle([*TABLE_BASE, ('BOTTOMPADDING',(0,1),(-1,-1), 18)]))
    e += [ozet, sp(4), bolum('İhtiyaç Analizi')]
    e += alan('Kullanıcının gerçek ihtiyacı (bunu yapmak istiyor, bunu başarmak istiyor...):', 2)
    e += [sp(3)]
    e += alan('Kısıtlar (para, zaman, fiziksel sınırlamalar...):', 2)
    e += [sp(3)]
    e += alan('İdeal çözüm nasıl olmalı? (kullanıcının gözünden):', 2)
    e += [sp(4), bolum('Tasarım Kriterleri'),
          Paragraph('Tasarımımın sağlaması gereken en önemli 3 özellik:', S_LBL)]
    krit = Table([
        [Paragraph('<b>#</b>', S_TH), Paragraph('<b>Kriter</b>', S_TH)],
        [Paragraph('1', S_TDC), ''],
        [Paragraph('2', S_TDC), ''],
        [Paragraph('3', S_TDC), ''],
    ], colWidths=[1*cm, 16*cm])
    krit.setStyle(TableStyle([
        *TABLE_BASE,
        ('ALIGN',         (0,0),(0,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,1),(-1,-1), 15),
    ]))
    e += [krit, sp(4), bolum('Yansıtma')]
    e += alan('Kullanıcımı anlamak için daha ne yapabilirdim?', 2)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK4 — Crazy 8 Beyin Fırtınası
# ═══════════════════════════════════════════════════════════════════════════
def ck4():
    e = header_blok(4, 'Crazy 8 Beyin Fırtınası', 'TT.7.3.2', '4', '~10 dk',
        'Her kutuya farklı bir fikir çiz veya yaz. 8 dakikan var — her fikre sadece '
        '1 dakika! Eleştirme, mükemmel olmak zorunda değil.', '8 dk + 2 dk seçim')
    crazy8 = Table([
        [Paragraph('<b>1</b>', S_NUM), Paragraph('<b>2</b>', S_NUM)],
        [Paragraph('<b>3</b>', S_NUM), Paragraph('<b>4</b>', S_NUM)],
        [Paragraph('<b>5</b>', S_NUM), Paragraph('<b>6</b>', S_NUM)],
        [Paragraph('<b>7</b>', S_NUM), Paragraph('<b>8</b>', S_NUM)],
    ], colWidths=[8.4*cm, 8.4*cm], rowHeights=[4.7*cm]*4)
    crazy8.setStyle(TableStyle([
        ('GRID',          (0,0),(-1,-1), 1,   COLOR_LIGHT_GREY),
        ('BOX',           (0,0),(-1,-1), 1.2, COLOR_PRIMARY),
        ('BACKGROUND',    (0,0),(-1,-1), white),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ('ALIGN',         (0,0),(-1,-1), 'LEFT'),
        ('TOPPADDING',    (0,0),(-1,-1), 4),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(-1,-1), 5),
        ('RIGHTPADDING',  (0,0),(-1,-1), 5),
    ]))
    e += [crazy8, sp(5),
          bilgi_kutu('En beğendiğim 2 fikir:  No: ____  ve  No: ____'
                     '     Neden bu ikisini seçtim: ______________________________')]
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK5 — Fikir Seçim Matrisi
# ═══════════════════════════════════════════════════════════════════════════
def ck5():
    e = header_blok(5, 'Fikir Seçim Matrisi', 'TT.7.3.2', '4', '~10 dk',
        'Crazy 8\'den seçtiğin en iyi fikirleri buraya yaz. '
        'Her fikri kriterlere göre 1–3 puan ver.',
        '10 dakika')
    e += [Paragraph('<b>Puanlama:</b>  1 = Zayıf    2 = Orta    3 = İyi', S_SML), sp(4)]
    matris = Table([
        [Paragraph('<b>Kriter</b>', S_TH), Paragraph('<b>Ağır.</b>', S_TH),
         Paragraph('<b>Fikir A</b>', S_TH), Paragraph('<b>Fikir B</b>', S_TH),
         Paragraph('<b>Fikir C</b>', S_TH)],
        [Paragraph('Fikir / Tasarım Adı', S_TD), Paragraph('—', S_TDC),
         Paragraph('__________', S_TDC), Paragraph('__________', S_TDC),
         Paragraph('__________', S_TDC)],
        [Paragraph('Kullanıcı ihtiyacını karşılıyor mu?', S_TD),
         Paragraph('× 3', S_TDC), '', '', ''],
        [Paragraph('Yapılabilir mi? (malzeme, süre)', S_TD),
         Paragraph('× 2', S_TDC), '', '', ''],
        [Paragraph('Özgün / yaratıcı mı?', S_TD),
         Paragraph('× 2', S_TDC), '', '', ''],
        [Paragraph('Ergonomik olabilir mi?', S_TD),
         Paragraph('× 1', S_TDC), '', '', ''],
        [Paragraph('Sürdürülebilir malzeme kullanılabilir mi?', S_TD),
         Paragraph('× 1', S_TDC), '', '', ''],
        [Paragraph('<b>TOPLAM (maks. 27)</b>', S_SMBD),
         Paragraph('—', S_TDC),
         Paragraph('___', S_TDC), Paragraph('___', S_TDC), Paragraph('___', S_TDC)],
    ], colWidths=[7*cm, 1.5*cm, 2.83*cm, 2.83*cm, 2.84*cm])
    matris.setStyle(TableStyle([
        *TABLE_BASE,
        ('BOTTOMPADDING', (0,1),(-1,-1), 20),
        ('BACKGROUND',    (0,7),(-1,7),  COLOR_VERY_LIGHT_GREY),
        ('FONTNAME',      (0,7),(-1,7),  'TR-Bold'),
        ('ALIGN',         (1,0),(-1,-1), 'CENTER'),
    ]))
    e += [matris, sp(6),
          bilgi_kutu('Kazanan fikir: _______________________________________')]
    e += [sp(4), bolum('Seçim Gerekçesi')]
    e += alan('Neden bu fikri seçtim:', 3)
    e += [sp(3)]
    e += alan('Bu fikri geliştirmek için düşündüğüm değişiklikler:', 2)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK6 — Tasarım Eskizi Sayfası
# ═══════════════════════════════════════════════════════════════════════════
def ck6():
    e = header_blok(6, 'Tasarım Eskizi Sayfası', 'TT.7.3.2', '5', '~15 dk',
        'Seçtiğin fikri çiz. Mükemmel olmak zorunda değilsin — fikri aktarması yeterli. '
        'Boyutları ve malzeme notlarını da ekle.', '15 dakika')
    isim = Table([[
        Paragraph('<b>Tasarım Adı:</b>', S_LBL), '',
        Paragraph('<b>Versiyon:</b>', S_LBL), '',
    ]], colWidths=[3*cm, 10.5*cm, 2*cm, 1.5*cm])
    isim.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 2),
        ('LEFTPADDING',   (0,0),(-1,-1), 2),
    ]))
    e += [isim, sp(4), bolum('Ana Eskiz  (Ön Görünüş)'),
          DrawingBox(height=9*cm, caption='Ön görünüşü buraya çiz')]
    e += [sp(4), bolum('Detay Görünüşler')]
    detail = Table([[
        DrawingBox(width=8.2*cm, height=5*cm, caption='Yan görünüş'),
        DrawingBox(width=8.2*cm, height=5*cm, caption='Üst görünüş'),
    ]], colWidths=[8.5*cm, 8.5*cm])
    detail.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ('TOPPADDING',    (0,0),(-1,-1), 0),
        ('BOTTOMPADDING', (0,0),(-1,-1), 0),
        ('LEFTPADDING',   (0,0),(-1,-1), 0),
        ('RIGHTPADDING',  (0,0),(-1,-1), 4),
    ]))
    e += [detail, sp(4), bolum('Ölçüler ve Malzeme Notları'),
          Paragraph('<b>Tahmini boyutlar:</b>  En: _____ cm   Boy: _____ cm   Yükseklik: _____ cm',
                    S_SML)]
    e += alan('Kullanmayı düşündüğüm malzemeler:', 1)
    e += [sp(2)]
    e += alan('Özel dikkat edilmesi gereken detay:', 1)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK7 — Malzeme Planlama Tablosu
# ═══════════════════════════════════════════════════════════════════════════
def ck7():
    e = header_blok(7, 'Malzeme Planlama Tablosu', 'TT.7.3.2', '5', '~10 dk',
        'Prototipini yapmak için ihtiyaç duyduğun malzemeleri listele. '
        'Her malzemeyi gerçekçi şekilde değerlendir.', '10 dakika')
    e += [bolum('Malzeme Listesi')]
    m_data = [[
        Paragraph('<b>#</b>', S_TH),
        Paragraph('<b>Malzeme</b>', S_TH),
        Paragraph('<b>Miktar</b>', S_TH),
        Paragraph('<b>Boyut / Özellik</b>', S_TH),
        Paragraph('<b>Nereden Temin?</b>', S_TH),
        Paragraph('<b>Maliyet</b>', S_TH),
    ]]
    for i in range(1, 9):
        m_data.append([Paragraph(str(i), S_TDC), '', '', '', '', ''])
    malzeme = Table(m_data, colWidths=[0.8*cm, 4.8*cm, 1.8*cm, 3.5*cm, 3.7*cm, 2.4*cm])
    malzeme.setStyle(TableStyle([
        *TABLE_BASE,
        ('ALIGN',         (0,0),(0,-1), 'CENTER'),
        ('ALIGN',         (2,0),(2,-1), 'CENTER'),
        ('ALIGN',         (5,0),(5,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,1),(-1,-1), 12),
    ]))
    e += [malzeme, bilgi_kutu('Tahmini toplam maliyet: _____________ TL'), sp(4)]
    e += [bolum('Araçlar ve Ekipmanlar')]
    e += alan('Kullanmam gereken araçlar:', 1)
    e += [sp(3), bolum('Sürdürülebilirlik Notu')]
    surd = Table([
        [Paragraph('<b>Konu</b>', S_TH), Paragraph('<b>Yanıt</b>', S_TH)],
        [Paragraph('Geri dönüştürülmüş / atık malzeme kullandım mı?', S_TD),
         Paragraph('( ) Evet — ________________   ( ) Hayır', S_TD)],
        [Paragraph('Doğal / çevre dostu malzeme var mı?', S_TD),
         Paragraph('( ) Evet — ________________   ( ) Hayır', S_TD)],
        [Paragraph('Malzeme fazlası oluşursa ne yapacağım?', S_TD), ''],
    ], colWidths=[8*cm, 9*cm])
    surd.setStyle(TableStyle([*TABLE_BASE, ('BOTTOMPADDING',(0,1),(-1,-1), 12)]))
    e += [surd, sp(4), bolum('Yansıtma')]
    e += alan('Bu malzemelerle gerçekten yapabilir miyim? Aklımdaki en büyük zorluk:', 1)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK8 — Prototip Süreç Günlüğü  (2 sayfa)
# ═══════════════════════════════════════════════════════════════════════════
def ck8():
    e = header_blok(8, 'Prototip Süreç Günlüğü', 'TT.7.3.2', '6–7', '~20 dk × 2',
        'Her ders saatinin sonunda bu günlüğü doldur. '
        'Yanlış giden şeyler de tasarım sürecinin parçasıdır — dürüst yaz!',
        '5–8 dakika / ders')
    e += [bilgi_kutu('DERS 6 — İlk Üretim Günü'), sp(4),
          Paragraph('<b>Tarih:</b> ___________', S_LBL), sp(3)]
    e += alan('Bugün ne yaptım?', 3)
    e += [sp(3)]
    e += alan('Hangi adımı tamamladım?', 1)
    e += [sp(3)]
    e += alan('Karşılaştığım zorluk:', 2)
    e += [sp(3)]
    e += alan('Bu zorluğu nasıl çözdüm / çözmeye çalıştım?', 2)
    e += [sp(5), bolum('Bugünün Eskizi'),
          DrawingBox(height=5.5*cm, caption='Bugün ne görünüyordu?'), sp(3)]
    e += alan('Yarın devam edeceklerim:', 2)
    # Sayfa 2
    e += [PageBreak(),
          ck_baslik(8, 'Prototip Süreç Günlüğü — Ders 7', 'TT.7.3.2', '7', '~20 dk'),
          ogrenci_satiri(),
          HorizontalLine(color=COLOR_PRIMARY, thickness=1.5),
          sp(6),
          bilgi_kutu('DERS 7 — Tamamlama Günü'), sp(4),
          Paragraph('<b>Tarih:</b> ___________', S_LBL), sp(3)]
    e += alan('Bugün ne yaptım?', 3)
    e += [sp(3)]
    e += alan('Planlamadığım ama yaptığım değişiklik:', 2)
    e += [sp(3)]
    e += alan('Prototipim şu an nasıl görünüyor? (kısaca tanımla):', 2)
    e += [sp(4), bolum('Değerlendirme')]
    dg = Table([
        [Paragraph('<b>Konu</b>', S_TH), Paragraph('<b>Yanıt</b>', S_TH)],
        [Paragraph('Memnun olduğum kısım', S_TD), ''],
        [Paragraph('Hâlâ eksik olan kısım', S_TD), ''],
    ], colWidths=[5*cm, 12*cm])
    dg.setStyle(TableStyle([*TABLE_BASE, ('BOTTOMPADDING',(0,1),(-1,-1), 18)]))
    e += [dg, sp(5),
          bilgi_kutu('Teste hazır mıyım?  ( ) Evet — tam hazır    '
                     '( ) Evet — bazı eksiklerle    ( ) Hayır — neden: ___________________')]
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK9 — Ürün Test ve Geri Bildirim Formu
# ═══════════════════════════════════════════════════════════════════════════
def ck9():
    e = header_blok(9, 'Ürün Test ve Geri Bildirim Formu', 'TT.7.3.2', '8', '~15 dk',
        'Prototipini bir kullanıcıya dene. Test ederken gözlem yap; '
        'bittikten sonra geri bildirim al.', '15 dakika')
    e += [bolum('Test Bilgileri')]
    tb = Table([[
        Paragraph('<b>Test eden kişi:</b>', S_LBL), '',
        Paragraph('<b>İlişkisi:</b>', S_LBL), '',
    ]], colWidths=[3.5*cm, 5*cm, 2.5*cm, 6*cm])
    tb.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
        ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
        ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 2),
        ('LEFTPADDING',   (0,0),(-1,-1), 2),
    ]))
    e += [tb, sp(3), bolum('Gözlem Notları  (test sırasında al)')]
    e += alan('Test ederken kullanıcı şunları yaptı:', 2)
    e += [sp(3)]
    e += alan('Kullanıcının zorlandığı nokta:', 2)
    e += [sp(3)]
    e += alan('Kullanıcının kolayca yaptığı şey:', 1)
    e += [sp(4), bolum('Geri Bildirim Soruları  (test sonrası sor)')]
    r_data = [
        [Paragraph('<b>Soru</b>', S_TH),
         Paragraph('1\nZayıf', S_TH), Paragraph('2', S_TH), Paragraph('3', S_TH),
         Paragraph('4', S_TH), Paragraph('5\nMükemmel', S_TH)],
        [Paragraph('Ürünü kullanmak ne kadar kolaydı?', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Ürün problemi ne kadar çözüyor?', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Tasarım ne kadar güvenli hissettiriyor?', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Ürün ne kadar dayanıklı görünüyor?', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
        [Paragraph('Genel memnuniyet', S_TD),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC), Paragraph('( )', S_TDC),
         Paragraph('( )', S_TDC), Paragraph('( )', S_TDC)],
    ]
    rating = Table(r_data, colWidths=[8.5*cm, 1.7*cm, 1.7*cm, 1.7*cm, 1.7*cm, 1.7*cm])
    rating.setStyle(TableStyle([
        *TABLE_BASE,
        ('ALIGN',         (1,0),(-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,1),(-1,-1), 8),
    ]))
    e += [rating, sp(4), bolum('Açık Sorular')]
    e += alan('"Bu ürünü gerçekten kullanır mıydın? Neden?"', 2)
    e += [sp(3)]
    e += alan('"Değişmesini istediğin bir şey ne olurdu?"', 2)
    e += [sp(3), bolum('Test Sonucu')]
    e += alan('En önemli iyileştirme önerisi:', 1)
    e += [sp(2)]
    e += alan('Benim kendi gözlemim — değiştirmem gereken şey:', 1)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK10 — Revize Planı + Sürdürülebilirlik Kontrolü
# ═══════════════════════════════════════════════════════════════════════════
def ck10():
    e = header_blok(10, 'Revize Planı + Sürdürülebilirlik Kontrolü', 'TT.7.3.2', '9', '~15 dk',
        'ÇK9\'daki geri bildirimleri kullanarak ürününü iyileştir. '
        'Sürdürülebilirlik ve ergonomi kontrolünü de unutma.', '15 dakika')
    e += [bolum('Revize Listesi')]
    rv = Table([
        [Paragraph('<b>#</b>', S_TH),
         Paragraph('<b>Değiştirilecek Kısım</b>', S_TH),
         Paragraph('<b>Neden? (geri bildirim kaynağı)</b>', S_TH),
         Paragraph('<b>Yapıldı</b>', S_TH)],
        *[[Paragraph(str(i), S_TDC), '', '', Paragraph('( )', S_TDC)] for i in range(1, 6)],
    ], colWidths=[0.8*cm, 6.5*cm, 7.5*cm, 2.2*cm])
    rv.setStyle(TableStyle([
        *TABLE_BASE,
        ('ALIGN',         (0,0),(0,-1),  'CENTER'),
        ('ALIGN',         (-1,0),(-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,1),(-1,-1), 14),
    ]))
    e += [rv, sp(4), bolum('Revize Karşılaştırması')]
    karsil = Table([
        [Paragraph('<b>Önceki hali nasıldı?</b>', S_SMBD),
         Paragraph('<b>Şimdi nasıl?</b>', S_SMBD)],
        [WritingLines(2, 14), WritingLines(2, 14)],
    ], colWidths=[8.4*cm, 8.4*cm])
    karsil.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0),  COLOR_VERY_LIGHT_GREY),
        ('GRID',          (0,0),(-1,-1), 0.3, COLOR_LIGHT_GREY),
        ('TOPPADDING',    (0,0),(-1,-1), 4),
        ('BOTTOMPADDING', (0,0),(-1,-1), 4),
        ('LEFTPADDING',   (0,0),(-1,-1), 5),
        ('RIGHTPADDING',  (0,0),(-1,-1), 5),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
    ]))
    e += [karsil, sp(5), bolum('Ergonomi Kontrol Listesi'),
          kontrol_tablo([
              'Ürün tutulması / kullanılması kolay',
              'Keskin / tehlikeli kenar yok',
              'Ağırlık ve boyut kullanıcıya uygun',
              'Hareketli parçalar güvenli',
              'Uzun süre kullanımda rahat',
          ]),
          sp(5), bolum('Sürdürülebilirlik Kontrol Listesi'),
          kontrol_tablo([
              'Gereksiz malzeme kullanımından kaçınıldı',
              'En az bir geri dönüştürülmüş / atık malzeme kullanıldı',
              'Ürün onarılabilir ya da parçalanabilir',
              'Uzun ömürlü olacak şekilde tasarlandı',
              'Doğaya zarar vermeyen malzeme seçildi',
          ]),
          sp(4), bolum('Yansıtma')]
    e += alan('Bu revizeden sonra ürünüm nasıl değişti?', 1)
    e += [sp(2)]
    e += alan('Tasarım döngüsü sona mı erdi? Bir sonraki adımda ne yapardın?', 1)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÇK11 — Tasarım Süreci Sunum Şablonu
# ═══════════════════════════════════════════════════════════════════════════
def ck11():
    e = header_blok(11, 'Tasarım Süreci Sunum Şablonu', '—', '10', '~15 dk',
        'Tasarım sürecini bu şablona özetle. Sunum sırasında bu kâğıdı rehber olarak kullan.',
        '15 dakika hazırlık')
    e += [Paragraph(
        'Benim tasarımım  <b>_________________________</b>  için   '
        '<b>_________________________</b>  yapar,   '
        'çünkü  <b>_________________________</b>.', S_CUMLE)]
    e += [sp(5), bolum('7 Adım Özeti')]
    ozet = Table([
        [Paragraph('<b>Adım</b>', S_TH),
         Paragraph('<b>Yaptığım</b>', S_TH),
         Paragraph('<b>En Önemli Bulgum</b>', S_TH)],
        *[[Paragraph(a, S_TD), '', ''] for a in [
            '1 — Problem Tespiti', '2 — Analiz / Empati', '3 — Fikir Üretimi',
            '4 — Eskiz / Taslak', '5 — Uygulama', '6 — Test', '7 — Revize',
        ]],
    ], colWidths=[4.5*cm, 6.25*cm, 6.25*cm])
    ozet.setStyle(TableStyle([*TABLE_BASE, ('BOTTOMPADDING',(0,1),(-1,-1), 10)]))
    e += [ozet, sp(4), bolum('Ürünümü Tanıtıyorum')]
    urun = Table([
        [Paragraph('<b>Alan</b>', S_TH), Paragraph('<b>Bilgi</b>', S_TH)],
        *[[Paragraph(a, S_TD), ''] for a in [
            'Ürünümün adı', 'Hangi problemi çözüyor?', 'Kullanıcım kim?',
            'En özgün yanı', 'Sürdürülebilirlik özelliği',
        ]],
    ], colWidths=[5*cm, 12*cm])
    urun.setStyle(TableStyle([*TABLE_BASE, ('BOTTOMPADDING',(0,1),(-1,-1), 10)]))
    e += [urun, sp(4), bolum('Öz Değerlendirme')]
    oz = Table([
        [Paragraph('<b>Konu</b>', S_TH),
         Paragraph('<b>1</b>', S_TH), Paragraph('<b>2</b>', S_TH),
         Paragraph('<b>3</b>', S_TH), Paragraph('<b>4</b>', S_TH),
         Paragraph('<b>5</b>', S_TH)],
        *[[Paragraph(k, S_TD),
           Paragraph('( )', S_TDC), Paragraph('( )', S_TDC),
           Paragraph('( )', S_TDC), Paragraph('( )', S_TDC),
           Paragraph('( )', S_TDC)] for k in [
            'Tasarımım problemi çözüyor',
            'Tüm adımları uyguladım',
            'Kullanıcı geri bildirimini dikkate aldım',
            'Özgün ve yaratıcı bir çözüm ürettim',
        ]],
    ], colWidths=[9.2*cm, *[1.56*cm]*5])
    oz.setStyle(TableStyle([
        *TABLE_BASE,
        ('ALIGN',         (1,0),(-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,1),(-1,-1), 6),
    ]))
    e += [oz, sp(4)]
    e += alan('Bu ünitede en çok öğrendiğim şey:', 2)
    return e


# ═══════════════════════════════════════════════════════════════════════════
#  ÜRET
# ═══════════════════════════════════════════════════════════════════════════
CK_LIST = [
    ('CK1_Problem_Tespiti_Formu.pdf',           'ÇK1 — Problem Tespiti Formu',              ck1),
    ('CK2_Empati_Haritasi.pdf',                  'ÇK2 — Empati Haritası',                    ck2),
    ('CK3_Kullanici_Analiz_Tablosu.pdf',         'ÇK3 — Kullanıcı Analiz Tablosu',           ck3),
    ('CK4_Crazy8_Beyin_Firtinasi.pdf',           'ÇK4 — Crazy 8 Beyin Fırtınası',            ck4),
    ('CK5_Fikir_Secim_Matrisi.pdf',              'ÇK5 — Fikir Seçim Matrisi',                ck5),
    ('CK6_Tasarim_Eskizi_Sayfasi.pdf',           'ÇK6 — Tasarım Eskizi Sayfası',             ck6),
    ('CK7_Malzeme_Planlama_Tablosu.pdf',         'ÇK7 — Malzeme Planlama Tablosu',           ck7),
    ('CK8_Prototip_Surec_Gunlugu.pdf',           'ÇK8 — Prototip Süreç Günlüğü',             ck8),
    ('CK9_Urun_Test_Geri_Bildirim.pdf',          'ÇK9 — Ürün Test ve Geri Bildirim Formu',   ck9),
    ('CK10_Revize_Plani_Surdurulebilirlik.pdf',  'ÇK10 — Revize Planı + Sürdürülebilirlik',  ck10),
    ('CK11_Sunum_Sablonu.pdf',                   'ÇK11 — Tasarım Süreci Sunum Şablonu',      ck11),
]

try:
    from pypdf import PdfReader
    def sayfa_sayisi(p): return len(PdfReader(p).pages)
except ImportError:
    def sayfa_sayisi(p): return '?'

print('\n3. Unite - Calisma Kagitlari PDF Uretimi\n' + '-' * 46)
for fname, title, builder in CK_LIST:
    path = os.path.join(OUT, fname)
    doc = make_doc(fname, title)
    doc.build(builder(), onFirstPage=add_page_number, onLaterPages=add_page_number)
    n = sayfa_sayisi(path)
    title_safe = title.encode('ascii', 'replace').decode('ascii')
    print(f'  {title_safe:<52} -> {n} sayfa')
print('-' * 46)
print(f'Tum dosyalar: {OUT}')
