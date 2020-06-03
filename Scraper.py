##Analysis
### Imports ###
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

## Scrape Stock Data
def scrapeData(ticker):
    #url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch" #find the stock on yahoo finance
    url = "https://finance.yahoo.com/quote/"+ticker+"/history?p="+ticker

    try:
        page = urlopen(url)
    except:
        print("Error opening url")
    
    soup = BeautifulSoup(page,"html.parser")
    return soup

def getCurrentPrice(soup):
    currentPrice = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text #find the stock price from the website
    return currentPrice

def getHistoricPrices(soup,length):
    rows = soup.find('div',{'class': 'Pb(10px) Ovx(a) W(100%)'}).find_all("tr")
    historicPrices = []
    for i in range(length):
        current_row = rows[i+1]
        row_data = current_row.find_all("td")
        try:
            price = float(row_data[1].text.replace(',',''))
            historicPrices.append(price)
        except ValueError:
            print(row_data[1].text + " is not a float") 

    return historicPrices


## main method only called when file is run directly
def main():
    soup = scrapeData('aapl')
    print(getHistoricPrices(scrapeData('aapl'),5))
    return 

## only true if this file is run directly, not true if it is imported
if __name__ == '__main__':
    main()



