import requests
from bs4 import BeautifulSoup

class FairValue:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

        def __init__(self, url, html_class_parsing):
            self.url = url
            self.html_class_parsing = html_class_parsing
        
        def get_fair_value(self):
            request_to_page = requests.get(self.url, self.headers)
            soup = BeautifulSoup(request_to_page.content, 'html.parser') 
            converting = soup.findAll('span', self.html_class_parsing)
            fair_value_of_stock = converting[1].text
            return fair_value_of_stock
    
apple = FairValue(url='https://www.financecharts.com/stocks/AAPL/dcf-calculator/fair-value-price', html_class_parsing={'class': 'pull-right'})
apple_fair_value = apple.get_fair_value()
print(apple_fair_value)