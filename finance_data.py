import yfinance as yf

def get_financial_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    data = {
        "name": info.get("longName"),
        "symbol": ticker,
        "price": info.get("currentPrice"),
        "marketCap": info.get("marketCap"),
        "revenue": info.get("totalRevenue"),
        "peRatio": info.get("trailingPE"),
        "psRatio": info.get("priceToSalesTrailing12Months"),
        "freeCashflow": info.get("freeCashflow"),
        "grossMargins": info.get("grossMargins"),
        "ebitda": info.get("ebitda"),
        "ebitdaMargins": info.get("ebitdaMargins"),
        "debtToEquity": info.get("debtToEquity"),
        "beta": info.get("beta"),
        "sector": info.get("sector"),
        "summary": info.get("longBusinessSummary"),
    }

    return data
