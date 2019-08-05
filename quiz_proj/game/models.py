# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from player.models import Player
from question.models import Question,QuestionChoice,Category
# Create your models here.

class Game(models.Model):
    participants = models.ManyToManyField('GameParticipant')
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    asked_questions = models.ManyToManyField(Question)


    def get_next_question():
        pass



class GameParticipant(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    answers = models.ManyToManyField('GameAnswer')
    winner = models.BooleanField(default=False)

    def score():
        pass

class GameAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(QuestionChoice, on_delete=models.SET_NULL, null=True)
    score  = models.IntegerField()
    time = models.DurationField()
