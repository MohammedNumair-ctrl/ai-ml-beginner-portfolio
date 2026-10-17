import streamlit as st

st.set_page_config(
    page_title="Herbal Interaction Checker",
    page_icon="🌿"
)

st.title("🌿 Herbal Medicine Interaction Checker")

st.write(
    "A small educational reference lookup prototype "
    "for herb and medication combinations."
)

st.warning(
    "Educational demo only. This is not a medical decision tool. "
    "Do not start, stop, or change medicines based on this app."
)

# Example reference records for demonstrating the application.
# Replace or expand these only with properly sourced evidence.
records = {
    ("St John's wort", "Oral contraceptives"): {
        "status": "Potential interaction documented",
        "note": (
            "St John's wort can reduce the effectiveness of some "
            "hormonal contraceptives."
        ),
        "source": "NCCIH: St. John's Wort and Depression"
    },
    ("Goldenseal", "Metformin"): {
        "status": "Potential interaction requiring review",
        "note": (
            "Goldenseal may affect how the body processes some "
            "medicines. This prototype does not establish a "
            "specific clinical interaction with metformin."
        ),
        "source": "NCCIH: Using Dietary Supplements Wisely"
    }
}

herb = st.selectbox(
    "Select an herb",
    ["St John's wort", "Goldenseal", "Turmeric", "Ashwagandha"]
)

medicine = st.selectbox(
    "Select a medicine",
    ["Oral contraceptives", "Metformin", "Blood pressure medicine"]
)

if st.button("Check reference"):
    result = records.get((herb, medicine))

    if result:
        st.subheader(result["status"])
        st.write(result["note"])
        st.caption("Reference to verify: " + result["source"])
    else:
        st.info(
            "No entry for this combination in the demo dataset. "
            "That does not mean the combination is safe."
        )

st.caption(
    "The dataset is incomplete and requires source verification "
    "before any real-world use."
)
