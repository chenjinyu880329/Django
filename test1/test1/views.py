from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")



def runoob(request):
    context          = {}
    context['hello'] = 'Hello World传递的参数!1'
    context['indexs'] = '传递的参数2!'
    return render(request, 'index.html', context)
