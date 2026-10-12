# Research: AI-Powered Symptom Checkers and Triage

**Project:** CarePilot AI  
**Author:** Tien Manh Nguyen  
**Course:** ITAI 2372

## 1. Introduction

Artificial intelligence (AI) and natural language processing (NLP) are increasingly being explored for healthcare applications. One example is the digital symptom checker, which allows users to describe their symptoms and receive information or guidance about possible next steps.

These tools may help people access health information and navigate healthcare services. However, they must be designed carefully because incorrect symptom interpretation or triage recommendations could affect patient decisions.

CarePilot AI is a small educational prototype inspired by this type of healthcare technology. It demonstrates how NLP preprocessing, symptom matching, and rule-based logic can be combined in a web application.

## 2. Existing Research on Symptom Checkers

Semigran and colleagues evaluated 23 symptom checkers in a study published in *The BMJ* in 2015. Across 532 standardized case evaluations involving triage recommendations, the tools provided appropriate triage advice in 57% of evaluations. Performance varied depending on the urgency and characteristics of the cases.

The study illustrates why symptom checkers should not automatically be assumed to provide accurate medical guidance. Their recommendations require careful evaluation, especially when users may have urgent or serious conditions.

A systematic review published in *npj Digital Medicine* in 2022 also examined the diagnostic and triage accuracy of digital symptom checkers. The authors found that diagnostic accuracy was generally limited and that triage performance varied considerably between tools and studies.

Together, these studies highlight the importance of evaluating symptom-checking systems rather than judging them solely by whether they produce an answer.

## 3. How NLP Can Support Symptom Analysis

NLP allows computer programs to process and analyze human language. In a symptom checker, a user might enter a sentence such as "I have a headache and feel tired."

A basic NLP pipeline can include:

1. **Tokenization:** Splitting the sentence into individual words or tokens.
2. **Stop-word removal:** Removing selected common words while preserving meaningful terms, including negations such as "not."
3. **Lemmatization:** Converting words into normalized forms where appropriate.
4. **Symptom matching:** Comparing the processed text with a predefined vocabulary of symptom phrases.
5. **Rule-based guidance:** Applying predefined rules to determine what educational guidance the application displays.

CarePilot AI demonstrates these techniques using Python, NLTK, and Streamlit. Its symptom matching and guidance are based on predefined rules rather than a trained medical prediction model or a clinically validated knowledge base.

Consequently, the application demonstrates basic NLP concepts but does not establish a likely diagnosis or determine a medically validated level of urgency.

## 4. Benefits and Limitations

### Potential benefits

- Provides an interactive way to explore general health information.
- Demonstrates how computers can process natural-language descriptions.
- Makes NLP concepts accessible through a simple web interface.
- Shows how predefined rules can connect symptom matching with educational guidance.

### Limitations and risks

- **Incomplete vocabulary:** The application recognizes only selected symptoms and may miss unfamiliar descriptions.
- **Context and negation:** Simple keyword matching can misunderstand complex sentences or the relationships between symptoms.
- **Potentially incorrect guidance:** A matching rule does not establish the user's medical condition or actual level of urgency.
- **Limited validation:** Passing software tests demonstrates expected behavior for tested examples, not clinical accuracy.
- **Bias and accessibility:** Healthcare technologies need evaluation across different populations, language patterns, and user needs.

CarePilot AI should therefore be considered a classroom demonstration, not a replacement for professional medical assessment.

## 5. Ethical Considerations

The World Health Organization's guidance on ethics and governance of AI for health emphasizes human autonomy, safety, transparency, accountability, and protection of privacy.

These principles are relevant to symptom-checking applications. Users should understand the limitations of automated guidance, and medical decisions should not be delegated to an unvalidated program.

CarePilot AI includes a safety disclaimer and does not require a paid AI service. Its design should continue to avoid presenting rule-based results as confirmed diagnoses. Any future version intended for real healthcare use would require much more extensive clinical evaluation, privacy safeguards, and appropriate oversight.

## 6. Connection to CarePilot AI

This research informed the design goals of CarePilot AI: demonstrate a simple NLP workflow, provide transparent rule-based guidance, and communicate the limitations of automated symptom analysis.

The project uses NLTK for text preprocessing and symptom matching, Python for rule-based logic, and Streamlit for the user interface. Automated tests check selected examples, including symptom matching, basic negation handling, empty input, and expected guidance categories.

These tests are software checks only. They do not measure diagnostic accuracy, establish clinical safety, or validate the application for use with patients.

## 7. Conclusion

AI-powered symptom checkers are a useful area for studying the opportunities and challenges of AI in healthcare. Research shows that their diagnostic and triage performance can vary, making validation and responsible design essential.

CarePilot AI provides a small, understandable demonstration of NLP and rule-based symptom guidance. Its main purpose is educational: to show how a healthcare-related AI application can be developed while recognizing the limitations and ethical responsibilities involved.

## References

1. Semigran, H. L., Linder, J. A., Gidengil, C., and Mehrotra, A. (2015). “Evaluation of symptom checkers for self diagnosis and triage: audit study.” *The BMJ*, 351, h3480. https://www.bmj.com/content/351/bmj.h3480

2. Wallace, W., Chan, C., Chidambaram, S., et al. (2022). “The diagnostic and triage accuracy of digital and online symptom checker tools: a systematic review.” *npj Digital Medicine*, 5, 118. https://pmc.ncbi.nlm.nih.gov/articles/PMC9385087/

3. World Health Organization. (2021). *Ethics and governance of artificial intelligence for health: WHO guidance.* https://www.who.int/publications/i/item/9789240029200
