from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.index),
    url(r'chenjinyu/', views.chenjinyu),
    url(r'dels', views.dels),

    # url(r'^herolist/(\d+)/$', views.lists, name='lists'),



    # url(r'^herolist(?P<pindex>[0-9]*)/$', views.lists, name='lists'),
    # url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^herolist2/$', views.listspage, name='listspage'),

    url(r'^urlceshi/$', views.urlceshi),
    url(r'^urlanalysis/(\d+)/(\d+)$', views.urlanalysis, name='ceshi1'), #反向解析带参数
    # url(r'^urlanalysis/$', views.urlanalysis, name='ceshi1'), #反向解析不带参数
    url(r'^urlanalysis2/(?P<id>\d+)/(?P<age>\d+)$', views.urlanalysis2, name='ceshi2'), #反向解析带参数

    url(r'^imgstatic/$', views.imgStatic),
]


