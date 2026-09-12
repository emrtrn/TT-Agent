"""
PDF Stil Modülü — Teknoloji ve Tasarım Öğretim Programı
Ortak tasarım, Türkçe karakter desteği, koyu turuncu tema
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, Color, black, white, grey
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Flowable
)

# ============================================================
# FONT KAYITLARI - Türkçe karakter desteği için DejaVu Sans
# ============================================================

def register_fonts():
    """Türkçe karakter destekli fontları kaydet"""
    import os
    _here = os.path.dirname(os.path.abspath(__file__))
    _local = os.path.join(_here, 'fonts')
    _linux = '/usr/share/fonts/truetype/dejavu'
    _font_dir = _local if os.path.isfile(os.path.join(_local, 'DejaVuSans.ttf')) else _linux

    pdfmetrics.registerFont(TTFont('TR-Regular',    os.path.join(_font_dir, 'DejaVuSans.ttf')))
    pdfmetrics.registerFont(TTFont('TR-Bold',       os.path.join(_font_dir, 'DejaVuSans-Bold.ttf')))
    pdfmetrics.registerFont(TTFont('TR-Italic',     os.path.join(_font_dir, 'DejaVuSans-Oblique.ttf')))
    pdfmetrics.registerFont(TTFont('TR-BoldItalic', os.path.join(_font_dir, 'DejaVuSans-BoldOblique.ttf')))
    pdfmetrics.registerFont(TTFont('TR-Mono',       os.path.join(_font_dir, 'DejaVuSansMono.ttf')))

    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily('TR-Regular',
                       normal='TR-Regular',
                       bold='TR-Bold',
                       italic='TR-Italic',
                       boldItalic='TR-BoldItalic')

# ============================================================
# RENK PALETİ - Koyu turuncu tema
# ============================================================

COLOR_PRIMARY = HexColor('#C2410C')      # Koyu turuncu (başlıklar)
COLOR_SECONDARY = HexColor('#9A3412')    # Daha koyu turuncu (vurgu)
COLOR_ACCENT = HexColor('#EA580C')       # Orta turuncu (alt başlıklar)
COLOR_LIGHT = HexColor('#FED7AA')        # Açık turuncu (tablo arka plan)
COLOR_VERY_LIGHT = HexColor('#FFF7ED')   # Çok açık turuncu (kapak arka plan)

COLOR_TEXT = HexColor('#1F2937')         # Koyu gri (ana metin)
COLOR_MUTED = HexColor('#6B7280')        # Orta gri (yardımcı metin)
COLOR_LIGHT_GREY = HexColor('#E5E7EB')   # Açık gri (çerçeveler)
COLOR_VERY_LIGHT_GREY = HexColor('#F9FAFB')  # Çok açık gri (arka plan şeritleri)

# Öğrenci çalışma alanı çizgisi için (çıktıda silik görünecek)
COLOR_WRITING_LINE = HexColor('#D1D5DB')

# ============================================================
# PARAGRAF STİLLERİ
# ============================================================

def get_styles():
    """Tüm paragraf stillerini döndür"""
    styles = {}
    
    styles['Title'] = ParagraphStyle('Title', fontName='TR-Bold', fontSize=22,
        textColor=COLOR_PRIMARY, alignment=TA_LEFT, spaceAfter=6, leading=26)
    
    styles['Subtitle'] = ParagraphStyle('Subtitle', fontName='TR-Regular', fontSize=13,
        textColor=COLOR_MUTED, alignment=TA_LEFT, spaceAfter=16, leading=16)
    
    styles['Heading1'] = ParagraphStyle('Heading1', fontName='TR-Bold', fontSize=16,
        textColor=COLOR_PRIMARY, alignment=TA_LEFT, spaceAfter=8, spaceBefore=14, leading=20)
    
    styles['Heading2'] = ParagraphStyle('Heading2', fontName='TR-Bold', fontSize=13,
        textColor=COLOR_SECONDARY, alignment=TA_LEFT, spaceAfter=6, spaceBefore=10, leading=16)
    
    styles['Heading3'] = ParagraphStyle('Heading3', fontName='TR-Bold', fontSize=11,
        textColor=COLOR_ACCENT, alignment=TA_LEFT, spaceAfter=4, spaceBefore=6, leading=14)
    
    styles['Body'] = ParagraphStyle('Body', fontName='TR-Regular', fontSize=9,
        textColor=COLOR_TEXT, alignment=TA_JUSTIFY, spaceAfter=3, leading=12)

    styles['BodyCompact'] = ParagraphStyle('BodyCompact', fontName='TR-Regular', fontSize=9,
        textColor=COLOR_TEXT, alignment=TA_LEFT, spaceAfter=2, leading=11)

    styles['Bullet'] = ParagraphStyle('Bullet', fontName='TR-Regular', fontSize=9,
        textColor=COLOR_TEXT, alignment=TA_LEFT, spaceAfter=3, leading=12,
        leftIndent=14, bulletIndent=4)

    styles['Note'] = ParagraphStyle('Note', fontName='TR-Italic', fontSize=8,
        textColor=COLOR_MUTED, alignment=TA_LEFT, spaceAfter=3, leading=11,
        leftIndent=8, rightIndent=8)
    
    styles['Highlight'] = ParagraphStyle('Highlight', fontName='TR-Bold', fontSize=10,
        textColor=COLOR_SECONDARY, alignment=TA_LEFT, spaceAfter=6, leading=14)
    
    styles['CoverTitle'] = ParagraphStyle('CoverTitle', fontName='TR-Bold', fontSize=28,
        textColor=COLOR_PRIMARY, alignment=TA_CENTER, spaceAfter=12, leading=34)
    
    styles['CoverSubtitle'] = ParagraphStyle('CoverSubtitle', fontName='TR-Regular', fontSize=16,
        textColor=COLOR_TEXT, alignment=TA_CENTER, spaceAfter=24, leading=20)
    
    styles['CoverMeta'] = ParagraphStyle('CoverMeta', fontName='TR-Regular', fontSize=12,
        textColor=COLOR_MUTED, alignment=TA_CENTER, spaceAfter=8, leading=16)
    
    styles['FormLabel'] = ParagraphStyle('FormLabel', fontName='TR-Bold', fontSize=10,
        textColor=COLOR_TEXT, alignment=TA_LEFT, spaceAfter=2, leading=13)
    
    styles['Yonerge'] = ParagraphStyle('Yonerge', fontName='TR-Regular', fontSize=10,
        textColor=COLOR_TEXT, alignment=TA_LEFT, spaceAfter=8, leading=14,
        leftIndent=8, rightIndent=8, backColor=COLOR_VERY_LIGHT, borderPadding=8)
    
    return styles

# ============================================================
# TABLO STİLLERİ
# ============================================================

def table_header_style_compact(font_size=8):
    """Ders planı tabloları için sıkıştırılmış stil"""
    return TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'TR-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), font_size),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, 0), 4),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
        ('FONTNAME', (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE', (0, 1), (-1, -1), font_size),
        ('TEXTCOLOR', (0, 1), (-1, -1), COLOR_TEXT),
        ('VALIGN', (0, 1), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 1), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('LINEBELOW', (0, 0), (-1, 0), 1.5, COLOR_SECONDARY),
    ])


def table_header_style(font_size=10):
    """Başlık satırı olan tablolar için standart stil"""
    return TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'TR-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), font_size),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'TR-Regular'),
        ('FONTSIZE', (0, 1), (-1, -1), font_size),
        ('TEXTCOLOR', (0, 1), (-1, -1), COLOR_TEXT),
        ('VALIGN', (0, 1), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, COLOR_VERY_LIGHT_GREY]),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_LIGHT_GREY),
        ('LINEBELOW', (0, 0), (-1, 0), 1.5, COLOR_SECONDARY),
    ])

# ============================================================
# ÖZEL FLOWABLES
# ============================================================

class WritingLines(Flowable):
    """Birden fazla yazı çizgisi (öğrenci uzun cevaplar için)"""
    def __init__(self, num_lines=3, line_spacing=20, width=None):
        Flowable.__init__(self)
        self.num_lines = num_lines
        self.line_spacing = line_spacing
        self.width = width
        self.height = num_lines * line_spacing
    
    def draw(self):
        self.canv.setStrokeColor(COLOR_WRITING_LINE)
        self.canv.setLineWidth(0.5)
        w = self.width or (A4[0] - 4*cm)
        for i in range(self.num_lines):
            y = self.height - (i + 1) * self.line_spacing
            self.canv.line(0, y, w, y)
    
    def wrap(self, availWidth, availHeight):
        if self.width is None:
            self.width = availWidth
        return (self.width, self.height)


class HorizontalLine(Flowable):
    """Dekoratif yatay çizgi (bölüm ayırıcı)"""
    def __init__(self, width=None, color=None, thickness=1):
        Flowable.__init__(self)
        self.width = width
        self.color = color or COLOR_ACCENT
        self.thickness = thickness
        self.height = thickness + 4
    
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        w = self.width or (A4[0] - 4*cm)
        self.canv.line(0, 2, w, 2)
    
    def wrap(self, availWidth, availHeight):
        if self.width is None:
            self.width = availWidth
        return (self.width, self.height)


class Checkbox(Flowable):
    """Tek bir onay kutusu"""
    def __init__(self, size=10):
        Flowable.__init__(self)
        self.size = size
        self.height = size + 2
        self.width = size + 2
    
    def draw(self):
        self.canv.setStrokeColor(COLOR_TEXT)
        self.canv.setLineWidth(0.8)
        self.canv.rect(1, 1, self.size, self.size, stroke=1, fill=0)
    
    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)


class MindMapCanvas(Flowable):
    """Zihin haritası: merkez kelime + 8 dal"""
    def __init__(self, center_word, width=None, height=9*cm, num_branches=8):
        Flowable.__init__(self)
        self.center_word = center_word
        self.width = width
        self.height = height
        self.num_branches = num_branches
    
    def draw(self):
        from math import cos, sin, pi
        
        w = self.width or (A4[0] - 4*cm)
        h = self.height
        cx = w / 2
        cy = h / 2
        
        # Merkez kutu
        box_w = 4*cm
        box_h = 1.2*cm
        self.canv.setFillColor(COLOR_LIGHT)
        self.canv.setStrokeColor(COLOR_PRIMARY)
        self.canv.setLineWidth(1.5)
        self.canv.roundRect(cx - box_w/2, cy - box_h/2, box_w, box_h, 8, stroke=1, fill=1)
        
        # Merkez kelime
        self.canv.setFillColor(COLOR_PRIMARY)
        self.canv.setFont('TR-Bold', 14)
        self.canv.drawCentredString(cx, cy - 4, self.center_word)
        
        # Dallar
        self.canv.setStrokeColor(COLOR_WRITING_LINE)
        self.canv.setLineWidth(0.6)
        
        branch_len = 3.2*cm
        angles = [i * (2 * pi / self.num_branches) for i in range(self.num_branches)]
        
        for angle in angles:
            start_dist = box_w/2 * abs(cos(angle)) + box_h/2 * abs(sin(angle)) + 4
            sx = cx + start_dist * cos(angle)
            sy = cy + start_dist * sin(angle)
            
            mid_x = cx + (start_dist + branch_len * 0.7) * cos(angle)
            mid_y = cy + (start_dist + branch_len * 0.7) * sin(angle)
            
            line_len = 2.5*cm
            if cos(angle) >= 0:
                end_x = mid_x + line_len
            else:
                end_x = mid_x - line_len
            
            self.canv.line(sx, sy, mid_x, mid_y)
            self.canv.line(mid_x, mid_y, end_x, mid_y)
    
    def wrap(self, availWidth, availHeight):
        if self.width is None:
            self.width = availWidth
        return (self.width, self.height)


class VennDiagram(Flowable):
    """İki örtüşen Venn dairesi"""
    def __init__(self, width=None, height=9*cm, label1='Ürün 1', label2='Ürün 2'):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.label1 = label1
        self.label2 = label2
    
    def draw(self):
        w = self.width or (A4[0] - 4*cm)
        h = self.height
        
        radius = min(w * 0.28, h * 0.42)
        overlap = radius * 0.55
        cx1 = w / 2 - radius + overlap
        cx2 = w / 2 + radius - overlap
        cy = h / 2
        
        self.canv.setStrokeColor(COLOR_PRIMARY)
        self.canv.setLineWidth(1.5)
        self.canv.setFillColor(Color(1, 0.95, 0.9, alpha=0.3))
        self.canv.circle(cx1, cy, radius, stroke=1, fill=1)
        
        self.canv.setStrokeColor(COLOR_ACCENT)
        self.canv.setFillColor(Color(1, 0.88, 0.82, alpha=0.3))
        self.canv.circle(cx2, cy, radius, stroke=1, fill=1)
        
        self.canv.setFillColor(COLOR_PRIMARY)
        self.canv.setFont('TR-Bold', 11)
        self.canv.drawCentredString(cx1 - radius*0.4, cy + radius + 8, self.label1 + "'e Özgü")
        self.canv.setFillColor(COLOR_ACCENT)
        self.canv.drawCentredString(cx2 + radius*0.4, cy + radius + 8, self.label2 + "'ye Özgü")
        self.canv.setFillColor(COLOR_SECONDARY)
        self.canv.drawCentredString((cx1 + cx2) / 2, cy + radius*0.7, "ORTAK")
    
    def wrap(self, availWidth, availHeight):
        if self.width is None:
            self.width = availWidth
        return (self.width, self.height)


class DrawingBox(Flowable):
    """Öğrenci çizim alanı"""
    def __init__(self, width=None, height=5*cm, caption=None):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.caption = caption
    
    def draw(self):
        w = self.width or (A4[0] - 4*cm)
        h = self.height
        
        self.canv.setStrokeColor(COLOR_WRITING_LINE)
        self.canv.setLineWidth(0.8)
        self.canv.setFillColor(white)
        self.canv.rect(0, 0, w, h, stroke=1, fill=0)
        
        if self.caption:
            self.canv.setFont('TR-Italic', 8)
            self.canv.setFillColor(COLOR_MUTED)
            self.canv.drawCentredString(w/2, h/2, self.caption)
    
    def wrap(self, availWidth, availHeight):
        if self.width is None:
            self.width = availWidth
        return (self.width, self.height)


# ============================================================
# SAYFA NUMARASI VE ALTBİLGİ
# ============================================================

def add_page_number(canvas, doc):
    """Her sayfanın alt kısmına sayfa numarası, üst-alt bant"""
    canvas.saveState()
    
    # Üst bant
    canvas.setStrokeColor(COLOR_ACCENT)
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, A4[1] - 1.3*cm, A4[0] - 2*cm, A4[1] - 1.3*cm)
    
    # Üst sağ: doküman başlığı
    if hasattr(doc, 'doc_title'):
        canvas.setFont('TR-Regular', 8)
        canvas.setFillColor(COLOR_MUTED)
        canvas.drawRightString(A4[0] - 2*cm, A4[1] - 1*cm, doc.doc_title)
    
    # Üst sol: ünite bilgisi
    canvas.setFont('TR-Regular', 8)
    canvas.setFillColor(COLOR_MUTED)
    unite_info = getattr(doc, 'unite_info', 'Teknoloji ve Tasarım')
    canvas.drawString(2*cm, A4[1] - 1*cm, unite_info)
    
    # Alt bant
    canvas.setStrokeColor(COLOR_LIGHT_GREY)
    canvas.setLineWidth(0.3)
    canvas.line(2*cm, 1.3*cm, A4[0] - 2*cm, 1.3*cm)
    
    # Alt sağ: sayfa numarası
    canvas.setFont('TR-Regular', 9)
    canvas.setFillColor(COLOR_MUTED)
    canvas.drawRightString(A4[0] - 2*cm, 1*cm, f"Sayfa {doc.page}")
    
    # Alt sol: Türkiye Yüzyılı Maarif Modeli
    canvas.setFont('TR-Italic', 8)
    canvas.drawString(2*cm, 1*cm, 'Türkiye Yüzyılı Maarif Modeli')
    
    canvas.restoreState()


# ============================================================
# DOKUMAN ŞABLONU
# ============================================================

def create_doc(filename, title="Doküman", unite_info=None):
    """Standart bir A4 doküman oluştur"""
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        topMargin=1.8*cm,
        bottomMargin=1.8*cm,
        leftMargin=2*cm,
        rightMargin=2*cm,
        title=title,
        author='Teknoloji ve Tasarım Öğretim Programı',
    )
    doc.doc_title = title
    if unite_info:
        doc.unite_info = unite_info
    return doc


# ============================================================
# KAPAK SAYFASI
# ============================================================

def make_cover(title, subtitle, meta_info, document_type="Öğretmen Rehberi"):
    """Kapak sayfası oluştur"""
    styles = get_styles()
    elements = []
    
    elements.append(Spacer(1, 3*cm))
    
    label_style = ParagraphStyle('Label', fontName='TR-Bold', fontSize=11,
        textColor=COLOR_ACCENT, alignment=TA_CENTER, spaceAfter=8)
    elements.append(Paragraph(document_type.upper(), label_style))
    
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph(title, styles['CoverTitle']))
    
    if subtitle:
        elements.append(Paragraph(subtitle, styles['CoverSubtitle']))
    
    elements.append(Spacer(1, 1.5*cm))
    elements.append(HorizontalLine(width=5*cm, color=COLOR_ACCENT, thickness=2))
    elements.append(Spacer(1, 1.5*cm))
    
    if meta_info:
        for key, value in meta_info.items():
            meta_text = f"<b>{key}:</b>  {value}"
            elements.append(Paragraph(meta_text, styles['CoverMeta']))
    
    elements.append(Spacer(1, 3*cm))
    
    footer_style = ParagraphStyle('CoverFooter', fontName='TR-Italic', fontSize=10,
        textColor=COLOR_MUTED, alignment=TA_CENTER)
    elements.append(Paragraph("Türkiye Yüzyılı Maarif Modeli", footer_style))
    elements.append(Paragraph("Teknoloji ve Tasarım Dersi", footer_style))
    sinif = str(meta_info.get("Sınıf", "")).strip()
    sinif_etiketi = f"{sinif}. Sınıf" if sinif.isdigit() else sinif
    if sinif_etiketi:
        elements.append(Paragraph(f"{sinif_etiketi} Öğretim Programı", footer_style))
    
    elements.append(PageBreak())
    
    return elements


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def make_student_info_header():
    """Öğrenci için Ad-Soyad / Sınıf / Tarih alanı"""
    styles = get_styles()
    
    data = [[
        Paragraph('<b>Adı Soyadı:</b>', styles['FormLabel']),
        '',
        Paragraph('<b>Sınıf/No:</b>', styles['FormLabel']),
        '',
        Paragraph('<b>Tarih:</b>', styles['FormLabel']),
        '',
    ]]
    
    table = Table(data, colWidths=[2.7*cm, 5.1*cm, 2*cm, 2.8*cm, 1.5*cm, 2.9*cm])
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LINEBELOW', (1, 0), (1, 0), 0.8, COLOR_WRITING_LINE),
        ('LINEBELOW', (3, 0), (3, 0), 0.8, COLOR_WRITING_LINE),
        ('LINEBELOW', (5, 0), (5, 0), 0.8, COLOR_WRITING_LINE),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return table


def section_title(text, level=1):
    """Bölüm başlığı oluştur"""
    styles = get_styles()
    if level == 1:
        return Paragraph(text, styles['Heading1'])
    elif level == 2:
        return Paragraph(text, styles['Heading2'])
    else:
        return Paragraph(text, styles['Heading3'])


def yonerge_box(text):
    """Yönerge kutusu (açık turuncu arka planlı)"""
    styles = get_styles()
    return Paragraph(text, styles['Yonerge'])


# İlk yükleme
register_fonts()
