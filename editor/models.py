from __future__ import unicode_literals
from django.db import models
from article.models import School
from article.models import Article


class Editor(models.Model):
    sid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    school = models.ForeignKey(School)
    authority = models.ForeignKey(Authority)

    def __unicode__(self):
        return self.name


class Authority(models.Model):
    level = models.IntegerField()

    def __unicode__(self):
        return self.level


class Event(models.Model):
    ADD = 'ADD'
    DELETE = 'DEL'
    UPDATE = 'UPD'
    CHECK = 'CHK'
    KIND_CHOICES = (
        (ADD, 'Add'),
        (DELETE, 'Delete'),
        (UPDATE, 'Update'),
        (CHECK, 'Check'),
    )
    Kind = models.CharField(max_length=3,
                            choices=KIND_CHOICES)
    article = models.ForeignKey(Article)
    user = models.ForeignKey(Editor)
