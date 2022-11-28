from django.shortcuts import render
from django.http import HttpResponse

import requests

from datetime import datetime


# Create your views here.


def index(request):
    today = datetime.today().strftime('%Y-%m-%d')
    url = "https://apiv3.apifootball.com/?action=get_events&league_id=149&match_live=1&from="+today+"&to="+today+"&APIkey=8acf77a31fc19bb7a9e6b469a4322a968341f22c1e1352dfae8f6c0e44212afc"
    #url = "https://apiv3.apifootball.com/?action=get_events&league_id=149&from=2022-11-01&to=2022-11-27&APIkey=8acf77a31fc19bb7a9e6b469a4322a968341f22c1e1352dfae8f6c0e44212afc"
    response = requests.get(url)
    jsonResponse = response.json()  # This is an array
    return render(request,'blog/index.html',{'jsonResponse':jsonResponse})

def specific(request):
    list1 = [1,2,3,4]
    return HttpResponse(list1)
