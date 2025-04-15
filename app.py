import streamlit as st
from finance_data import get_financial_data
from analysis import generate_analysis

st.set_page_config(page_title="Stock Analyzer", layout="centered")

st.title("📊 GPT-basierte Aktienanalyse")
st.write("Automatisierte Fundamentalanalyse für Value- und Growth-Investing")

ticker = st.text_input("Unternehmens-Ticker eingeben (z. B. VHI.TO)", "VHI.TO")
mode = st.selectbox("Analysemodus", ["value", "growth"])

if st.button("📈 Analyse starten"):
    with st.spinner("Hole Finanzdaten und analysiere..."):
        financials = get_financial_data(ticker)
        gpt_analysis = generate_analysis(financials, mode)

    st.subheader(f"Analyse für {financials['name']}")
    st.markdown(gpt_analysis)
