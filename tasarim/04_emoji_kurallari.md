# 🚫 Emoji Kuralları

> DejaVu Sans fontu birçok emojiyi desteklemiyor. Bu dosya hangi emoji'lerin **kullanılabilir**, hangilerinin **kaçınılması gerektiğini** açıklar.

---

## 🎯 Temel Prensip

**Markdown'da yazılan dekoratif emojiler PDF üretiminde otomatik olarak temizlenir.**

`md_converter.py` içindeki `clean_emojis()` fonksiyonu bu işlemi otomatik yapar. Aşağıdaki Unicode aralıkları **silinir**:

```python
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
```

---

## ❌ KULLANMA — Otomatik Temizlenenler

### Renkli Kareler ve Şekiller
🟦 🟥 🟧 🟨 🟩 🟪 🟫 🟢 🟠 🔴 🟡 🟣 🟤 ⚫ ⚪

### Ofis ve İletişim
📊 📈 📉 📋 📌 📎 📁 📂 📄 📑 📃 📜 📚 📖 📕 📗 📘 📙
✉️ 📧 📨 📩 📤 📥 📫 📪 📬 📭 📮

### Dekoratif ve Motivasyonel
✨ 🎉 🎊 🎈 🎁 🎀 ⭐ 🌟 💫 🔥 💥 ⚡ 💪 🤝 🎓 🏆 🥇
💡 💭 🧠 ❤️ 💚 💙 💜 💛 🤍 🖤 🤎

### Teknoloji
🤖 💻 📱 💾 💿 🖥️ 🖱️ 🖨️ ⌨️ 🎮 🕹️ 📷 📹 🎥
🌐 🛰️ 📡 🔌 🔋

### Yüz İfadeleri
😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 😉 😊 😇 🥰 😍 🤩
😎 🤓 🧐 🤔 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖

### Doğa ve Hava
🌳 🌴 🌲 🌵 🌷 🌸 🌹 🌺 🌻 🌼 🌽 🌾 🌿 🍀
☀️ ⛅ ☁️ 🌧️ 🌨️ 🌩️ 🌪️ ⚡ ❄️ ☃️

### Yiyecek ve İçecek
🍎 🍐 🍊 🍋 🍌 🍉 🍇 🍓 🥑 🥦 🥬 🥒 🌶️
☕ 🍵 🥛 🧃 🥤 🍷 🍺 🍕 🍔 🍟 🌭 🥪 🌮 🌯

### Aktivite ve Spor
⚽ 🏀 🏈 ⚾ 🎾 🏐 🏉 🎱 🏓 🏸 🥏 🥏 🥏

### Cihaz ve Eşya
🔍 🔎 🔬 🔭 🎨 🖌️ 🖍️ 📐 📏 ✂️ ✏️ 🖊️ 🖋️
📔 📕 📒 📓 📚 🗂️ 📂 📁

### Roket ve Uzay
🚀 🛸 🌍 🌎 🌏 🌐 🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘
☄️ ⭐ 🌟 💫

### Para ve Sayılar
💰 💵 💴 💶 💷 💸 💳 🧾 ⚖️
🔢 🔣 🔤 🔠 🔡

---

## ✅ KULLANILABİLİR — DejaVu Destekler

### Geometrik Şekiller
| Karakter | Adı | Unicode |
|:--------:|-----|---------|
| ● | Dolu daire | U+25CF |
| ○ | Boş daire | U+25CB |
| ■ | Dolu kare | U+25A0 |
| □ | Boş kare | U+25A1 |
| ◆ | Dolu elmas | U+25C6 |
| ◇ | Boş elmas | U+25C7 |
| ▲ | Dolu üçgen | U+25B2 |
| △ | Boş üçgen | U+25B3 |
| ▼ | Aşağı üçgen | U+25BC |
| ▽ | Boş aşağı üçgen | U+25BD |
| ▪ | Küçük dolu kare | U+25AA |
| ▫ | Küçük boş kare | U+25AB |
| ★ | Dolu yıldız | U+2605 |
| ☆ | Boş yıldız | U+2606 |

### Oklar (Genelde Çalışır)
| Karakter | Adı |
|:--------:|-----|
| → | Sağ ok |
| ← | Sol ok |
| ↑ | Yukarı ok |
| ↓ | Aşağı ok |
| ↔ | Çift yönlü ok |
| ⇒ | Çift sağ ok |
| ⇐ | Çift sol ok |
| ⇔ | Çift yönlü çift ok |

### Onay/İptal
| Karakter | Adı |
|:--------:|-----|
| ✓ | Onay (genelde çalışır) |
| ✗ | İptal (genelde çalışır) |
| ✔ | Bold onay (riskli, test et) |
| ✘ | Bold iptal (riskli, test et) |

### Para ve Matematik
| Karakter | Adı |
|:--------:|-----|
| ₺ | Türk lirası |
| $ € £ ¥ | Para birimleri |
| % ‰ | Yüzde, binde |
| × ÷ | Çarpma, bölme |
| ± ∓ | Artı eksi |
| ≤ ≥ ≠ | Eşit/eşit değil |
| ∞ | Sonsuz |
| ° | Derece |

### Kart Sembolleri
| Karakter | Adı |
|:--------:|-----|
| ♠ ♣ ♥ ♦ | Kart simgeleri |

### Diğer Yararlı Semboller
| Karakter | Adı |
|:--------:|-----|
| § | Paragraf |
| ¶ | Pilcrow |
| © ® ™ | Telif/marka |
| ℗ | Ses kaydı telifi |
| † ‡ | Hançer (dipnot) |

---

## 💡 Emoji Yerine Ne Kullanmalı?

### Madde Listeleri
**Yerine** 📋 📝 ✏️ 🔹 🔸 → **Bunları kullan** • ▪ ●

❌:
```markdown
- 📋 Listeleme yap
- 📝 Yazı yaz
- ✏️ İmza at
```

✅:
```markdown
- Listeleme yap
- Yazı yaz
- İmza at
```

> Markdown'daki `-` zaten PDF'te `•` olur, ek emoji gerekmez.

### Vurgu / Önem
**Yerine** 💡 🎯 ⚡ 🔥 → **Bunları kullan** Bold metin (`**önemli**`)

❌:
```markdown
🔥 Bu çok önemli bir nokta!
```

✅:
```markdown
**Önemli:** Bu kritik bir nokta.
```

### Başlıklar
**Yerine** 🎓 📚 🚀 → **Hiç ekleme** (sadece başlık metni yeter)

❌:
```markdown
## 🎓 Öğrenme Çıktıları
```

✅:
```markdown
## Öğrenme Çıktıları
```

### Onay/Kontrol
**Yerine** ✅ ❌ ⚠️ → **Bunları kullan** ✓ ✗ veya kelimeyi yaz

❌:
```markdown
- ✅ Tamamlandı
- ❌ Eksik
- ⚠️ Dikkat
```

✅:
```markdown
- ✓ Tamamlandı
- ✗ Eksik
- **Dikkat:** ...
```

### Renkli Vurgular (Tasarım için)
**Yerine** 🟦 🟥 🟧 → Kullanma, **PDF üretiminde otomatik kaldırılır**

❌:
```markdown
### 🟦 1. Ders Saati: Kavramları Keşfetmek
```

✅:
```markdown
### 1. Ders Saati: Kavramları Keşfetmek
```

---

## 🔍 Test Etme

Bir karakterin DejaVu Sans tarafından desteklenip desteklenmediğini test etmek için:

### Yöntem 1: Manuel Test
```python
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('TR', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

doc = SimpleDocTemplate('test.pdf')
style = ParagraphStyle('test', fontName='TR', fontSize=14)

# Test edilecek karakter
test_chars = '★ ☆ ✓ ✗ → ← ▲ ●'

doc.build([Paragraph(test_chars, style)])
```

PDF'i aç. Kutucuk varsa o karakter desteklenmiyor.

### Yöntem 2: fc-list Komutu (Linux)
```bash
fc-list :charset=2605  # ★ karakteri için
```

### Yöntem 3: Karakter Online Test
[unicodecharacter.com](https://www.unicodecharacter.com) gibi sitelerde karakteri kontrol et.

---

## 🔄 Yeni Emoji Eklenirse

Yeni bir emoji türü çıkarsa (örn. 2024'te bir şey eklendi) ve **temizlenmesini istiyorsan**:

`md_converter.py`'da `UNSUPPORTED_EMOJI_PATTERN`'i güncelle:

```python
UNSUPPORTED_EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\U00002600-\U000026FF"
    "\U00002700-\U000027BF"
    "\U0001F000-\U0001F2FF"
    "\U0001FB00-\U0001FBFF"  # YENİ EKLENEN ARALIK
    "]+",
    flags=re.UNICODE
)
```

---

## 📝 Markdown Yazımında Pratik Kurallar

### Kural 1: Sınıf İçinde Düşün
"Bu emoji bana basılı kâğıtta nasıl görünür?" diye sor:
- 📋 → Sadece kutucuk olur, gerek yok
- 📊 → Sadece kutucuk olur, gerek yok
- ★ → Yıldız olarak çıkar, kullanılabilir

### Kural 2: Vurgu için **Bold** Kullan
Vurgu için **emoji ekleme**, **bold metin** kullan:
- ❌ "🔥 Önemli not"
- ✅ "**Önemli not**"

### Kural 3: Liste Başında Emoji Kullanma
Markdown listeleri zaten `•` ile başlar, ek emoji gereksiz:
- ❌ "📌 Madde 1"
- ✅ "Madde 1" (otomatik `•` eklenir)

### Kural 4: Bölüm Başlıklarına Emoji Koyma
- ❌ "## 🎯 Hedefler"
- ✅ "## Hedefler"

### Kural 5: PDF Üretim Otomatik Temizler
Bu kuralları unutsan bile, PDF üretimi **otomatik olarak** dekoratif emojileri siler. Ama:
- Yine de markdown'da temiz tutmak iyi (insan okumada da güzel)
- Bazen `clean_emojis` algoritması beklenmedik temizlikler yapabilir, sürpriz olmaması için kullanma

---

## ✅ Kontrol Listesi

Markdown yazarken:

- [ ] Renkli kare emojiler **yok** (🟦 🟥)
- [ ] Ofis emojileri **yok** (📋 📊 📁)
- [ ] Dekoratif emojiler **yok** (✨ 🎯 🚀)
- [ ] Yüz emojileri **yok** (😀 🤔)
- [ ] Vurgu için **bold** kullanılıyor
- [ ] Liste başlarında emoji **yok**
- [ ] Başlıklarda emoji **yok**

PDF üretimi sonrası:

- [ ] Kutucuk (□) yok
- [ ] Türkçe karakterler net
- [ ] Madde listeleri düzgün başlıyor
