import streamlit as st

# Title of the web app
st.title("Simple Streamlit App")

# Add a slider widget
slider_value = st.slider("Select a value:", 0, 100, 50)

# Display the selected value
st.write(f"You selected: {slider_value}")

# Add a text input widget
text_input = st.text_input("Enter some text:", "Hello, Spandan")

# Display the entered text
st.write(f"You entered: {text_input}")