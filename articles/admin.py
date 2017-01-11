from django.contrib import admin
from articles.models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
