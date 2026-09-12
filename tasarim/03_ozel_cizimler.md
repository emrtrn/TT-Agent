# 🖌️ Özel Çizimler ve Flowable'lar

> Markdown'da ASCII sanatla yapılması zor olan görsel öğeler için özel reportlab flowable'ları.

---

## 🎯 Neden Özel Flowable?

Markdown, metin tabanlı bir formattır. Çizim, diyagram, çizgili alan gibi öğeler için **uyumsuzdur**. Önceki denemelerde:

- ASCII zihin haritası → PDF'te okunamadı, öğrenci üzerine yazamadı
- ASCII Venn diyagramı → İki örtüşen daire görünmüyordu
- Metin tabanlı yazı çizgileri → Düzensiz görünüm

**Çözüm:** Markdown'da yer tutucu yaz, PDF üretiminde özel **reportlab Flowable** kullan.

---

## 📋 Mevcut Özel Flowable'lar

### 1. WritingLines — Yazı Çizgileri

**Amaç:** Öğrencinin uzun cevap için yazı yazabileceği hafif gri çizgiler.

**Görünüm:**
```
________________________________________
________________________________________
________________________________________
```

**Parametreler:**
- `num_lines` (int): Kaç çizgi? Varsayılan: 3
- `line_spacing` (int): Çizgiler arası boşluk (pt). Varsayılan: 20
- `width` (float): Genişlik. Varsayılan: sayfa genişliği

**Renk:** Hafif gri (#D1D5DB) — çıktıda silik

**Kullanım:**
```python
from pdf_style import WritingLines

# Standart 3 çizgi
elements.append(WritingLines(num_lines=3))

# Daha fazla satır
elements.append(WritingLines(num_lines=5))

# Daha sık aralık
elements.append(WritingLines(num_lines=4, line_spacing=18))

# Sınırlı genişlik
elements.append(WritingLines(num_lines=2, width=10*cm))
```

**Markdown'da:**
```markdown
[Yazma alanı, 3 satır]
```
PDF üretiminde bu satır algılanıp `WritingLines(num_lines=3)` flowable'a dönüştürülebilir (özel implementasyon gerekir) ya da PDF üretim kodunda direkt eklenebilir.

---

### 2. MindMapCanvas — Zihin Haritası

**Amaç:** Merkez kelimeden 8 dala uzanan, her dalın ucunda yazı çizgisi olan zihin haritası.

**Görünüm:**
```
                 ___________
        \       /
         \     /
   _______\___/_______
  /        ___        \
 /        |TEK|       _\__________
        ../NOL/       
        / |OJİ|
   ____/  |___| \____
        \      \
         \      \
          ___    \___________
```

**Parametreler:**
- `center_word` (str): Merkezde yazılacak kelime
- `width` (float): Genişlik. Varsayılan: sayfa genişliği
- `height` (float): Yükseklik. Varsayılan: 9 cm
- `num_branches` (int): Kaç dal? Varsayılan: 8

**Renkler:**
- Merkez kutu: Koyu turuncu kenar, açık turuncu dolgu
- Merkez metin: Koyu turuncu, Bold 14pt
- Dallar: Hafif gri (yazı çizgisi rengiyle aynı)

**Kullanım:**
```python
from pdf_style import MindMapCanvas

# Standart zihin haritası
elements.append(MindMapCanvas('TEKNOLOJİ', height=8.5*cm))

# Daha az dal
elements.append(MindMapCanvas('TASARIM', height=7*cm, num_branches=6))

# Sınırlı genişlik
elements.append(MindMapCanvas('STEAM', width=14*cm, height=8*cm))
```

---

### 3. VennDiagram — Venn Diyagramı

**Amaç:** İki örtüşen Venn dairesi, etiketlerle birlikte. Öğrenci içine yazı yazabilir.

**Görünüm:**
```
   Ürün 1'e Özgü        Ürün 2'ye Özgü
        ___                  ___
      .'   `.              .'   `.
     /       \  ORTAK     /       \
    |         |    ↓     |         |
     \       / |       | \       /
      `.___.'  |       |  `.___.'
              ←---ORTAK---→
```

**Parametreler:**
- `width` (float): Genişlik. Varsayılan: sayfa genişliği
- `height` (float): Yükseklik. Varsayılan: 9 cm
- `label1` (str): Sol etiket. Varsayılan: 'Ürün 1'
- `label2` (str): Sağ etiket. Varsayılan: 'Ürün 2'

**Renkler:**
- Sol daire: Koyu turuncu kenar, çok açık turuncu yarı saydam dolgu
- Sağ daire: Aksan turuncu kenar, biraz daha koyu yarı saydam dolgu
- Ortak alan: Doğal olarak koyulaşır (iki dolgu üst üste)
- Etiketler: Bold 11pt

**Kullanım:**
```python
from pdf_style import VennDiagram

# Standart
elements.append(VennDiagram(label1='Akıllı Saat', label2='Klasik Saat', height=8*cm))

# Geniş
elements.append(VennDiagram(label1='Mimari', label2='Endüstriyel',
                             width=16*cm, height=10*cm))
```

---

### 4. DrawingBox — Çizim Alanı

**Amaç:** Boş bir kare/dikdörtgen alan. Öğrenci içine çizim yapabilir.

**Görünüm:**
```
┌──────────────────────────────┐
│                              │
│                              │
│      Buraya çizim yap        │
│                              │
│                              │
└──────────────────────────────┘
```

**Parametreler:**
- `width` (float): Genişlik. Varsayılan: sayfa genişliği
- `height` (float): Yükseklik. Varsayılan: 5 cm
- `caption` (str): İç metin (italik, gri). Varsayılan: yok

**Renkler:**
- Kenar: Yazı çizgisi rengi (#D1D5DB) — çıktıda silik
- İç dolgu: Beyaz
- Caption: 8pt İtalik, yardımcı gri

**Kullanım:**
```python
from pdf_style import DrawingBox

# Boş alan
elements.append(DrawingBox(height=6*cm))

# Caption ile
elements.append(DrawingBox(height=8*cm, caption='Buraya tasarımını çiz'))

# Sınırlı boyut
elements.append(DrawingBox(width=10*cm, height=10*cm, caption='Logonun taslağı'))
```

---

### 5. Checkbox — Onay Kutusu

**Amaç:** Tek bir [☐] onay kutusu. Liste maddelerinin yanında kullanılabilir.

**Görünüm:**
```
☐
```

**Parametreler:**
- `size` (int): Boyut (pt). Varsayılan: 10

**Kullanım:**
```python
from pdf_style import Checkbox

# Tek kutucuk
elements.append(Checkbox(size=10))
```

> **Not:** Kontrol listesi yapmak için genelde `[ ]` markdown çevrimini kullan, kütüphane `<strike>` ile yapar.

---

### 6. HorizontalLine — Yatay Çizgi

**Amaç:** Bölüm ayırıcı dekoratif çizgi.

**Görünüm:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Parametreler:**
- `width` (float): Genişlik. Varsayılan: sayfa genişliği
- `color` (Color): Renk. Varsayılan: COLOR_ACCENT (turuncu)
- `thickness` (float): Kalınlık (pt). Varsayılan: 1

**Kullanım:**
```python
from pdf_style import HorizontalLine, COLOR_ACCENT, COLOR_LIGHT_GREY

# Dekoratif (kalın turuncu)
elements.append(HorizontalLine(width=5*cm, color=COLOR_ACCENT, thickness=2))

# Bölüm ayırıcı (ince gri)
elements.append(HorizontalLine(color=COLOR_LIGHT_GREY, thickness=0.5))
```

---

## 🎨 Markdown'dan Özel Flowable'a Geçiş

### Strateji 1: Markdown'da Yer Tutucu, PDF'de Manuel Üretim

Bu yöntem **ÖNERİLEN**. Markdown okunabilir kalır, üretim sırasında özel flowable kullanılır.

**Markdown:**
```markdown
## Çalışma Kâğıdı: Zihin Haritam

> **Yönerge:** İki kavram için zihin haritası çiz.

### TEKNOLOJİ
[Zihin haritası alanı — MindMapCanvas, height=8cm]

### TASARIM
[Zihin haritası alanı — MindMapCanvas, height=8cm]

### Son Soru
Sence bu iki kavram ilişkili mi?

[Yazma alanı, 3 satır]
```

**PDF Üretim:**
```python
# Standart markdown→PDF dönüşümü ile çalışmaz!
# Çünkü "[Zihin haritası alanı]" düz metin olur.

# Bu durumda ÖZEL ÜRETİM yap:
def produce_zihin_haritasi(pdf_path):
    doc = create_doc(pdf_path, title='Zihin Haritam')
    elements = []
    
    elements.append(make_student_info_header())
    elements.append(yonerge_box('<b>Yönerge:</b> ...'))
    
    elements.append(Paragraph('TEKNOLOJİ', styles['Heading2']))
    elements.append(MindMapCanvas('TEKNOLOJİ', height=8*cm))
    
    elements.append(Paragraph('TASARIM', styles['Heading2']))
    elements.append(MindMapCanvas('TASARIM', height=8*cm))
    
    elements.append(Paragraph('Son Soru', styles['Heading2']))
    elements.append(Paragraph('Sence bu iki kavram ilişkili mi?', styles['Body']))
    elements.append(WritingLines(num_lines=3))
    
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
```

### Strateji 2: Otomatik Yer Tutucu Algılama (Gelişmiş)

Markdown'da özel etiketler kullanıp `md_converter.py`'da algılanmasını sağlamak. Bu **şu an mevcut değil**, geliştirilebilir.

**Örnek (gelecek):**
```markdown
{{MIND_MAP center="TEKNOLOJİ" branches=8 height="8cm"}}
{{VENN label1="Mimari" label2="Endüstriyel" height="9cm"}}
{{WRITING_LINES count=5}}
{{DRAWING_BOX height="6cm" caption="Çizim alanı"}}
```

> Bu etiketler **şu an md_converter.py'da yok**. Eğer ihtiyaç duyulursa eklenebilir.

---

## 📐 Boyut ve Yerleşim Önerileri

### Sayfa Üzerinde Yerleşim

A4 sayfa boyutu: 210 × 297 mm (~21 × 30 cm)  
Kenar boşlukları: 2cm yan, 1.8cm üst-alt  
**Kullanılabilir alan:** ~17 × 26 cm

| Flowable | İdeal Boyut | Kullanılabilir Alan Yüzdesi |
|----------|------------|---------------------------|
| MindMapCanvas | 17 cm × 8.5 cm | ~30% (1/3 sayfa) |
| VennDiagram | 17 cm × 7.5 cm | ~25% (1/4 sayfa) |
| DrawingBox (orta) | 10-15 cm × 5-7 cm | ~20-25% |
| WritingLines (5 satır) | tüm genişlik × 10 cm yükseklik | ~38% |

### Bir A4'e Sığacak Birleşim

**Tipik bir öğrenci çalışma kâğıdı:**
```
┌─ Üst bant ─────────────────────────┐
│                                    │
├─ Adı-Soyadı bilgi alanı (1 cm) ────┤
├─ Yönerge kutusu (3 cm) ────────────┤
├─ Ana içerik (15 cm) ───────────────┤
│  • Bir MindMap (8 cm)              │
│  • Yazı çizgileri (5 satır = 10cm) │
│  veya                              │
│  • Soru + WritingLines             │
├─ Yansıtma alanı (2 cm) ────────────┤
├─ Kontrol listesi (1.5 cm) ─────────┤
└─ Alt bant ─────────────────────────┘
```

---

## 🔧 Yeni Bir Flowable Üretmek

Eğer ihtiyaç duyulursa yeni özel flowable'lar ekleyebilirsiniz. Örnek:

```python
from reportlab.platypus import Flowable
from reportlab.lib.units import cm

class TimelineCanvas(Flowable):
    """Tarih şeridi flowable'ı"""
    def __init__(self, events, width=None, height=4*cm):
        Flowable.__init__(self)
        self.events = events  # [(year, label), ...]
        self.width = width
        self.height = height
    
    def draw(self):
        w = self.width or (A4[0] - 4*cm)
        # Yatay çizgi çiz
        self.canv.setStrokeColor(COLOR_PRIMARY)
        self.canv.setLineWidth(2)
        self.canv.line(0, self.height/2, w, self.height/2)
        
        # Olaylar için noktalar ve etiketler
        if self.events:
            step = w / (len(self.events) - 1) if len(self.events) > 1 else w / 2
            for i, (year, label) in enumerate(self.events):
                x = i * step
                # Nokta
                self.canv.setFillColor(COLOR_PRIMARY)
                self.canv.circle(x, self.height/2, 4, stroke=0, fill=1)
                # Yıl
                self.canv.setFont('TR-Bold', 10)
                self.canv.drawCentredString(x, self.height/2 + 12, str(year))
                # Etiket
                self.canv.setFont('TR-Regular', 9)
                self.canv.drawCentredString(x, self.height/2 - 16, label)
    
    def wrap(self, availWidth, availHeight):
        if self.width is None:
            self.width = availWidth
        return (self.width, self.height)
```

---

## ✅ Üretim Sırasında Kontrol

Her özel flowable kullanırken:

- [ ] Doğru parametreler verildi mi?
- [ ] Yükseklik **sayfada sığar** mı? (Çok büyükse sayfa atar)
- [ ] **Markdown'da yer tutucu** belirtildi mi? (Üretim hatırlatması için)
- [ ] **Görsel testi** yapıldı mı? (PDF açılıp kontrol edildi mi?)
- [ ] **Çıktı testi** uygun mu? (Yazıcıdan çıkıldığında okunabilir mi?)
