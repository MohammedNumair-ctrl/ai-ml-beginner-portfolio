import re
import streamlit as st

st.set_page_config(
    page_title="Medical Interpreter Checker",
    page_icon="🩺"
)

st.title("Medical Interpreter Accuracy Checker")
st.write("A prototype for flagging potentially missing medical terms.")

st.warning(
    "Educational demo only. Not validated for clinical use. "
    "A qualified interpreter must review medical translations."
)

original = st.text_area(
    "Original statement",
    "Take the medication twice daily. Do not take it with food."
)

translated = st.text_area(
    "Back-translated statement",
    "Take the medication daily. Do not take it with food."
)

terms_input = st.text_input(
    "Terms to check (comma-separated)",
    "twice daily, do not, with food"
)


def contains_term(text, term):
    pattern = r"\b" + re.escape(term.strip()) + r"\b"
    return re.search(pattern, text, re.IGNORECASE) is not None


if st.button("Check statement"):
    if not original.strip() or not translated.strip():
        st.error("Enter both statements first.")
    else:
        terms = [
            term.strip()
            for term in terms_input.split(",")
            if term.strip()
        ]

        missing = [
            term for term in terms
            if contains_term(original, term)
            and not contains_term(translated, term)
        ]

        if missing:
            st.error("Potentially missing terms:")
            for term in missing:
                st.write(f"- {term}")
        else:
            st.success("No configured terms were flagged as missing.")

        st.caption(
            "This checks configured phrases, not medical meaning. "
            "It may miss changed dosages, negation, or paraphrases."
        )
