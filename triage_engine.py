
from nlp_engine import extract_symptoms


EMERGENCY_SYMPTOMS = {
    "chest pain",
    "shortness of breath",
}

URGENT_SYMPTOMS = {
    "fever",
    "vomiting",
}


def assess_symptoms(text: str) -> dict:
    """
    Provide conservative educational guidance.
    This is not a diagnosis or a validated medical triage tool.
    """

    symptoms = extract_symptoms(text)

    # Do not assume that no matched symptoms means no medical risk.
    if not text or not text.strip():
        return {
            "symptoms": [],
            "level": "Information needed",
            "message": "Please describe your symptoms.",
        }

    if any(symptom in symptoms for symptom in EMERGENCY_SYMPTOMS):
        return {
            "symptoms": symptoms,
            "level": "Emergency warning",
            "message": (
                "Chest pain or difficulty breathing can be an emergency. "
                "If this is happening now, call 911 or seek emergency care. "
                "Do not rely on this prototype to assess your safety."
            ),
        }

    if any(symptom in symptoms for symptom in URGENT_SYMPTOMS):
        return {
            "symptoms": symptoms,
            "level": "Medical advice",
            "message": (
                "Consider contacting a healthcare professional for advice, "
                "especially if symptoms are severe, persistent, or worsening."
            ),
        }

    return {
        "symptoms": symptoms,
        "level": "General guidance",
        "message": (
            "This prototype found limited symptom matches. It cannot determine "
            "the cause or severity of your symptoms. Seek medical advice if "
            "you are concerned, or if symptoms are severe or worsening."
        ),
    }
