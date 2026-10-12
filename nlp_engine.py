
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize


# Download the small NLTK resources needed for processing.
# These downloads are free and happen only when this setup runs.
def setup_nltk():
    resources = {
        "corpora/stopwords": "stopwords",
        "corpora/wordnet": "wordnet",
        "corpora/omw-1.4": "omw-1.4",
    }

    for resource_path, package_name in resources.items():
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(package_name, quiet=True)


setup_nltk()

# Preserve negation words because they can change symptom meaning.
NEGATION_WORDS = {"no", "not", "never", "without", "neither"}

STOP_WORDS = set(stopwords.words("english")) - NEGATION_WORDS

lemmatizer = WordNetLemmatizer()

# Starter vocabulary for text matching only.
# This is not a medically validated symptom dictionary.
SYMPTOM_VOCABULARY = {
    "fever": {"fever", "febrile"},
    "cough": {"cough", "coughing"},
    "headache": {"headache", "headaches"},
    "sore throat": {"sore throat", "throat pain"},
    "fatigue": {"fatigue", "tired", "tiredness", "exhaustion"},
    "nausea": {"nausea", "nauseous"},
    "vomiting": {"vomit", "vomiting", "threw up"},
    "diarrhea": {"diarrhea"},
    "shortness of breath": {
        "shortness of breath",
        "difficulty breathing",
        "trouble breathing",
        "breathlessness",
    },
    "chest pain": {"chest pain", "pain in my chest"},
}


def preprocess_text(text: str) -> dict:
    """Tokenize, normalize, remove stop words, and lemmatize text."""

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    cleaned_text = text.lower()
    cleaned_text = re.sub(r"[^a-z\s'-]", " ", cleaned_text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

    tokens = wordpunct_tokenize(cleaned_text)

    processed_tokens = []
    for token in tokens:
        if token in STOP_WORDS:
            continue

        if token.isalpha():
            token = lemmatizer.lemmatize(token)

        processed_tokens.append(token)

    return {
        "original_text": text,
        "cleaned_text": cleaned_text,
        "tokens": tokens,
        "processed_tokens": processed_tokens,
    }



def extract_symptoms(text: str) -> list:
    """Find symptom phrases while filtering simple nearby negations."""

    normalized_text = re.sub(
        r"\s+", " ", re.sub(r"[^a-z\s'-]", " ", text.lower())
    ).strip()

    found_symptoms = []

    for symptom, phrases in SYMPTOM_VOCABULARY.items():
        for phrase in sorted(phrases, key=len, reverse=True):
            pattern = r"(?<![a-z])" + re.escape(phrase) + r"(?![a-z])"

            for match in re.finditer(pattern, normalized_text):
                # Examine the few words immediately before the phrase.
                preceding_text = normalized_text[:match.start()]
                preceding_words = preceding_text.split()[-3:]

                # Ignore a match if a simple negation appears nearby.
                if any(word in NEGATION_WORDS for word in preceding_words):
                    continue

                found_symptoms.append(symptom)
                break

            if symptom in found_symptoms:
                break

    return found_symptoms

