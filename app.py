from flask import Flask, request, render_template
import pickle

# Flask uygulamasını başlat
app = Flask(__name__)

# Modeli ve Vectorizer'ı yükle
with open('knn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('email_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Ana sayfa (Form Gösterilecek)
@app.route('/')
def home():
    return render_template('index.html')

# Tahmin işlemi (Formdan veri gelecek)
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Formdan gelen text veriyi al
        email_text = request.form['email_text']
        
        # Temizleme ve vectorizer ile vektörize etme
        transformed_text = vectorizer.transform([email_text])
        
        # Modelle tahmin yap
        prediction = model.predict(transformed_text)
        
        # Sonucu yorumla
        result = "Spam" if prediction[0] == 1 else "Ham (Normal)"

        return render_template('index.html', prediction_text=f'Tahmin: {result}')

if __name__ == "__main__":
    app.run(debug=True)
