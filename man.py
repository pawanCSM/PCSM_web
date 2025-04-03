import streamlit as st

name=st.text_input ("Enter your name: ")
em=st.text_input("Enter your email: ")
ph=st.text_input("Enter your phone number: ")
fname=st.text_input("Enter your father name:")
t=st.text_area("Enter your text:")
buttum=st.button("Don")
if buttum:
    st.markdown(f'''
    your name={name}\n
    your email={em}\n
    your phon number={ph}\n
    your father name={fname}\n
    text={t}''')


