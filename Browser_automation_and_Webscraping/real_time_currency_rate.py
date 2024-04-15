from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find("span" , class_ = 'ccOutputRslt').text      # this will get the value with currency name
    currency = round(float((currency.split(' ')[0])),2)
    print(currency)
    
get_currency('EUR','INR')