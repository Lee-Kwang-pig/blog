from django.shortcuts import render
from django.core.paginator import Paginator
from myblog.models import Article
import math


def index(request, num=1):
    """主页视图"""

    # 获取文章对象
    article_list = Article.objects.all().order_by('-pub_date')

    # 创建分页器， 参数 per_page 是每页的记录条数
    page_obj = Paginator(article_list, per_page=1)

    # 获取第 n 页
    page = page_obj.page(num)

    # 生成页码数列表，这里分 10 个页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    end = begin + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    page_list = range(begin, end + 1)
    content = {'article_list': page,
               'page_list': page_list,
               'current_page': num
               }
    return render(request, 'myblog/index.html', content)


def detail(request, article_id):
    """文章内容详情视图"""
    article = Article.objects.get(pk=article_id)
    return render(request, 'myblog/detail.html', {'article': article})
