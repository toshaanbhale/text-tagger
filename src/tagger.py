import pickle
from src.preprocess import clean_text

class Tagger:
    def __init__(self):
        with open("models/model.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open("models/vectorizer.pkl", "rb") as f:
            self.vectorizer = pickle.load(f)

    def predict(self, text):
        text = clean_text(text)
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]
