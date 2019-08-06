# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from player.serializers import PlayerSerializer, PlayerQueueSerializer

class CreatePlayerAPI(CreateAPIView):
    serializer_class = PlayerSerializer

class AddToQueueAPI(CreateAPIView):
    serializer_class = PlayerQueueSerializer
