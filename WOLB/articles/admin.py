from django.contrib import admin
from . models import Article, Comment, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_title', 'pub_date', 'redact_date', 'is_published', 'category',)
    list_display_links = ('id', 'article_title',)
    search_fields = ('article_title', 'article_text', )
    list_editable =('is_published', 'category',)
    search_fields = ('is_published', 'category', )


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display =('id', 'article', 'author_name','comment_text')
    list_display_links = ('id', 'article')
    search_fields = ('id', 'article', 'author_name' )


admin.site.register(Comment, CommentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', )


admin.site.register(Category, CategoryAdmin)
