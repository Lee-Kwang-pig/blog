from django.contrib import admin

from .models import Category, Tag, Article, Author


class ArticleAdmin(admin.ModelAdmin):
    fields = (('title', 'author', 'category'),
              'description', 'content', 'tag')
    list_display = ('title', 'pub_date', 'category', 'author')
    ordering = ('pub_date', )
    list_filter = ('category', 'pub_date', )
    search_fields = ('title', 'author', 'category', 'tag', )


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'sex', 'introduce')
    list_display = ('name', 'sex', 'birth')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Tag)
