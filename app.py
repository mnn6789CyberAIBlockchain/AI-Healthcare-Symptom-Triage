
import streamlit as st

from nlp_engine import preprocess_text
from triage_engine import assess_symptoms


st.set_page_config(
    page_title="CarePilot AI",
    page_icon="🩺",
    layout="centered",
)

st.title("🩺 CarePilot AI")
st.subheader("NLP-Based Healthcare Symptom Assistant")

st.warning(
    "Educational prototype only — not a diagnosis or a medically validated "
    "triage tool. It can miss symptoms and emergencies. Do not use it to "
    "decide whether you are safe."
)

st.markdown(
    """
    Describe the symptoms in your own words. The app uses basic Python and
    NLP keyword matching to identify selected symptom terms and provide
    general educational guidance. No paid AI API is used.
    """
)

with st.form("symptom_form"):
    symptom_text = st.text_area(
        "What symptoms are you experiencing?",
        placeholder="Example: I have a headache and feel tired.",
        height=130,
    )

    submitted = st.form_submit_button(
        "Analyze symptoms",
        use_container_width=True,
    )

if submitted:
    if not symptom_text.strip():
        st.info("Please describe your symptoms first.")
    else:
        result = assess_symptoms(symptom_text)

        st.subheader("Assessment")

        if result["level"] == "Emergency warning":
            st.error(result["message"])
        elif result["level"] == "Medical advice":
            st.warning(result["message"])
        else:
            st.info(result["message"])

        st.write("**Matched symptoms:**")

        if result["symptoms"]:
            st.write(", ".join(result["symptoms"]))
        else:
            st.write("No symptoms matched the starter vocabulary.")

        with st.expander("View NLP processing details"):
            processed = preprocess_text(symptom_text)
            st.write("**Cleaned text:**", processed["cleaned_text"])
            st.write("**Tokens:**", processed["tokens"])
            st.write("**Processed tokens:**", processed["processed_tokens"])

st.divider()

st.caption(
    "CarePilot AI | Student project | Python, NLTK, and Streamlit"
)
