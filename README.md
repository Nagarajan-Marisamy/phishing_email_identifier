📧 Phishing Email Detection using Machine Learning
🚀 Project Overview

This project is a simple Phishing Email Detection System built using Python and Machine Learning. The model is trained on email text data and classifies emails as either:

Phishing ⚠️
Legitimate (Safe) ✅

The project uses TF-IDF Vectorization for text feature extraction and Multinomial Naive Bayes for classification.

🎯 Features
Load email dataset from CSV file
Convert email text into numerical features using TF-IDF
Train a Machine Learning model
Evaluate model performance using:
Accuracy Score
Confusion Matrix
Classification Report
Predict whether a new email is phishing or legitimate
🛠️ Technologies Used
Python
Pandas
Scikit-learn
Libraries
pandas
scikit-learn
📂 Project Structure
Phishing-Email-Detection/
│
├── email.csv
├── phishing_detector.py
├── README.md
└── requirements.txt
📊 Dataset Format

The CSV file should contain two columns:

text	label
Congratulations! You won a prize. Click here.	phishing
Meeting scheduled for tomorrow.	legitimate

Example:

text,label
"Congratulations! Claim your reward now.",phishing
"Please find the attached report.",legitimate
⚙️ Installation
1. Clone the Repository
git clone https://github.com/yourusername/Phishing-Email-Detection.git
2. Navigate to Project Folder
cd Phishing-Email-Detection
3. Install Required Packages
pip install pandas scikit-learn
▶️ How to Run

Run the Python file:

python phishing_detector.py
🧠 Machine Learning Workflow
Step 1: Load Dataset
data = pd.read_csv("email.csv")

Reads email data from the CSV file.

Step 2: Extract Features and Labels
x = data["text"]
y = data["label"]
x → Email content
y → Email category
Step 3: Convert Text to Numerical Data
vector = TfidfVectorizer()
xfeatures = vector.fit_transform(x)

TF-IDF converts text into machine-readable numerical vectors.

Step 4: Split Dataset
train_test_split()
70% Training Data
30% Testing Data
Step 5: Train Model
model = MultinomialNB()
model.fit(xtrain, ytrain)

Uses the Naive Bayes algorithm for text classification.

Step 6: Evaluate Model
accuracy_score()
confusion_matrix()
classification_report()

Performance metrics are displayed after testing.

Step 7: Predict New Emails
email = input("Enter email content:")

Users can enter any email text and receive a prediction.

📈 Sample Output
The accuracy of the model is : 96.67 %

The confusion matrix is:
[[14  1]
 [ 0 15]]

The classification report:
              precision    recall  f1-score   support

 legitimate       1.00      0.93      0.97        15
 phishing         0.94      1.00      0.97        15

Email content Tester:
Enter the content in your email:
Claim your account reward now

The prediction is : PHISHING
🔒 Applications
Email Security
Spam Detection
Cybersecurity Awareness
Phishing Prevention Systems
🔮 Future Improvements
Use larger datasets
Add GUI using Tkinter
Deploy as a web application using Flask
Use advanced NLP models
Add URL and attachment analysis
👨‍💻 Author

Nagarajan

Cybersecurity & Python Enthusiast

📜 License

This project is open-source and available under the MIT License.
