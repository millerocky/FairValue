from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Stocksy
from django.db.models import Q

def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(symbol__icontains=q))
        stocks = Stocksy.objects.filter(multiple_q)
    else:
         stocks = Stocksy.objects.all()

    class FairValue:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

        def __init__(self, url, html_class_parsing):
            self.url = url
            self.html_class_parsing = html_class_parsing
        
        def get_fair_value(self):
            page = requests.get(self.url, headers=self.headers)
            soup = BeautifulSoup(page.content, 'html.parser') 
            converting = soup.findAll('span', self.html_class_parsing)
            fair_value_of_stock = converting[0].text
            return fair_value_of_stock
    
    apple = FairValue(url='https://www.alphaspread.com/security/nasdaq/aapl/summary', html_class_parsing={'class': 'restriction-sensitive-data space-no-wrap'})
    apple_fair_value = apple.get_fair_value()

    tesla = FairValue(url='https://www.alphaspread.com/security/nasdaq/tsla/summary', html_class_parsing={'class': 'restriction-sensitive-data space-no-wrap'})
    tesla_fair_value = tesla.get_fair_value()

    microsoft = FairValue(url='https://www.alphaspread.com/security/nasdaq/msft/summary', html_class_parsing={'class': 'restriction-sensitive-data space-no-wrap'})
    microsoft_fair_value = microsoft.get_fair_value()

    context = {'stocks': stocks, 'apple_fair_value': apple_fair_value, 'tesla_fair_value': tesla_fair_value, 'microsoft_fair_value': microsoft_fair_value,
    }

    return render(request, 'main/index.html', context)


def faq(request):
    return render(request, 'main/faq.html')


def fair_values(request):
    return render(request, 'main/values.html')