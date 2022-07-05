from django.contrib import admin
from .models import *

class modsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'time_create')
    list_display_links = ('id','title')
    search_fields = ('title','content')
admin.site.register(mods, modsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
