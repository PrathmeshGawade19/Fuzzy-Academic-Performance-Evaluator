# Fuzzy-Academic-Performance-Evaluator

# 🎓 Fuzzy Academic Performance Evaluator

A fuzzy logic–based intelligent system to evaluate student academic performance using multiple holistic parameters such as marks, attendance, behavior, discipline, project work, and class participation.

---

## Features

- **Multi-parameter Evaluation:** Considers academic and behavioral aspects:
  - Attendance
  - Internal Marks
  - External Marks
  - Behavior
  - Discipline
  - Project/Assignment Score
  - Class Participation
- **Fuzzy Logic Model:** Built using `scikit-fuzzy` with trapezoidal membership functions
- **Graded Output:** Numerical performance score mapped to grades like A+, A, B, etc.
- **Explainability:** Outputs natural language explanation for each prediction
- **Streamlit GUI:** Interactive user interface for easy input and visualization

---

## Technologies Used

- Python 3.10+
- [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy)
- Streamlit
- NumPy
- matplotlib

---

## Inputs Description
Parameter	Range	Description
Attendance	0–100	Attendance percentage
Internal Marks	0–100	Average internal assessment score
External Marks	0–100	External university exam score
Behavior	0–100	General classroom behavior score
Discipline	0–100	Adherence to rules and regulations
Project Score	0–100	Project or assignment performance
Class Participation	0–100	Involvement in classroom activities

---

## Output
Performance Score: Numerical value (0–100)
Grade Mapping:
A+ : 85–100
A : 75–84
B : 60–74
C : 45–59
D : <45

---

## 📌 Conclusion
This system offers a transparent, holistic, and explainable approach to assessing student performance using fuzzy logic principles. It enhances traditional grading by incorporating behavioral and participatory metrics along with academics.
