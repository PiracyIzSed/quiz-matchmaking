from django.conf.urls import url, include
from django.contrib import admin
from game import views

urlpatterns = [
    url(r'^match-find/(?P<player_id>\d+)/$', views.MatchMaking.as_view(), name='match-find'),
    url(r'^match-found/$', views.MatchFoundAPI.as_view(), name='match-found'),
]
