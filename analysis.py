import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_analysis(data, mode="growth"):
    # Fallbacks für fehlende Werte
    safe = lambda key: data.get(key, "–")

    # Einzelne Werte ggf. mit Prüfung/Umrechnung
    ebitda = safe("ebitda")
    gross_margin = round(safe("grossMargins") * 100, 2) if isinstance(safe("grossMargins"), (int, float)) else "–"
    ebitda_margin = round(safe("ebitdaMargins") * 100, 2) if isinstance(safe("ebitdaMargins"), (int, float)) else "–"
    net_margin = round(safe("netMargin") * 100, 2) if isinstance(safe("netMargin"), (int, float)) else "–"

    # GPT-Prompt
    prompt = f"""
        You are a financial analyst assistant. Based on the following fundamental data of a company, write a clear and concise analysis in English, from the perspective of a {mode}-investor. Conclude with a short recommendation: whether the current stock price is attractive or not, and suggest a fair value range if possible.
        
        Company: {safe("name")} ({safe("symbol")})
        Current Price: {safe("price")}
        Market Cap: {safe("marketCap")}
        P/E Ratio: {safe("peRatio")}
        P/S Ratio: {safe("psRatio")}
        Free Cash Flow: {safe("freeCashflow")}
        Gross Margin: {gross_margin} %
        EBITDA: {ebitda}
        EBITDA Margin: {ebitda_margin} %
        Net Margin: {net_margin} %
        Debt-to-Equity Ratio: {safe("debtToEquity")}
        Sector: {safe("sector")}
        
        Business Summary: {safe("summary")}
    """

    # Anfrage an GPT senden
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
