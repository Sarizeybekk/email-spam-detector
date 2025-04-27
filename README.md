#  Spam Email Detection System

Bu proje, e-posta veya tweet gibi metin içeriklerinin spam olup olmadığını tespit etmek için geliştirilmiş bir **Makine Öğrenmesi** tabanlı sistemdir.  
Kullanıcılar, basit bir web arayüzü üzerinden bir metin girerek anında **Spam** veya **Ham (Normal)** sonucunu alabilir.

---

## Kullanılan Teknolojiler

- **Python 3.9+**
- **Flask** (Web sunucu)
- **scikit-learn** (Makine Öğrenmesi Modelleri: KNN)
- **NLTK** (Doğal Dil İşleme: Stopwords, Stemmer)
- **TF-IDF Vectorizer** (Metin verisini sayısal veriye çevirme)
- **HTML5 / CSS3** (Modern, responsive arayüz)

---

## Proje Yapısı
- `app.py`: Flask backend uygulaması
- `templates/index.html`: Web arayüzü sayfası
- `static/style.css`: Sayfa stil dosyası
- `knn_model.pkl`: Eğitilmiş KNN makine öğrenmesi modeli
- `email_vectorizer.pkl`: Eğitilmiş TF-IDF vektörizer
- `requirements.txt`: Proje bağımlılıkları
- `README.md`: Proje tanıtımı

  # Proje Kurulum ve Çalıştırma Komutları

```bash
# 1. Projeyi klonla
git clone https://github.com/Sarizeybekk/email-spam-detector.git
cd email-spam-detector

# 2. Sanal ortam oluştur 
python -m venv venv
source venv/bin/activate  # Mac/Linux

# 3. Gerekli paketleri yükle
pip install -r requirements.txt

# 4. Flask uygulamasını başlat
python app.py

```



![image](https://github.com/user-attachments/assets/0800eac6-5886-4399-b178-7a1ee9fed41f)
