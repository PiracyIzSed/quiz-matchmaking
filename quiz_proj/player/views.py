# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from player.serializers import PlayerSerializer, PlayerQueueSerializer

class CreatePlayerAPI(CreateAPIView):
    serializer_class = PlayerSerializer

class AddToQueueAPI(CreateAPIView):
    serializer_class = PlayerQueueSerializer

    def post(self, request, *args, **kwargs):
        super(AddToQueueAPI, self).create(request, *args, **kwargs)
        player_id = request.POST.get('player')
        category_id = request.POST.get('category')
        return redirect('/game/match-find/'+player_id+'/')
