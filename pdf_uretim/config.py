"""PDF üretimi için sınıf ve ünite kataloğu.

Bu modül 7. sınıf çağrılarını korurken 8. sınıf üretimini de aynı API ile
destekler. Programda değişiklik olduğunda yalnızca ``SINIFLAR`` güncellenir.
"""

DERS_SURESI_DK = 40
DERS_SURESI_STR = "40 dakika"
OGRENCI_SAYISI = 20


SINIFLAR = {
    7: {
        "etiket": "7. Sınıf", "toplam_saat": 72,
        "uniteler": {
            1: {"ad": "Teknoloji ve Tasarım Öğreniyorum", "saat": 4, "cikti_sayisi": 4},
            2: {"ad": "Temel Tasarım", "saat": 6, "cikti_sayisi": 4},
            3: {"ad": "Tasarım Odaklı Süreç", "saat": 10, "cikti_sayisi": 2},
            4: {"ad": "Bilgisayar Destekli Tasarım", "saat": 8, "cikti_sayisi": 3},
            5: {"ad": "Mimari Tasarım", "saat": 8, "cikti_sayisi": 4},
            6: {"ad": "Doğadan Tasarıma", "saat": 8, "cikti_sayisi": 3},
            7: {"ad": "Enerjinin Dönüşümü ve Tasarım", "saat": 8, "cikti_sayisi": 5},
            8: {"ad": "Bütünleşik Öğrenme: STEAM", "saat": 10, "cikti_sayisi": 6},
            9: {"ad": "Yapay Zekâ ve Akıllı Ürünler", "saat": 8, "cikti_sayisi": 4},
        },
    },
    8: {
        "etiket": "8. Sınıf", "toplam_saat": 70,
        "uniteler": {
            1: {"ad": "İnovatif Düşüncenin Geliştirilmesi, Fikirlerin Korunması ve Etik", "saat": 8, "cikti_sayisi": 3},
            2: {"ad": "Tanıtım ve Pazarlama", "saat": 10, "cikti_sayisi": 3},
            3: {"ad": "Görsel İletişim Tasarımı", "saat": 8, "cikti_sayisi": 3},
            4: {"ad": "Ürün Geliştirme", "saat": 10, "cikti_sayisi": 3},
            5: {"ad": "Mühendislik ve Tasarım", "saat": 10, "cikti_sayisi": 4},
            6: {"ad": "Ulaşım Teknolojileri", "saat": 8, "cikti_sayisi": 3},
            7: {"ad": "Özgün Ürünümü Tasarlıyorum", "saat": 10, "cikti_sayisi": 2},
            8: {"ad": "Bunu Ben Yaptım", "saat": 6, "cikti_sayisi": 1},
        },
    },
}

# Eski üretim betiklerinin kullandığı 7. sınıf görünümü.
UNITELER = SINIFLAR[7]["uniteler"]


def toplam_sure_str(saat_sayisi):
    return f"{saat_sayisi} × {DERS_SURESI_DK} dk"


def hafta_sayisi(saat_sayisi):
    """Ders haftada iki saat işlendiğinde gereken hafta sayısı."""
    return saat_sayisi // 2


def sinif_bilgisi(sinif_no):
    """Sınıf kataloğunu döndürür; geçersiz sınıf için ``None`` döner."""
    return SINIFLAR.get(sinif_no)


def kapak_meta(saat_sayisi=4, sinif_no=7, **ekstra):
    """Her PDF için sınıf-bağımsız kapak meta bilgilerini oluşturur."""
    if sinif_no not in SINIFLAR:
        raise ValueError(f"Desteklenmeyen sınıf: {sinif_no}")
    base = {
        "Sınıf": str(sinif_no),
        "Ders": "Teknoloji ve Tasarım",
        "Süre": f"{saat_sayisi} Ders Saati ({toplam_sure_str(saat_sayisi)})",
        "Süreç": f"{hafta_sayisi(saat_sayisi)} Hafta",
    }
    base.update(ekstra)
    return base


def kapak_meta_kazanim(saat_sayisi=4, kazanim_baslangic="1", kazanim_bitis="4", sinif_no=7, unite_no="[N]", **ekstra):
    """Kazanım kodlarını seçilen sınıf ve üniteyle birlikte kapak metasında verir."""
    base = kapak_meta(saat_sayisi, sinif_no=sinif_no)
    kod = f"TT.{sinif_no}.{unite_no}"
    base["Öğrenme Çıktıları"] = f"{kazanim_bitis} Kazanım ({kod}.{kazanim_baslangic} – {kod}.{kazanim_bitis})"
    base.update(ekstra)
    return base


def unite_bilgisi(unite_no, sinif_no=7):
    """Seçilen sınıfın ünite bilgisini döndürür; bulunamazsa ``None`` döner."""
    sinif = sinif_bilgisi(sinif_no)
    if not sinif or unite_no not in sinif["uniteler"]:
        return None
    unite = sinif["uniteler"][unite_no]
    return {
        "no": unite_no, "sinif": sinif_no, "ad": unite["ad"], "saat": unite["saat"],
        "hafta": hafta_sayisi(unite["saat"]), "cikti_sayisi": unite["cikti_sayisi"],
        "unite_info_string": f"Teknoloji ve Tasarım • {sinif['etiket']} • {unite_no}. Ünite",
    }


def unite_klasoru(unite_no, sinif_no=7):
    """Depodaki sınıf-temelli ünite göreli yolunu döndürür."""
    if unite_bilgisi(unite_no, sinif_no) is None:
        raise ValueError(f"Tanımsız ünite: {sinif_no}. sınıf / {unite_no}. ünite")
    return f"units/{sinif_no}_sinif/unit{unite_no}"


def md_dosya_adi(unite_no, tip):
    """Markdown dosyası adı oluşturur."""
    return f"Unite{unite_no}_{tip}.md"


def pdf_dosya_adi(no, ad):
    """PDF dosyası adı oluşturur (numara_ad formatında)."""
    return f"{no:02d}_{ad}.pdf"
