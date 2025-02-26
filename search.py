import requests
import os
from dotenv import load_dotenv
# used this api - https://site.financialmodelingprep.com/developer/docs

#class for any functions related to the stock market
class StockMarket:
    def __init__(self):
        #load environment variables from .env file - specifically to get the api key
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        
        #list of sectors in the stock market
        self.sectors = [
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
        
        #list of exchanges that you can filter by
        self.exchanges = [
            "NASDAQ",
            "NYSE",
            "AMEX"
        ]
      
    #search stock market for company name's or tickers that contain keyword entered  
    def nameSearch(self, keyword="", limit=None):
        url = f"https://financialmodelingprep.com/stable/search-symbol?query={keyword}&limit={limit}&apikey={self.api_key}"
        listOfSearched = []
        response = requests.get(url)
        data = response.json()
        
        for i, stock in enumerate(data):
            listOfSearched.append(stock['symbol'])
            print(f"Result: {i + 1}") 
            print(f"Symbol: {stock['symbol']}")    
            print(f"Name: {stock['name']}")
            print(f"Exchange: {stock['exchange']}\n")
            
        return listOfSearched


    #More specific search for stocks that match sector, exchange, and market cap specified. Can also limit number of results given
    def advancedFilter(self, sector="", exchange="", mktCapMax=None, mktCapMin=None, limit=None):
        params = {
            "marketCapMoreThan": mktCapMin, 
            "marketCapLowerThan": mktCapMax,
            "sector": sector,
            "exchange": exchange,
            "limit": limit
                }
        
        listOfSearched = []
        url = f"https://financialmodelingprep.com/stable/company-screener?apikey={self.api_key}"
        
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

    #get speicifc information on a stock
    def getStockInfo(self, ticker):
        url = f"https://financialmodelingprep.com/stable/profile?symbol={ticker}&apikey={self.api_key}" 
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
        
        return data
    
#method for stock market main menu
def stockMain():
    session = StockMarket()
    print("Searching Stock Market...")
    print("Select one of the options below to begin: ")
    print(" 1. See Available Sectors")  
    print(" 2. See Available Stock Exchanges to Filter By")  
    print(" 3. Search By Company Name/Ticker")  
    print(" 4. Advanced Search Options") 
    option = input("To proceed enter the option number: ")

    if option == "1" or option == "2":
        if option == "1":
            print("Here are a list of sectors:")
            for sector in session.sectors:
                print(sector)
        else:
            print("Here is a list of stock exchanges that you can filter by:")
            for exchange in session.exchanges:
                print(exchange)
            
        proceed = input("Would you like to continue (Y/N)?")
        if proceed == "Y":
            stockMain()
        else:
            pass
    elif option == "3" or option == "4":
        results = []
        if option == "3":
            keyword = input("Enter the Company Name or Ticker Name: ")
            limit = input("If you want to limit the number of results enter a number (5 or below) or press enter to see all results.")
            try:
                limit = int(limit)
                if not 0 <= limit <= 5:
                    limit = None
            except:
                limit = None       
            results = session.nameSearch(keyword, limit)
        elif option == "4":
            print("Fill out the form below. If you do not want to specify an option then press enter.")
            sector = input("Enter the sector you would like to search: ")
            if sector not in session.sectors:
                sector = ""
            exchange = input("Enter the exchange you would like to search1: ")
            if exchange not in session.exchanges:
                exchange = ""
            mktMaxCap = input("Enter the max market cap you would like to search: ")
            try:
                mktMaxCap = int(mktMaxCap)
            except:
                mktMaxCap = None
            mktMinCap = input("Enter the min market cap you would like to search: ")
            try:
                mktMinCap = int(mktMinCap)
            except:
                mktMinCap = None
            limit = input("If you want to limit the number of results enter a number (5 or below) or press enter to see all results.")
            try:
                limit = int(limit)
                if not 0 <= limit <= 5:
                    limit = None
            except:
                limit = None  
            results = session.advancedFilter(sector, exchange, mktMaxCap, mktMinCap, limit)
        print("What would you like to do next?")
        print("1. View more details on a stock listed")
        print("2. Go back to main menu")
        print("3. Quit")
        option = input("Type the option number you would like to do: ")
        if option == "1":
            stockView(session, results)
        elif option == "2":
            stockMain()
        else:
            pass
        

#method for viewing specific stock menu        
def stockView(session, stocks):
    stock = input("Enter the result number of the stock you want to view more information on: ")
    
    try:
        stock = int(stock)
        if 0 <= stock <= len(stocks):
            stockInfo = session.getStockInfo(stocks[stock - 1])
            print("What would you like to do now?")
            print("1. Save Stock")
            print("2. Search More Stocks")
            print("3. Quit")
            option = input("Enter the option number: ")
            if option == "1":
                saveStock(session, stockInfo)
            elif option == "2":
                stockMain()
            else:
                pass          
        else:
            print("Input is not valid. Try again")
            stockView(session, stocks)
            
    except:
        print("Input is not valid. Try again")
        stockView(session, stocks)
        
    
#session = StockMarket()
#session.getStockInfo("AAPL")       
        
def saveStock(session, stock):
    pass    

stockMain()
        

    # can get company information - based on quick searches
    # Use Screener Stock to search by market cap or sector
    # can get very specific information on a company after selecting learn more
    #learn more about the different industries - all available industries api
    #all exchange options - all exchange options available
    #can potentially get all financial statements

        
