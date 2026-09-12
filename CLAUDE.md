## Başlangıç Talimatı
Her oturum başında proje kökündeki `SKILL.md` dosyasını oku.
Sonra kullanıcının isteğine göre `workflow/`, `referans/` ve ilgili `units/8_sinif/unitN/` klasöründeki hazırlık planını oku. Ünite planındaki **Oturum devri** bölümü kaldığı yerin bağlayıcı kaydıdır.

# Proje: Teknoloji ve Tasarım Ders Materyali Üretici

> Bu dosya, Claude Code tarafından her oturumda otomatik okunur. Proje hakkında bilmeniz gereken **kalıcı bilgileri** içerir.

## 🎯 Proje Amacı

Türkiye'de bir ortaokulda görev yapan Teknoloji ve Tasarım öğretmeni için güncel Türkiye Yüzyılı Maarif Modeli'ne uygun 8. sınıf ünite materyalleri üretmek.

## 📌 Sabit Bilgiler (Bunlar hiç değişmez)

### Ders Yapısı
- **Sınıf:** 8
- **Ders adı:** Teknoloji ve Tasarım
- **Program:** Güncel Türkiye Yüzyılı Maarif Modeli
- **Bir ders saati:** 40 dakika
- **Haftalık ders:** 2 ders saati (peş peşe işlenir, atölye + sınıf bölünmesi)
- **Sınıf mevcudu:** Ortalama 20 öğrenci (sınıf, mevcut 25'i geçince ikiye bölünür)
- **Atölye yapısı:** Bir grup atölyede, bir grup sınıfta — sırayla rotasyon

### Süre Hesabı (Önemli!)
- 4 ders saatlik ünite → **2 hafta** sürer
- 6 ders saatlik ünite → **3 hafta** sürer
- 8 ders saatlik ünite → **4 hafta** sürer
- 10 ders saatlik ünite → **5 hafta** sürer

### 8. Sınıf Üniteleri
1. İnovatif Düşüncenin Geliştirilmesi, Fikirlerin Korunması ve Etik (8 saat)
2. Tanıtım ve Pazarlama (10 saat)
3. Görsel İletişim Tasarımı (8 saat)
4. Ürün Geliştirme (10 saat)
5. Mühendislik ve Tasarım (10 saat)
6. Ulaşım Teknolojileri (8 saat)
7. Özgün Ürünümü Tasarlıyorum (10 saat)
8. Bunu Ben Yaptım (6 saat)
Ünitelerin resmî sayfalardaki toplamı: 70 ders saati ve 22 öğrenme çıktısı.

> Bağlayıcı kaynak: https://tymm.meb.gov.tr/ogretim-programlari/teknoloji-tasarim-dersi/9  
> Kaynak kuralları: `referans/8_sinif/00_resmi_kaynak.md`  
> Yerel katalog: `referans/8_sinif/03_unite_listesi.md`

Her içerik üretiminde canlı MEB sayfası yeniden açılır. Eski yerel özetler veya bellekte kalan kazanım listeleri kaynak kabul edilmez.

## 🎨 Tasarım Tercihleri

### Renkler (PDF için)
- **Ana:** `#C2410C` (koyu turuncu — başlıklar, vurgu)
- **İkincil:** `#9A3412` (daha koyu turuncu — alt vurgu)
- **Aksan:** `#EA580C` (orta turuncu — alt başlıklar)
- **Açık:** `#FED7AA` (açık turuncu — kutu arka planı)
- **Çok açık:** `#FFF7ED` (kapak/info kutu arka planı)
- **Yazı çizgisi:** `#D1D5DB` (hafif gri, çıktıda silik)

### Font (PDF için)
- **Türkçe karakter desteği şart!** → DejaVu Sans ailesi
  - Yol: `/usr/share/fonts/truetype/dejavu/DejaVuSans*.ttf`

### Sayfa
- **Boyut:** A4 (her zaman)
- **Kenar boşlukları:** 2 cm yan, 1.8 cm üst-alt
- **Üst bant:** Ünite + doküman adı (8pt italik)
- **Alt bant:** Türkiye Yüzyılı Maarif Modeli (sol) + sayfa no (sağ)

### Kapak Sayfası
- **Sadece 4+ sayfalık dokümanlarda** ekle
- Üst etiket: "ÖĞRETMEN REHBERİ" / "ÖĞRENCİ MATERYALİ" / "DESTEKLEME MATERYALİ" gibi
- Ana başlık: 28pt, koyu turuncu
- Meta bilgi: Sınıf, Ders, Süre, Kazanım

## 🚫 Asla Yapma

1. **45 dakika yazma** — her zaman 40 dakika
2. **"2025" tarih damgası ekleme** kapağa — sadece "[Sınıf]. Sınıf Öğretim Programı"
3. **"Uygulama Dönemi"** alanı ekleme kapağa — kullanıcı yıllarca kullanacak
4. **Süreç gözlem formuna 30 öğrenci** koyma — 20 yeter
5. **Cevap anahtarını öğrenci sınavıyla aynı PDF'te** verme — daima ayrı
6. **Markdown'a şu emojileri PDF için yazma:** 🟦 📊 💡 🎯 📋 📝 🚀 🎨 🔍 (DejaVu desteklemez)
   - PDF üretimi sırasında otomatik temizlenir, ama kaynak markdown'larda az kullanmak daha iyi
7. **"Projeksiyon" yazma** — her zaman **"akıllı tahta"** kullan (hem metin içinde hem materyal listelerinde)

## ✅ Hatırlatmalar (her oturum başında düşün)

- Kullanıcı **öğretmen** — soruları öğretmen perspektifiyle yanıtla
- **Türkçe** içerik üret — terimler, başlıklar, açıklamalar hepsi Türkçe
- **Pedagojik bağlam** önemli — Maarif Modeli'nin "beceri temelli öğrenme" yaklaşımına uygun ol
- **Programlar arası bileşenler** (KB, OB, SDB, D, E) etkinliklere mutlaka entegre et
- **Önce markdown, sonra PDF** — kullanıcı markdown'ı görmek ister, PDF'i sonra
- **Sunum iki aşamalı** — ders planından sonra taslak başlar; kaynak entegrasyonları ve dönüş akışı doğrulanınca nihai olur
- **Sunum öğrenme omurgası** — Öğren, Pekiştir, Uygula ve Materyaller geçişleri `workflow/04_etkilesimli_sunum_entegrasyonu.md` kurallarına göre tasarlanır
- **Oturum devrini güncelle** — tamamlanan, aktif, sıradaki tek iş, açık kararlar ve doğrulama kanıtları ünite planına yazılır
- **Adımları atlama** — 7 adımlık yol haritasına sadık kal

## 📂 Klasör Yapısı

```
TT-Agent/
├── SKILL.md                      # Ana giriş
├── CLAUDE.md                     # Bu dosya
├── workflow/                     # Süreç ve tercihler
├── referans/                     # Müfredat bilgisi
├── sablonlar/                    # Doküman şablonları
├── pdf_uretim/                   # PDF kodları
├── tasarim/                      # Tasarım sistemi
└── units/                        # Önceki örnekler
```

## 🔧 Komut Önerileri

Kullanıcı şu komutlarla çalışabilir:

- **"Yeni ünite başlat: [ünite adı]"** — 7 adımlık süreci başlatır
- **"X ünitesi için Y materyalini hazırla"** — Tek bir adım
- **"Şu PDF'i revize et: [dosya adı]"** — Mevcut PDF'i güncelle
- **"PDF'e çevir"** — Markdown çıktılarını PDF'e dönüştür

## 💬 İletişim Tarzı

- **Net ve organize** ol — uzun açıklamalar yerine listeler/tablolar
- **Türkçe** konuş
- **Adım adım ilerle** — kullanıcı onayını bekle
- **Markdown formatı** kullan responses'ta da
- **Emoji'leri ölçülü** kullan (chat için OK, PDF için kaçın)

## 📝 Bu Skill'in Geçmişi

Bu skill, Claude.ai üzerinde 1. Ünite (Teknoloji ve Tasarım Öğreniyorum) için tüm materyallerin üretildiği bir konuşmanın çıktısıdır. Tüm tercihler ve kurallar o oturumda kullanıcıdan alınmış ve test edilmiştir.

İlk versiyon: 1. Ünite tamamlandıktan sonra
