import streamlit as st

st.title('st.form')

st.header('1. Example of using `with`notation')
st.subheader('milk machine')

with st.form('my_form'):
    st.subheader('**Order your Milk**')

    milk_val = st.selectbox('Milk', ['Angus', 'Jersey'])
    milk_val = st.selectbox('Milk roast', ['Light', 'Medium', 'Dark',])
    brewing_val = st.selectbox('Brewing method', ['fresh', 'fridge', 'pan', 'stove', 'microwave'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val  = st.checkbox('Bring own cup')

    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        You have ordered:
        -Milk kind: `{milk_kind_val}`
        -Milk roast: `{milk_roast_val}`
        -Brewing: `{brewing_val}`
        -Milk: `{milk_val}`
        -Bring own cup: `{owncup_val}`
        ''')

else:
    st.write('Place your order!')
   
st.header('2. Example of object notaion')

form = st.form('my_form_2')
selected_val =  form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
