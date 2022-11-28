from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('specific', views.specific, name='specific')
]

#https://apiv3.apifootball.com/?action=get_events&league_id=149&from=2022-11-01&to=2022-11-11&APIkey=8acf77a31fc19bb7a9e6b469a4322a968341f22c1e1352dfae8f6c0e44212afc