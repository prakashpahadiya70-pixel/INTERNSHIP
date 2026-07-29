import numpy as np

# -------------------------------
# Student Marks Analyzer
# -------------------------------

# Sample student marks
marks = np.array([78, 65, 89, 92, 55, 70, 81, 76, 68, 95])

print("========== Student Marks Analyzer ==========\n")

print("Student Marks:", marks)

# Basic Statistics
print(f"\nAverage Marks      : {np.mean(marks):.2f}")
print("Highest Marks      :", np.max(marks))
print("Lowest Marks       :", np.min(marks))
print("Total Marks        :", np.sum(marks))
print(f"Standard Deviation : {np.std(marks):.2f}")

# Pass / Fail Count
passed = np.sum(marks >= 35)
failed = np.sum(marks < 35)

print("\nPassed Students :", passed)
print("Failed Students :", failed)

# Grade Report
print("\n========== Grade Report ==========")

for i, mark in enumerate(marks, start=1):
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Student {i}: Marks = {mark} --> Grade = {grade}")

print("\n========== Analysis Completed ==========")