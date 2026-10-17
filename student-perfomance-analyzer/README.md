# Student Performance Analyzer

An exploratory data analysis project built with Python, Pandas,
Matplotlib, and Streamlit using the UCI Student Performance dataset.

## Features

- Summarizes student records and final mathematics grades.
- Visualizes the distribution of final grades.
- Compares average final grades across reported study-time categories.
- Provides an interactive dashboard with filters.
- Allows users to inspect the dataset.

## Technologies

- Python
- Pandas
- Matplotlib
- Streamlit

## Dataset

The project uses the Student Performance dataset from the UCI
Machine Learning Repository.

Source: https://archive.ics.uci.edu/dataset/320/student+performance

This version uses `student-mat.csv`, containing 395 student records
and 33 columns.

## Run Locally

1. Clone or download this repository.
2. Install Python 3.
3. Create and activate a virtual environment.
4. Install the dependencies:

   `pip install pandas matplotlib streamlit`

5. Place `student-mat.csv` in the project folder.
6. Run the analysis script:

   `python3 analyze.py`

7. Launch the dashboard:

   `streamlit run app.py`

## Project Structure

- `analyze.py` — basic dataset analysis and summary statistics
- `visualize.py` — generates two visualization images
- `app.py` — interactive Streamlit dashboard
- `student-mat.csv` — dataset file
- `grade_distribution.png` — final grade distribution
- `studytime_vs_final_grade.png` — study time comparison

## Limitations

This project explores associations in an educational dataset.
It does not establish causation, predict individual student outcomes,
or provide evidence that study time alone determines grades.
The dataset reflects a particular study context and may not generalize
to all students or educational systems.

## Author

Mohammed Numair — First-year B.Tech CSE (AI/ML) student.
