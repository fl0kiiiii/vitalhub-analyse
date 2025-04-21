def get_financial_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    revenue = info.get("totalRevenue")
    net_income = info.get("netIncome")
    gross_margins = info.get("grossMargins")
    ebitda_margins = info.get("ebitdaMargins")

    data = {
        "name": info.get("longName"),
        "symbol": ticker,
        "price": info.get("currentPrice"),
        "marketCap": info.get("marketCap"),
        "revenue": revenue,
        "netIncome": net_income,
        "peRatio": info.get("trailingPE"),
        "psRatio": info.get("priceToSalesTrailing12Months"),
        "freeCashflow": info.get("freeCashflow"),
        "grossMargins": gross_margins,
        "ebitdaMargins": ebitda_margins,
        "netMargin": (net_income / revenue) if net_income and revenue else None,
        "debtToEquity": info.get("debtToEquity"),
        "beta": info.get("beta"),
        "sector": info.get("sector"),
        "summary": info.get("longBusinessSummary"),
    }

    return data
