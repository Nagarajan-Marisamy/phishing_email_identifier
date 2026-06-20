# 📧 Phishing Email Detection using Machine Learning

## 🚀 Project Overview
This project is a simple **Phishing Email Detection System** built using **Python** and **Machine Learning**. The model is trained on email text data and classifies emails as either:

- **Phishing** ⚠️
- **Legitimate (Safe)** ✅

The project uses **TF-IDF Vectorization** for text feature extraction and **Multinomial Naive Bayes** for classification.

## 🎯 Features
- Load email dataset from CSV file
- Convert email text into numerical features using TF-IDF
- Train a Machine Learning model
- Evaluate model performance using Accuracy Score, Confusion Matrix, and Classification Report
- Predict whether a new email is phishing or legitimate

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn

## 📂 Project Structure
```text
Phishing-Email-Detection/
│
├── email.csv
├── phishing_detector.py
├── README.md
└── requirements.txt
```

## 📊 Dataset Format

| text | label |
|------|--------|
| Congratulations! You won a prize. Click here. | phishing |
| Meeting scheduled for tomorrow. | legitimate |

## ⚙️ Installation

```bash
pip install pandas scikit-learn
```

## ▶️ How to Run

```bash
python phishing_detector.py
```

## 🧠 Machine Learning Workflow
1. Load Dataset
2. Extract Features and Labels
3. Convert Text to Numerical Data using TF-IDF
4. Split Dataset into Training and Testing Sets
5. Train Model using Multinomial Naive Bayes
6. Evaluate Performance
7. Predict New Emails

## 📈 Sample Output

```text
The accuracy of the model is : 96.67 %

The confusion matrix is:
[[14 1]
 [0 15]]

The prediction is : PHISHING
```

## 🔒 Applications
- Email Security
- Spam Detection
- Cybersecurity Awareness
- Phishing Prevention Systems

## 🔮 Future Improvements
- Larger datasets
- GUI using Tkinter
- Flask web application
- Advanced NLP models
- URL analysis

## 👨‍💻 Author
**Nagarajan**

## 📜 License
MIT License
