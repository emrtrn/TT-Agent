# 🎓 Teknoloji ve Tasarım Ders Materyali Üretici Agent Paketi

> Bu paket, **Türkiye Yüzyılı Maarif Modeli 8. sınıf Teknoloji ve Tasarım** dersi için ünite materyalleri üretir. Birincil içerik kaynağı canlı [MEB 8. sınıf program sayfasıdır](https://tymm.meb.gov.tr/ogretim-programlari/teknoloji-tasarim-dersi/9).

---

## 🚀 Hızlı Başlangıç

### 1. Depoyu Aç

```powershell
git clone https://github.com/emrtrn/TT-Agent.git
Set-Location TT-Agent
code .
```

### 2. Agent Oturumunu Başlat

Proje kökündeki **`CLAUDE.md`** ve **`SKILL.md`** kalıcı kuralları içerir. Ünite çalışmasına başlamadan önce ilgili ünite planındaki **Oturum devri** bölümü okunur.

```
TT-Agent/
├── CLAUDE.md                    # Kalıcı proje bağlamı
├── SKILL.md                     # Agent giriş noktası
├── workflow/                    # Yol haritası ve tercihler
├── referans/                    # Resmî kaynak kayıtları
├── sablonlar/                   # Doküman şablonları
├── pdf_uretim/                  # PDF üretim kodları
├── tasarim/                     # Tasarım sistemi
└── units/                       # 8_sinif/ ünite materyalleri ve oturum devri
```

### 3. Bağımlılıkları Kur

```bash
pip install reportlab pypdf pdf2image
```

Sistem fontları (Türkçe karakter desteği için):
```bash
# Ubuntu/Debian
sudo apt install fonts-dejavu

# macOS
brew install --cask font-dejavu
```

### 4. İlk Komutu Ver

VS Code'da Claude Code'a yazın:

```
3. ünite (Görsel İletişim Tasarımı) için tüm materyalleri hazırla.
```

Agent:
1. `CLAUDE.md`'yi okuyacak (kalıcı bağlam)
2. `SKILL.md`'yi okuyacak (giriş)
3. İlgili ünite planındaki `Oturum devri` bölümünden kaldığı işi belirleyecek
4. `workflow/00_yol_haritasi.md` ve `workflow/04_etkilesimli_sunum_entegrasyonu.md` kurallarını uygulayacak
5. Canlı MEB sayfasını doğrulayıp sıradaki üretim dilimine devam edecek

---

## 📦 Paket İçeriği

### 📄 Ana Dosyalar
- **`SKILL.md`** — Skill tanımı (agent giriş noktası)
- **`CLAUDE.md`** — Proje hafızası (Claude Code otomatik okur)
- **`README.md`** — Bu dosya (kullanım kılavuzu)

### 📂 Workflow (`workflow/`)
- **`00_yol_haritasi.md`** — 7 adımlık üretim süreci
- **`01_kullanici_tercihleri.md`** — Tüm ayarlar tek yerde
- **`02_kontrol_listesi.md`** — Her ünite için checklist
- **`03_oneriler_ipuclari.md`** — Edinilen pratik ipuçları
- **`04_etkilesimli_sunum_entegrasyonu.md`** — Öğren/Pekiştir/Uygula/Materyaller ve sunum bağlantıları

### 📂 Referans (`referans/`)
- **`ortak/`** — Ders yapısı, Maarif Modeli ve pedagojik yaklaşım
- **`8_sinif/00_resmi_kaynak.md`** — Bağlayıcı MEB bağlantısı ve doğrulama kuralları
- **`8_sinif/03_unite_listesi.md`** — Canlı ünite sayfalarından doğrulanmış katalog
- **`ortak/`** — Ders yapısı ve pedagojik yaklaşım

### 📂 Şablonlar (`sablonlar/`)
- **`01_ders_plani.md`** — Ünite ders planı şablonu
- **`02_on_degerlendirme.md`** — Ön değerlendirme aracı (5 alt araç)
- **`03_kavram_kartlari.md`** — Kavram kartları + etkinlikler
- **`04_sunum_icerigi.md`** — Etkileşimli sunumun slayt, kaynak ve dönüş sözleşmesi
- **`05_calisma_kagitlari.md`** — Öğrenci çalışma kâğıtları
- **`06_degerlendirme_araclari.md`** — Rubrikler, sınav, vb. (10 araç)
- **`07_zenginlestirme.md`** — Zenginleştirme paketi (5-7 etkinlik)
- **`08_destekleme.md`** — Destekleme paketi (6-8 materyal)
- **`09_yansitma_kapanis.md`** — Öğretmen yansıtma + kapanış (5 araç)

### 📂 PDF Üretim (`pdf_uretim/`)
- **`pdf_style.py`** — Stil, font, renk, özel flowable'lar
- **`md_converter.py`** — Markdown → PDF dönüştürücü
- **`config.py`** — Merkezi tercih ayarları
- **`ornek_uretim.py`** — Örnek üretim script'i
- **`README.md`** — Kullanım talimatı

### 📂 Tasarım (`tasarim/`)
- **`01_renk_paleti.md`** — Koyu turuncu tema detayları
- **`02_tipografi.md`** — Font ve boyut hiyerarşisi
- **`03_ozel_cizimler.md`** — MindMapCanvas, VennDiagram, vb.
- **`04_emoji_kurallari.md`** — Hangi emojiler PDF'te kalacak

### 📂 Örnekler (`units/`)

- **`README.md`** — Örnek materyaller burada (boş başlar, ünite tamamlandıkça doldurulur)

---

## 🎯 Kullanım Akışı

### Senaryo 1: Tüm Üniteyi Hazırlatma

```
Sen: "3. Ünite (Görsel İletişim Tasarımı) için tüm materyalleri hazırla."

Agent:
1. ✅ Ünite planındaki `Oturum devri` bölümünden kaldığı yeri belirler
2. ✅ Canlı MEB program ve ilgili ünite sayfasını doğrular
3. ✅ Öğretmen hazırlığı ve ders planını yazar
4. ⏸ Ders planını onaya sunar
5. ✅ Sunum entegrasyon haritasını ve ilk sunum taslağını hazırlar
6. ✅ Ön değerlendirme, Pekiştir/Uygula içerikleri ve materyalleri sunumla birlikte geliştirir
7. ✅ Gerçek kaynak kimliklerini işler ve etkileşimli sunum dönüş akışını doğrular
8. ✅ Tüm Markdown'lar tamamlanınca istenen PDF çıktılarını üretir
9. ✅ Ünite planındaki durum ve sıradaki işi günceller
10. ✅ Değişiklikleri Git ile kaydeder
```

Sunum üretiminin ayrıntılı kuralları için `workflow/04_etkilesimli_sunum_entegrasyonu.md` kullanılır.

### Senaryo 2: Tek Materyal İsteme

```
Sen: "5. Ünite (Mühendislik ve Tasarım) için sadece çalışma kâğıtlarını yap."

Agent:
1. ✅ sablonlar/05_calisma_kagitlari.md'yi okur
2. ✅ Çalışma kâğıtlarını yazar
3. ✅ Markdown'ı sunar
4. ⏸ "PDF'e çevireyim mi?"
5. (Onay)
6. ✅ PDF'leri üretir
```

### Senaryo 3: Revizyon

```
Sen: "16 numaralı PDF'in başlığında 'Süreç Değerlendirme' yerine 'Süreç Gözlem' yazsın."

Agent:
1. ✅ İlgili markdown'ı bulur
2. ✅ Değişikliği uygular
3. ✅ PDF'i tekrar üretir
4. ✅ Sadece o PDF'i sunar
```

### Senaryo 4: Çoklu Ünite

```
Sen: "1, 6 ve 9. üniteler için ders planlarını üret."

Agent:
1. ✅ Her ünite için ayrı klasör oluşturur (materials/unite-1/, vb.)
2. ✅ Üç ünite için sırayla ders planı yazar
3. ✅ Üç markdown sunar
4. ⏸ "Hepsini PDF'e çevireyim mi?"
```

---

## 🎨 Tasarım Kararları

Bu paket aşağıdaki kararları **kalıcı** olarak uygular:

### Görsel
- ✅ **Koyu turuncu tema** (#C2410C ana renk)
- ✅ **DejaVu Sans** font (Türkçe karakter desteği)
- ✅ **A4** sayfa boyutu
- ✅ **Kapak sayfası** sadece 4+ sayfada
- ✅ **Sayfa numarası** sağ alt
- ✅ **Üst-alt bantlar** her sayfada

### İçerik
- ✅ **40 dakika** ders saati (45 değil)
- ✅ **20 öğrenci** sınıf mevcudu
- ✅ **2 hafta** = 4 ders saati
- ✅ **"[Sınıf]. Sınıf Öğretim Programı"** (yıl yok)
- ✅ **Cevap anahtarı ayrı PDF**
- ✅ **Zihin haritası, Venn için özel çizimler**

### Pedagoji
- ✅ **Beceri temelli** öğrenme
- ✅ **Programlar arası bileşenler** (KB, OB, SDB, D, E)
- ✅ **Maarif Modeli** felsefesi
- ✅ **Farklılaştırma** (zenginleştirme + destekleme)

> Tüm tercihler `workflow/01_kullanici_tercihleri.md`'de.

---

## 🔧 Yapılandırma

### Tercihleri Değiştirmek

Bir tercih değişikliği yapmak istiyorsan:

1. **`workflow/01_kullanici_tercihleri.md`** dosyasını aç
2. İlgili tercihi güncelle
3. **`pdf_uretim/config.py`**'i de güncelle (kod tarafı)
4. Yeni üretimlerde otomatik uygulanır

### Tasarımı Değiştirmek

Renk veya font değişikliği için:

1. **`pdf_uretim/pdf_style.py`** açın
2. `COLOR_PRIMARY`, `COLOR_SECONDARY` vb. değerleri değiştir
3. Veya farklı font ailesi kullanmak isterseniz `register_fonts()` güncelle
4. **`tasarim/01_renk_paleti.md`** ve **`02_tipografi.md`**'yi de güncelle (dokümantasyon)

---

## 🚧 Sınırlamalar

### Şu An Mümkün Değil
- ❌ Otomatik dış görsel/fotoğraf ekleme
- ❌ Karmaşık iç içe Markdown listeleri
- ❌ Excel formatına dönüşüm
- ❌ Otomatik öğrenci kayıt/dijital değerlendirme
- ❌ Yıllık plan oluşturma (ünite bazında üretim var)

### Bilinen Çözümler
- **Sunum için:** Markdown içerik ve entegrasyon kaynağıdır; etkileşimli HTML sunum ayrıca üretilir
- **Form yönetimi için:** Google Forms / EBA sistemi öneriliyor
- **Yıllık plan için:** İlgili `referans/<sinif>_sinif/03_unite_listesi.md` dosyasından derleniyor

---

## 🤝 Yardım ve Destek

### Hata Karşılaşırsan
1. **`workflow/03_oneriler_ipuclari.md`** dosyasındaki "Sık Karşılaşılan Hatalar" bölümünü oku
2. **`pdf_uretim/README.md`** dosyasındaki "Sorun Giderme" bölümüne bak
3. Türkçe karakter sorunu varsa: DejaVu Sans yüklü mü kontrol et

### Yeni Bir Şablon Eklemek
- `sablonlar/` klasörüne yeni bir `.md` dosyası oluştur
- Yapısını mevcut şablonlara benzet
- `SKILL.md`'de listele

### Yeni Bir Özel Flowable
- `pdf_uretim/pdf_style.py`'a yeni bir `Flowable` sınıfı ekle
- `tasarim/03_ozel_cizimler.md`'de dokümante et

---

## 📊 Başarı Göstergeleri

Bu paketin doğru çalıştığını anlamak için:

### Markdown Çıktıları
- ✅ Türkçe karakter sorunsuz
- ✅ Şablona uygun yapı
- ✅ Programlar arası bileşenler her ders saatinde
- ✅ Süre hesabı tutarlı (40 dk × N saat)

### PDF Çıktıları
- ✅ Koyu turuncu başlıklar
- ✅ Türkçe karakterler net
- ✅ Kutucuk (□) yok (emoji temizlendi)
- ✅ Tablolar düzgün
- ✅ Sayfa numarası ve bantlar her sayfada
- ✅ 4+ sayfa olan dokümanda kapak var

### Pedagojik Tutarlılık
- ✅ Maarif Modeli felsefesine uygun
- ✅ Seçilen sınıfa uygun zorluk seviyesi
- ✅ Açık-uçlu sorular ağırlıkta
- ✅ Çoklu değerlendirme yöntemleri

---

## 📝 Lisans ve Atıf

Bu paket Türkiye'deki bir Teknoloji ve Tasarım öğretmeni için hazırlanmıştır. İçerik üretiminde güncel Türkiye Yüzyılı Maarif Modeli sayfaları esas alınır.

Diğer öğretmenler bu paketi kendi öğretim sürecinde **rehber olarak** kullanabilir, ancak içerik üretimi her zaman **kendi sınıfınızın ihtiyaçlarına göre** özelleştirilmelidir.

---

## 🌟 Son Söz

Bu paket **dolu bir başlangıç noktası**dır, sınırsız bir sistem değil. Her ünite için:
- 🎨 Yaratıcılığı sen ekle
- 👥 Sınıfını sen tanı
- 📚 Programa sadık kal
- 💡 Yansıtarak gelişmeye devam et

İyi dersler! 🌱

---

## 📞 Hızlı Referans

| İhtiyaç | Dosya |
|---------|-------|
| Genel başlangıç | Bu dosya (README.md) |
| Üretim adımları | `workflow/00_yol_haritasi.md` |
| Tüm ayarlar | `workflow/01_kullanici_tercihleri.md` |
| Şablonlar | `sablonlar/` |
| PDF kodları | `pdf_uretim/` |
| Önceki ipuçları | `workflow/03_oneriler_ipuclari.md` |
| Sorun çözümü | `pdf_uretim/README.md` (sonu) |
