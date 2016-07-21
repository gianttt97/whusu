from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from .models import Article


def index(request):
    head_article = Article.objects.filter(headline="true").order_by('create_time')[:3]
    spotlight_article = Article.objects.filter(kind='spotlight').order_by('create_time')[:5]
    school_article = Article.objects.filter(kind='school').order_by('create_time')[:6]

    return render(request, 'article/index.html', context)


def article_list(request):
    return HttpResponse('list')


def article_detail(request):
    return HttpResponse('detail')
