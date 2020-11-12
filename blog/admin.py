from django.contrib import admin

# Register your models here.

from .models import Blog

# @admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'status', 'author')

admin.site.register(Blog, BlogAdmin)