from __future__ import unicode_literals
from django.db import models
from random import Random
from editor.models import Editor
from editor.models import School


class Article(models.Model):
    title = models.CharField(max_length=50)
    subhead = models.CharField(max_length=20)
    introduction = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    editor = models.ForeignKey('editor.Editor', related_name='editor')
    publisher = models.ForeignKey('editor.Editor', related_name='publisher')
    create_time = models.DateTimeField()
    last_change_time = models.DateTimeField()
    content = models.TextField()
    cover_page_photo_path = models.CharField(max_length=100)
    kind = models.ForeignKey('Kind')
    from_school = models.ForeignKey('editor.School')
    headline = models.BooleanField(default='false')

    def get_create_date(self):
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

    def _get_query_id(self):
        query_str = ''
        chars = '0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(6):
            query_str += chars[random.randint(0, length)]
        return query_str

    query_id = property(_get_query_id)


class Kind(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    def _get_query_id(self):
        query_str = ''
        chars = '0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(4):
            query_str += chars[random.randint(0, length)]
        return query_str

    query_id = property(_get_query_id)


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
    article = models.ForeignKey('Article')
    user = models.ForeignKey('editor.Editor')
