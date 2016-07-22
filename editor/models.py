from __future__ import unicode_literals
from django.db import models


class Editor(models.Model):
    sid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    school = models.ForeignKey('School')
    authority = models.ForeignKey('Authority')

    def __unicode__(self):
        return self.name


class Authority(models.Model):
    level = models.IntegerField()

    def __unicode__(self):
        return self.level


class School(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
