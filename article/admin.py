from django.contrib import admin
from .models import Article, School, Kind

# Register your models here.
admin.site.register(Article)
admin.site.register(Kind)
admin.site.register(School)
