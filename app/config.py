from pydantic import BaseSettings

class Settings(BaseSettings):
    model_path: str = "saved_models/spam_classifier.pkl"
    vectorizer_path: str = "saved_models/tfidf_vectorizer.pkl"

settings = Settings()
