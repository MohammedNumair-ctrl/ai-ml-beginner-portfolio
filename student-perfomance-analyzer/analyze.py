import pandas as pd

# Load the student mathematics dataset
df = pd.read_csv("student-mat.csv", sep=";")

print("\n===== STUDENT PERFORMANCE ANALYZER =====")
print("\nDataset shape (rows, columns):", df.shape)

print("\n===== FIRST 5 STUDENTS =====")
print(df.head())

print("\n===== DATASET INFORMATION =====")
print(df.info())

print("\n===== SUMMARY OF GRADES =====")
print(df[["G1", "G2", "G3"]].describe())

print("\n===== AVERAGE GRADES =====")
print(df[["G1", "G2", "G3"]].mean().round(2))

print("\n===== MISSING VALUES =====")
print(df.isnull().sum().sum())
