from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    """Article model"""
    title = models.CharField(max_length=50)
    subhead = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    editor_id = models.IntegerField()
    create_time = models.DateTimeField()
    last_change_time = models.DateTimeField()
    content = models.TextField()
    kind = models.ForeignKey('Kind')
    headline = models.BooleanField()

    def get_create_date(self):
        """get date like 2016-01-01"""
        return '%s-%s-%s' % (self.create_time.year,
                             self.create_time.month,
                             self.create_time.day)

    def get_create_day(self):
        return '%s' % self.create_time.day

    def get_create_month_capital(self):
        month = self.create_time.month
        if month == 1:
            return 'Jan.'
        elif month == 2:
            return 'Feb.'
        elif month == 3:
            return 'Mar.'
        elif month == 4:
            return 'Apr.'
        elif month == 5:
            return 'May.'
        elif month == 6:
            return 'Jun.'
        elif month == 7:
            return 'Jul.'
        elif month == 8:
            return 'Aug.'
        elif month == 9:
            return 'Sep.'
        elif month == 10:
            return 'Oct.'
        elif month == 11:
            return 'Nov.'
        elif month == 12:
            return 'Dec.'

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
