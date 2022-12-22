import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Oreo Milkshake')

if icecream:
    st.write("Great! Here's some more :icecream:")

if coffee:
    st.write("Okay, no coffee :coffee:")

if cola:
    st.write("Oreo milkshake :cup_with_straw:")

