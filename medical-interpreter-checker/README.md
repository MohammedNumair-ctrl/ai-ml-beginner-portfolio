# Medical Interpreter Accuracy Checker

A Python and Streamlit prototype that flags configured phrases
present in an original statement but missing from a
back-translated statement.

## Run locally

    pip install streamlit
    streamlit run app.py

This prototype uses keyword matching. It does not validate
translation meaning or clinical accuracy.
