# What is this

使用 Python + Django 开发一个博客系统。

在实际开发中掌握 Python 的使用。

## Django

Django 是一个基于 Python 的高级 Web 开发框架

它能够让开发人员进行高效且快速的开发

它高度集成（不用自己造轮子），免费且开源

慕课网学习视频：https://www.imooc.com/learn/790

## Useful Links

+ [Python 官方网站](https://www.python.org/)

+ [Python3 菜鸟教程](http://www.runoob.com/python3/python3-tutorial.html)

+ [Python 教程 by 廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

+ [Django 官方网站](https://www.djangoproject.com/)

+ [Django 菜鸟教程](http://www.runoob.com/django/django-tutorial.html)

## 搭建环境

### Python

> Python 2.7 或者 Python 3.x

Windows: Python 官网下载对应 MSI 安装文件
Mac 和 Linux 自带 Python，无需安装

### Django

命令行中使用 pip 安装

```sh
pip install Django==2.0.7
```

### 开发工具

编辑器：Pycharm / Sublime / Atom / VScode

## 创建项目

执行命令：

```sh
django-admin startproject myblog
```

会生成如下文件：

```sh
├── myblog
|   ├── __init__.py       # Python 中声明模块的文件，内容默认为空
|   ├── settings.py       # 项目的总配置文件，里面包含了数据库、Web 应用、时间等各种配置
│   └── urls.py           # url 配置文件
│   └── wsgi.py           # Python Web Server Gateway Interface (Python 服务器网关接口) Python 应用与 Web 服务器之间的接口
└── manage.py             # 与项目进行交互的命令行工具集的入口,执行 python manage.py 来查看所有命令
```

## 启动服务器

Django 自带一个小型服务器

```sh
python manage.py runserver
```

指定端口号

```sh
python manage.py runserver 9999
```

## 创建应用

在 manage.py 同级目录下执行命令：

```sh
python manage.py startapp blog
```

添加应用到 setting.py 中的 `INSTALLED_APPS` 数组中

## 应用目录介绍

```sh
migrations  数据迁移模块
__init__.py
admin.py      # 当前应用的后台管理系统配置
apps.py       # 当前应用的一些配置
models.py     # 数据模块，使用 ORM 框架
test.py       # 自动化测试模块
views.py      # 执行响应的代码所在模块，代码逻辑处理的主要地点
```