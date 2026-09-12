"""
Unite2 — CK6: Galeri Öz Değerlendirmesi (Öğrenci Formu)
6. Ders sonunda, galeri turu tamamlandıktan sonra dağıtılır.
Tek sayfaya sığdırılmış.

Kullanım:
    python pdf_uretim/uret_unite2_ck6_oz_degerlendirme.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, add_page_number,
    make_student_info_header, HorizontalLine, WritingLines,
    COLOR_PRIMARY, COLOR_ACCENT, COLOR_SECONDARY,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_TEXT, COLOR_MUTED,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_OUTPUT = os.path.join(
    ROOT, 'units', 'unit2', 'Unite2_CK6_Oz_Degerlendirme.pdf')

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite'
DOC_TITLE  = 'CK6 — Galeri Öz Değerlendirmesi'
PAGE_W     = A4[0] - 4 * cm

# ── Stil sabitleri ───────────────────────────────────────────────

BOLUM_ST = ParagraphStyle(
    'CK6_Bolum', fontName='TR-Bold', fontSize=9,
    textColor=white, leading=13, spaceAfter=4, spaceBefore=6,
    backColor=COLOR_ACCENT, leftIndent=-6, rightIndent=-6,
    borderPadding=(3, 6, 3, 6),
)

SORU_ST = ParagraphStyle(
    'CK6_Soru', fontName='TR-Regular', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=3,
)

SORU_BOLD_ST = ParagraphStyle(
    'CK6_SoruBold', fontName='TR-Bold', fontSize=9,
    textColor=COLOR_TEXT, leading=12, spaceAfter=2,
)

TAMAMLA_ST = ParagraphStyle(
    'CK6_Tamamla', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_MUTED, leading=11, spaceAfter=2,
    leftIndent=6,
)

TH_ST = ParagraphStyle(
    'CK6_TH', fontName='TR-Bold', fontSize=8,
    textColor=white, leading=10, alignment=TA_CENTER,
)

TD_ST = ParagraphStyle(
    'CK6_TD', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=11,
)

KUCUK_ST = ParagraphStyle(
    'CK6_Kucuk', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=10, spaceAfter=2,
)

KUCUK_BOLD_ST = ParagraphStyle(
    'CK6_KucukBold', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_TEXT, leading=10, spaceAfter=1,
)


# ── Bölüm 1: Değerlendirme tablosu ──────────────────────────────

def bolum1():
    OLCUTLER = [
        'Tasarım elemanlarını bilinçli kullandım',
        'Tasarım ilkelerini uyguladım',
        'Konu/problem ile tasarımım uyumluydu',
        'Orijinal ve özgün bir fikir ortaya koydum',
        'Süreci planlayarak ilerledim',
    ]
    SEVIYELER = ['Harika', 'İyi', 'Gelişiyor', 'Henüz Değil']

    olcut_w  = PAGE_W - 4 * 2.0 * cm
    seviye_w = 2.0 * cm

    hdr = [Paragraph('Ölçüt', TH_ST)] + [Paragraph(s, TH_ST) for s in SEVIYELER]
    rows = [hdr]
    for olcut in OLCUTLER:
        rows.append(
            [Paragraph(olcut, TD_ST)] +
            [Paragraph('( )', ParagraphStyle('CK6_Opt', fontName='TR-Regular',
                fontSize=9, textColor=COLOR_MUTED, leading=11,
                alignment=TA_CENTER)) for _ in SEVIYELER]
        )

    t = Table(rows, colWidths=[olcut_w] + [seviye_w] * 4, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_ACCENT),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 5),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 5),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN',         (1, 0), (-1, -1), 'CENTER'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    return t


# ── Bölüm 2 + 3: Yan yana (2 sütun) ─────────────────────────────

def bolum2_ve_3():
    col_w = (PAGE_W - 0.3 * cm) / 2

    def _yanit_kutu(baslik, soru, n_satir):
        """Başlık + soru + yazma çizgisi bloğunu tablo hücresi için döndür."""
        items = [
            Paragraph(baslik, BOLUM_ST),
            Spacer(1, 3),
            Paragraph(soru, SORU_ST),
            WritingLines(num_lines=n_satir, line_spacing=15),
        ]
        inner = Table([[p] for p in items], colWidths=[col_w - 0.1 * cm])
        inner.setStyle(TableStyle([
            ('TOPPADDING',    (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING',   (0, 0), (-1, -1), 0),
            ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
        ]))
        return inner

    sol = _yanit_kutu(
        'BÖLÜM 2 — Tasarımımın En Güçlü Yanı',
        'Ürününde en çok neyi beğendin? Neden?',
        n_satir=3,
    )
    sag = _yanit_kutu(
        'BÖLÜM 3 — Bir Sonra Farklı Yapacaklarım',
        'Şimdi başlasaydın neyi farklı yapardın?',
        n_satir=3,
    )

    outer = Table([[sol, sag]], colWidths=[col_w + 0.15 * cm, col_w + 0.15 * cm])
    outer.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
    ]))
    return outer


# ── Bölüm 4: Galeriden İzlenimler ───────────────────────────────

def bolum4():
    items = []
    items.append(Paragraph('BÖLÜM 4 — Galeriden İzlenimler', BOLUM_ST))
    items.append(Spacer(1, 3))

    # İki soru yan yana
    col_w4 = (PAGE_W - 0.3 * cm) / 2

    def _soru_blok(soru, n_satir):
        blok = [
            Paragraph(soru, SORU_ST),
            WritingLines(num_lines=n_satir, line_spacing=15),
        ]
        inner = Table([[p] for p in blok], colWidths=[col_w4 - 0.1 * cm])
        inner.setStyle(TableStyle([
            ('TOPPADDING',    (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING',   (0, 0), (-1, -1), 0),
            ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
        ]))
        return inner

    sol = _soru_blok(
        'En dikkatini çeken ürün hangisiydi ve hangi özelliği öne çıkıyordu?',
        n_satir=2,
    )
    sag = _soru_blok(
        'Sana verilen post-it\'lerden öğrendiğin bir şey var mı?',
        n_satir=2,
    )

    ic_tablo = Table(
        [[sol, sag]],
        colWidths=[col_w4 + 0.15 * cm, col_w4 + 0.15 * cm],
    )
    ic_tablo.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
    ]))
    items.append(ic_tablo)
    return items


# ── Bölüm 5: Ünite Sonu Öz Değerlendirmesi ──────────────────────

def bolum5():
    items = []
    items.append(Paragraph('BÖLÜM 5 — Ünite Sonu Öz Değerlendirmesi', BOLUM_ST))
    items.append(Spacer(1, 3))

    # Tamamlama cümleleri
    items.append(Paragraph(
        'Bu üniteden önce tasarım eleman ve ilkeleri hakkında...', TAMAMLA_ST))
    items.append(WritingLines(num_lines=1, line_spacing=15))
    items.append(Paragraph('...düşünüyordum.', TAMAMLA_ST))
    items.append(Spacer(1, 3))
    items.append(Paragraph('Şimdi ise...', TAMAMLA_ST))
    items.append(WritingLines(num_lines=1, line_spacing=15))
    items.append(Paragraph('...biliyorum.', TAMAMLA_ST))
    items.append(Spacer(1, 4))

    # Ders sorusu + eleman/ilke yan yana
    col5a = PAGE_W * 0.55
    col5b = PAGE_W - col5a

    ders_blok = [
        Paragraph('Bu ünitede en çok hangi ders saatini sevdin ve neden?', SORU_ST),
        WritingLines(num_lines=2, line_spacing=15),
    ]
    ders_t = Table([[p] for p in ders_blok], colWidths=[col5a - 0.2 * cm])
    ders_t.setStyle(TableStyle([
        ('TOPPADDING', (0,0),(-1,-1), 0), ('BOTTOMPADDING', (0,0),(-1,-1), 0),
        ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
    ]))

    el_data = [
        [Paragraph('Kullanmak istediğim:', KUCUK_BOLD_ST)],
        [Paragraph('Eleman: _____________________', KUCUK_ST)],
        [Paragraph('İlke: _____________________', KUCUK_ST)],
        [Paragraph('Neden?', KUCUK_BOLD_ST)],
        [WritingLines(num_lines=2, line_spacing=15)],
    ]
    el_t = Table(el_data, colWidths=[col5b - 0.2 * cm])
    el_t.setStyle(TableStyle([
        ('TOPPADDING', (0,0),(-1,-1), 1), ('BOTTOMPADDING', (0,0),(-1,-1), 1),
        ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
    ]))

    yan_yana = Table(
        [[ders_t, el_t]],
        colWidths=[col5a, col5b],
    )
    yan_yana.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
    ]))
    items.append(yan_yana)
    return items


# ── Yansıtma + Kontrol Listesi (yan yana) ───────────────────────

def yansitma_ve_kontrol():
    col_w = (PAGE_W - 0.3 * cm) / 2

    # Sol: Yansıtma
    yansitma_st = ParagraphStyle(
        'CK6_YansitmaBaslik', fontName='TR-Bold', fontSize=8.5,
        textColor=COLOR_SECONDARY, leading=11, spaceAfter=3, spaceBefore=4,
    )
    satir_st = ParagraphStyle(
        'CK6_YansitmaSatir', fontName='TR-Regular', fontSize=8.5,
        textColor=COLOR_TEXT, leading=11, spaceAfter=3,
    )
    sol_items = [
        Paragraph('Yansıtma', yansitma_st),
        Paragraph('En büyük başarım: _______________________________', satir_st),
        Paragraph('Daha çok çalışmam gereken: ______________________', satir_st),
    ]
    sol_t = Table([[p] for p in sol_items], colWidths=[col_w - 0.1 * cm])
    sol_t.setStyle(TableStyle([
        ('TOPPADDING', (0,0),(-1,-1), 0), ('BOTTOMPADDING', (0,0),(-1,-1), 0),
        ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
    ]))

    # Sağ: Kontrol Listesi
    kontrol_st = ParagraphStyle(
        'CK6_KontrolBaslik', fontName='TR-Bold', fontSize=8.5,
        textColor=COLOR_SECONDARY, leading=11, spaceAfter=3, spaceBefore=4,
    )
    madde_st = ParagraphStyle(
        'CK6_KontrolMadde', fontName='TR-Regular', fontSize=8.5,
        textColor=COLOR_TEXT, leading=11, spaceAfter=2, leftIndent=4,
    )
    sag_items = [
        Paragraph('Kontrol Listesi', kontrol_st),
        Paragraph('☐  Değerlendirme tablosunu doldurdum', madde_st),
        Paragraph('☐  Tasarımımın güçlü yanını açıkladım', madde_st),
        Paragraph('☐  Galeri izlenimlerimi yazdım', madde_st),
        Paragraph('☐  Ünite sonu bölümünü tamamladım', madde_st),
    ]
    sag_t = Table([[p] for p in sag_items], colWidths=[col_w - 0.1 * cm])
    sag_t.setStyle(TableStyle([
        ('TOPPADDING', (0,0),(-1,-1), 0), ('BOTTOMPADDING', (0,0),(-1,-1), 0),
        ('LEFTPADDING', (0,0),(-1,-1), 0), ('RIGHTPADDING', (0,0),(-1,-1), 0),
    ]))

    outer = Table(
        [[sol_t, sag_t]],
        colWidths=[col_w + 0.15 * cm, col_w + 0.15 * cm],
    )
    outer.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1),  0.5, COLOR_LIGHT_GREY),
        ('BOX',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('BACKGROUND',   (0, 0), (-1, -1), COLOR_VERY_LIGHT),
    ]))
    return outer


# ── Ana üretim fonksiyonu ────────────────────────────────────────

def build(output_path=None):
    out = output_path or _DEFAULT_OUTPUT
    doc = create_doc(out, title=DOC_TITLE, unite_info=UNITE_INFO)
    elems = []

    # Öğrenci bilgi satırı
    elems.append(make_student_info_header())
    elems.append(Spacer(1, 3))
    elems.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elems.append(Spacer(1, 3))

    # Başlık + Yönerge
    title_st = ParagraphStyle(
        'CK6_Title', fontName='TR-Bold', fontSize=12,
        textColor=COLOR_PRIMARY, leading=16, spaceAfter=2,
    )
    yonerge_st = ParagraphStyle(
        'CK6_Yonerge', fontName='TR-Regular', fontSize=8,
        textColor=COLOR_TEXT, leading=11, spaceAfter=4,
        backColor=COLOR_VERY_LIGHT, borderPadding=4,
    )
    elems.append(Paragraph(
        'CK6 — Galeri Öz Değerlendirmesi', title_st))
    elems.append(Paragraph(
        '<b>Yönerge:</b> Galeri turunu tamamladıktan sonra hem kendi tasarımını hem de '
        'ünite boyunca yaptığın çalışmaları değerlendir. Dürüst ve düşünceli ol — '
        'bu değerlendirme gelişiminin haritasıdır. '
        '&nbsp;&nbsp;<b>Süre: 8 dk</b>',
        yonerge_st,
    ))
    elems.append(Spacer(1, 3))

    # Bölüm 1
    elems.append(Paragraph('BÖLÜM 1 — Tasarımımı Değerlendiriyorum', BOLUM_ST))
    elems.append(Spacer(1, 3))
    elems.append(bolum1())
    elems.append(Spacer(1, 5))

    # Bölüm 2 + 3 yan yana
    elems.append(bolum2_ve_3())
    elems.append(Spacer(1, 5))

    # Bölüm 4
    for el in bolum4():
        elems.append(el)
    elems.append(Spacer(1, 5))

    # Bölüm 5
    for el in bolum5():
        elems.append(el)
    elems.append(Spacer(1, 5))

    # Yansıtma + Kontrol
    elems.append(yansitma_ve_kontrol())

    doc.build(elems, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return out


if __name__ == '__main__':
    result = build()
    print(f'PDF olusturuldu: {result}')
