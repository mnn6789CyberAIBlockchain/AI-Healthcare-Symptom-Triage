
# CarePilot AI

## Project Overview
CarePilot AI is an educational healthcare symptom assistant built with Python, NLTK, and Streamlit. It uses basic natural language processing and keyword matching to identify selected symptom terms and display general educational guidance.

## Features
- Accepts symptom descriptions in natural language
- Tokenizes and preprocesses text using NLTK
- Removes common stop words and lemmatizes tokens
- Matches selected symptom phrases
- Applies simple rule-based guidance
- Displays an emergency warning for recognized chest pain or breathing difficulty terms
- Shows NLP processing details for demonstration

## Technology Stack
- Python
- NLTK
- Streamlit

## Installation
1. Install Python.
2. Clone or download this repository.
3. Create and activate a virtual environment.
4. Install dependencies:

   `python -m pip install -r requirements.txt`

5. Run the app:

   `python -m streamlit run app.py`

## Project Files
- `app.py`: Streamlit interface
- `nlp_engine.py`: Text preprocessing and symptom matching
- `triage_engine.py`: Rule-based educational guidance
- `requirements.txt`: Python dependencies

## Limitations and Safety
This project is a classroom prototype, not a diagnosis system or medically validated triage tool. Its vocabulary and negation handling are limited. It may miss symptoms, misinterpret descriptions, or fail to recognize emergencies. It must not be used to make medical decisions or rule out urgent conditions.

## Author
Student project for ITAI 2372.
