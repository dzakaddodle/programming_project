import requests
from bs4 import BeautifulSoup

def get_soup(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_news(soup, tagname, classname, result):
    for each in soup.find_all(tagname, class_=classname):
        result.append(each.text.strip())
    return result

def news_scrape(ticker):
    ticker.lower()
    url = f'https://finviz.com/quote.ashx?t={ticker}&p=d'
    soup = get_soup(url)
    result = []
    result = get_news(soup, 'a', 'tab-link-news', result)
    if len(result) > 0:
        print(f'RECENT NEWS HEADLINES FOR {ticker.upper()}')
        i = 0
        while i < 20:
            print(f'{i+1}. {result[i]}')
            i+=1
    else:
        print(f'No news found for {ticker}')

ticker = input('Enter the ticker you wish to scrape: ')
news_scrape(ticker)
