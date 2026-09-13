# Teknoloji ve Tasarım — Sunum Üretim Rehberi
> 7. Sınıf · 1. Üniteden çıkarılan dersler + 2. Ünitede oturmuş sistem.
> Yeni ünite üretiminde **kaynak olarak ekle**.

---

## 0. Bu Rehberin Amacı

Aynı görsel dilde, aynı pedagojik akışla, aynı kalite çıtasında **birden fazla ünite** üretmek. Yeni sohbet bu dosyayı okuduğunda önceki üniteleri yapmış gibi başlamalı. Sıfırdan stil/sistem kararı vermesin.

**Birlikte ekle (her seferinde aynı 3 dosya + 1 referans):**
- `sistem/URETIM-REHBERI.md` — bu dosya
- `sistem/TASARIM-SISTEMI.css` — paletten **bağımsız** görsel iskelet (.rail / .kicker / .card / .plch / .road / .num / .kc / .ders-tag / .bn / .meta-strip / .color-band / .pill)
- `sistem/UNITE-PALET.css` — **üniteye özgü** renk kodları (palet bu dosyada yaşar)
- **Referans olarak**: bir önceki ünitenin `unite-N.html` dosyası — slayt kalıplarını oradan kopyala. (Ayrı bir `SLAYT-SABLONLARI.html` tutmuyoruz; canlı ünite zaten en iyi şablondur.)

---

## 1. Mutlak Kurallar (Pazarlık Yok)

### 1.1 Ders saati & hafta yapısı
- **Teknoloji ve Tasarım dersi haftada 2 saattir, ARDIŞIK işlenir** (yönetmelik gereği). Yani haftalık blok: `40 dk + 10 dk teneffüs + 40 dk`.
- **Ünite uzunluğu değişkendir.** Bazı üniteler 4 ders saati, bazıları 6, 8, hatta 10 ders saati olabilir — dolayısıyla işlenecek **hafta sayısı üniteye göre değişir** (4 ders = 2 hafta, 6 ders = 3 hafta, 8 ders = 4 hafta, 10 ders = 5 hafta). "X hafta" yazarken bunu `ders_sayısı / 2` ile doğrula.
- **Genelleştirilmiş ödev/mola örüntüsü** (her hafta = 2 ardışık ders):
  - **Haftanın 1. dersi sonu (tek-numaralı dersler: 1, 3, 5, 7, 9):** ✗ ÖDEV YOK — sadece 10 dk teneffüs var; **mola slaytı** koy.
  - **Haftanın 2. dersi sonu (çift-numaralı dersler: 2, 4, 6, 8):** ✓ EV ÖDEVİ verilebilir (1 hafta sonra bir sonraki haftanın ilk dersinde paylaşılır).
  - **Son ders sonu:** ünite kapanışı / öz değerlendirme / hazırsa final ödev.
- **Hatırlatma noktaları (genelleştirilmiş):**
  - **Haftanın 2. dersi başı** (10 dk teneffüsten sonra): "Az önce ne konuştuk?" (3 dk hızlı, **"geçen ders" deme** — 10 dk önceydi).
  - **Yeni haftanın 1. dersi başı** (1 hafta sonra): "Geçen hafta + ödev paylaşımı" (ilk 5–8 dk).
  - **Yeni haftanın 2. dersi başı:** 1 dk köprü ("10 dk önce" tonu).

### 1.2 İçerik kuralları
- **2025–2026 gibi akademik yıl yazma.** Sunum her yıl kullanılacak.
- **"Telefonları çıkarın" yazma.** Öğrenciler okula telefon getiremez.
- **Filler içerik EKLEME.** Boş hissedilen yer varsa layout sorunu, içerikle doldurma.
- **AI slop tropları yasak:** gradient bombardımanı, emoji yağmuru, sol-borderlı renk-aksanlı kutular, SVG ile çizilmiş icon orduları.
- **Brand kullanma:** MEB, Fatih Okulları gibi kurumsal kimlikleri kopyalama. Kendi orijinal estetiğini sürdür.

### 1.3 Boyut & ölçek
- Slayt: **1920 × 1080**, 16:9
- Min font: **24px** (gövde için 28-32 ideal)
- Padding standardı: **`140px 120px`** (ana slaytlar), **`130px 100px`** (üç-kart layout'ları)
- `<deck-stage width="1920" height="1080">` → ölçekleme/klavye/print otomatik

---

## 2. Tasarım Sistemi — İki Katmanlı Kurulum

### 2.1 İskelet (her ünitede AYNI) — `TASARIM-SISTEMI.css`
Tipografi, layout, .rail / .kicker / .card / .plch / .stamp / .road / .num — **tüm bileşenler renksiz tanımlı.** Renk kodlarını CSS değişkenleri (`var(--accent)`, `var(--paper)` vb.) üzerinden okur. Bu dosyaya ünite başına dokunmuyorsun.

### 2.2 Palet (üniteye ÖZGÜ) — `UNITE-PALET.css`
Renk kodları **yalnızca burada** yaşar. Yeni ünite açıldığında:
1. Bir önceki ünitenin `UNITE-PALET.css`'ini yeni proje klasörüne kopyala.
2. `--accent` ve `--accent-2` değerlerini ünitenin baskın temasına göre değiştir.
3. `--teal` (ikincil aksan) gerekirse başka bir hue'a kaydır.
4. `--ders-1...N` ünite içi ders sayısına göre ayarla.
5. **`--paper` / `--ink` ailesine DOKUNMA** — bu, üniteler-arası süreklilik omurgasıdır. Sadece sıcak/soğuk doğrultusunda ±2-3 luminance kayması yapılabilir, asla saturasyon eklenmez.

### 2.3 HTML'de yükleme sırası
ÖNCE palet, SONRA sistem (sistem paletten miras alır). `sistem/` klasörünü olduğu gibi kopyala, yollar göreceli kalsın:
```html
<link rel="stylesheet" href="sistem/UNITE-PALET.css">
<link rel="stylesheet" href="sistem/TASARIM-SISTEMI.css">
```
Proje yapısı:
```
proje-kök/
├─ unite-N.html         ← ana sunum
├─ deck-stage.js        ← slayt iskeleti
├─ sistem/              ← kanonik sistem (tek kaynak)
│  ├─ TASARIM-SISTEMI.css
│  ├─ UNITE-PALET.css
│  └─ URETIM-REHBERI.md
└─ assets/              ← ünite görselleri
```
Köke ayrı CSS kopyaları **bırakma**; iki kaynak ileride ayrışır.

### 2.4 Üniteye göre sabit değişkenler
```css
--paper:   #F4EFE6;  /* kırık beyaz, ana zemin — ÜNİTELER ARASI SABİT */
--paper-2: #EBE3D5;
--ink:     #1E3A5F;  /* koyu lacivert — metin + dark zemin (Ünite 2'den) */
--rule-soft: #D8CEBC;
--muted:   #6A5F4F;
```

### 2.5 Ünite paleti örnekleri

**1. Ünite (Teknoloji ve Tasarım Öğreniyorum):**
```css
--accent:   #C8553D;  /* terracotta */
--accent-2: #E8A84E;  /* ocra */
--teal:     #2F7D7E;  /* muted teal */
--ink:      #0E1B33;  /* derin gece lacivert (1. ünite varyantı) */
```

**2. Ünite (Temel Tasarım):**
```css
--accent:   #F59E0B;  /* amber — Türk sanatları + ilkeler */
--accent-2: #FBBF24;  /* açık amber */
--teal:     #0D9488;  /* canlı teal — elemanlar */
--ink:      #1E3A5F;  /* koyu lacivert (içerik dosyasından) */
/* ders nüansları: ders-3 mor, ders-4 zümrüt, ders-5 lacivert açık, ders-6 altın */
```

### 2.6 Tipografi (üniteler arası SABİT)
- **Başlık (`.hero`, `.display`, `.mid`):** Instrument Serif (Google Fonts), italik vurgu için `<em>`
- **Gövde (`.body`, `.lede`):** IBM Plex Sans
- **Mono (etiket, eyebrow, kicker):** JetBrains Mono, harf aralığı `letter-spacing: 0.12em-0.14em`
- **Inter, Roboto, Arial, Fraunces, system fonts KULLANMA.**

| Sınıf | Boyut | Kullanım |
|---|---|---|
| `.display` | 180-220px | Kapak, manifesto |
| `.hero` | 96-120px | Slayt başlığı |
| `.mid` | 44-60px | Kart başlığı |
| `.lede` | 28-34px | Açıklama paragraf |
| `.body` | 18-24px | Gövde |
| `.kicker` | 14-16px upper | "Yol Haritası", "Bu Ders" eyebrow'ları |
| `.eyebrow` | 12-14px upper | Kart içi mikro etiket |

### 2.7 Standart bileşenler
**İskelet:**
- **`.rail.top` / `.rail.bot`** — slayt üst/alt şeritleri, breadcrumb + sayfa numarası taşır
- **`.kicker`** — mono, küçük, harf-aralıklı eyebrow
- **`.card`** — kırık beyaz arka, ince border. `.card.inv` (lacivert), `.card.accent` (aksan), `.card.teal` varyantları
- **`.stamp`** — köşeli mini etiket (`.stamp.accent`, `.stamp.ink`, `.stamp.teal`)
- **`.num`** (`ol.num`) — numaralı liste
- **`.two`, `.three`, `.four`, `.five`** — grid yardımcıları
- **`.plch`** — görsel placeholder (G01, G02...)
- **`section.dark`** — ink zemin + paper yazı (ünite başına ≤4)
- **`section.accent-bg`** — accent zemin (ünite başına 1-2, ana soru / manifesto)

**Ünite 2'den terfi eden bileşenler (sistemin parçası):**
- **`.ders-tag.d1...d6`** — renkli ders rozeti, `--ders-N` paletinden okur
- **`.bn`** — kart içi büyük numara (80px serif). `.bn.teal`, `.bn.ink` varyantları
- **`.meta-strip`** — alt-bilgi şeridi, mono etiketler + `<b>` ile vurgu
- **`.color-band`** — kapak üstü ders renkleri bandı
- **`.pill`** — currentColor ile çalışan ince etiket
- **`.kc`** — kare kavram kartı görseli (ink zemin + ince çerçeve + alt gölge)
- **`.card .kc-strip`** — `.card` içine tam-genişlik üst görsel bandı

### 2.8 Görsel sistemi
- **Görsel önceden hazırsa** (`assets/` içinde sabit dosya): doğrudan `<img>` kullan, `.kc` / `.kc-strip` / `.plch` içine yerleştir. Sistem CSS'i her üçü için de `object-fit: cover` ayarlar.
- **Öğretmen sahada yükleyecekse** (drag-drop): `<image-slot id="..." placeholder="...">` kullan. Aynı `.kc` / `.kc-strip` / `.plch` kapsayıcıları image-slot için de hazır.
- Ünite 2 boyunca tüm görseller önceden üretildiği için pratikte `<img>` kullandık; image-slot opsiyonel kaldı.
- Dosya isimlendirme: `assets/kavramlar/01-isim.png` (numaralı kavram serileri) veya `assets/gorseller/G01-aciklama.png` (slayt içi referanslar).
- **Standart oran tablosu:**
  - 3 sütun yatay kart: **554 × 170 px** veya **1108 × 340 px** (2x)
  - 1 sütun büyük: **1100 × 720 px**
  - Kavram kartı kare (`.kc`): **600 × 600 px**
- Görsel paleti: **kırık beyaz zemin + lacivert çizgiler + aksan rengi vurgu** (editorial illüstrasyon stili)

---

## 3. Slayt Tipi Kataloğu (Şablonlar)

| # | Tip | Yapı | Ne zaman |
|---|---|---|---|
| 01 | Kapak | display başlık + breadcrumb rail | Ünite başlangıcı |
| 02 | Hedefler | hero + dim açıklama | Kapağın hemen sonrası |
| 03 | Yol Haritası | Ders sayısı kadar durak | 3. slayt |
| 04 | Köprü/Tartışma | hero soru + 2-3 açıklama | Her dersin başında |
| 05 | Ön Değerlendirme | bireysel form | 1. ders erken |
| 06 | Kavram Kartları | 3-15 kart grid | Tanıtım |
| 07 | Karşılaştırma | iki sütun (X vs Y) | İkili kavram |
| 08 | Üç-Dünya | 3 sütun + her sütunda 3 görsel | Kategori örnekleri |
| 09 | Etkinlik | sol açıklama + sağ şablon kartı | Her dersin ana etkinliği |
| 10 | Ana Soru (accent-bg) | ortalı display + lede | Ders dönüm noktası |
| 11 | 5'li liste (kontrol listesi) | 5 kart, sonuncu accent | "5 özellik" |
| 12 | **Mola** (`.card.inv` + dev "10dk") | sol özet + sağ mola kartı | Tek-numaralı ders sonu |
| 13 | **Ders sonu + Ödev** | sol özet + sağ `.card.inv` ödev | Çift-numaralı ders sonu |
| 14 | **Hatırlatma** (3 dk) | sol açıklama + sağ Q1-Q5 | 2. dersin başı (10 dk sonra) |
| 15 | Yolculuk/Süreç | 7 adımlı yatay grid | Süreç anlatımı |
| 16 | Akvaryum/Sunum | bireysel sunum + dinleyici görevleri | Galeri/sergi |
| 17 | Öz değerlendirme | form + serif başlık | Ünite sonu |
| 18 | Final özet | "Nereden nereye" iki sütun | Kapanış |
| 19 | Teşekkür | minimal | Son slayt |
| 20 | Kaynaklar | "öğretmen için" footnote | Son ek |

→ Şablonları **en son üretilen ünitenin** `unite-N.html` dosyasından kopyala. Canlı ünite ayrı bir şablon dosyasından her zaman daha güncel ve daha öğreticidir.

---

## 4. Ders Akış Şablonu (genel — N ders)

**Her hafta = 2 ardışık ders, arada 10 dk teneffüs.**

### Tek-numaralı dersler (haftanın 1. dersi: 1, 3, 5...)
- Açılış: köprü ya da geçen-hafta-hatırlatma+ödev paylaşımı (1. derste ön değerlendirme)
- Ana içerik (~25-30 dk)
- **Mola slaytı — ÖDEV YOK** (5 dk)

### 🔔 10 dk teneffüs

### Çift-numaralı dersler (haftanın 2. dersi: 2, 4, 6...)
- 3 dk: hızlı hatırlatma ("az önce" tonu)
- 5 dk: köprü/ısınma
- ~25-30 dk: ana içerik + etkinlik
- **EV ÖDEVİ** (5-7 dk) — 1 hafta sonra bir sonraki haftaya
- *Son derste:* ödev yerine ünite kapanışı + öz değerlendirme

---

## 5. Yazım & Ton Kuralları

- **Türkçe doğru imla:** "merak", "ölçüt", "endüstri" — TDK kaynaklı
- **Konuşma dili konuşma notlarında, slaytta öz:**
  - Slayt: `Bilgiye nasıl güveniriz?`
  - Speaker note: `İnternette bir bilgi gördünüz. Ne yapıyorsunuz?...`
- **Italic vurgu:** Sadece serif başlıklarda `<em>` ile, accent renk
- **Numara/etiket:** Mono font, `01 · 02 · 03` formatında, `letter-spacing: 0.12em+`
- **"Sonraki ders / Sonraki hafta" doğru kullan** — "haftaya" deme, çünkü 1→2 ders arası 10 dk

---

## 6. Speaker Notes Sistemi

```html
<script type="application/json" id="speaker-notes">
[
"Slayt 1 notu (1-2 cümle)...",
"Slayt 2 notu...",
...
]
</script>
```
- 0-indexed array, `deck-stage.js` otomatik yansıtır
- **Konuşma dili:** "Burada şunu sorun", "2-3 cevap alın, devam edin"
- **Pedagojik amaç açıkla:** "Amaç cevap almak değil, merak uyandırmak"
- **Süre belirt:** "5 dakika", "Hızlı geç"
- Yapı: TON → AMAÇ → AKSIYON

---

## 7. Üretim Akışı (Yeni Ünite Açıldığında)

1. **Sor:** Konu, hedef kazanım listesi, etkinlik fikirleri var mı
2. **Palet kararı:** Bir önceki ünitenin `UNITE-PALET.css`'ini kopyala, yeni ünitenin tematik aksanını seç (1 baskın + 1 ikincil + ders nüansları). `--paper` / `--ink` ailesine dokunma.
3. **Yarat:** `unite-N.html` ana dosya, `sistem/UNITE-PALET.css` + `sistem/TASARIM-SISTEMI.css` + `deck-stage.js`'i çek (sırayla).
4. **Plan:** Ders sayısına göre slayt haritası çıkar (kapak/hedef/yol haritası 1-3, dersler ortada, kapanış sonda). Ödev/mola yerleşimini KURAL 1.1'le doğrula.
5. **İnşa:** Slaytları en son üretilen `unite-(N-1).html`'den kopyala (slayt tipi kataloğundan tip seç → o tipin canlı örneğini bul → uyarla). İçeriği doldur.
6. **Kritik kontrol:** Mola slaytları (tek-numaralı ders sonları), ödev konumu (çift-numaralı ders sonları, son ders hariç).
7. **Speaker notes:** Her slayt için 1-2 cümle.
8. **Doğrula:** `done` → konsol temiz mi, tüm slaytlar 1080'e sığdı mı.
9. **Görseller:** Liste çıkar, kullanıcı üretsin, `images/G##-isim.png`.
10. **Çıktı:** PPTX (`gen_pptx`), standalone HTML (thumbnail template + `super_inline_html`).

---

## 8. Hatalardan Çıkarılan Dersler (Tekrarlama!)

| Hata | Çözüm |
|---|---|
| "4 hafta" yazıldı | 2 hafta (haftada 2 ders ardışık) |
| 1. ders sonunda ödev verildi | Mola slaytı; ödev 2. ders sonu |
| 2. ders başında "geçen ders" denildi | "Az önce" / "10 dk önce" |
| 3. ders başında ödev paylaşımı atlandı | Slayt 24'e şerit ekle |
| 2025-2026 yazıldı | Akademik yıl yazma |
| "Telefonları çıkarın" | Yasak (öğrenci telefon getiremez) |
| Görsel oranı tutmadı | 554×170 / 1108×340 standart |
| Renk kodu CSS'in içine gömülmüştü, sonraki ünitede her yere find-replace gerekti | **Renk kodları yalnızca `UNITE-PALET.css`'te yaşar** |
| Ders rengi olarak 6 farklı hue kullanıldı, "aynı elden çıkmamış" hissi | 1 baskın + 1 ikincil aksan; ders nüansları sadece bölüm başlığı şeritlerinde |
| Speaker notes ders akışıyla uyumsuz kaldı | İçerik değişince notları da güncelle |
| Standalone HTML thumbnail eksikti | `<template id="__bundler_thumbnail">` ekle |
| Aynı CSS hem kökte hem `sistem/`'de duruyordu, ayrışma riski | **Tek kaynak**: sadece `sistem/` altında tut, HTML'den `sistem/...` yolu ile çağır |
| `.ders-tag`, `.bn`, `.kc`, `.meta-strip` her slaytta inline tanımlandı | Sisteme terfi etti (§2.7); yeni ünitede hazır kullan |
| Rehber `<image-slot>` zorunlu diyordu, pratik `<img>` kullandı | Görsel hazırsa `<img>`, kullanıcı yükleyecekse `<image-slot>` (§2.8) |

---

## 9. Yeni Sohbete Başlarken Söyle

> "Önceki ünitelerin üretim rehberini ve tasarım sistemini ekledim: `sistem/URETIM-REHBERI.md` + `sistem/TASARIM-SISTEMI.css` + `sistem/UNITE-PALET.css`, ek olarak referans için bir önceki ünitenin `unite-(N-1).html` dosyası. Bu üniteyi de aynı tasarım sistemiyle, aynı ders akış kurallarıyla üreteceksin. **Renk paletini yeni üniteye göre `sistem/UNITE-PALET.css` içinde değiştir** — sistem CSS dosyasına dokunma. Slayt kalıplarını önceki ünite HTML'inden kopyala. Önce slayt haritası çıkar."

Yeni Claude bu rehberi okuyunca:
- Tipografi/layout kararı vermeyecek (sistem hazır)
- Ders saati/hafta hatası yapmayacak (kurallar net)
- Slayt tiplerini kataloğdan seçecek, kalıbı önceki üniteden alacak
- Ödev/mola yerleşimini doğru yapacak
- Renk paletini `sistem/UNITE-PALET.css`'te konsolide edecek, sistem CSS'ini kirletmeyecek
- Görsel oranlarını standartla isteyecek
