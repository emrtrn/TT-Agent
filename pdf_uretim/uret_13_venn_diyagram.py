"""
Çalışma Kâğıdı 6 — Venn Diyagramı Karşılaştırma
Tek sayfa, Adı Soyadı/Sınıf/Tarih tek satırda.

Kullanım:
    python pdf_uretim/uret_13_venn_diyagram.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from pdf_style import (
    create_doc, get_styles, add_page_number,
    make_student_info_header, HorizontalLine, WritingLines,
    VennDiagram, COLOR_LIGHT_GREY, COLOR_MUTED, COLOR_VERY_LIGHT,
    COLOR_TEXT, COLOR_PRIMARY, COLOR_LIGHT,
    A4, cm,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import white

OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'units', 'unit1', '13_Calisma_Kagidi_6_Venn_Diyagrami.pdf'
)

UNITE_INFO = 'Teknoloji ve Tasarım • 7. Sınıf • 1. Ünite'
DOC_TITLE = 'Çalışma Kâğıdı 6 — Venn Diyagramı Karşılaştırma'


def build():
    doc = create_doc(OUTPUT_PATH, title=DOC_TITLE, unite_info=UNITE_INFO)
    styles = get_styles()
    elements = []

    # Öğrenci bilgi satırı (tek satır: Adı Soyadı / Sınıf/No / Tarih)
    elements.append(make_student_info_header())
    elements.append(Spacer(1, 4))
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 6))

    # Başlık
    elements.append(Paragraph(DOC_TITLE, styles['Heading1']))

    # Yönerge + Süre tek kutuda
    yonerge_style = ParagraphStyle(
        'Yonerge2',
        fontName='TR-Regular', fontSize=9,
        textColor=COLOR_TEXT, leading=13,
        leftIndent=8, rightIndent=8,
        backColor=COLOR_VERY_LIGHT, borderPadding=7,
    )
    elements.append(Paragraph(
        '<b>Yönerge:</b> Bu derste incelenen üç tasarım alanından iki ürün seç. '
        'Aşağıdaki Venn diyagramı üzerinde bu iki ürünü karşılaştır. '
        '&nbsp;&nbsp;<b>Süre: 10 dakika</b>',
        yonerge_style
    ))
    elements.append(Spacer(1, 8))

    # Seçilen ürünler — iki sütunlu kompakt tablo
    elements.append(Paragraph('Seçilen Ürünler', styles['Heading2']))
    elements.append(Spacer(1, 4))

    label_s = ParagraphStyle('UrunLabel', fontName='TR-Bold', fontSize=9,
                             textColor=COLOR_TEXT, leading=12)
    line_s  = ParagraphStyle('UrunLine', fontName='TR-Regular', fontSize=9,
                             textColor=COLOR_TEXT, leading=12)

    avail = A4[0] - 4 * cm
    urun_data = [[
        Paragraph('<b>Ürün 1:</b>', label_s), Paragraph('', line_s),
        Paragraph('<b>Ürün 2:</b>', label_s), Paragraph('', line_s),
    ], [
        Paragraph('<b>Kategorisi:</b>', label_s), Paragraph('', line_s),
        Paragraph('<b>Kategorisi:</b>', label_s), Paragraph('', line_s),
    ]]

    col_w = [2.5 * cm, avail / 2 - 2.5 * cm, 2.5 * cm, avail / 2 - 2.5 * cm]
    urun_table = Table(urun_data, colWidths=col_w)
    urun_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW', (1, 0), (1, 0), 0.8, COLOR_LIGHT_GREY),
        ('LINEBELOW', (3, 0), (3, 0), 0.8, COLOR_LIGHT_GREY),
        ('LINEBELOW', (1, 1), (1, 1), 0.8, COLOR_LIGHT_GREY),
        ('LINEBELOW', (3, 1), (3, 1), 0.8, COLOR_LIGHT_GREY),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    elements.append(urun_table)
    elements.append(Spacer(1, 8))

    # Venn diyagramı
    elements.append(Paragraph('Venn Diyagramı', styles['Heading2']))
    elements.append(Spacer(1, 4))
    elements.append(VennDiagram(height=8.5 * cm, label1='Ürün 1', label2='Ürün 2'))

    # İpucu notu
    ipucu_style = ParagraphStyle('Ipucu', fontName='TR-Italic', fontSize=8,
                                 textColor=COLOR_MUTED, leading=11,
                                 leftIndent=6, spaceAfter=6)
    elements.append(Paragraph(
        '<i>İpucu: Ortak alana yazacağın özellikler, iki tasarım türünün ortak ilkelerini '
        'gösterir (örn. estetik, işlevsellik, denge vb.).</i>',
        ipucu_style
    ))
    elements.append(Spacer(1, 6))

    # Yorumlama soruları
    elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph('Yorumlama Soruları', styles['Heading2']))

    sorular = [
        '1. İki üründe ne gibi beklenmedik ortaklıklar buldun?',
        '2. Ortak alandaki özellikler sana hangi tasarım ilkelerini hatırlatıyor?',
        '3. Farklılık alanındaki özellikler neden farklı? (İşlevleri mi farklı, kullanıcıları mı?)',
    ]
    for soru in sorular:
        elements.append(Paragraph(soru, styles['BodyCompact']))
        elements.append(WritingLines(num_lines=2, line_spacing=16))
        elements.append(Spacer(1, 4))

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF olusturuldu: {OUTPUT_PATH}')


if __name__ == '__main__':
    build()
