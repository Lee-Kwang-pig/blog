# blog
个人博客，专注于记录成长历程与分享优秀技术
<hr>

[TOC]

# 简介

Intro ：本项目以CSDN为模板，搭建一个简略版的个人博客，用于记录与分享学习，预期要实现的功能有：
- 博文的分类、归档
- 查询近期发布
- 全文搜索
- 实现百度的分页功能
- 支持富文本编辑器
- 支持分享到微信、QQ、新浪等
- 用户登录时，若格式错误，使用Ajax实现页面无跳转提醒
- 实现用户跟踪

# 项目搭建过程

<strong>第一次提交:</strong><br/>
划分首页功能区，初步搭建页面雏形。<br/>
不足之处：CSS 样式拼凑在一个文件中，后期更改较困难。
![页面布局](https://github.com/Lee-Kwang-pig/blog/blob/master/magics/blog%E9%A6%96%E9%A1%B5(%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%8F%90%E4%BA%A4).png)

<strong>第二次提交:</strong><br/>
创建数据模型，使用后台管理添加数据。<br/>
初步掌握ModelAdmin类，后台管理界面实现了排序、搜索、过滤等功能；但未实现多对多关系复选框。
![后台管理界面](https://github.com/Lee-Kwang-pig/blog/blob/master/magics/%E5%90%8E%E5%8F%B0%E7%AE%A1%E7%90%86%EF%BC%88%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%8F%90%E4%BA%A4%EF%BC%89.png)

<strong>第三次提交:</strong><br/>
实现了百度的分页功能，添加了对富文本编辑器的支持，但对markdown语法的支持不完善，没有实现代码高亮。
![百度分页功能](https://github.com/Lee-Kwang-pig/blog/blob/master/magics/%E5%88%86%E9%A1%B5%E5%8A%9F%E8%83%BD.png)
