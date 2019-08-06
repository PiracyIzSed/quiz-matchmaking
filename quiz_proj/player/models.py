# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from question.models import Category
# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=30)
    mobile_no = models.BigIntegerField()
    country_code = models.CharField(default='+91', max_length=5)

class PlayerQueue(models.Model):
    player = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True)
    category  = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
