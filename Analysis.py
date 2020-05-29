##Analysis
### Imports ###
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

## Scrape Stock Data
def scrapeData(ticker):
    url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch" #find the stock on yahoo finance
    try:
        page = urlopen(url)
    except:
        print("Error opening url")
    
    soup = BeautifulSoup(page,"html.parser")
    return soup

def getCurrentPrice(soup):
    currentPrice = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text #find the stock price from the website
    return currentPrice

print(getCurrentPrice(scrapeData("AAPL")))