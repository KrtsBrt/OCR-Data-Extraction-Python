📸 OCR Tabanlı Konum Veri Madenciliği (GPS Data Extraction)

Bu çalışma; büyük ölçekli bir görsel veri setinden (3000+ imaj), manuel veri girişini ortadan kaldırmak ve dijitalleştirme sürecini otomatize etmek amacıyla geliştirilmiştir. 

 Proje Özeti
Saha fotoğraflarının alt panelinde yer alan karmaşık meta verileri (Enlem/Boylam), Tesseract OCR ve özel görüntü işleme teknikleri kullanılarak yapılandırılmış veri haline getirilmiştir. Manuel iş gücünü %99 oranında azaltarak veri tutarlılığını artırmaktadır.

🛠 Teknik Altyapı ve Metotlar
- **Görüntü İşleme (PIL & Pillow):** OCR doğruluğunu artırmak amacıyla görseller gri tonlamaya (Grayscale) çevrilmiş, otokontrast ve dinamik parlaklık iyileştirmeleri uygulanmıştır.
- **Optik Karakter Tanıma (Tesseract OCR):** `--psm 3` sayfa analiz modu kullanılarak görsel üzerindeki metin blokları dijitalize edilmiştir.
- **Veri Ayıklama (Regex):** Ham metin yığını içerisinden koordinat verileri, düzenli ifadeler (Regular Expressions) kullanılarak hata payı minimize edilmiş şekilde çekilmiştir.
- **Veri Raporlama (Pandas):** Ayıklanan veriler, analiz ve takip için Excel (.xlsx) formatında çıktıya dönüştürülmüştür.

📂 Dosya Yapısı
- `veri_bul.py`: Görüntü iyileştirme ve veri madenciliği algoritmasını içeren ana betik.
- `örnek#.jpg/jpeg`: Algoritmanın performansını doğrulamak için dizinde yer alan test görselleri.

 Uygulama Adımları
1. Proje dizinindeki resim formatlı (`.jpg`, `.jpeg`, `.png`) tüm dosyalar taranır.
2. OCR motoru öncesi görüntü ön işleme tabi tutulur.
3. Ham metin içerisinden "Lat" ve "Long" ifadelerini takip eden sayısal karakterler ayıklanır.
4. Çıktılar `Koordinat_Verileri.xlsx` dosyasına otomatik olarak aktarılır.
