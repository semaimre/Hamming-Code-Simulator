# 🧠 Hamming SEC-DED Web Simülatörü

Bu proje, kullanıcıların ikili verileri Hamming SEC-DED (Single Error Correction, Double Error Detection) algoritması ile kodlamasını, hatalı verileri simüle etmesini ve hataları tespit edip düzeltmesini sağlayan web tabanlı bir simülatördür.

## 🚀 Özellikler

- Kullanıcıdan 8, 16 veya 32 bitlik ikili veri girişi alır.
- Hamming kodunu hesaplar ve bellek adresine kaydeder.
- Hata ekleme (bit flip) simülasyonu yapar.
- Hata kontrolü ve otomatik düzeltme uygular.
- Kodlama, bellek, hata ekleme ve düzeltme işlemleri tamamen görseldir.
- Sayfa her yüklendiğinde önceki bellek temizlenir.

## 🖥️ Ekranlar

- **1. Veri Girişi** – Hamming kodu hesapla
- **2. Bellek** – Hesaplanan kodları adresli olarak gör
- **3. Hata Ekle** – Adrese bit hatası ekle
- **4. Hata Kontrolü** – Hatalı veriyi kontrol et ve düzelt

## 📁 Proje Yapısı

```
proje-dizini/
├── main.py             # Flask sunucusu
├── hamming.py          # Hamming kodlama ve hata düzeltme mantığı
├── templates/
│   └── index.html      # Web arayüzü
├── static/
│   └── style.css
``` 

## ✅ Planlanan Geliştirmeler

- Kodlama adımlarının animasyonlu gösterimi
- Kod kopyalama butonu
- Hamming 74/SECDED-SEC kodlarının görsel karşılaştırması
- Dark mode tasarımı

## Demo ve Bağlantılar
- Tanıtım Videosu: [YouTube](https://youtu.be/WioUexpAxpg)
- Uygulama için:[Tıklayınız](https://hamming-code-simulator-1.onrender.com)
- Kaynak Kodlar: [hamming.py](https://github.com/semaimre/Hamming-Code-Simulator/blob/main/hamming.py)
- [main.py](



## 👩‍💻 Geliştirici

**Adınız:** Semanur İmre
**İletişim:** sem4imre@gmail.com

## 📝 Lisans

Bu proje eğitim amaçlıdır. Ticari olmayan kullanım için serbesttir.

