# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from player.serializers import PlayerSerializer
from rest_framework.views import APIView
from game.serializers import GameSerializer
from django.views.generic import TemplateView
from game import models
from rest_framework.response import Response

class MatchFoundAPI(APIView):
    def get(self, request, *args, **kwargs):
            game = models.Game.objects.filter(participants__player__id=request.GET.get('player_id'), completed=False).first()
            if game :
                data = GameSerializer(game).data
                print(data)
                data['found']=True
                return Response(data)
            else :
                return Response({ 'found' : False })

class MatchMaking(TemplateView):
    template_name = 'matchmaking.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MatchMaking, self).get_context_data(*args, **kwargs)
        print(context)
        return context
