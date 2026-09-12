"""
Unite2 — Araç 2: Öğrenci Dönüt Anketi  (tek sayfa)
Ünite sonunda öğrencilere dağıtılır.

Kullanım:
    python pdf_uretim/uret_unite2_donut_anketi.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, add_page_number,
    HorizontalLine, WritingLines,
    COLOR_PRIMARY, COLOR_ACCENT, COLOR_SECONDARY,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_TEXT, COLOR_MUTED, COLOR_WRITING_LINE,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import white

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_OUTPUT = os.path.join(
    ROOT, 'units', 'unit2', 'Unite2_Arac2_Ogrenci_Donut_Anketi.pdf'
)

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 2. Ünite'
DOC_TITLE  = 'Araç 2 — Öğrenci Dönüt Anketi'
PAGE_W     = A4[0] - 4 * cm   # ~17 cm kullanılabilir genişlik

# ── Stil sabitleri ────────────────────────────────────────────────

BOLUM_ST = ParagraphStyle(
    'DA_Bolum', fontName='TR-Bold', fontSize=8.5,
    textColor=white, leading=12, spaceAfter=3, spaceBefore=5,
    backColor=COLOR_ACCENT, leftIndent=-4, rightIndent=-4,
    borderPadding=(2, 4, 2, 4),
)

SORU_ST = ParagraphStyle(
    'DA_Soru', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=2,
)

SORU_BOLD_ST = ParagraphStyle(
    'DA_SoruBold', fontName='TR-Bold', fontSize=8.5,
    textColor=COLOR_TEXT, leading=12, spaceAfter=1,
)

CHECK_ST = ParagraphStyle(
    'DA_Check', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=1, leftIndent=4,
)

TH_ST = ParagraphStyle(
    'DA_TH', fontName='TR-Bold', fontSize=7.5,
    textColor=white, leading=10, alignment=TA_CENTER,
)

TD_ST = ParagraphStyle(
    'DA_TD', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=10,
)

OPT_ST = ParagraphStyle(
    'DA_Opt', fontName='TR-Regular', fontSize=8.5,
    textColor=COLOR_MUTED, leading=11, alignment=TA_CENTER,
)

MINI_BOLD_ST = ParagraphStyle(
    'DA_MiniBold', fontName='TR-Bold', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=1,
)

MINI_ST = ParagraphStyle(
    'DA_Mini', fontName='TR-Regular', fontSize=8,
    textColor=COLOR_TEXT, leading=11, spaceAfter=1,
)


# ── Yardımcı: Iç tablo (sütun içi dikey yığın) ──────────────────

def _inner(items, w):
    t = Table([[p] for p in items], colWidths=[w])
    t.setStyle(TableStyle([
        ('TOPPADDING',    (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING',   (0, 0), (-1, -1), 0),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 0),
    ]))
    return t


# ── Üst bant: başlık + yönerge + ad-soyad ────────────────────────

def header_block():
    title_st = ParagraphStyle(
        'DA_Title', fontName='TR-Bold', fontSize=13,
        textColor=COLOR_PRIMARY, leading=16, spaceAfter=2,
    )
    yonerge_st = ParagraphStyle(
        'DA_Yonerge', fontName='TR-Regular', fontSize=8,
        textColor=COLOR_TEXT, leading=11, spaceAfter=3,
        backColor=COLOR_VERY_LIGHT, borderPadding=4,
    )
    label_st = ParagraphStyle(
        'DA_Label', fontName='TR-Regular', fontSize=8.5,
        textColor=COLOR_TEXT, leading=12,
    )

    items = [
        Paragraph('ARAÇ 2 — ÖĞRENCİ DÖNÜT ANKETİ', title_st),
        Paragraph(
            '<b>Sevgili Öğrenci,</b> Bu ankete samimi cevaplar vermen, bir sonraki dönem için '
            'çok değerli. Adını yazma zorunluluğun yok.',
            yonerge_st,
        ),
    ]

    header_row = [[
        Paragraph('<b>Ad-Soyad</b> <i>(İsteğe bağlı):</i>', label_st), '',
        Paragraph('<b>Tarih:</b>', label_st), '',
    ]]
    info_table = Table(header_row, colWidths=[4 * cm, 8.2 * cm, 1.8 * cm, 3 * cm])
    info_table.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW',    (1, 0), (1, 0), 0.7, COLOR_WRITING_LINE),
        ('LINEBELOW',    (3, 0), (3, 0), 0.7, COLOR_WRITING_LINE),
        ('TOPPADDING',   (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 3),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    items.append(info_table)
    return items


# ── BÖLÜM 1: Kavramlar ───────────────────────────────────────────

def _bolum1(col_w):
    items = [
        Paragraph('BÖLÜM 1 — KAVRAMLAR', BOLUM_ST),
        Spacer(1, 2),
        Paragraph('1.  Bu ünitede en kolay öğrendiğim konu:', SORU_ST),
        WritingLines(num_lines=1, line_spacing=13),
        Spacer(1, 3),
        Paragraph('2.  Bu ünitede en zor gelen konu:', SORU_ST),
        WritingLines(num_lines=1, line_spacing=13),
        Spacer(1, 3),
        Paragraph('3.  En ilginç bulduğum kavram ya da etkinlik:', SORU_ST),
        WritingLines(num_lines=1, line_spacing=13),
    ]
    return _inner(items, col_w)


# ── BÖLÜM 4: Öneriler ────────────────────────────────────────────

def _bolum4(col_w):
    items = [
        Paragraph('BÖLÜM 4 — ÖNERİLER', BOLUM_ST),
        Spacer(1, 2),
        Paragraph('1.  Bir sonraki ünitede olmasını istediğim bir şey:', SORU_ST),
        WritingLines(num_lines=1, line_spacing=13),
        Spacer(1, 3),
        Paragraph('2.  Bir sonraki ünitede olmamasını istediğim:', SORU_ST),
        WritingLines(num_lines=1, line_spacing=13),
        Spacer(1, 3),
        Paragraph('3.  Öğretmenime söylemek istediğim:', SORU_ST),
        WritingLines(num_lines=1, line_spacing=13),
    ]
    return _inner(items, col_w)


# ── BÖLÜM 3: Öğrenme Deneyimim ───────────────────────────────────

def _bolum3(col_w):
    items = [
        Paragraph('BÖLÜM 3 — ÖĞRENME DENEYİMİM', BOLUM_ST),
        Spacer(1, 2),
        Paragraph('<b>Ünite sonunda nasıl hissediyorsun?</b>', SORU_BOLD_ST),
        Paragraph('( ) Çok şey öğrendim, memnunum', CHECK_ST),
        Paragraph('( ) Bir şeyler öğrendim ama daha fazla olabilirdi', CHECK_ST),
        Paragraph('( ) Bazı şeyler kafama tam oturmadı    ( ) Pek bir şey öğrenmedim', CHECK_ST),
        Spacer(1, 4),
        Paragraph('<b>Öğretmenin anlatımı nasıldı?</b>', SORU_BOLD_ST),
        Paragraph('( ) Çok net, her şeyi anladım    ( ) Çoğunlukla netti', CHECK_ST),
        Paragraph('( ) Zaman zaman kayboldum    ( ) Çoğu zaman karışıktı', CHECK_ST),
        Spacer(1, 4),
        Paragraph('<b>Sınıf içi ortam nasıldı?</b>', SORU_BOLD_ST),
        Paragraph('( ) Rahatça soru sorabildim    ( ) Soru sormaktan çekindim', CHECK_ST),
        Paragraph('( ) Arkadaşlarımla iyi çalıştık    ( ) Grup çalışmalarında zorlandım', CHECK_ST),
    ]
    return _inner(items, col_w)


# ── BÖLÜM 5: Kendine Bir Not ─────────────────────────────────────

def _bolum5(col_w):
    puan_st = ParagraphStyle(
        'DA_Puan', fontName='TR-Bold', fontSize=9,
        textColor=COLOR_TEXT, leading=12, spaceAfter=2,
    )
    items = [
        Paragraph('BÖLÜM 5 — KENDİNE BİR NOT', BOLUM_ST),
        Spacer(1, 2),
        Paragraph('Bu üniteden 10 yıl sonra hatırlayacağım bir şey:', SORU_ST),
        WritingLines(num_lines=2, line_spacing=13),
        Spacer(1, 4),
        Paragraph('Bu ünitede kendime verdiğim puan: _____ / 10', puan_st),
        Paragraph('Bu puanı vermimin nedeni:', SORU_ST),
        WritingLines(num_lines=1, line_spacing=13),
    ]
    return _inner(items, col_w)


# ── Sol sütun (B1 + B4) ve Sağ sütun (B3 + B5) ──────────────────

def sol_sag_bolumler():
    col_l = PAGE_W * 0.54 - 0.2 * cm   # ~9.0 cm
    col_r = PAGE_W - col_l - 0.3 * cm  # ~7.7 cm

    sol_items = [
        _bolum1(col_l),
        Spacer(1, 5),
        _bolum4(col_l),
    ]
    sag_items = [
        _bolum3(col_r),
        Spacer(1, 5),
        _bolum5(col_r),
    ]

    sol_t = _inner(sol_items, col_l)
    sag_t = _inner(sag_items, col_r)

    outer = Table(
        [[sol_t, Spacer(0.3 * cm, 1), sag_t]],
        colWidths=[col_l, 0.3 * cm, col_r],
    )
    outer.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1), 0.4, COLOR_LIGHT_GREY),
    ]))
    return outer


# ── BÖLÜM 2: Etkinlik Puanlama (tam genişlik) ────────────────────

def bolum2():
    items = []
    items.append(Paragraph('BÖLÜM 2 — ETKİNLİKLER', BOLUM_ST))
    items.append(Spacer(1, 2))

    inst_st = ParagraphStyle(
        'DA_Inst', fontName='TR-Regular', fontSize=8,
        textColor=COLOR_MUTED, leading=11, spaceAfter=3,
    )
    items.append(Paragraph(
        'Her etkinliğe 1–5 puan ver (1 = hiç sevmedim, 5 = çok sevdim):',
        inst_st,
    ))

    etkinlikler = [
        'Eleman Avı (CK1)',
        'İlkeler Karşılaştırma (CK2)',
        'Eseri İnceliyorum / Yeniden Yorumlama (CK3)',
        'Dörtlü Analoji (CK4)',
        'Taslak çizimi ve tasarım planı (CK5)',
        'Üretim ve Tasarım Galerisi (6. Ders)',
    ]

    puan_w   = 1.45 * cm
    etkinlik_w = PAGE_W - 5 * puan_w

    rows = [
        [Paragraph('Etkinlik', TH_ST)] + [Paragraph(str(i), TH_ST) for i in range(1, 6)]
    ]
    for e in etkinlikler:
        rows.append(
            [Paragraph(e, TD_ST)] +
            [Paragraph('( )', OPT_ST) for _ in range(5)]
        )

    tbl = Table(rows, colWidths=[etkinlik_w] + [puan_w] * 5, repeatRows=1)
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), COLOR_ACCENT),
        ('TOPPADDING',    (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN',         (1, 0), (-1, -1), 'CENTER'),
        ('GRID',          (0, 0), (-1, -1), 0.3, COLOR_LIGHT_GREY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    items.append(tbl)
    items.append(Spacer(1, 4))

    # En çok / en az sevdiğim — 2 sütun
    col2 = (PAGE_W - 0.3 * cm) / 2

    sol = _inner([
        Paragraph('<b>En çok sevdiğim etkinlik:</b>', MINI_BOLD_ST),
        WritingLines(num_lines=1, line_spacing=13),
        Spacer(1, 2),
        Paragraph('<b>Neden?</b>', MINI_BOLD_ST),
        WritingLines(num_lines=1, line_spacing=13),
    ], col2 - 0.15 * cm)

    sag = _inner([
        Paragraph('<b>En az sevdiğim etkinlik:</b>', MINI_BOLD_ST),
        WritingLines(num_lines=1, line_spacing=13),
        Spacer(1, 2),
        Paragraph('<b>Neden?</b>', MINI_BOLD_ST),
        WritingLines(num_lines=1, line_spacing=13),
    ], col2 - 0.15 * cm)

    enc = Table(
        [[sol, Spacer(0.3 * cm, 1), sag]],
        colWidths=[col2 + 0.15 * cm, 0.3 * cm, col2 + 0.15 * cm],
    )
    enc.setStyle(TableStyle([
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING',   (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        ('LINEAFTER',    (0, 0), (0, -1), 0.4, COLOR_LIGHT_GREY),
    ]))
    items.append(enc)
    return items


# ── Ana üretim fonksiyonu ────────────────────────────────────────

def build(output_path=None):
    out = output_path or _DEFAULT_OUTPUT
    doc = create_doc(out, title=DOC_TITLE, unite_info=UNITE_INFO)
    elems = []

    for el in header_block():
        elems.append(el)
    elems.append(Spacer(1, 3))
    elems.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elems.append(Spacer(1, 4))

    elems.append(sol_sag_bolumler())
    elems.append(Spacer(1, 6))

    for el in bolum2():
        elems.append(el)

    doc.build(elems, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return out


if __name__ == '__main__':
    result = build()
    print(f'PDF olusturuldu: {result}')
