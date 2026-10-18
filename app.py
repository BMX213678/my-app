import streamlit as st
st.title("Phishing Scanner")
url = st.text_input('Enter a URL: ')
score = 0
if st.button("Check"):
    if len(url) > 75:
        score = score + 1
    if '@' in url:
        score = score + 1
    if url.count('.') > 3:
        score = score + 1
    if score > 0:
        st.error(f'phishing! score: {score}')
    else:
        st.success('safe url')
