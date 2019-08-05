# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField()
    choices  = models.ManyToManyField('QuestionChoice')

class QuestionChoice(models.Model):
    choice = models.TextField()
    correct = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    category = models.CharField(max_length=40)
