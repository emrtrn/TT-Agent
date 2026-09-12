"""
15 — Çalışma Kâğıdı 8: Öz Değerlendirme
Tek sayfa, 4. ve 5. sorular yok.

Kullanım:
    python pdf_uretim/uret_15_oz_degerlendirme.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_style import (
    create_doc, get_styles, add_page_number,
    make_student_info_header, HorizontalLine, WritingLines,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT,
    COLOR_LIGHT, COLOR_VERY_LIGHT, COLOR_LIGHT_GREY,
    COLOR_TEXT, COLOR_MUTED, COLOR_WRITING_LINE,
    A4, cm,
)
from reportlab.platypus import (
    Paragraph, Spacer, Table, TableStyle, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import white

OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'units', 'unit1', '15_Calisma_Kagidi_8_Oz_Degerlendirme.pdf'
)

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 1. Ünite'
DOC_TITLE  = 'Çalışma Kâğıdı 8 — Öz Değerlendirme'

PAGE_W = A4[0] - 4 * cm


def build():
    doc = create_doc(OUTPUT_PATH, title=DOC_TITLE, unite_info=UNITE_INFO)
    styles = get_styles()
    elements = []

    # ── Öğrenci bilgi satırı ──
    elements.append(make_student_info_header())
    elements.append(Spacer(1, 3))
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 5))

    # ── Başlık ──
    elements.append(Paragraph(DOC_TITLE, styles['Heading1']))

    # ── Yönerge ──
    yonerge_st = ParagraphStyle(
        'Yonerge', fontName='TR-Regular', fontSize=9,
        textColor=COLOR_TEXT, leading=13,
        backColor=COLOR_VERY_LIGHT, borderPadding=6,
        leftIndent=6, rightIndent=6, spaceAfter=6,
    )
    elements.append(Paragraph(
        'Bu ünite boyunca kendini nasıl gördüğünü dürüstçe yaz. '
        'Bu form notla ölçülmez — amaç öğrenme yolculuğunu fark etmek.',
        yonerge_st
    ))
    elements.append(Spacer(1, 4))

    # ── Derecelendirme tablosu ──
    elements.append(Paragraph(
        'Ünite Boyunca Kendimi Nasıl Değerlendiriyorum?',
        styles['Heading2']
    ))

    alt_st = ParagraphStyle('AltYonerge', fontName='TR-Italic', fontSize=8,
                            textColor=COLOR_MUTED, leading=11, spaceAfter=4)
    elements.append(Paragraph('Her madde için 1–5 arası puan ver. (1 = Hiç, 5 = Çok iyi)', alt_st))

    hdr_st = ParagraphStyle('TblHdr', fontName='TR-Bold', fontSize=8.5,
                            textColor=white, leading=11, alignment=TA_CENTER)
    cel_st = ParagraphStyle('TblCel', fontName='TR-Regular', fontSize=8.5,
                            textColor=COLOR_TEXT, leading=11)
    ctr_st = ParagraphStyle('TblCtr', fontName='TR-Regular', fontSize=8.5,
                            textColor=COLOR_TEXT, leading=11, alignment=TA_CENTER)

    maddeler = [
        'Kavramları anladım',
        'Grup çalışmalarına katıldım',
        'Sorular sordum',
        'Araştırma yaptım',
        'Kaynakları değerlendirdim',
        'Kendi fikrimi oluşturdum',
        'Arkadaşlarımı dinledim',
        'Görevlerimi zamanında tamamladım',
    ]

    col_w = [PAGE_W - 5 * 1.2 * cm] + [1.2 * cm] * 5
    tbl_data = [[
        Paragraph('Öğrenme Alanı', hdr_st),
        Paragraph('1', hdr_st), Paragraph('2', hdr_st),
        Paragraph('3', hdr_st), Paragraph('4', hdr_st),
        Paragraph('5', hdr_st),
    ]]
    for m in maddeler:
        tbl_data.append([Paragraph(m, cel_st), '', '', '', '', ''])

    tbl = Table(tbl_data, colWidths=col_w,
                rowHeights=[0.55 * cm] + [0.6 * cm] * len(maddeler))
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
        ('TEXTCOLOR',     (0, 0), (-1, 0),  white),
        ('FONTNAME',      (0, 0), (-1, 0),  'TR-Bold'),
        ('ALIGN',         (1, 0), (-1, -1), 'CENTER'),
        ('VALIGN',        (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('GRID',          (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('LINEBELOW',     (0, 0), (-1, 0),  1.5, COLOR_SECONDARY),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [white, COLOR_VERY_LIGHT]),
    ]))
    elements.append(tbl)
    elements.append(Spacer(1, 8))

    # ── Kendime Sorular ──
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph('Kendime Sorular', styles['Heading2']))

    soru_st = ParagraphStyle('Soru', fontName='TR-Bold', fontSize=9,
                             textColor=COLOR_TEXT, leading=13, spaceAfter=2)
    sorular = [
        '1. Bu ünitede en çok ne öğrendim?',
        '2. En zor gelen konu / etkinlik hangisiydi? Neden?',
        '3. En çok hangi etkinlikten keyif aldım?',
    ]
    for soru in sorular:
        elements.append(KeepTogether([
            Paragraph(soru, soru_st),
            WritingLines(num_lines=2, line_spacing=16),
            Spacer(1, 5),
        ]))

    # ── Kendime Verdiğim Not ──
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 5))
    not_st = ParagraphStyle('NotSt', fontName='TR-Regular', fontSize=9,
                            textColor=COLOR_TEXT, leading=13)
    elements.append(Paragraph(
        '<b>Kendime Verdiğim Not:</b> '
        'Bu ünitedeki çalışmalarımı genel olarak _______ / 10 olarak değerlendiriyorum.',
        not_st
    ))
    elements.append(Spacer(1, 6))

    # ── Öğretmenime Mesajım ──
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph('Öğretmenime Mesajım', styles['Heading2']))
    mesaj_st = ParagraphStyle('MesajSt', fontName='TR-Italic', fontSize=8,
                              textColor=COLOR_MUTED, leading=11, spaceAfter=3)
    elements.append(Paragraph(
        '(Bu bölümü doldurmak isteğe bağlıdır. Öğretmene bir mesaj, soru veya öneri yazabilirsin.)',
        mesaj_st
    ))
    elements.append(WritingLines(num_lines=2, line_spacing=16))

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF olusturuldu: {OUTPUT_PATH}')


if __name__ == '__main__':
    build()
