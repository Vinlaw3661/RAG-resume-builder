import streamlit as st
import pandas as pd

top_biz_and_tech = pd.read_csv('toptechandbiz.csv')
underclassmen_internships = pd.read_csv('underclassmeninternships.csv')

st.title('Top Internships in Tech and Biz')
st.write(
    top_biz_and_tech
)


st.title('Underclassmen Internships')

st.write(
    underclassmen_internships
)
