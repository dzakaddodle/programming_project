import requests
import os
from dotenv import load_dotenv
load_dotenv()

def filterBy(filter, keyword):
    top = 10
    exchange = "NASDAQ"
    #to search by ticker
    if filter == 1:
        url = f"https://financialmodelingprep.com/api/v3/search-ticker?query={keyword}&limit={top}&exchange={exchange}&apikey={os.getenv('API_KEY')}"
        response = requests.get(url)
        data = response.json()
        
        print(data) 
        
filterBy(1, "AA")