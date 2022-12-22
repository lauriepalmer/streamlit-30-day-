import streamlit as st

st. header('st.latex')

st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} a^k=
a \left(\frac{1-r^{n}}{1-r}\right)
''')

