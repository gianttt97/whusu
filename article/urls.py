from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list/(?P<list_id>[0-9]{4})/$', views.article_list, name='article_list'),
    url(r'^detail/(?P<news_id>[0-9]{6})', views.article_detail, name='article_detail'),
]
