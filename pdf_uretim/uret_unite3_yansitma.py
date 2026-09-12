"""
3. Unite -- Ogretmen Yansitma ve Kapanis PDF Ureticisi
5 ayri PDF uretir (units/7_sinif/unit3/ klasorune kaydeder).

Calistir: python pdf_uretim/uret_unite3_yansitma.py
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
    WritingLines, HorizontalLine,
)

register_fonts()

OUT        = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units', 'unit3')
UNITE_INFO = '3. Ünite: Tasarım Odaklı Süreç  •  Teknoloji ve Tasarım  •  7. Sınıf'
TW         = 17 * cm

# ── Stiller ─────────────────────────────────────────────────────────────────

S_BAS  = ParagraphStyle('u3y_BAS',  fontName='TR-Bold',    fontSize=13, textColor=COLOR_PRIMARY,   leading=16)
S_ALT  = ParagraphStyle('u3y_ALT',  fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     alignment=TA_RIGHT, leading=10)
S_BLM  = ParagraphStyle('u3y_BLM',  fontName='TR-Bold',    fontSize=9,  textColor=COLOR_SECONDARY, leading=12, spaceBefore=6, spaceAfter=2)
S_LBL  = ParagraphStyle('u3y_LBL',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=11, spaceAfter=1)
S_SML  = ParagraphStyle('u3y_SML',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SML7 = ParagraphStyle('u3y_SML7', fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      leading=9.5)
S_SMBD = ParagraphStyle('u3y_SMBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      leading=11)
S_SMIT = ParagraphStyle('u3y_SMIT', fontName='TR-Italic',  fontSize=8,  textColor=COLOR_MUTED,     leading=11)
S_TH   = ParagraphStyle('u3y_TH',   fontName='TR-Bold',    fontSize=7.5,textColor=white,           alignment=TA_CENTER, leading=10)
S_TH7  = ParagraphStyle('u3y_TH7',  fontName='TR-Bold',    fontSize=7,  textColor=white,           alignment=TA_CENTER, leading=9.5)
S_TD   = ParagraphStyle('u3y_TD',   fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10.5)
S_TD7  = ParagraphStyle('u3y_TD7',  fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=9.5)
S_TDC  = ParagraphStyle('u3y_TDC',  fontName='TR-Regular', fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=10.5)
S_TDC7 = ParagraphStyle('u3y_TDC7', fontName='TR-Regular', fontSize=7,  textColor=COLOR_TEXT,      alignment=TA_CENTER, leading=9.5)
S_TDBD = ParagraphStyle('u3y_TDBD', fontName='TR-Bold',    fontSize=8,  textColor=COLOR_TEXT,      alignment=TA_LEFT,   leading=10.5)
S_YON  = ParagraphStyle('u3y_YON',  fontName='TR-Regular', fontSize=8.5,textColor=COLOR_TEXT,      leading=12)
S_KAP  = ParagraphStyle('u3y_KAP',  fontName='TR-Italic',  fontSize=8.5,textColor=COLOR_TEXT,      leading=13, spaceAfter=2)

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

def araç_baslik(no_str, ad, alt=''):
    t = Table([[
        Paragraph(f'<b>{no_str} — {ad}</b>', S_BAS),
        Paragraph(alt, S_ALT),
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

def ogretmen_satiri():
    t = Table([[
        Paragraph('<b>Öğretmen:</b>', S_LBL), '',
        Paragraph('<b>Okul:</b>',     S_LBL), '',
    ]], colWidths=[2.5*cm, 6.5*cm, 1.8*cm, 6.2*cm])
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

def ogrenci_satiri():
    t = Table([[
        Paragraph('<b>Ad-Soyad (İsteğe bağlı):</b>', S_LBL), '',
        Paragraph('<b>Tarih:</b>',                    S_LBL), '',
    ]], colWidths=[5*cm, 7.5*cm, 1.5*cm, 3*cm])
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

def secim_satiri(soru, seçenekler):
    secim_str = '     '.join(f'( ) {s}' for s in seçenekler)
    return [
        Paragraph(f'<b>{soru}</b>', S_LBL),
        sp(2),
        Paragraph(secim_str, S_SML),
        sp(6),
    ]

def yazma_alani(etiket, n=2):
    return [Paragraph(f'<b>{etiket}</b>', S_LBL), WritingLines(n, 15), sp(4)]

def ders_blogu(no, baslik, plan_evet=True, sorular=None, notlar=None):
    """Her ders için yansıtma bloğu."""
    items = [
        KeepTogether([
            blm(f'{no}. Ders — "{baslik}"'),
            sp(3),
            Table([[
                Paragraph('<b>Planlanan süreye uygun geçti mi?</b>', S_LBL),
                Paragraph('( ) Evet  ( ) Hayır', S_SML),
            ]], colWidths=[8*cm, 9*cm],
            style=TableStyle([
                ('TOPPADDING',    (0,0),(-1,-1), 2),
                ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING',   (0,0),(-1,-1), 0),
                ('RIGHTPADDING',  (0,0),(-1,-1), 0),
                ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
            ])),
            sp(3),
            Table([[
                Paragraph('<b>Planlanan:</b>', S_LBL), Paragraph('_____ dk', S_SML),
                Paragraph('<b>Gerçekleşen:</b>', S_LBL), Paragraph('_____ dk', S_SML),
            ]], colWidths=[2.5*cm, 5*cm, 3.5*cm, 6*cm],
            style=TableStyle([
                ('TOPPADDING',    (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING',   (0,0),(-1,-1), 0), ('RIGHTPADDING',  (0,0),(-1,-1), 0),
                ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
            ])),
            sp(5),
        ]),
    ]
    if sorular:
        for soru in sorular:
            items += yazma_alani(soru, 2)
    if notlar:
        items += [
            Paragraph('<b>Bir sonraki sefere için not:</b>', S_LBL),
            sp(2),
        ]
        for not_str in notlar:
            items.append(Paragraph(f'( ) {not_str}', S_SML))
        items.append(sp(4))
    items.append(HorizontalLine(TW, COLOR_LIGHT_GREY, 0.3))
    items.append(sp(6))
    return items

# ── ARAÇ 1: ÖĞRETMEN YANSITMA GÜNLÜĞÜ ────────────────────────────────────────

def arac1():
    doc   = make_doc('Kapanis1_Ogretmen_Yansitma.pdf', 'Araç 1 — Öğretmen Yansıtma Günlüğü')
    story = []

    story += [
        araç_baslik('Araç 1', 'Öğretmen Yansıtma Günlüğü', 'ÖĞRETMEN REHBERİ'),
        sp(6),
        ogretmen_satiri(),
        sp(4),
        Table([[
            Paragraph('<b>Sınıf:</b>', S_LBL), '',
            Paragraph('<b>Uygulama Dönemi:</b>', S_LBL), '',
        ]], colWidths=[1.8*cm, 5*cm, 4*cm, 6.2*cm],
        style=TableStyle([
            ('VALIGN',        (0,0),(-1,-1), 'BOTTOM'),
            ('LINEBELOW',     (1,0),(1,0),   0.8, COLOR_WRITING_LINE),
            ('LINEBELOW',     (3,0),(3,0),   0.8, COLOR_WRITING_LINE),
            ('TOPPADDING',    (0,0),(-1,-1), 2),
            ('BOTTOMPADDING', (0,0),(-1,-1), 2),
            ('LEFTPADDING',   (0,0),(-1,-1), 2),
            ('RIGHTPADDING',  (0,0),(-1,-1), 4),
        ])),
        sp(8),
        blm('Genel Yansıtma'),
        sp(4),
    ] + yazma_alani('Bu üniteyi tek bir cümleyle nasıl özetlersiniz?', 1) + [
        sp(2),
    ] + yazma_alani('Hangi beklentiniz karşılandı?', 2) + [
        sp(2),
    ] + yazma_alani('Hangi beklentiniz karşılanmadı? Olası nedeni neydi?', 2) + [
        sp(2),
        Paragraph('<b>Öğrencilerin Design Thinking döngüsünü kavrama düzeyi genel olarak nasıldı?</b>', S_LBL),
        sp(2),
        Paragraph('( ) Büyük çoğunluk döngüyü anladı ve akıcı uyguladı', S_SML),
        Paragraph('( ) Çoğunluk bazı adımları kavradı; 1–2 adımda zorlandı', S_SML),
        Paragraph('( ) Döngü kavramı yerleşti ama uygulama yavaştı', S_SML),
        Paragraph('( ) Döngü kavramı henüz tam oturmadı; destekleme gerekti', S_SML),
        sp(8),
        blm('Ders Saati Bazında Yansıtma'),
        sp(4),
    ]

    # 1. Ders
    story += ders_blogu('1', 'Tasarım Nedir? + Design Thinking Tanıtımı',
        sorular=[
            '"Design Thinking nedir?" sorusuna öğrencilerin ilk tepkisi nasıldı?',
            'En iyi çalışan etkinlik / an:',
        ],
        notlar=[
            'Günlük hayat örneğini değiştireceğim',
            'Giriş etkinliğini kısaltacağım / uzatacağım',
            'Design Thinking tanıtımını farklı materyalle yapacağım',
            'Diğer: ___________________________',
        ]
    )

    # 2. Ders
    story += ders_blogu('2', 'Problem Tespiti',
        sorular=[
            'Öğrenciler gerçek bir problem belirleyebildi mi, yoksa soyut/hayali problemlere yöneldi mi?',
            'ÇK1 (Problem Tespiti Formu) ne kadar işe yaradı?',
        ],
        notlar=[
            'Problem örnekleri havuzunu genişleteceğim',
            'ÇK1 yönergesini netleştireceğim',
            'Destekleme Materyal 3\'ü daha fazla öğrenciye sunacağım',
            'Diğer: ___________________________',
        ]
    )

    # 3. Ders
    story += ders_blogu('3', 'Empati ve Kullanıcı Analizi',
        sorular=[
            '"Empati ile sempati arasındaki fark" öğrencilerde ne kadar yerleşti?',
        ],
        notlar=None
    )
    story += [
        Paragraph('<b>Empati haritasında (ÇK2) en çok hangi bölümde zorlanıldı?</b>', S_LBL),
        sp(2),
        Paragraph('( ) Ne Düşünüyor?     ( ) Ne Hissediyor?     ( ) Ne Söylüyor?     ( ) Ne Yapıyor?', S_SML),
        sp(4),
    ] + yazma_alani('Bir sonraki sefere için not', 2) + [sp(2)]
    story.append(HorizontalLine(TW, COLOR_LIGHT_GREY, 0.3))
    story.append(sp(6))

    # 4. Ders
    story += ders_blogu('4', 'Fikir Üretimi — Crazy 8 + SCAMPER',
        sorular=[
            'Crazy 8 etkinliğinde öğrenciler "yeterince saçma" fikir üretebildi mi?',
            'Fikir seçim matrisi (ÇK5) işlevsel miydi?',
            'Bir sonraki sefere için not:',
        ],
        notlar=None
    )

    # 5. Ders
    story += ders_blogu('5', 'Eskiz ve Malzeme Planlama',
        sorular=[
            'Öğrenciler fikir ile eskiz arasındaki köprüyü kurabildi mi?',
            'Malzeme planlaması (ÇK7) gerçekçi yapıldı mı? Sonraki aşamada sorun çıktı mı?',
            'Bir sonraki sefere için not:',
        ],
        notlar=None
    )

    # 6-7. Ders
    story += ders_blogu('6–7', 'Prototip Yapımı (Uygulama)',
        sorular=[
            'ISG kurallarına uyum nasıldı?',
            'Prototipi tamamlayamayan öğrenci oldu mu? Nasıl ele aldınız?',
            'Öğrencilerin süreç günlüğünü (ÇK8) tutması nasıl geçti?',
        ],
        notlar=[
            'Malzeme hazırlığını daha erken yaptıracağım',
            'Gruplama stratejisini değiştireceğim',
            'Destekleme Materyal 2 (Prototip Rehberi) daha erken sunacağım',
            'Diğer: ___________________________',
        ]
    )

    # 8. Ders
    story += ders_blogu('8', 'Test ve Geri Bildirim',
        sorular=[
            'Akran değerlendirme süreci nasıl geçti?',
            '"Ne değiştirirdin?" sorusunu öğrenciler uygulayabildi mi?',
            'Bir sonraki sefere için not:',
        ],
        notlar=None
    )

    # 9. Ders
    story += ders_blogu('9', 'Revize + Sürdürülebilirlik Kontrolü',
        sorular=[
            'Öğrenciler gerçek bir iyileştirme yapabildi mi, yoksa yüzeysel bir değişiklikle mi yetindi?',
            'Sürdürülebilirlik kontrolü ne kadar işlevseldi?',
            'Bir sonraki sefere için not:',
        ],
        notlar=None
    )

    # 10. Ders
    story += [
        KeepTogether([
            blm('10. Ders — "Sunum + Ünite Kapanışı"'),
            sp(3),
            Table([[
                Paragraph('<b>Planlanan süreye uygun geçti mi?</b>', S_LBL),
                Paragraph('( ) Evet  ( ) Hayır', S_SML),
            ]], colWidths=[8*cm, 9*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
                ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
            ])),
            sp(4),
            Paragraph('<b>Sunum kalitesi genel olarak nasıldı?</b>', S_LBL),
            sp(2),
            Paragraph('( ) Çoğunluk hem süreci hem ürünü akıcı anlattı', S_SML),
            Paragraph('( ) Ürünü anlattılar ama süreci yeterince aktaramadılar', S_SML),
            Paragraph('( ) Sunum kaygısı içeriği gölgeledi', S_SML),
            Paragraph('( ) Süre yönetiminde sorun yaşandı', S_SML),
            sp(5),
        ]),
    ] + yazma_alani('Sınıf atmosferi kapanışta nasıldı?', 2) + [
        sp(2),
    ] + yazma_alani('Bir sonraki sefere için not', 2) + [
        HorizontalLine(TW, COLOR_LIGHT_GREY, 0.3),
        sp(8),
        KeepTogether([
            blm('Öğrenci Performansları'),
            sp(4),
            Paragraph('<b>En Büyük Gelişimi Gösteren Öğrenciler</b>', S_SMBD),
            sp(3),
            Table([
                [Paragraph('Öğrenci', S_TH), Paragraph('Gözlenen Gelişim', S_TH), Paragraph('Bunu Destekleyen Faktör', S_TH)],
                [Paragraph('', S_SML), Paragraph('', S_SML), Paragraph('', S_SML)],
                [Paragraph('', S_SML), Paragraph('', S_SML), Paragraph('', S_SML)],
                [Paragraph('', S_SML), Paragraph('', S_SML), Paragraph('', S_SML)],
            ], colWidths=[4*cm, 7*cm, 6*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 0.9*cm),
            ])),
            sp(6),
            Paragraph('<b>Ek Destek Gereksinimi Olan Öğrenciler</b>', S_SMBD),
            sp(3),
            Table([
                [Paragraph('Öğrenci', S_TH), Paragraph('Gözlenen Zorluk', S_TH), Paragraph('Bir Sonraki Ünitede Denenecek Yaklaşım', S_TH7)],
                [Paragraph('', S_SML), Paragraph('', S_SML), Paragraph('', S_SML)],
                [Paragraph('', S_SML), Paragraph('', S_SML), Paragraph('', S_SML)],
            ], colWidths=[4*cm, 6*cm, 7*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 0.9*cm),
            ])),
        ]),
        sp(6),
        KeepTogether([
            Paragraph('<b>Zenginleştirmeye Yönlendirilebilecek Öğrenciler</b>', S_SMBD),
            sp(3),
            Table([
                [Paragraph('Öğrenci', S_TH), Paragraph('Güçlü Yön', S_TH), Paragraph('Önerilen Zenginleştirme', S_TH)],
                [Paragraph('', S_SML), Paragraph('', S_SML), Paragraph('Etkinlik ____', S_SML)],
                [Paragraph('', S_SML), Paragraph('', S_SML), Paragraph('Etkinlik ____', S_SML)],
            ], colWidths=[4*cm, 7*cm, 6*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 0.9*cm),
            ])),
        ]),
        sp(8),
        KeepTogether([
            blm('Materyal Değerlendirmesi'),
            sp(3),
            Table([
                [Paragraph('Materyal', S_TH), Paragraph('Değerlendirme (1–5)', S_TH7), Paragraph('Geliştirilecek Yön', S_TH)],
                *[[Paragraph(m, S_TD), Paragraph('____', S_TDC), Paragraph('', S_SML)] for m in [
                    'Ön Değerlendirme Paketi',
                    'Süreç Akış Posteri + Referans Kartı',
                    'ÇK1–ÇK5 (Problem, Empati, Fikir)',
                    'ÇK6–ÇK8 (Eskiz, Malzeme, Prototip Günlüğü)',
                    'ÇK9–ÇK11 (Test, Revize, Sunum)',
                    'Değerlendirme Araçları (Araç 1–7)',
                    'Zenginleştirme Paketi (Zen1–5)',
                    'Destekleme Paketi (Des1–6)',
                ]]
            ], colWidths=[6*cm, 3.5*cm, 7.5*cm],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        KeepTogether([
            blm('Kazanım Düzeyleri — Sınıf Geneli'),
            sp(3),
            Table([
                [Paragraph('Kazanım', S_TH7),
                 Paragraph('Üstün\n(%)', S_TH7),
                 Paragraph('Yeterli\n(%)', S_TH7),
                 Paragraph('Gelişiyor\n(%)', S_TH7),
                 Paragraph('Destek\n(%)', S_TH7)],
                *[[Paragraph(k, S_TD7),
                   Paragraph('', S_TDC7), Paragraph('', S_TDC7),
                   Paragraph('', S_TDC7), Paragraph('', S_TDC7)] for k in [
                    'TT.7.3.1.a — Problem tespiti',
                    'TT.7.3.1.b — Empati haritası',
                    'TT.7.3.1.c — Fikir geliştirme yöntemleri',
                    'TT.7.3.1.d — Eskiz ve malzeme planlaması',
                    'TT.7.3.1.e — Prototip/maket üretimi',
                    'TT.7.3.1.f — Test ve geri bildirim',
                    'TT.7.3.1.g — Revize ve iyileştirme',
                    'TT.7.3.2 — Tasarım sürecini sunma',
                ]]
            ], colWidths=[7.8*cm, 2.3*cm, 2.3*cm, 2.3*cm, 2.3*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 0.7*cm),
            ])),
        ]),
        sp(8),
    ] + yazma_alani('En başarılı olunan kazanım', 1) + [
        sp(2),
    ] + yazma_alani('En çok zorlanılan kazanım', 1) + [
        sp(6),
        blm('Profesyonel Gelişim Notu'),
        sp(4),
    ] + yazma_alani('Bu ünitede ben ne öğrendim?', 2) + [
        sp(2),
    ] + yazma_alani('Bir sonraki dönem kendim için ne deneyeceğim?', 2) + [
        sp(2),
    ] + yazma_alani('Hangi konuda okuma ya da eğitim yapmam gerekiyor?', 2)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


# ── ARAÇ 2: ÖĞRENCİ DÖNÜT ANKETİ ────────────────────────────────────────────

def arac2():
    doc   = make_doc('Kapanis2_Ogrenci_Donut_Anketi.pdf', 'Araç 2 — Öğrenci Dönüt Anketi')
    story = []

    def puan_satiri(etkinlik):
        return [
            Paragraph(etkinlik, S_TD),
            Paragraph('( )1  ( )2  ( )3  ( )4  ( )5', S_TDC),
        ]

    story += [
        araç_baslik('Araç 2', 'Öğrenci Dönüt Anketi', 'ÖĞRENCİ MATERYALİ'),
        sp(6),
        Table([[
            Paragraph('<b>Sevgili Öğrenci,</b> Bu ankete samimi cevaplar vermen, bir sonraki dönem için çok değerli. '
                      'Adını yazma zorunluluğun yok.', S_YON),
        ]], colWidths=[TW], style=TableStyle([
            ('BACKGROUND',    (0,0),(-1,-1), COLOR_VERY_LIGHT),
            ('BOX',           (0,0),(-1,-1), 0.5, COLOR_ACCENT),
            ('LEFTPADDING',   (0,0),(-1,-1), 8), ('RIGHTPADDING',  (0,0),(-1,-1), 8),
            ('TOPPADDING',    (0,0),(-1,-1), 5), ('BOTTOMPADDING', (0,0),(-1,-1), 5),
        ])),
        sp(6),
        ogrenci_satiri(),
        sp(8),
        blm('Bölüm 1: Süreç'),
        sp(4),
    ] + yazma_alani('Bu ünitede en kolay anladığım aşama', 1) + [
        sp(2),
    ] + yazma_alani('Bu ünitede en zor gelen aşama', 1) + [
        sp(2),
    ] + yazma_alani('Bu ünitede en ilginç bulduğum etkinlik ya da an', 1) + [
        sp(8),
        KeepTogether([
            blm('Bölüm 2: Etkinlikler'),
            sp(3),
            Paragraph('Her etkinliğe 1–5 puan ver (1 = hiç sevmedim, 5 = çok sevdim):', S_SML),
            sp(4),
            Table([
                [Paragraph('Etkinlik', S_TH), Paragraph('Puanım', S_TH)],
                puan_satiri('Problem tespiti (ÇK1)'),
                puan_satiri('Empati haritası doldurma (ÇK2)'),
                puan_satiri('Crazy 8 beyin fırtınası (ÇK4)'),
                puan_satiri('Eskiz çizimi (ÇK6)'),
                puan_satiri('Prototip/maket yapımı (6–7. Ders)'),
                puan_satiri('Test ve geri bildirim alma (ÇK9)'),
                puan_satiri('Tasarım süreci sunumu (10. Ders)'),
            ], colWidths=[11*cm, 6*cm],
            style=TableStyle(TABLE_BASE)),
            sp(5),
        ]),
    ] + yazma_alani('En çok sevdiğim etkinlik ve nedeni', 1) + [
        sp(2),
    ] + yazma_alani('En az sevdiğim etkinlik ve nedeni', 1) + [
        sp(8),
        KeepTogether([
            blm('Bölüm 3: Öğrenme Deneyimim'),
            sp(3),
            Paragraph('<b>Ünite sonunda nasıl hissediyorsun?</b>', S_LBL),
            sp(2),
            Paragraph('( ) Çok şey öğrendim, memnunum', S_SML),
            Paragraph('( ) Bir şeyler öğrendim ama daha fazla olabilirdi', S_SML),
            Paragraph('( ) Bazı şeyler kafama tam oturmadı', S_SML),
            Paragraph('( ) Pek bir şey öğrenmedim', S_SML),
            sp(5),
            Paragraph('<b>Design Thinking döngüsünü anladım:</b>', S_LBL),
            sp(2),
            Paragraph('( ) Evet, tüm adımları biliyorum ve uygulayabilirim', S_SML),
            Paragraph('( ) Çoğunu anladım, birkaç adımda zorlandım', S_SML),
            Paragraph('( ) Temel adımları biliyorum ama döngüyü tam uygulamak zor', S_SML),
            Paragraph('( ) Henüz tam anlamadım', S_SML),
            sp(5),
            Paragraph('<b>Sınıf içi ortam nasıldı?</b>', S_LBL),
            sp(2),
            Paragraph('( ) Rahatça soru sorabildim', S_SML),
            Paragraph('( ) Soru sormaktan çekindim', S_SML),
            Paragraph('( ) Prototipi yaparken arkadaşlarımla iyi çalıştık', S_SML),
            Paragraph('( ) Grup çalışmalarında zorlandım', S_SML),
        ]),
        sp(8),
        blm('Bölüm 4: Öneriler'),
        sp(4),
    ] + yazma_alani('Bir sonraki ünitede olmasını istediğim bir şey', 1) + [
        sp(2),
    ] + yazma_alani('Bir sonraki ünitede olmamasını istediğim bir şey', 1) + [
        sp(2),
    ] + yazma_alani('Öğretmenime söylemek istediğim bir şey', 1) + [
        sp(8),
        KeepTogether([
            blm('Bölüm 5: Kendine Bir Not'),
            sp(4),
        ] + yazma_alani('Bu üniteden 10 yıl sonra hatırlayacağım bir şey', 1) + [
            sp(2),
        ] + yazma_alani('Design Thinking\'i gerçek hayatımda kullanabilir miyim? Nerede?', 1) + [
            sp(4),
            Table([[
                Paragraph('<b>Bu ünitede kendime verdiğim puan (1–10):</b>', S_LBL),
                Paragraph('____ / 10', S_SML),
            ]], colWidths=[9*cm, 8*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
                ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
            ])),
            sp(4),
        ] + yazma_alani('Bu puanı vermimin nedeni', 1)),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


# ── ARAÇ 3: ZÜMRE PAYLAŞIM ŞABLONU ──────────────────────────────────────────

def arac3():
    doc   = make_doc('Kapanis3_Zumre_Paylasim.pdf', 'Araç 3 — Zümre Paylaşım Şablonu')
    story = []

    story += [
        araç_baslik('Araç 3', 'Zümre Paylaşım Şablonu', 'ÖĞRETMEN REHBERİ'),
        sp(6),
        Table([[
            Paragraph('<b>Öğretmen:</b>', S_LBL), '',
            Paragraph('<b>Okul:</b>',     S_LBL), '',
        ]], colWidths=[2.5*cm, 6.5*cm, 1.8*cm, 6.2*cm],
        style=TableStyle([
            ('VALIGN', (0,0),(-1,-1), 'BOTTOM'),
            ('LINEBELOW', (1,0),(1,0), 0.8, COLOR_WRITING_LINE),
            ('LINEBELOW', (3,0),(3,0), 0.8, COLOR_WRITING_LINE),
            ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
            ('LEFTPADDING', (0,0),(-1,-1), 2), ('RIGHTPADDING', (0,0),(-1,-1), 4),
        ])),
        sp(4),
        Table([[
            Paragraph('<b>Sınıf Sayısı:</b>', S_LBL), '',
            Paragraph('<b>Öğrenci Sayısı (toplam):</b>', S_LBL), '',
        ]], colWidths=[3*cm, 4*cm, 5.5*cm, 4.5*cm],
        style=TableStyle([
            ('VALIGN', (0,0),(-1,-1), 'BOTTOM'),
            ('LINEBELOW', (1,0),(1,0), 0.8, COLOR_WRITING_LINE),
            ('LINEBELOW', (3,0),(3,0), 0.8, COLOR_WRITING_LINE),
            ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
            ('LEFTPADDING', (0,0),(-1,-1), 2), ('RIGHTPADDING', (0,0),(-1,-1), 4),
        ])),
        sp(8),
        blm('1. Ana Deneyim'),
        sp(3),
        Paragraph('Bu üniteyi nasıl uyguladın? Kısa bir paragrafla özetle.', S_SML),
        sp(4),
    ] + [WritingLines(4, 15), sp(8)] + [
        KeepTogether([
            blm('2. İşe Yarayan 3 Uygulama'),
            sp(4),
        ] + yazma_alani('Uygulama 1 — Neden işe yaradı?', 2)
          + yazma_alani('Uygulama 2 — Neden işe yaradı?', 2)
          + yazma_alani('Uygulama 3 — Neden işe yaradı?', 2)),
        sp(6),
        blm('3. Zorluklar ve Denenen Çözümler'),
        sp(4),
    ] + yazma_alani('Zorluk 1 — Denediğim çözüm ve sonucu', 2) + [
        sp(2),
    ] + yazma_alani('Zorluk 2 — Denediğim çözüm', 2) + [
        sp(6),
        blm('4. Diğer Öğretmenler İçin Pratik Öneriler'),
        sp(4),
        WritingLines(3, 15),
        sp(8),
        KeepTogether([
            blm('5. Ölçme ve Değerlendirme'),
            sp(3),
            Paragraph('<b>Hangi araçları kullandım?</b>', S_LBL),
            sp(2),
            Table([[
                Paragraph('( ) Süreç Gözlem Formu', S_SML),
                Paragraph('( ) Eskiz Rubriği', S_SML),
                Paragraph('( ) Prototip Rubriği', S_SML),
                Paragraph('( ) Sunum Rubriği', S_SML),
            ]], colWidths=[4.25*cm, 4.25*cm, 4.25*cm, 4.25*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
            ])),
            Table([[
                Paragraph('( ) Akran Değerlendirme Formu', S_SML),
                Paragraph('( ) Ünite Sonu Sınavı', S_SML),
                Paragraph('( ) Genel Değerlendirme Tablosu', S_SML),
                Paragraph('( ) Diğer: ___________', S_SML),
            ]], colWidths=[5*cm, 4*cm, 5*cm, 3*cm],
            style=TableStyle([
                ('TOPPADDING', (0,0),(-1,-1), 2), ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
            ])),
            sp(5),
            Paragraph('<b>Sınıf genelinde kazanım dağılımı:</b>', S_LBL),
            sp(3),
            Table([
                [Paragraph('Düzey', S_TH), Paragraph('Yaklaşık Yüzde', S_TH)],
                [Paragraph('Üstün', S_TD),          Paragraph('% ____', S_TDC)],
                [Paragraph('Yeterli', S_TD),         Paragraph('% ____', S_TDC)],
                [Paragraph('Gelişiyor', S_TD),       Paragraph('% ____', S_TDC)],
                [Paragraph('Destek Gerekli', S_TD),  Paragraph('% ____', S_TDC)],
            ], colWidths=[8*cm, 9*cm],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        blm('6. Disiplinler Arası Bağlantı'),
        sp(3),
        Paragraph(
            '( ) Fen Bilgisi (malzeme, enerji, sürdürülebilirlik)    '
            '( ) Türkçe (sunum, yazılı anlatım)    '
            '( ) Matematik (ölçme, maliyet)    '
            '( ) Görsel Sanatlar (estetik)    '
            '( ) Diğer: ___________',
            S_SML),
        sp(8),
    ] + yazma_alani('7. Paylaşmak İstediğim Materyaller', 2) + [
        sp(2),
    ] + yazma_alani('8. Ortak Gündem Önerisi', 2)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


# ── ARAÇ 4: ÜNİTE ÖZET TABLOSU ──────────────────────────────────────────────

def arac4():
    doc   = make_doc('Kapanis4_Unite_Ozet_Tablosu.pdf', 'Araç 4 — Ünite Özet Tablosu')
    story = []

    materyaller = [
        ('1',  'Ünite Ders Planı',                     'Tüm ünite — öğretmen rehberi',      'Öğretmen rehberi'),
        ('2',  'Ön Değerlendirme Paketi',               '1. ders başında',                   'Öğrenci uygulaması'),
        ('3',  'Süreç Akış Posteri',                    'Sınıf duvarı — tüm ünite',          'A3 poster'),
        ('4',  'A5 Referans Kartı',                     'Öğrenci masası — tüm ünite',        'A5 lamineli'),
        ('5',  'Sunum İçeriği',                         'Her ders — akıllı tahta',           'Canva/Slides'),
        ('6',  'ÇK1 — Problem Tespiti Formu',           '2. Ders',                           'Öğrenci çalışması'),
        ('7',  'ÇK2 — Empati Haritası',                 '3. Ders',                           'Öğrenci çalışması'),
        ('8',  'ÇK3 — Kullanıcı Analiz Tablosu',        '3. Ders',                           'Öğrenci çalışması'),
        ('9',  'ÇK4 — Crazy 8 Beyin Fırtınası',         '4. Ders',                           'Öğrenci çalışması'),
        ('10', 'ÇK5 — Fikir Seçim Matrisi',             '4. Ders',                           'Öğrenci çalışması'),
        ('11', 'ÇK6 — Tasarım Eskizi Sayfası',          '5. Ders',                           'Öğrenci çalışması'),
        ('12', 'ÇK7 — Malzeme Planlama Tablosu',        '5. Ders',                           'Öğrenci çalışması'),
        ('13', 'ÇK8 — Prototip Süreç Günlüğü',          '6–7. Ders',                         'Öğrenci çalışması'),
        ('14', 'ÇK9 — Ürün Test ve Geri Bildirim',      '8. Ders',                           'Öğrenci + akran'),
        ('15', 'ÇK10 — Revize Planı + Sürdürülebilirlik','9. Ders',                          'Öğrenci çalışması'),
        ('16', 'ÇK11 — Tasarım Süreci Sunum Şablonu',   '10. Ders',                          'Öğrenci çalışması'),
        ('17', 'Araç 1 — Süreç Gözlem Formu',           'Her ders',                          'Öğretmen gözlem'),
        ('18', 'Araç 2–4 — Eskiz/Prototip/Sunum Rubrikleri','5./8./10. Ders',               'Öğretmen değerlendirme'),
        ('19', 'Araç 5 — Akran Değerlendirme Formu',    '8. Ders',                           'Öğrenci'),
        ('20', 'Araç 6 — Sınav (Öğrenci + Cevap Anahtarı)','Ünite sonu',                   'Ayrı PDF\'ler'),
        ('21', 'Araç 7 — Genel Değerlendirme Tablosu',  'Ünite sonu',                        'Öğretmen'),
        ('22', 'Zenginleştirme Paketi (Zen1–5)',         'İhtiyaç bazında',                   'İleri düzey'),
        ('23', 'Destekleme Paketi (Des1–6)',             'İhtiyaç bazında',                   'Destek gerektiren'),
    ]

    kazanimlar = [
        ('TT.7.3.1.a', 'Problem tespiti',           '2. Ders, ÇK1, Araç 1'),
        ('TT.7.3.1.b', 'Empati haritası',           '3. Ders, ÇK2, ÇK3, Araç 1'),
        ('TT.7.3.1.c', 'Fikir geliştirme yöntemleri','4. Ders, ÇK4, ÇK5, Araç 1'),
        ('TT.7.3.1.d', 'Eskiz ve malzeme planlaması','5. Ders, ÇK6, ÇK7, Araç 2'),
        ('TT.7.3.1.e', 'Prototip/maket üretimi',    '6–7. Ders, ÇK8, Araç 3'),
        ('TT.7.3.1.f', 'Test ve geri bildirim',     '8. Ders, ÇK9, Araç 5'),
        ('TT.7.3.1.g', 'Revize ve iyileştirme',     '9. Ders, ÇK10, Araç 3'),
        ('TT.7.3.2',   'Tasarım sürecini sunma',    '10. Ders, ÇK11, Araç 4'),
    ]

    story += [
        araç_baslik('Araç 4', 'Ünite Özet Tablosu', 'ÖĞRETMEN REHBERİ'),
        sp(6),
        blm('Tüm Materyaller'),
        sp(3),
        Table(
            [[Paragraph('#', S_TH7), Paragraph('Dosya', S_TH7),
              Paragraph('Kullanım Yeri', S_TH7), Paragraph('Format', S_TH7)]] +
            [[Paragraph(no, S_TDC7), Paragraph(dosya, S_TD7),
              Paragraph(yer, S_TD7), Paragraph(fmt, S_TD7)]
             for no, dosya, yer, fmt in materyaller],
            colWidths=[0.6*cm, 6.4*cm, 5.5*cm, 4.5*cm],
            style=TableStyle(TABLE_BASE)),
        sp(8),
        KeepTogether([
            blm('Kazanım–Materyal Eşleşmesi'),
            sp(3),
            Table(
                [[Paragraph('Kazanım Kodu', S_TH7), Paragraph('Açıklama', S_TH7), Paragraph('İlgili Materyaller', S_TH7)]] +
                [[Paragraph(kod, S_TD7), Paragraph(aciklama, S_TD7), Paragraph(mat, S_TD7)]
                 for kod, aciklama, mat in kazanimlar],
                colWidths=[2.5*cm, 5*cm, 9.5*cm],
                style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        KeepTogether([
            blm('Hazırlık Kontrol Listesi'),
            sp(3),
            Paragraph('<b>1 Hafta Öncesi:</b>', S_SMBD),
            sp(2),
            Paragraph('( ) Tüm materyaller gözden geçirildi', S_SML),
            Paragraph('( ) Sunum slaytları oluşturuldu (Canva / Google Slides)', S_SML),
            Paragraph('( ) Süreç Akış Posteri yazdırıldı (A3)', S_SML),
            Paragraph('( ) Referans Kartları yazdırıldı ve lamine edildi (20 adet)', S_SML),
            Paragraph('( ) ÇK1–ÇK11 fotokopileri çekildi (20 öğrenci x 11 sayfa)', S_SML),
            Paragraph('( ) Değerlendirme araçları hazırlandı', S_SML),
            sp(4),
            Paragraph('<b>1 Gün Öncesi:</b>', S_SMBD),
            sp(2),
            Paragraph('( ) Atölye malzemeleri kontrol edildi (karton, köpük, tel, makas, tutkal, boya)', S_SML),
            Paragraph('( ) Akıllı tahta test edildi', S_SML),
            Paragraph('( ) ISG bilgilendirmesi hazırlandı (6. ders için)', S_SML),
            Paragraph('( ) Destekleme Materyal 1 (Döngü Kartı) lamine edildi', S_SML),
            sp(4),
            Paragraph('<b>Ders Günü:</b>', S_SMBD),
            sp(2),
            Paragraph('( ) O güne ait ÇK masalarda hazır', S_SML),
            Paragraph('( ) Süreç Posteri sınıf duvarında görünür yerde asılı', S_SML),
            Paragraph('( ) Akran değerlendirme formları hazır (8. ders için)', S_SML),
        ]),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


# ── ARAÇ 5: 4. ÜNİTEYE GEÇİŞ NOTLARI ────────────────────────────────────────

def arac5():
    doc   = make_doc('Kapanis5_Gecis_Notlari.pdf', 'Araç 5 — 4. Üniteye Geçiş Notları')
    story = []

    story += [
        araç_baslik('Araç 5', '4. Üniteye Geçiş Notları', 'ÖĞRETMEN REHBERİ'),
        sp(6),
        Table([[Paragraph(
            '4. Ünite: Bilgisayar Destekli Tasarım  •  8 ders saati — 4 hafta  •  '
            'Tasarım fikirlerini dijital ortama taşımak',
            S_SMIT)]], colWidths=[TW],
            style=TableStyle([
                ('BACKGROUND', (0,0),(-1,-1), COLOR_VERY_LIGHT),
                ('BOX', (0,0),(-1,-1), 0.5, COLOR_ACCENT),
                ('LEFTPADDING', (0,0),(-1,-1), 8), ('RIGHTPADDING', (0,0),(-1,-1), 8),
                ('TOPPADDING', (0,0),(-1,-1), 5), ('BOTTOMPADDING', (0,0),(-1,-1), 5),
            ])),
        sp(8),
        KeepTogether([
            blm('3. Ünite ↔ 4. Ünite Köprüleri'),
            sp(3),
            Table([
                [Paragraph('3. Üniteden Gelen', S_TH), Paragraph('4. Ünitede Derinleşecek', S_TH)],
                [Paragraph('El çizimi eskiz becerisi', S_TD),
                 Paragraph('Aynı eskiz mantığını dijital araçlara aktarma', S_SML)],
                [Paragraph('Malzeme seçimi ve boyut düşüncesi', S_TD),
                 Paragraph('Bilgisayar destekli ölçü ve hassasiyet', S_SML)],
                [Paragraph('Prototip üretme deneyimi', S_TD),
                 Paragraph('Dijital modelden çıktıya (3B baskı, lazer kesim)', S_SML)],
                [Paragraph('Sürdürülebilirlik ve ergonomi farkındalığı', S_TD),
                 Paragraph('Dijital tasarımda optimizasyon ve verimlilik', S_SML)],
                [Paragraph('Design Thinking döngüsü', S_TD),
                 Paragraph('Aynı döngüyü dijital ortamda uygulama', S_SML)],
            ], colWidths=[8.5*cm, 8.5*cm],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        KeepTogether([
            blm('Geçiş Köprü Sorusu'),
            sp(3),
            Table([[Paragraph(
                '"3. ünitede bir prototip yaptınız. Eğer o prototipi kâğıt-karton yerine '
                'bir bilgisayar programında tasarlasaydınız ne değişirdi? '
                'Ne kolaylaşırdı, ne zorlaşırdı?"',
                S_YON)]], colWidths=[TW],
                style=TableStyle([
                    ('BACKGROUND', (0,0),(-1,-1), COLOR_VERY_LIGHT),
                    ('BOX', (0,0),(-1,-1), 0.5, COLOR_ACCENT),
                    ('LEFTPADDING', (0,0),(-1,-1), 8), ('RIGHTPADDING', (0,0),(-1,-1), 8),
                    ('TOPPADDING', (0,0),(-1,-1), 6), ('BOTTOMPADDING', (0,0),(-1,-1), 6),
                ])),
            sp(3),
            Paragraph(
                'Bu soru öğrencileri fiziksel ↔ dijital tasarım farkını düşünmeye hazırlar. '
                'Son derste veya 4. ünitenin ilk dersinde kullanılabilir.',
                S_SMIT),
        ]),
        sp(8),
        KeepTogether([
            blm('5 Dakikalık Hatırlama Turu — 4. Ünite Başında Kullan'),
            sp(3),
            Table([
                [Paragraph('Soru', S_TH)],
                [Paragraph('3. ünitede tasarımınızın eskizini nasıl yaptınız?', S_TD)],
                [Paragraph('Prototipin ölçüleri ne kadar önemliydi?', S_TD)],
                [Paragraph('"Dijital tasarım" denince ne geliyor aklınıza?', S_TD)],
                [Paragraph('Bir ürünü bilgisayarda tasarlamak ne işe yarar?', S_TD)],
            ], colWidths=[TW],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        KeepTogether([
            blm('Hazırlık Ödevi (3. Ünite Kapandığında Ver)'),
            sp(3),
            Table([[Paragraph(
                '"Evde ya da okulda kullandığın bir nesneyi incele: bu nesne bilgisayarda tasarlanmış mıdır? '
                '(Bak, araştır, sor.) 4. ünitede bu sorunun cevabını tartışacağız."',
                S_YON)]], colWidths=[TW],
                style=TableStyle([
                    ('BACKGROUND', (0,0),(-1,-1), COLOR_VERY_LIGHT),
                    ('BOX', (0,0),(-1,-1), 0.5, COLOR_ACCENT),
                    ('LEFTPADDING', (0,0),(-1,-1), 8), ('RIGHTPADDING', (0,0),(-1,-1), 8),
                    ('TOPPADDING', (0,0),(-1,-1), 6), ('BOTTOMPADDING', (0,0),(-1,-1), 6),
                ])),
        ]),
        sp(8),
        KeepTogether([
            blm('4. Ünite İçin Disiplinler Arası İpucu'),
            sp(3),
            Table([
                [Paragraph('Ders', S_TH), Paragraph('Bağlantı Noktası', S_TH)],
                [Paragraph('Bilişim Teknolojileri', S_TD),
                 Paragraph('Yazılım kullanımı, dosya formatları, 2B/3B görselleştirme', S_SML)],
                [Paragraph('Matematik', S_TD),
                 Paragraph('Ölçek, oran, geometrik şekiller, koordinat sistemi', S_SML)],
                [Paragraph('Fen Bilgisi', S_TD),
                 Paragraph('Malzeme dayanımı, fiziksel kısıtlar, kuvvet ve denge', S_SML)],
            ], colWidths=[4.5*cm, 12.5*cm],
            style=TableStyle(TABLE_BASE)),
        ]),
        sp(8),
        KeepTogether([
            blm('Öğrenci Profilinin Bir Sonraki Üniteye Yansıması'),
            sp(3),
            Table([
                [Paragraph('Öğrenci Profili', S_TH), Paragraph('Öneri', S_TH)],
                [Paragraph('Bu ünitede zorlanan öğrenciler', S_TD),
                 Paragraph(
                     'Destekleme paketini 4. ünitede de sunun. '
                     'Ekran başında çalışmak bazı öğrenciler için atölyeden daha rahatlayıcı olabilir.',
                     S_SML)],
                [Paragraph('Üstün performans gösteren öğrenciler', S_TD),
                 Paragraph(
                     '3. ünitedeki tasarımı CAD yazılımında yeniden modellemeyi önerin. '
                     'Bu 3. ve 4. ünitenin en doğal bağlantısıdır.',
                     S_SML)],
            ], colWidths=[4.5*cm, 12.5*cm],
            style=TableStyle(TABLE_BASE + [
                ('ROWMINIMUMHEIGHT', (1,1), (-1,-1), 1.5*cm),
            ])),
        ]),
        sp(10),
        Table([[Paragraph(
            '3. Ünite "Tasarım Odaklı Süreç" tamamlandı.\n\n'
            'Bu ünite; 10 ders saati, 2 kazanım kümesi ve fiziksel bir prototiple öğrencilerin '
            'Design Thinking döngüsünü gerçek bir problemde yaşadıkları en kapsamlı ünitelerden biriydi.\n\n'
            'Öğrenciler problemi tespit etti, kullanıcıyla empati kurdu, fikir üretti, '
            'eskiz çizdi, ellerini hamura attı, test etti, geri bildirime açık kaldı ve süreci anlattı.\n\n'
            'Bu sadece bir ünite değil — bir düşünme biçiminin başlangıcıdır.\n\n'
            'Bir sonraki ünitede iyi dersler, anlamlı öğrenmeler ve güçlü bağlantılar.',
            S_KAP)]], colWidths=[TW],
            style=TableStyle([
                ('BACKGROUND', (0,0),(-1,-1), COLOR_VERY_LIGHT),
                ('BOX', (0,0),(-1,-1), 1, COLOR_PRIMARY),
                ('LEFTPADDING', (0,0),(-1,-1), 12), ('RIGHTPADDING', (0,0),(-1,-1), 12),
                ('TOPPADDING', (0,0),(-1,-1), 10), ('BOTTOMPADDING', (0,0),(-1,-1), 10),
            ])),
    ]

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


# ── Ana Üretim Döngüsü ───────────────────────────────────────────────────────

PDFS = [
    ('Kapanis1_Ogretmen_Yansitma.pdf',   'Kapanis 1 - Ogretmen Yansitma',    arac1),
    ('Kapanis2_Ogrenci_Donut_Anketi.pdf','Kapanis 2 - Ogrenci Donut Anketi', arac2),
    ('Kapanis3_Zumre_Paylasim.pdf',      'Kapanis 3 - Zumre Paylasim',       arac3),
    ('Kapanis4_Unite_Ozet_Tablosu.pdf',  'Kapanis 4 - Unite Ozet Tablosu',   arac4),
    ('Kapanis5_Gecis_Notlari.pdf',       'Kapanis 5 - Gecis Notlari',        arac5),
]

if __name__ == '__main__':
    print('\n3. Unite - Kapanis PDF Uretimi\n' + '-' * 40)
    toplam = 0
    for fname, aciklama, builder in PDFS:
        try:
            builder()
            toplam += 1
            print(f'  {aciklama:<42} -> OK')
        except Exception as e:
            print(f'  HATA [{aciklama}]: {e}')
    print('-' * 40)
    print(f'Tamamlanan: {toplam}/{len(PDFS)}')
    print(f'Konum: {OUT}')
