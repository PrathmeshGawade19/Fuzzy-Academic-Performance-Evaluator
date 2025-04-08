import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st

# Define input ranges
x_range = np.arange(0, 101, 1)

# Create Antecedents and Consequent
attendance = ctrl.Antecedent(x_range, 'Attendance')
internal = ctrl.Antecedent(x_range, 'Internal')
external = ctrl.Antecedent(x_range, 'External')
behavior = ctrl.Antecedent(x_range, 'Behavior')
discipline = ctrl.Antecedent(x_range, 'Discipline')
project = ctrl.Antecedent(x_range, 'Project')
participation = ctrl.Antecedent(x_range, 'Participation')
performance = ctrl.Consequent(x_range, 'Performance')

# Membership functions
for ant in [attendance, internal, external, behavior, discipline, project, participation]:
    ant['Poor'] = fuzz.trimf(x_range, [0, 0, 50])
    ant['Average'] = fuzz.trimf(x_range, [30, 50, 70])
    ant['Good'] = fuzz.trimf(x_range, [50, 70, 90])
    ant['Excellent'] = fuzz.trimf(x_range, [70, 100, 100])

performance['Poor'] = fuzz.trimf(x_range, [0, 0, 50])
performance['Average'] = fuzz.trimf(x_range, [30, 50, 70])
performance['Good'] = fuzz.trimf(x_range, [50, 70, 90])
performance['Excellent'] = fuzz.trimf(x_range, [70, 100, 100])

# Rules
rules = [
    ctrl.Rule(attendance['Excellent'] & internal['Excellent'] & external['Excellent'] &
              behavior['Excellent'] & discipline['Excellent'] &
              project['Excellent'] & participation['Excellent'],
              performance['Excellent']),

    ctrl.Rule(attendance['Good'] & internal['Good'] & external['Good'] &
              behavior['Good'] & discipline['Good'] &
              project['Good'] & participation['Good'],
              performance['Good']),

    ctrl.Rule(attendance['Average'] & internal['Average'] & external['Average'] &
              behavior['Average'] & discipline['Average'] &
              project['Average'] & participation['Average'],
              performance['Average']),

    ctrl.Rule(attendance['Poor'] | internal['Poor'] | external['Poor'] |
              behavior['Poor'] | discipline['Poor'] |
              project['Poor'] | participation['Poor'],
              performance['Poor'])
]

# Control System
performance_ctrl = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(performance_ctrl)

# Streamlit UI
st.title("📊 Fuzzy Academic Performance Evaluator")

# Sliders for input
att = st.slider("Attendance", 0, 100, 75)
intr = st.slider("Internal Marks", 0, 100, 65)
extr = st.slider("External Marks", 0, 100, 70)
beh = st.slider("Behavior", 0, 100, 80)
disc = st.slider("Discipline", 0, 100, 85)
proj = st.slider("Project / Assignment Score", 0, 100, 75)
part = st.slider("Class Participation", 0, 100, 70)

# Set inputs
sim.input['Attendance'] = att
sim.input['Internal'] = intr
sim.input['External'] = extr
sim.input['Behavior'] = beh
sim.input['Discipline'] = disc
sim.input['Project'] = proj
sim.input['Participation'] = part

# Compute
try:
    sim.compute()
    perf_score = sim.output['Performance']

    # Grading
    def map_grade(score):
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B+"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        else:
            return "F"

    grade = map_grade(perf_score)

    # Explanation
    explanation = f"""
    Student has {map_grade(att)} attendance, {map_grade(intr)} internal marks, 
    {map_grade(extr)} external marks, {map_grade(beh)} behavior, 
    {map_grade(disc)} discipline, {map_grade(proj)} project performance, 
    and {map_grade(part)} participation. Overall performance is {grade}.
    """

    st.success(f"🎯 Performance Score: {perf_score:.2f} → Grade: **{grade}**")
    st.info(explanation.strip())

except Exception as e:
    st.error(f"Error: {e}")


 
#To run in vs code terminal - streamlit run fuzzy_performance_app.py
