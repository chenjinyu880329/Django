from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Max, F, Q

from django.core.paginator import Paginator  # 分页模块


# Create your views here.
def index(request):
    context = {}
    return render(request, 'websites/index.html', context)


def chenjinyu(request):
    # list = WebsiteChenjinyu.books1.filter(Q(pk__lt=4))
    list = WebsiteChenjinyu.books2.filter(Q(pk__lt=4))  # 自定义管理器使用
    # re1 = WebsiteChenjinyu.books2.get(id=2)
    re1 = WebsiteChenjinyu.books2.filter(id=2)
    re2 = WebsiteChenjinyu.books2.filter(id=2).first()
    # print(re1)

    context = {'list1': list, 'get1': re1, 'get2': re2}
    return render(request, 'websites/chenjinyu.html', context)


def dels(request):
    # re = WebsiteChenjinyu.books1.filter(id=11).delete()
    re = WebsiteChenjinyu.books2.filter(id=2)
    if re.exists():
        return HttpResponse(re)
    else:
        return HttpResponse(re.exists())


# 分页功能实现
def listspage(request):
    pindex = request.GET.get('pindex', '1')
    list = WebsiteChenjinyu.books2.order_by('-id')  # 倒序 使用 - 号
    # list = WebsiteChenjinyu.books2.all()
    paginator = Paginator(list, 5, 2)
    numbers = paginator.num_pages
    page = paginator.page(int(pindex))
    context = {'page': page, 'numbers': numbers}
    return render(request, "websites/borrow_show2.html", context)


################ # 反向解析测试
def urlceshi(request):
    return render(request, 'websites/urlceshi.html')


def urlanalysis(request, id1, id2):
    return render(request, 'websites/urlanalysis.html')


def urlanalysis2(request, id, age):
    context = {'id': id, 'age': age}
    return render(request, 'websites/urlanalysis2.html', context)

################ # 静态文件

def imgStatic(request):

    return render(request, 'statics/imgstatic.html')



