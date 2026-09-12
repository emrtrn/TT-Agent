---
name: teknoloji-tasarim-icerik-uretici
description: Teknoloji ve Tasarım dersi 8. sınıf güncel Türkiye Yüzyılı Maarif Modeli için ünite materyalleri üretir ve bunları profesyonel PDF'lere dönüştürür. Her üretimde canlı MEB program ve ünite sayfalarını doğruluk kaynağı olarak kullanır.
---

# Teknoloji ve Tasarım Ders Materyali Üretici

Bu skill, **Türkiye Yüzyılı Maarif Modeli 8. sınıf Teknoloji ve Tasarım Dersi** için ünite materyalleri üretir. Bağlayıcı kaynak canlı [MEB 8. sınıf program sayfasıdır](https://tymm.meb.gov.tr/ogretim-programlari/teknoloji-tasarim-dersi/9).

## ⚡ Hızlı Başlangıç

Kullanıcı bir ünite üretimi istediğinde:

1. **`workflow/00_yol_haritasi.md`** dosyasını oku — 7 adımlık süreç
2. **`workflow/01_kullanici_tercihleri.md`** dosyasını oku — Tüm önemli ayarlar
3. **`workflow/04_etkilesimli_sunum_entegrasyonu.md`** dosyasını oku — Öğren/Pekiştir/Uygula/Materyaller ve sunum entegrasyonu
4. İlgili ünite klasöründeki hazırlık planının **Oturum devri** bölümünü oku
5. **`referans/8_sinif/00_resmi_kaynak.md`** dosyasını oku ve canlı MEB sayfasını aç
6. İlgili resmî ünite sayfasındaki ders saati, öğrenme çıktıları, süreç bileşenleri, içerik çerçevesi ve uygulamaları doğrula
7. **`referans/8_sinif/03_unite_listesi.md`** kataloğuyla karşılaştır; çelişkide canlı MEB sayfasını esas al
8. Hangi adıma gelinmişse o adımın **şablon dosyasını** (`sablonlar/`) oku ve uygula
9. Her oturum sonunda ünite planındaki durum, sıradaki iş ve açık kararları güncelle
10. PDF'e çevirme aşamasında **`pdf_uretim/`** klasörünü kullan

## 🎯 Ne Üretir?

Bir ünite için aşağıdaki **7 ana çıktı**:

| # | Doküman | Şablon |
|:-:|---------|--------|
| 1 | Ayrıntılı Ünite Ders Planı | `sablonlar/01_ders_plani.md` |
| 2 | Ön Değerlendirme Aracı (5 alt araç) | `sablonlar/02_on_degerlendirme.md` |
| 3 | Sunum omurgası + entegrasyon haritası + kavram kartları | `workflow/04_etkilesimli_sunum_entegrasyonu.md`, `sablonlar/03_kavram_kartlari.md`, `sablonlar/04_sunum_icerigi.md` |
| 4 | Öğrenci Çalışma Kâğıtları | `sablonlar/05_calisma_kagitlari.md` |
| 5 | Değerlendirme Araçları (Rubrikler, Sınav, vb.) | `sablonlar/06_degerlendirme_araclari.md` |
| 6 | Farklılaştırma Materyalleri (Zenginleştirme + Destekleme) | `sablonlar/07_zenginlestirme.md`, `sablonlar/08_destekleme.md` |
| 7 | Öğretmen Yansıtma + Ünite Kapanış | `sablonlar/09_yansitma_kapanis.md` |

Tamamlandığında ~9-10 markdown dosyası ve **~38 ayrı PDF** üretilir.

## 🔑 Kritik Kullanıcı Tercihleri

Detayları `workflow/01_kullanici_tercihleri.md` içinde, ama kısaca:

- **Ders süresi:** 40 dakika (45 değil!)
- **Haftalık ders:** 2 ders saati peş peşe (yani 4 saatlik ünite 2 hafta sürer)
- **Sınıf mevcudu:** 20 öğrenci (T.T. dersinde sınıf ikiye bölünür)
- **PDF rengi:** Koyu turuncu (#C2410C)
- **Font:** DejaVu Sans (Türkçe karakter desteği)
- **Kapak:** Sadece 4+ sayfalık dokümanlarda
- **Çalışma kâğıdı çizgileri:** Hafif gri (çıktıda silik görünür)

## 🚫 Yapılmaması Gerekenler

- ❌ Materyalleri tek bir markdown dosyasında toplama → her bir tür ayrı dosya
- ❌ Emojileri PDF üretiminde dekoratif amaçla kullanma → DejaVu Sans desteklemez (kutucuk olur)
- ❌ Cevap anahtarlı sınavı öğrenciye verme → her zaman ayrı PDF
- ❌ "45 dakika" referansları → her zaman 40 dakika
- ❌ "2025" tarih damgası → "[Sınıf]. Sınıf Öğretim Programı" yaz
- ❌ Atölye çalışmaları için 4'ten fazla kişi grup → 2-3 kişi grupların ideal

## 📚 Kaynaklar ve Düzen

```
TT-Agent/
├── SKILL.md                           # Bu dosya — agent buradan başlar
├── CLAUDE.md                          # Proje hafızası (her oturumda okunur)
├── README.md                          # Genel kullanım
│
├── workflow/                          # 🗺️ Yol haritası
│   ├── 00_yol_haritasi.md            # 7 adımlık süreç
│   ├── 01_kullanici_tercihleri.md    # Tüm ayarlar
│   ├── 02_kontrol_listesi.md         # Her ünite checklist
│   ├── 03_oneriler_ipuclari.md       # Edinilen ipuçları
│   └── 04_etkilesimli_sunum_entegrasyonu.md # Sunum ve portal kaynak geçişleri
│
├── referans/                          # Müfredat bilgisi — GERÇEK PROGRAM BELGESİNE DAYALI
│   ├── ortak/                         # Ortak ders yapısı, Maarif Modeli ve pedagoji
│   └── 8_sinif/                       # Resmî kaynak kaydı ve güncel katalog
│
├── sablonlar/                         # 📋 Doküman şablonları
│   ├── 01_ders_plani.md
│   ├── 02_on_degerlendirme.md
│   ├── 03_kavram_kartlari.md
│   ├── 04_sunum_icerigi.md
│   ├── 05_calisma_kagitlari.md
│   ├── 06_degerlendirme_araclari.md
│   ├── 07_zenginlestirme.md
│   ├── 08_destekleme.md
│   └── 09_yansitma_kapanis.md
│
├── pdf_uretim/                        # 🐍 PDF üretim altyapısı
│   ├── pdf_style.py                  # Ortak stil (font, renk, flowable)
│   ├── md_converter.py               # Markdown → PDF dönüştürücü
│   ├── config.py                     # Merkezi yapılandırma
│   ├── ornek_uretim.py               # Kullanım örneği
│   └── README.md                     # Kullanım talimatı
│
├── tasarim/                           # 🎨 Tasarım sistemi
│   ├── 01_renk_paleti.md
│   ├── 02_tipografi.md
│   ├── 03_ozel_cizimler.md           # Venn, zihin haritası, kontrol kutusu
│   └── 04_emoji_kurallari.md         # Hangi emojiler PDF'te kalacak
│
└── units/                             # 📑 8. sınıf ünite materyalleri
    └── 8_sinif/unit1 ... unit8
```

## Tipik Bir Çalışma Akışı

Kullanıcı: *"3. ünite (Görsel İletişim Tasarımı) için materyalleri hazırla"*

Agent:
1. SKILL.md'yi okudu (zaten burada)
2. **`workflow/00_yol_haritasi.md`** → 7 adımı görüyor
3. **`workflow/01_kullanici_tercihleri.md`** → Tercihleri biliyor
4. **`workflow/04_etkilesimli_sunum_entegrasyonu.md`** → Sunumun kaynak geçişlerini görüyor
5. Ünite planındaki **Oturum devri** → Kaldığı işi belirliyor
6. **`referans/8_sinif/00_resmi_kaynak.md`** → Canlı MEB sayfasını açıyor
7. İlgili resmî ünite sayfası → Tam öğrenme çıktıları ve süreç bileşenlerini doğruluyor
8. İlgili şablonu okuyup sıradaki Markdown dilimini üretiyor
9. Ünite planındaki durum ve sıradaki işi güncelliyor
10. Tüm içerikler onaylanınca **`pdf_uretim/`**'i kullanıyor

## ⚠️ Önemli Hatırlatmalar

- **Önce markdown, sonra PDF** — Tüm içeriği önce markdown olarak yaz, gözden geçir, onaylanınca PDF'e çevir
- **Sunum iki aşamalıdır** — Ders planından sonra taslak başlar; gerçek kaynak kimlikleri ve dönüş akışı doğrulandıktan sonra nihai olur
- **Oturum devri zorunludur** — Her çalışmanın sonunda ünite planındaki durum ve sıradaki tek iş güncellenir
- **Kapsam denetimi** — Her şablon dosyasında "minimum içerik" listesi var, atlama
- **Türkçe karakter** — `pdf_uretim/pdf_style.py` zaten DejaVu Sans kayıtlı
- **Emoji temizliği** — `md_converter.py` otomatik halletmekte; manuel emoji kullanma ihtiyacı yok
- **Soru-cevap ayrımı** — Sınav PDF'lerinde öğrenci kopyası ve cevap anahtarı **mutlaka ayrı PDF'ler**
