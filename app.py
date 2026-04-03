from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)


model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "url", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        email_text = request.form["email"]
        cleaned = clean_text(email_text)
        vector = vectorizer.transform([cleaned])
        result = model.predict(vector)[0]

        prediction = "⚠️ Phishing Email" if result == "phishing" else "✅ Safe Email"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)