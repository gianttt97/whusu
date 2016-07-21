from django.contrib import admin
from .models import Article
from .models import Kind
from .models import School


admin.site.register(Article)
admin.site.register(Kind)
admin.site.register(School)
