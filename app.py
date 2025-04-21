import streamlit as st
from finance_data import get_financial_data
from analysis import generate_analysis
import pandas as pd

st.set_page_config(page_title="GPT-Aktien-Watchlist", layout="centered")
st.title("📊 GPT-basierte Aktienanalyse (Watchlist)")
st.write("Analysiere mehrere Aktien automatisiert mit GPT für Value- oder Growth-Investing")

tickers_input = st.text_input("Unternehmens-Ticker (kommagetrennt, z. B. VHI.TO, AAPL)", "VHI.TO, AAPL")
mode = st.selectbox("Analysemodus", ["value", "growth"])

if st.button("📈 Watchlist analysieren"):
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
    results = []
    
    for ticker in tickers:
        with st.spinner(f"Hole Daten & analysiere {ticker} ..."):
            try:
                data = get_financial_data(ticker)
                gpt_summary = generate_analysis(data, mode)

                # GPT-Analyseblock anzeigen
                st.subheader(f"📘 Analyse für {data['name']} ({ticker})")
                st.markdown(gpt_summary)

                # Ergebnisse sammeln für Tabelle
                results.append({
                    "Name": data["name"],
                    "Symbol": ticker,
                    "Kurs (USD)": f"${round(data['price'], 2)}" if data["price"] else "–",
                    "KGV (x)": round(data["peRatio"], 2) if data["peRatio"] else "–",
                    "KUV (x)": round(data["psRatio"], 2) if data["psRatio"] else "–",
                    "Cashflow (Mio)": f"{round(data['freeCashflow'] / 1e6, 1)} Mio" if data["freeCashflow"] else "–",
                    "Debt/Equity (%)": f"{round(data['debtToEquity'] * 100, 2)} %" if data["debtToEquity"] else "–",
                    "Bruttomarge (%)": round(data["grossMargins"] * 100, 2) if data["grossMargins"] else "–",
                    "EBITDA-Marge (%)": round(data["ebitdaMargins"] * 100, 2) if data["ebitdaMargins"] else "–",
                    "Nettomarge (%)": round(data["netMargin"] * 100, 2) if data["netMargin"] else "–",
                    "GPT-Fazit": gpt_summary.split("\n")[0][:100] + "..."
                })


            except Exception as e:
                st.error(f"⚠️ Fehler bei {ticker}: {e}")
    
    if results:
        st.subheader("📊 Übersicht aller Aktien in der Watchlist")
        df = pd.DataFrame(results)
        st.dataframe(df)
