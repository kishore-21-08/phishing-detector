# 📌 Phishing Email Detection System

A **Machine Learning + Flask web application** that detects whether an email is **Phishing** or **Safe** based on its content.

---

## 🚀 Features

* 🔍 Detect phishing emails using ML
* 🧠 Trained using Scikit-learn
* ✉️ Text + URL pattern analysis
* 🌐 User-friendly web interface (Flask)
* 📊 Displays prediction results instantly
* 🎨 Modern professional UI (CSS)

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn
* **Libraries:** Pandas, NumPy, Regex

---

## 📁 Project Structure

```
phishing_detector/
│
├── app.py
├── model.py
├── phishing_model.pkl
├── vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── dataset.csv
```

---

## 🧠 How It Works

1. Dataset contains emails labeled as:

   * phishing
   * safe

2. Text preprocessing:

   * Convert to lowercase
   * Remove special characters
   * Replace URLs with "url"

3. Feature extraction:

   * TF-IDF Vectorization

4. Model training:

   * Logistic Regression

5. Prediction:

   * Input email → Model → Result

---

## 📊 Model Performance

* Accuracy: ~90%+ (depends on dataset)
* Metrics:

  * Accuracy Score
  * Confusion Matrix

---

## ⚙️ Installation & Setup

### Clone Repository

```
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
```

---

### Install Dependencies

```
pip install flask scikit-learn pandas
```

---

### Train Model

```
python model.py
```

---

### Run App

```
python app.py
```

---

### Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Sample Input

```
URGENT! Your account has been compromised.
Click here: http://fake-link.com
```

Output:

```
⚠️ Phishing Email
```

---

## 🎯 Expected Outcome

* Detect phishing patterns
* Identify suspicious URLs
* Classify emails accurately

---

## 🔥 Future Improvements

* Use Random Forest / XGBoost
* Show confusion matrix in UI
* Upload .eml files
* Deploy online
* Add login system

---

## 🤝 Contributing

Fork the repo and submit pull requests.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Kishore R
Cybersecurity Enthusiast
