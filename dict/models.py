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

    @classmethod
    def create(cls):
        word = cls()
        word.identifier = ""
        word.save()
        language_list = Language.objects.order_by('name_eng')
        for language in language_list:
            trnsl = Translation.create(word, language)
        return word

class Translation(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    translation = models.CharField(max_length=500)
    description = models.CharField(max_length=512, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    likes = GenericRelation(Like)
    
    def __str__(self):
        return self.translation

    @classmethod
    def create(cls, Wo, La):
        translation = cls()
        translation.word = Wo
        translation.language = La
        translation.translation = ""
        translation.description = ""
        translation.save()
        return translation
