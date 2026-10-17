import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep=";")

# Graph 1: Distribution of final grades
plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=range(0, 22), edgecolor="black")
plt.title("Distribution of Final Mathematics Grades")
plt.xlabel("Final Grade (G3), out of 20")
plt.ylabel("Number of Students")
plt.xticks(range(0, 21, 2))
plt.tight_layout()
plt.savefig("grade_distribution.png", dpi=150)
plt.close()

# Graph 2: Study time and average final grade
study_labels = {
    1: "Less than 2 hours",
    2: "2–5 hours",
    3: "5–10 hours",
    4: "Over 10 hours"
}

average_grades = df.groupby("studytime")["G3"].mean()
average_grades.index = [
    study_labels[i] for i in average_grades.index
]

plt.figure(figsize=(8, 5))
average_grades.plot(kind="bar", edgecolor="black")
plt.title("Study Time vs Average Final Grade")
plt.xlabel("Weekly Study Time")
plt.ylabel("Average Final Grade (out of 20)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("studytime_vs_final_grade.png", dpi=150)
plt.close()

print("Visualizations created successfully!")
print("Saved: grade_distribution.png")
print("Saved: studytime_vs_final_grade.png")
print("\nAverage final grade by study-time category:")
print(average_grades.round(2))
