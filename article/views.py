from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Article


def index(request):
    list = Article.objects.all()
    context = RequestContext(request, {
        'article_list': list,
    })
    return render(request, 'article/index.html', context)


def article_list(request):
    return HttpResponse('list')


def article_detail(request):
    return HttpResponse('detail')
