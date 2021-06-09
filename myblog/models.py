from django.db import models


class Category(models.Model):
    """文章类别模型"""
    cname = models.CharField(max_length=20, unique=True, verbose_name='类别')

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'tb_category'


class Tag(models.Model):
    """文章标签模型"""
    tname = models.CharField(max_length=20, unique=True, verbose_name='标签')

    def __str__(self):
        return self.tname

    class Meta:
        db_table = 'tb_tag'


class Author(models.Model):
    """作者模型"""
    name = models.CharField('名字', max_length=20, unique=True)
    sex = models.BooleanField('性别')
    birth = models.DateField('出生日期')
    introduce = models.CharField('个人简介', null=True, max_length=200,
                                 default='这个作者很懒，什么都没有留下 *_^_*!')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_author'


class Article(models.Model):
    """"文章模型"""
    title = models.CharField('文章标题', max_length=100, unique=True)
    description = models.CharField('描述', max_length=100, default='暂无相关描述')
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布期日', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类型')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_article'
        ordering = ['pub_date']
