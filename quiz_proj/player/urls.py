from django.conf.urls import url, include
from django.contrib import admin
from player import views

urlpatterns = [
    url(r'^add-queue/$', views.AddToQueueAPI.as_view(), name='add-queue'),
    # url(r'^player/', include('player.urls'))
]
