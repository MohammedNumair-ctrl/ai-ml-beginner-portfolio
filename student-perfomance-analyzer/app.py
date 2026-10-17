import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("student-mat.csv", sep=";")

df = load_data()

st.title("📊 Student Performance Analyzer")
st.write(
    "An exploratory data analysis dashboard using "
    "the UCI Student Performance dataset."
)

st.info(
    "This dataset contains anonymized student records. "
    "The patterns shown are associations, not proof of causation."
)

# Key metrics
col1, col2, col3 = st.columns(3)
col1.metric("Students", len(df))
col2.metric("Average final grade", f"{df['G3'].mean():.2f} / 20")
col3.metric("Missing values", int(df.isnull().sum().sum()))

st.divider()

# Filter by study time
st.subheader("Explore study time and grades")

study_labels = {
    1: "Less than 2 hours",
    2: "2–5 hours",
    3: "5–10 hours",
    4: "Over 10 hours"
}

selected = st.multiselect(
    "Select weekly study-time categories",
    options=[1, 2, 3, 4],
    default=[1, 2, 3, 4],
    format_func=lambda x: study_labels[x]
)

filtered = df[df["studytime"].isin(selected)]

if not filtered.empty:
    averages = filtered.groupby("studytime")["G3"].mean()

    chart_data = pd.DataFrame({
        "Study time": [
            study_labels[i] for i in averages.index
        ],
        "Average final grade": averages.values
    }).set_index("Study time")

    st.bar_chart(chart_data)

    st.write(f"Students in selected categories: {len(filtered)}")
else:
    st.warning("Select at least one study-time category.")

st.divider()

# Grade distribution
st.subheader("Final grade distribution")
fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(df["G3"], bins=range(0, 22), edgecolor="black")
ax.set_xlabel("Final grade (out of 20)")
ax.set_ylabel("Number of students")
ax.set_xticks(range(0, 21, 2))
st.pyplot(fig)
plt.close(fig)

# Raw data preview
with st.expander("View dataset"):
    st.dataframe(df, use_container_width=True)

st.caption(
    "Educational project by Mohammed Numair | "
    "Python • Pandas • Matplotlib • Streamlit"
)
