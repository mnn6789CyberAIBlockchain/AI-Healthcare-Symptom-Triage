# CarePilot AI by Tien Manh Nguyen

## Project Overview

CarePilot AI is an educational healthcare symptom assistant built with Python, NLTK, and Streamlit. It uses basic natural language processing (NLP) and keyword matching to identify selected symptom terms and display general educational guidance.

## Features

- Accepts symptom descriptions in natural language
- Tokenizes and preprocesses text using NLTK
- Removes common stop words while preserving selected negation words
- Lemmatizes tokens to normalize word forms
- Matches selected symptom phrases
- Applies simple rule-based guidance
- Displays an emergency warning when recognized chest pain or breathing difficulty terms are detected
- Shows NLP processing details for demonstration

## Technology Stack

- Python
- NLTK
- Streamlit
- `unittest` for automated testing

## Installation

1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment.
5. Install dependencies:

   `python -m pip install -r requirements.txt`

6. Run the application:

   `python -m streamlit run app.py`

## Project Files

- `app.py`: Streamlit user interface
- `nlp_engine.py`: Text preprocessing and symptom matching
- `triage_engine.py`: Rule-based educational guidance
- `test_app.py`: Automated unit tests
- `requirements.txt`: Python dependencies

## Testing

Run the automated test suite with:

`python -m unittest -v test_app.py`

The tests cover symptom matching, basic negation handling, NLP preprocessing, empty input, and rule-based guidance for selected symptoms.

These tests verify expected software behavior for the included examples. They do not establish clinical accuracy or validate the application for medical use.

## Limitations and Safety

CarePilot AI is a classroom prototype, not a diagnostic system or medically validated triage tool. Its symptom vocabulary, keyword matching, and negation handling are limited. It may miss symptoms, misinterpret descriptions, or fail to recognize emergencies.

**Do not use this application to make medical decisions or to rule out an urgent condition.** If you believe you are experiencing a medical emergency, seek emergency medical assistance rather than relying on this application.

## Author

Tien Manh Nguyen

Student project for ITAI 2372.
