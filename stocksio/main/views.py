from django.shortcuts import render
from .models import Stocksy
from django.db.models import Q

def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(symbol__icontains=q))
        stocks = Stocksy.objects.filter(multiple_q)
    else:
         stocks = Stocksy.objects.all()
    context = {'stocks': stocks}
    return render(request, 'main/index.html', context)


def faq(request):
    return render(request, 'main/faq.html')