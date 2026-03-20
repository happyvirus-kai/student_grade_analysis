import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_grade_analysis.csv")

print(df.head())

# Graph 1: Average GPA by Gender
df.groupby("Gender")["GPA"].mean().plot(kind="bar")
plt.title("Average GPA by Gender")
plt.savefig("gpa_by_gender.png")
plt.clf()

# Graph 2: GPA Distribution
df["GPA"].plot(kind="hist", bins=20)
plt.title("GPA Distribution")
plt.savefig("gpa_distribution.png")
plt.clf()

# Graph 3: Grade Class Distribution
df["GradeClass"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Grade Class Distribution")
plt.savefig("grade_class.png")
plt.clf()

# Bonus Graph
if "StudyTimeWeekly" in df.columns:
    plt.scatter(df["StudyTimeWeekly"], df["GPA"])
    plt.title("Study Time vs GPA")
    plt.savefig("study_vs_gpa.png")
    plt.clf()
