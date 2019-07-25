from django.db import models
from datetime import datetime
from django.dispatch import Signal
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like

class Language(models.Model):
    name = models.CharField(max_length=20)
    name_eng = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name + "(" + self.name_eng + ")"


class Word(models.Model):
    identifier = models.CharField(max_length=20, default="")
    def __str__(self):
        return self.identifier

class Translation(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    translation = models.CharField(max_length=500)
    description = models.CharField(max_length=512, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    likes = GenericRelation(Like)
    
    def __str__(self):
        return self.translation

