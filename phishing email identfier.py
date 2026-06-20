import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
data=pd.read_csv(r"D:\thiranex internship\project 3\email.csv")
x=data["text"]
y=data["label"]
vector=TfidfVectorizer()
xfeatures=vector.fit_transform(x)
xtrain , xtest , ytrain, ytest=train_test_split(
xfeatures,y
,test_size=0.3,
random_state=42,
stratify=y
)
model=MultinomialNB()
model.fit(xtrain,ytrain)
prediction=model.predict(xtest)
accuracy=accuracy_score(ytest,prediction)
print(" \n the accuracy of the model is : ", round(accuracy * 100 , 2),"%" )
print("the confusion matrix is: ")
print(confusion_matrix(ytest,prediction))
print("the classification report : ")
print(classification_report(ytest,prediction,zero_division=0))
print("Email content Tester: ")
email=input("enter the content in your email: ")
emailvector=vector.transform([email])
result=model.predict(emailvector)
print("the prediction is : ", result[0].upper())