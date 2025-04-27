from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

with open('knn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('email_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
     
        email_text = request.form['email_text']
        

        transformed_text = vectorizer.transform([email_text])
        

        prediction = model.predict(transformed_text)

        result = "Spam" if prediction[0] == 1 else "Ham (Normal)"

        return render_template('index.html', prediction_text=f'Tahmin: {result}')

if __name__ == "__main__":
    app.run(debug=True)
