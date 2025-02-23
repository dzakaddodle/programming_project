import requests
import os
from dotenv import load_dotenv
load_dotenv()
# used this database - https://site.financialmodelingprep.com/developer/docs

def nameSearch(keyword, limit):
    url = f"https://financialmodelingprep.com/stable/search-symbol?query={keyword}&limit={limit}&apikey={os.getenv('API_KEY')}"
    listOfSearched = []
    response = requests.get(url)
    data = response.json()
    print(data)
    
    for i, stock in enumerate(data):
        listOfSearched.append(stock['symbol'])
        print(f"Result: {i + 1}") 
        print(f"Symbol: {stock['symbol']}")    
        print(f"Name: {stock['name']}")
        print(f"Exchange: {stock['exchange']}\n")
        
    return listOfSearched



def advancedFilter(sector, exchange,mktCapMax, mktCapMin, limit):
    params = {
        "marketCapMoreThan": mktCapMin, 
        "marketCapLowerThan": mktCapMax,
        "sector": sector,
        "exchange": exchange,
        "limit": limit
              }
    
    listOfSearched = []
    url = f"https://financialmodelingprep.com/stable/company-screener?apikey={os.getenv('API_KEY')}"
    
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

def getStockInfo(ticker):
    url = f"https://financialmodelingprep.com/stable/profile?symbol={ticker}&apikey={os.getenv('API_KEY')}" 
    response = requests.get(url)
    stock = response.json()
    data = stock[0]
    
    print(f"Symbol: {data['symbol']}")
    print(f"Company Name: {data['companyName']}")
    print(f"Website: {data['website']}")
    print(f"Description: {data['description']}")  
    print(f"Country: {data['country']}") 
    print(f"Number of Full-Time Employees: {data['fullTimeEmployees']}") 
    print(f"Price: {data['price']}")
    print(f"Market Cap: {data['marketCap']}")
    print(f"Beta: {data['beta']}")
    print(f"Last Dividend: {data['lastDividend']}")
    print(f"Range: {data['range']}")
    print(f"Change: {data['change']}")
    print(f"Change %: {data['changePercentage']}")
    print(f"Volume: {data['volume']}")
    print(f"Average Volume: {data['averageVolume']}")
    print(f"Currency: {data['currency']}")
    print(f"Sector: {data['sector']}")
    print(f"Industry: {data['industry']}")
    print(f"Exchange: {data['exchange']}\n")
    
    return ticker
    
        
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

def getExchanges():
    exchanges = [
        "NASDAQ",
        "NYSE",
        "AMEX"
    ]
    return exchanges

        
#advancedFilter("", "NASDAQ", 10000000000000, 10, 9)
#nameSearch("A", None)
#getStockInfo("AAPL")



# can get company information - based on quick searches
# Use Screener Stock to search by market cap or sector
# can get very specific information on a company after selecting learn more
#learn more about the different industries - all available industries api
#all exchange options - all exchange options available
#can potentially get all financial statements
