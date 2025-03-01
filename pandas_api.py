import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

API_KEY = "hgVAQPj8NKeoMoaXKyVjI9cqontuWz18p7nGcsKj"

#user enter stock symbol
STOCK_SYMBOL = input("Enter stock ticker: ").strip().upper()

#display monthly data for past 12 months
INTERVAL = "month"
DATE_TO = datetime.today().strftime("%Y-%m-%d")
DATE_FROM = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

#API Endpoint
URL = (
    f"https://api.stockdata.org/v1/data/eod"
    f"?symbols={STOCK_SYMBOL}"
    f"&api_token={API_KEY}"
    f"&interval={INTERVAL}"
    f"&date_from={DATE_FROM}"
    f"&date_to={DATE_TO}"
    f"&sort=asc"
)

response = requests.get(URL)
data = response.json()

df = pd.DataFrame(data["data"])

df["date"] = pd.to_datetime(df["date"]).dt.tz_localize(None)

df = df.sort_values(by="date")

#unable to display past twelve months as latest data from API is from 2024-08-28
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["close"], label="Closing Price", color="blue")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.title(f"{STOCK_SYMBOL} Historical Stock Prices (Last 12 months)")