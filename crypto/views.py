from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    request_data = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,USDT,LTC,EOS,BNB,BSV,XLM&tsyms=USD,EUR')
    data = request_data.json()
    request_news_data = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    news_data = request_news_data.json()
    return render(request, 'index.html',{'data':data, 'news_data': news_data})


def search(request):
    if request.method == 'POST':
        crypto = request.POST['search'].upper().replace(' ','')
        request_data = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+crypto+'&tsyms=USD,EUR')
        data = request_data.json()
        return render(request, 'search.html',{'data':data})
    else:
        request_data = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,USDT,LTC,EOS,BNB,BSV,XLM&tsyms=USD,EUR')
        data = request_data.json()
        return render(request, 'search.html',{'data':data})
