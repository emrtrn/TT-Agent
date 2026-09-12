"""
Markdown → PDF dönüştürücü yardımcı fonksiyonları
Markdown elementlerini reportlab flowables'a çevirir
Emoji temizleme, tablo desteği, başlık ve liste işleme dahil.
"""

import re
import sys
import os

# Bu dosya import edildiğinde pdf_style aynı klasörden gelir
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_style import *
from reportlab.platypus import KeepTogether


# DejaVu Sans'ın desteklemediği dekoratif emojileri kaldır
UNSUPPORTED_EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F9FF"  # Geniş emoji aralığı
    "\U0001FA00-\U0001FAFF"
    "\U00002600-\U000026FF"  # Çeşitli semboller
    "\U00002700-\U000027BF"  # Dingbats
    "\U0001F000-\U0001F2FF"
    "]+",
    flags=re.UNICODE
)


def clean_emojis(text):
    """Desteklenmeyen emojileri kaldır, etrafındaki boşlukları normalize et"""
    cleaned = UNSUPPORTED_EMOJI_PATTERN.sub('', text)
    cleaned = re.sub(r'  +', ' ', cleaned)
    cleaned = re.sub(r'^ +(?=#)', '', cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r'(#+)\s+([—\-•])\s*', r'\1 ', cleaned)
    cleaned = re.sub(r'^\s*—\s*', '', cleaned, flags=re.MULTILINE)
    return cleaned


def md_inline_to_rl(text):
    """Markdown inline stilleri (bold, italic, code) reportlab XML'e çevir"""
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'`([^`]+?)`', r'<font name="TR-Mono" size="9" color="#9A3412">\1</font>', text)
    text = re.sub(r'~~(.+?)~~', r'<strike>\1</strike>', text)
    
    return text


def process_md_line(line, styles):
    """Tek bir markdown satırını işleyip uygun flowable döndür"""
    stripped = line.rstrip()
    
    if not stripped.strip():
        return None
    
    if stripped.strip() in ('---', '***', '___'):
        return HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5)
    
    if stripped.startswith('# '):
        return Paragraph(md_inline_to_rl(stripped[2:]), styles['Title'])
    if stripped.startswith('## '):
        return Paragraph(md_inline_to_rl(stripped[3:]), styles['Heading1'])
    if stripped.startswith('### '):
        return Paragraph(md_inline_to_rl(stripped[4:]), styles['Heading2'])
    if stripped.startswith('#### '):
        return Paragraph(md_inline_to_rl(stripped[5:]), styles['Heading3'])
    
    if stripped.startswith('> '):
        content = stripped[2:]
        return Paragraph(md_inline_to_rl(content), styles['Note'])
    
    m = re.match(r'^[\s]*[-*•]\s+(.+)$', stripped)
    if m:
        return Paragraph('• ' + md_inline_to_rl(m.group(1)), styles['Bullet'])
    
    m = re.match(r'^[\s]*(\d+)\.\s+(.+)$', stripped)
    if m:
        return Paragraph(f"{m.group(1)}. " + md_inline_to_rl(m.group(2)), styles['Bullet'])
    
    return Paragraph(md_inline_to_rl(stripped), styles['Body'])


def parse_md_table(lines, start_idx):
    """Markdown tablosunu parse et, (rows, yeni_idx) döndür"""
    header = [c.strip() for c in lines[start_idx].strip().strip('|').split('|')]
    idx = start_idx + 2
    
    rows = [header]
    while idx < len(lines):
        line = lines[idx].strip()
        if not line.startswith('|'):
            break
        row = [c.strip() for c in line.strip('|').split('|')]
        row_clean = [md_inline_to_rl(cell) for cell in row]
        rows.append(row_clean)
        idx += 1
    
    return rows, idx


def md_to_flowables(md_content, styles=None, skip_top_title=False, compact_mode=False):
    """Markdown içeriğini reportlab flowables listesine çevir"""
    if styles is None:
        styles = get_styles()

    if compact_mode:
        styles['Heading1'] = ParagraphStyle('Heading1', fontName='TR-Bold', fontSize=14,
            textColor=COLOR_PRIMARY, alignment=TA_LEFT, spaceAfter=4, spaceBefore=8, leading=17)
        styles['Heading2'] = ParagraphStyle('Heading2', fontName='TR-Bold', fontSize=12,
            textColor=COLOR_SECONDARY, alignment=TA_LEFT, spaceAfter=3, spaceBefore=5, leading=15)
        styles['Heading3'] = ParagraphStyle('Heading3', fontName='TR-Bold', fontSize=10,
            textColor=COLOR_ACCENT, alignment=TA_LEFT, spaceAfter=3, spaceBefore=4, leading=13)
        styles['Body'] = ParagraphStyle('Body', fontName='TR-Regular', fontSize=9,
            textColor=COLOR_TEXT, alignment=TA_JUSTIFY, spaceAfter=2, leading=11)
        styles['Bullet'] = ParagraphStyle('Bullet', fontName='TR-Regular', fontSize=9,
            textColor=COLOR_TEXT, alignment=TA_LEFT, spaceAfter=2, leading=11,
            leftIndent=14, bulletIndent=4)
        styles['Note'] = ParagraphStyle('Note', fontName='TR-Italic', fontSize=8,
            textColor=COLOR_MUTED, alignment=TA_LEFT, spaceAfter=2, leading=10,
            leftIndent=8, rightIndent=8)

    flowables = []
    lines = md_content.split('\n')
    i = 0
    skipped_first_title = False
    in_code_block = False
    code_lines = []
    
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        
        # Sayfa sonu işaretçisi
        if stripped.strip() == '<!-- PAGEBREAK -->':
            flowables.append(PageBreak())
            i += 1
            continue

        # Code block
        if stripped.startswith('```'):
            if in_code_block:
                code_text = '\n'.join(code_lines)
                code_para = Paragraph(
                    f'<font name="TR-Mono" size="8">{code_text}</font>',
                    ParagraphStyle('Code', fontName='TR-Mono', fontSize=8,
                        textColor=COLOR_TEXT, leftIndent=10, rightIndent=10,
                        backColor=COLOR_VERY_LIGHT_GREY, borderPadding=6, leading=11)
                )
                flowables.append(code_para)
                flowables.append(Spacer(1, 4))
                in_code_block = False
                code_lines = []
            else:
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            code_lines.append(line)
            i += 1
            continue
        
        # Tablo
        if stripped.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1].strip()):
            rows, new_i = parse_md_table(lines, i)
            if rows and len(rows) > 1:
                n_cols = len(rows[0])
                avail_width = A4[0] - 4*cm
                # "Süre" sütunu varsa (2. kolon) onu daralt, geri kalanı içeriğe ver
                is_sure_table = n_cols == 3 and rows[0][1] == 'Süre'
                if is_sure_table:
                    col_widths = [3.8*cm, 1.4*cm, avail_width - 3.8*cm - 1.4*cm]
                    cell_fs = 8
                    cell_leading = 11
                else:
                    col_widths = [avail_width / n_cols] * n_cols
                    cell_fs = 9
                    cell_leading = 12

                if compact_mode:
                    cell_fs = 8
                    cell_leading = 10

                table_data = []
                for r_idx, row in enumerate(rows):
                    new_row = []
                    for cell in row:
                        # <br> etiketini self-closing yap
                        cell_fixed = cell.replace('<br>', '<br/>').replace('<BR>', '<br/>')
                        if r_idx == 0:
                            p = Paragraph(cell_fixed, ParagraphStyle('TH',
                                fontName='TR-Bold', fontSize=cell_fs, textColor=white,
                                alignment=TA_CENTER, leading=cell_leading))
                        else:
                            p = Paragraph(cell_fixed, ParagraphStyle('TD',
                                fontName='TR-Regular', fontSize=cell_fs, textColor=COLOR_TEXT,
                                alignment=TA_LEFT, leading=cell_leading))
                        new_row.append(p)
                    table_data.append(new_row)

                t = Table(table_data, colWidths=col_widths, repeatRows=1)
                if is_sure_table or compact_mode:
                    t.setStyle(table_header_style_compact(font_size=cell_fs))
                else:
                    t.setStyle(table_header_style(font_size=9))
                flowables.append(t)
                flowables.append(Spacer(1, 4 if compact_mode else 8))
            i = new_i
            continue
        
        # Üst başlığı atlama mantığı
        if skip_top_title and not skipped_first_title and stripped.startswith('# '):
            skipped_first_title = True
            i += 1
            continue
        
        fl = process_md_line(line, styles)
        if fl is not None:
            flowables.append(fl)
        else:
            flowables.append(Spacer(1, 4))
        
        i += 1
    
    return _group_keep_together(flowables)


def _group_keep_together(flowables):
    """
    Başlık + hemen ardından gelen içerik bloğunu KeepTogether ile sarar.
    Böylece bir başlık sayfanın altında kalıp içeriği bir sonraki sayfaya taşmaz.
    Tablolar da asla iki sayfaya bölünmez.
    """
    result = []
    i = 0
    heading_styles = {'Title', 'Heading1', 'Heading2', 'Heading3'}

    while i < len(flowables):
        fl = flowables[i]

        # Tablo: KeepTogether ile sar (iki sayfaya bölünmesin)
        if isinstance(fl, Table):
            result.append(KeepTogether([fl]))
            i += 1
            continue

        # Başlık: başlık + ardından gelen paragraf/spacer/tablo bloğunu bir arada tut
        is_heading = (
            isinstance(fl, Paragraph)
            and hasattr(fl, 'style')
            and fl.style.name in heading_styles
        )
        if is_heading:
            group = [fl]
            j = i + 1
            # Başlığın hemen ardından gelen en fazla 6 flowable'ı aynı blokta tut
            collected = 0
            while j < len(flowables) and collected < 6:
                nxt = flowables[j]
                # Bir sonraki başlıkla veya PageBreak ile karşılaşınca dur
                if isinstance(nxt, PageBreak):
                    break
                if (isinstance(nxt, Paragraph)
                        and hasattr(nxt, 'style')
                        and nxt.style.name in heading_styles):
                    break
                group.append(nxt)
                j += 1
                collected += 1
            result.append(KeepTogether(group))
            i = j
            continue

        result.append(fl)
        i += 1

    return result


def read_md_file(path):
    """Markdown dosyasını oku"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def build_pdf_from_md(md_content, output_path, title, subtitle=None,
                      meta_info=None, doc_type='Öğretmen Rehberi',
                      add_cover=None, skip_top_title=True, unite_info=None,
                      compact_mode=False):
    """
    Markdown'dan direkt PDF oluştur
    add_cover: None (otomatik 4+ sayfada), True (zorunlu), False (asla)
    compact_mode: Tablo padding, başlık aralıkları ve font boyutunu küçültür
    """
    # Desteklenmeyen emojileri temizle
    md_content = clean_emojis(md_content)

    doc = create_doc(output_path, title=title, unite_info=unite_info)
    styles = get_styles()

    elements = []

    content_flowables = md_to_flowables(md_content, styles, skip_top_title=skip_top_title,
                                        compact_mode=compact_mode)
    
    # Sayfa sayısı tahmini
    content_char_count = len(md_content)
    estimated_pages = max(1, content_char_count // 2500)
    
    if add_cover is True or (add_cover is None and estimated_pages >= 4):
        elements.extend(make_cover(
            title=title,
            subtitle=subtitle or '',
            meta_info=meta_info or {},
            document_type=doc_type,
        ))
    
    elements.extend(content_flowables)
    
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return output_path


def extract_section(md_content, start_marker, end_marker=None):
    """
    Markdown içeriğinden bir bölümü çıkar.
    start_marker: Bölümü başlatan satırın içermesi gereken metin
    end_marker: Bölümü bitiren satırın içermesi gereken metin (None ise sona kadar)
    """
    lines = md_content.split('\n')
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        if start_idx is None and start_marker in line:
            start_idx = i
        elif start_idx is not None and end_marker and end_marker in line:
            end_idx = i
            break
    
    if start_idx is None:
        return ''
    
    if end_idx is None:
        section_lines = lines[start_idx:]
    else:
        section_lines = lines[start_idx:end_idx]
    
    return '\n'.join(section_lines)
