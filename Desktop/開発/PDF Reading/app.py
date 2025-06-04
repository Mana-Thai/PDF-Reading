import streamlit as st
import pdfplumber

st.set_page_config(page_title="PDF テキスト抽出", layout="centered")
st.title("PDF ドラッグ＆ドロップでテキスト化")

uploaded_file = st.file_uploader("PDFファイルをドロップしてください", type=["pdf"])

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text() or ""
    st.subheader("抽出されたテキスト：")
    st.text_area("PDFテキスト", value=all_text, height=400)
