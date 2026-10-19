import streamlit as st

st.title("Week 1 - Question 9 Layout")
st.write("Pin-to-Row Connections:")

data = {
    "Component": ["Red LED", "Green LED"],
    "Arduino Pin": ["Pin 8", "Pin 9"],
    "Breadboard Row": ["Row 5", "Row 25"],
    "Resistor": ["330 Ω", "330 Ω"]
}

st.table(data)
