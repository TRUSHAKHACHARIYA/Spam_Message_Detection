import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords
import re

nltk.download("stopwords")

def load_data():
    data = pd.read_csv("https://raw.githubusercontent.com/ankurzing/sms-spam-classification/master/SMSSpamCollection", sep='\t', names=["label", "text"])
    data['label'] = data['label'].map({'ham': 0, 'spam': 1})
    return data

def clean_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text.lower())
    words = text.split()
    stop_words = set(stopwords.words("english"))
    return " ".join([w for w in words if w not in stop_words])

def train():
    df = load_data()
    df['text'] = df['text'].apply(clean_text)
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)
    tfidf = TfidfVectorizer()
    clf = MultinomialNB()
    X_train_vec = tfidf.fit_transform(X_train)
    X_test_vec = tfidf.transform(X_test)
    clf.fit(X_train_vec, y_train)
    preds = clf.predict(X_test_vec)
    acc = accuracy_score(y_test, preds)
    print(f"Accuracy: {acc:.4f}")
    joblib.dump(clf, "saved_models/spam_classifier.pkl")
    joblib.dump(tfidf, "saved_models/tfidf_vectorizer.pkl")

if __name__ == "__main__":
    train()
