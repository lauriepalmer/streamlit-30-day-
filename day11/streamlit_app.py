import streamlit as st

st.header ('st.multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Violet', 'Blue'],
    ['Yellow', 'Violet'])

st.write('You selected:', options)


