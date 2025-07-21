import streamlit as st
import os


st.title('베포 테스트')
st.write('베포 테스트용 앱입니다.')

st.write('자동입니까?')

api_key  = os.environ.get("API_SECRET_KEY")

st.write(f'api key = {api_key}')