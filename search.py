import requests
import os
from dotenv import load_dotenv
load_dotenv()
# used this database - https://site.financialmodelingprep.com/developer/docs
def advancedFilter(sector, exchange,mktCapMax, mktCapMin, limit):
    params = {
        "marketCapMoreThan": mktCapMin, 
        "marketCapLowerThan": mktCapMax,
        "sector": sector,
        "exchange": exchange,
        "limit": limit
              }
    
    listOfSearched = []
    #top = 10
    #exchange = "NASDAQ"
    url = f"https://financialmodelingprep.com/stable/company-screener?apikey={os.getenv('API_KEY')}"
    #to search by ticker
    # if filter == 1:
    #     #url = f"https://financialmodelingprep.com/api/v3/search-ticker?query={keyword}&limit={top}&exchange={exchange}&apikey={os.getenv('API_KEY')}"
    #     #url = f"https://financialmodelingprep.com/api/v3/profile/{keyword}?apikey={os.getenv('API_KEY')}"
    # #to search by name
    # elif filter == 2:
    #     url = f"https://financialmodelingprep.com/api/v3/search-name?query={keyword}&limit={top}&exchange={exchange}"
    
    response = requests.get(url, params = params)
    data = response.json()
       
    for i, stock in enumerate(data):
        listOfSearched.append(stock['symbol'])
        print(f"Result: {i + 1}") 
        print(f"Symbol: {stock['symbol']}")    
        print(f"Name: {stock['companyName']}")
        print(f"Market Cap: {stock['marketCap']}")
        print(f"Sector: {stock['sector']}")
        print(f"Price: {stock['price']}")
        print(f"Volume: {stock['volume']}")
        print(f"Exchange: {stock['exchange']}\n")
        
    return listOfSearched
        
    #print(data)
        
def getSectors():
    sectors = [
    "Technology",
    "Health Care",
    "Financials",
    "Consumer Discretionary",
    "Consumer Staples",
    "Energy",
    "Utilities",
    "Real Estate",
    "Materials",
    "Industrials",
    "Communication Services",
    "Information Technology",
    "Basic Materials",
    "Telecommunications",
    "Consumer Services"
    ]
    
    return sectors

        
filterBy("", "NASDAQ", 10000000000000, 10, 9)



# can get company information - based on quick searches
# Use Screener Stock to search by market cap or sector
# can get very specific information on a company after selecting learn more
#learn more about the different industries - all available industries api
#all exchange options - all exchange options available
#can potentially get all financial statements
