from django.contrib import admin

# Register your models here.

from .models import Post, Boarding
admin.site.register(Post)
admin.site.register(Boarding)
