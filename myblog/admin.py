from django.contrib import admin
from .models import Category, Tag, Article, Author
from django import forms


# class TagForm(forms.ModelForm):
#     checkbox = forms.ModelMultipleChoiceField(label='多选',
#             queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
#
#     class Meta:
#         model = Article
#         fields = ('checkbox',)
#
#
# class TagInline(admin.StackedInline):
#     model = Tag
#     form = TagForm

class ArticleAdmin(admin.ModelAdmin):
    fields = (('title', 'author', 'category'),
              'description', 'content', 'tag')
    list_display = ('title', 'pub_date', 'category', 'author')
    ordering = ('pub_date', )
    list_filter = ('category', 'pub_date', )
    search_fields = ('title', 'author', 'category', 'tag', )


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'sex', 'birth', 'introduce')
    list_display = ('name', 'sex', 'birth')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Tag)
