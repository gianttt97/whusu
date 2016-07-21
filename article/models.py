from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    subhead = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    editor_id = models.IntegerField()
    create_time = models.DateTimeField()
    last_change_time = models.DateTimeField()
    content = models.TextField()
    kind = models.ForeignKey('Kind')

    def get_create_date(self):
        return '%s' % self.create_time.date

    def get_create_day(self):
        return '%s' % self.create_time.day

    def __unicode__(self):
        return self.title


class Kind(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
