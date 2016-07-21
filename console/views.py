from django.shortcuts import render
from django.http import HttpResponse


def console_home(request):
    return HttpResponse('Home')


def console_list(request):
    return HttpResponse('list')


def console_add(request):
    return HttpResponse('add')


def console_edit(request):
    return HttpResponse('edit')
