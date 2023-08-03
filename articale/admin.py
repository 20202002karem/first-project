from django.contrib import admin
from .models import Article
# Register your models here.
class ArticaleAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields= ['title','contant']

admin.site.register(Article,ArticaleAdmin)