from django.contrib import admin
from .models import News, Author, Comment, Category
# Register your models here.
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)