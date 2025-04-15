import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_analysis(financials, mode="value"):
    prompt = f"""
You are a financial analyst. Analyze the stock {financials['name']} ({financials['symbol']}) with the following metrics:
- Current price: {financials['price']} CAD
- Market Cap: {financials['marketCap']}
- Revenue: {financials['revenue']}
- P/E Ratio: {financials['peRatio']}
- P/S Ratio: {financials['psRatio']}
- Free Cash Flow: {financials['freeCashflow']}
- EBITDA: {financials['ebitda']}
- Gross Margin: {financials['grossMargins']}
- EBITDA Margin: {financials['ebitdaMargins']}
- Debt-to-Equity: {financials['debtToEquity']}

Business summary:
{financials['summary']}

Give a {mode}-investing style assessment. Is the stock attractively valued? Should one buy now or wait? Suggest a fair value range.
"""
    
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

return response.choices[0].message.content

