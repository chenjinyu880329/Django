from django.http import HttpResponse
from django.shortcuts import render


from . import testdb




def admins(request):


    return HttpResponse("<p>" + b.name + "！</p>")


def bookdbs(request):
    context = testdb.bookdb()
    data = {'list': context}
    # print(b)
    # context = {}
    # context['index1'] = '传递的参数1books！'
    # context['index2'] = '传递的参数2!books'
    return render(request, 'mybook.html', data)
    # return HttpResponse("<p>"+b.name+"！</p>")

# 首页
def hello(request):
    # return HttpResponse("Hello world ! ")
    context = {}
    context['index1'] = '首页-传递的参数1！'
    context['index2'] = '传递的参数2!'
    return render(request, 'indexs.html', context)


def runoob(request):
    context          = {}
    context['hello'] = 'Hello World传递的参数!1'
    context['indexs'] = '传递的参数2!'
    return render(request, 'index.html', context)
