from django.contrib import admin

from .models import Blog, BlogEntry

admin.site.register(Blog)
admin.site.register(BlogEntry)
