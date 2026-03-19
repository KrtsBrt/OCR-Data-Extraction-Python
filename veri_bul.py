import pytesseract
import pandas as pd
import os
import re
from PIL import Image, ImageOps, ImageEnhance

# Tesseract path (Kendi yoluna göre güncelle)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Mevcut klasör ve örnek klasörü
ana_dizin = os.getcwd()
alt_klasorler = ['samples'] 
data_list = []

print(f"{'DOSYA ADI':<30} | {'HAM LAT':<20} | {'HAM LONG':<20}")
print("-" * 75)

for klasor in alt_klasorler:
    yol = os.path.join(ana_dizin, klasor)
    if not os.path.exists(yol): continue
    
    dosyalar = [f for f in os.listdir(yol) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    for dosya_adi in dosyalar:
        try:
            img = Image.open(os.path.join(yol, dosya_adi))
            
            # Goruntu iyilestirme
            img = img.convert('L') 
            img = ImageOps.autocontrast(img)
            img = ImageEnhance.Contrast(img).enhance(2.5)
            
            # OCR Islemi
            text = pytesseract.image_to_string(img, config='--psm 3')
            
            # Veri ayiklama (Noktasi virgulune ham veri)
            lat_match = re.search(r"Lat\s*(\S+)", text, re.IGNORECASE)
            long_match = re.search(r"Long\s*(\S+)", text, re.IGNORECASE)
            
            lat_raw = lat_match.group(1) if lat_match else ""
            long_raw = long_match.group(1) if long_match else ""

            print(f"{dosya_adi[:30]:<30} | {lat_raw:<20} | {long_raw:<20}")
            data_list.append({"Dosya": dosya_adi, "Ham_Lat": lat_raw, "Ham_Long": long_raw})

        except Exception:
            data_list.append({"Dosya": dosya_adi, "Ham_Lat": "HATA", "Ham_Long": "HATA"})

# Excel cikti
if data_list:
    df = pd.DataFrame(data_list)
    df.to_excel(os.path.join(ana_dizin, "Koordinat_Verileri.xlsx"), index=False)
    print("\nIslem tamamlandi. Veriler kaydedildi.")