
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
    """
    Match known symptom phrases and filter simple nearby negations.

    This is a basic keyword heuristic, not medical language understanding.
    It may misinterpret contractions, sentence structure, and context.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    normalized_text = re.sub(
        r"\s+", " ", re.sub(r"[^a-z\s'-]", " ", text.lower())
    ).strip()

    # Normalize common negation contractions before matching.
    normalized_text = re.sub(r"\bdon't\b", "do not", normalized_text)
    normalized_text = re.sub(r"\bdoesn't\b", "does not", normalized_text)
    normalized_text = re.sub(r"\bdidn't\b", "did not", normalized_text)
    normalized_text = re.sub(r"\bcan't\b", "cannot", normalized_text)
    normalized_text = re.sub(r"\bcannot\b", "not", normalized_text)
    normalized_text = re.sub(r"\bwon't\b", "will not", normalized_text)
    normalized_text = re.sub(r"\bisn't\b", "is not", normalized_text)
    normalized_text = re.sub(r"\baren't\b", "are not", normalized_text)
    normalized_text = re.sub(r"\bwasn't\b", "was not", normalized_text)
    normalized_text = re.sub(r"\bweren't\b", "were not", normalized_text)
    normalized_text = re.sub(r"\bhaven't\b", "have not", normalized_text)
    normalized_text = re.sub(r"\bhasn't\b", "has not", normalized_text)

    found_symptoms = []

    for symptom, phrases in SYMPTOM_VOCABULARY.items():
        for phrase in sorted(phrases, key=len, reverse=True):
            pattern = r"(?<![a-z])" + re.escape(phrase) + r"(?![a-z])"

            for match in re.finditer(pattern, normalized_text):
                # Check the three words immediately before the match.
                preceding_words = normalized_text[:match.start()].split()[-3:]

                # Skip this match when a simple negation appears nearby.
                if any(word in NEGATION_WORDS for word in preceding_words):
                    continue

                found_symptoms.append(symptom)
                break

            if symptom in found_symptoms:
                break

    return found_symptoms

