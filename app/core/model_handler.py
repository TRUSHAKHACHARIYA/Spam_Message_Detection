import joblib
from app.config import settings

class ModelHandler:
    def __init__(self):
        self.model = joblib.load(settings.model_path)
        self.vectorizer = joblib.load(settings.vectorizer_path)

    def predict(self, text: str) -> str:
        text_vector = self.vectorizer.transform([text])
        pred = self.model.predict(text_vector)[0]
        return "Spam" if pred == 1 else "Ham"
