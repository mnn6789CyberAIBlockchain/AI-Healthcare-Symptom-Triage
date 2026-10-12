
import unittest

from nlp_engine import preprocess_text, extract_symptoms
from triage_engine import assess_symptoms


class TestCarePilotNLP(unittest.TestCase):
    """Test CarePilot AI text preprocessing and symptom matching."""

    def test_headache_and_fatigue(self):
        result = extract_symptoms("I have headaches and feel tired")
        self.assertIn("headache", result)
        self.assertIn("fatigue", result)

    def test_negated_headache(self):
        result = extract_symptoms("I do not have a headache")
        self.assertNotIn("headache", result)

    def test_negated_chest_pain_contraction(self):
        result = extract_symptoms("I don't have chest pain")
        self.assertNotIn("chest pain", result)

    def test_cough_without_fever(self):
        result = extract_symptoms("I have a cough but no fever")
        self.assertIn("cough", result)
        self.assertNotIn("fever", result)

    def test_preprocessing_returns_tokens(self):
        result = preprocess_text("I have headaches and feel tired")
        self.assertIn("tokens", result)
        self.assertIn("processed_tokens", result)
        self.assertIn("headache", result["processed_tokens"])

    def test_chest_pain_triggers_emergency_warning(self):
        result = assess_symptoms("I have chest pain")
        self.assertEqual(result["level"], "Emergency warning")

    def test_fever_triggers_medical_advice(self):
        result = assess_symptoms("I have a fever")
        self.assertEqual(result["level"], "Medical advice")

    def test_headache_gets_general_guidance(self):
        result = assess_symptoms("I have a headache")
        self.assertEqual(result["level"], "General guidance")

    def test_empty_input_requests_information(self):
        result = assess_symptoms("")
        self.assertEqual(result["level"], "Information needed")


    def test_breathing_difficulty_triggers_emergency_warning(self):
        result = assess_symptoms("I have difficulty breathing")
        self.assertEqual(result["level"], "Emergency warning")
        self.assertIn("shortness of breath", result["symptoms"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
