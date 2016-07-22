"""whusu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from article import views as article_view
from editor import views as editor_view

urlpatterns = [
    url(r'^$', article_view.index, name='index'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^article/', include('article.urls')),
    url(r'^console/', include('console.urls')),
    url(r'^login/', editor_view.login, name='login'),
    url(r'^tt/$', article_view.test_page),
]
