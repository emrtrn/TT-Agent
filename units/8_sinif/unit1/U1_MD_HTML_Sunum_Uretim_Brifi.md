# 8. Sınıf 1. Ünite — HTML Sunum Üretim Brifi

## Amaç ve durum

Bu brif, `U1_MD_Sunum_Icerigi.md` içindeki 64 slaytın **nihai** etkileşimli HTML sürümünü üretmek içindir. Pedagojik ve kaynak davranışı bu belgelerde tanımlanır; HTML, tüm bağlı dokümanlar ve etkinlikler tamamlandıktan sonra bu kararları görsel ve erişilebilir bir akışa dönüştürür.

**Durum:** Bekliyor; gerçek katalog kimlikleri, dokümanlar, etkinlikler ve portal davranışları tamamlanmadan üretime başlanmaz.  
**Ölçü:** 1920 × 1080, 16:9, 64 slayt, 8 ders × 40 dakika.  
**Kapsam:** Bağlantılı nihai HTML sunumu; PDF üretimi değildir.

## HTML üretim kapısı

Aşağıdaki koşulların tamamı karşılanmadan bu brifle 64 slaytlık HTML üretimi yapılmaz:

- Ön değerlendirme, kavram kartları, bireysel/grup çalışma kâğıtları, Pekiştir/Uygula etkinlikleri, değerlendirme araçları ve gerekli öğretmen materyalleri tamamlandı.
- `U1_Sunum_Entegrasyon_Haritasi.md` içindeki her bağlı kaynak gerçek katalog kimliği, açılma biçimi ve dönüş davranışıyla güncellendi.
- `U1_MD_Sunum_Icerigi.md` kaynak yer tutucuları yerine gerçek materyal adlarıyla nihai hâle getirildi.
- 16 slaytlık 1–2. ders örneği yalnızca görsel prototip olarak kabul edildi; nihai sunumun kısmi yayını değildir.

## Üreticiye birlikte verilecek dosyalar

1. `U1_MD_Sunum_Icerigi.md` — slayt metni, konuşma notu ve HTML üretim profili.
2. `U1_Sunum_Entegrasyon_Haritasi.md` — kaynak, açılma ve dönüş sözleşmesi.
3. `docs/ClaudeDesign/sistem/URETIM-REHBERI.md` — ortak üretim kuralları.
4. `docs/ClaudeDesign/sistem/TASARIM-SISTEMI.css` — değiştirilmeyecek ortak görsel iskelet.
5. `docs/ClaudeDesign/deck-stage.js` — gezinme, ölçekleme, yazdırma ve speaker notes altyapısı.
6. `docs/ClaudeDesign/unite-2.html` — canlı slayt kalıbı referansı.

Öncelik sırası: içerik ve kaynak davranışı için ilk iki dosya; görsel uygulama için ClaudeDesign rehberi ve canlı HTML referansı.

## Tasarım kararı

Ayrı bir tasarım sistemi oluşturulmaz. ClaudeDesign sistemi korunur; yalnızca Ünite 1’e özgü palet dosyası üretilir.

```css
:root {
  --accent: #C2410C;   /* inovasyon: koyu turuncu */
  --accent-2: #EA580C; /* açık vurgu */
  --teal: #0F766E;     /* araştırma / doğrulama ikincil aksanı */
  --ders-1: #0F766E;
  --ders-2: #C2410C;
  --ders-3: #B45309;
  --ders-4: #0F766E;
  --ders-5: #7C3AED;
  --ders-6: #1D4ED8;
  --ders-7: #9A3412;
  --ders-8: #475569;
}
```

- `--paper`, `--paper-2`, `--ink`, `--rule-soft` ve tipografi ailesi korunur.
- `TASARIM-SISTEMI.css` değişmez; renkler yalnızca yeni `UNITE-PALET.css` dosyasında tutulur.
- Başlıkta Instrument Serif, gövdede IBM Plex Sans, etiketlerde JetBrains Mono kullanılır.
- Eski 7. sınıf belgesindeki Poppins/Montserrat, logo alanı ve mavi-turuncu şema kullanılmaz.

## HTML iskeleti

```text
unit1-html/
├─ unite-1.html
├─ deck-stage.js
├─ sistem/
│  ├─ TASARIM-SISTEMI.css
│  └─ UNITE-PALET.css
└─ assets/
   ├─ gorseller/
   └─ kavramlar/
```

- `<deck-stage width="1920" height="1080">` doğrudan 64 adet `<section>` içerir.
- Her bölüm `data-screen-label="NN kısa etiket"` taşır.
- Her slaytın `.rail.top` ve `.rail.bot` bilgisi ders, aşama ve slayt numarasını gösterir.
- `<script type="application/json" id="speaker-notes">` içinde 64, sıralı konuşma notu bulunur.
- Her slaytta ana mesaj kısa tutulur; konuşma notunun tamamı görünür metne taşınmaz.
- Hazır görsel varsa `<img>`, öğretmenin sonradan yükleyeceği görsel için `<image-slot>` kullanılır.

## Slayt tipinin uygulanması

`U1_MD_Sunum_Icerigi.md` içindeki **HTML üretim profili** tablosu bağlayıcıdır.

| Tip ailesi | Öncelikli ClaudeDesign bileşeni |
|---|---|
| Kapak, köprü, final | `.rail`, `.kicker`, `.display`, gerektiğinde `section.dark` veya `section.accent-bg` |
| Hedef, kontrol listesi, süreç | `.card`, `.num`, `.meta-strip` |
| Karşılaştırma, kullanıcı profili, akran dönütü | `.two` veya `.three` grid + dengeli kartlar |
| Etkinlik, çalışma kâğıdı, eskiz | Sol yönerge + sağ şablon / `.plch` alanı |
| Mola | `.card.inv` ile büyük “10 dk ara”; ödev içermez |
| Ders sonu + ödev | Sol özet + sağ `.card.inv` ödev kartı |
| Galeri, sunum, öz değerlendirme | `.kc`, `.meta-strip`, büyük zamanlayıcı veya form kartı |

## Kaynak ve etkileşim sınırları

- `TASLAK` kaynaklar için kırık bağlantı veya sahte portal kimliği üretmeyin. Slaytta öğretmen notu/yer tutucu gösterin.
- Slayt 7’deki ön değerlendirme ve Slayt 21’deki çalışma kâğıdı, kaynak belgeleri üretilene kadar basılı materyal yönergesi olarak kalır.
- Slayt 8, 24, 40 ve 56 yalnızca 10 dakikalık ara geçişidir; ödev düğmesi veya yeni görev içermez.
- Slayt 16, 31 ve 48 bir sonraki hafta için ödev verebilir. Slayt 64 yeni görev vermeden kapanır.
- Slayt 19’daki Yerel İnovasyon Atölyesi MVP, öğretmen tarafından önceden açılır. Sunum kendi içinde yerel Windows yolunu açmaya veya uygulamayı iframe içine zorlamaya çalışmaz. Bu slayt, 10 dakikalık yönlendirme ekranı ve aşama özeti olarak tasarlanır.
- Kaynak açılışı, kapanışı ve sunuma dönüş davranışı ancak gerçek portal/katalog entegrasyonunda test edilerek nihai kabul alır.

## Nihai üretim için kopyala-yapıştır istemi

> Bu dosyalar 8. sınıf Teknoloji ve Tasarım 1. Ünite için bağlayıcı **nihai üretim** girdileridir. HTML üretim kapısındaki tüm koşulların karşılandığını önce doğrula. `U1_MD_Sunum_Icerigi.md` içindeki 64 slaytın sırasını, metnini, konuşma notlarını ve HTML üretim profilini koru. `U1_Sunum_Entegrasyon_Haritasi.md` içindeki gerçek kaynak kimlikleri ile açılış/dönüş davranışlarına uy. `docs/ClaudeDesign/sistem/URETIM-REHBERI.md`, `TASARIM-SISTEMI.css`, `deck-stage.js` ve onaylı 1–2. ders örneği tasarım ve çalışma altyapısıdır. Yeni bir tasarım sistemi kurma; Ünite 1 paletini ayrı `UNITE-PALET.css` dosyasında tanımla ve ders renklerini 1’den 8’e kadar ekle. 1920×1080 ölçüsünde, 64 adet doğrudan `deck-stage` çocuğu olan HTML üret. Her slayta kısa `data-screen-label`, her slayt için sıralı speaker note ekle. TASLAK kaynaklar için çalışanmış gibi görünen bağlantı üretme. Slayt 19’da yerel MVP’ye mutlak Windows yolu bağlama; öğretmen önceden açar. Üretim sonunda slayt sayısını, speaker-note sayısını, taşan metni, 40 dakikalık ders sürelerini ve her kaynak dönüşünü doğrula.

## İlk HTML kabul kontrolü

- [ ] 64 `<section>` ve 64 speaker note var.
- [ ] Her dersin sekiz slaydındaki süre toplamı 40 dakikadır.
- [ ] Tek-numaralı ders sonları ara slaytıdır; ödev içermez.
- [ ] Çift-numaralı ders sonlarındaki ödevler, sonraki haftaya taşınır; son ders kapanışla biter.
- [ ] Slayt 19 notsuz ön alıştırma olarak kalır.
- [ ] `TASARIM-SISTEMI.css` değişmeden kalır; renkler yalnızca palette yaşar.
- [ ] Masaüstü 16:9 görünümünde taşan/çakışan metin yoktur.
- [ ] Akıllı tahta görsel kabulü ve kaynak dönüş davranışları ayrı doğrulanır.
