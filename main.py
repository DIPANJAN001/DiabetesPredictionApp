import streamlit as st
import model


# Title of the web app
st.title("Diabetes predictor")
st.write("Dipanjan's diabetes prediction app")
# Add a slider widget
age = st.slider("Age:", 0, 105, 50)
bmi = st.slider("bmi:",0, 50, 10)
glu = st.slider("Sugar level:", 0, 300, 120)
bp = st.slider("blood pressure:", 0, 200, 120)

hasDiabetes=model.predict_diabetes(glu,bmi,bp,age)


# Display the entered text
msg="predicting"
if hasDiabetes <0.4:
    msg="you have less chance having diabetes"
elif hasDiabetes<0.75:
    msg="you have mild  chance having diabetes,pls consult doctor"
else:
    msg="Dude you are swrewed.visit doctor right now"

st.write(f"comment :{msg}")
st.write(f"Probability of Diabetes: {round(hasDiabetes*100)} %")
