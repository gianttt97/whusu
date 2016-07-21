from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.console_home, name='console_home'),
    url(r'^list/$', views.console_list, name='console_list'),
    url(r'^add/$', views.console_add, name='console_add'),
    url(r'^edit/$', views.console_edit, name='console_edit'),
]
