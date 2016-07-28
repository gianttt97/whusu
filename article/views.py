from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def index(request):
    head_article = Article.objects.filter(is_headline='true').order_by('create_time')[:3]
    spotlight_article = Article.objects.filter(kind__pk='1').order_by('create_time')[:4]
    school_article = Article.objects.filter(kind__pk='2').order_by('create_time')[:6]
    notice_article = Article.objects.filter(kind__pk='3').order_by('create_time')[:4]
    context = {'headline_list': head_article,
               'spotlight_list': spotlight_article,
               'school_list': school_article,
               'notice_list': notice_article,
               }
    return render(request, 'article/index.html', context)


def article_list(request, list_id):
    news_list = Article.objects.filter(kind__query_id=list_id).order_by('create_time')
    context = {'news_list': news_list}
    return render(request, 'article/list.html', context)


def article_detail(request, news_id):
    news = Article.objects.get(query_id=news_id)
    context = {'article': news}
    return render(request, 'article/detail.html', context)


def test_page(request):
    a = Article.objects.count()
    return HttpResponse(a)
