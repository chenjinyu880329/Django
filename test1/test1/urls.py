"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import url
from . import views,testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexs/', views.runoob),
    url(r'^$', views.hello),
    path('testdb/', testdb.testdb),
    path('books/', views.bookdbs),

    url(r'guanliqi/', views.admins)
]
# 相当于路由 定义的两种方式 一个用path  一个用url
