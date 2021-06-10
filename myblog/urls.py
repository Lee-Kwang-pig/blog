#coding=utf-8

from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'page/<int:num>/', views.index),
    path(r'article_<int:article_id>/details/', views.detail, name='detail'),

]
