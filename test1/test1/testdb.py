from django.http import HttpResponse

from TestModel.models import Test

# 自定义的表  Bool_list
from Book.models import Lists


def bookdb():
    # re = Lists.objects.all()  # 通过调用 初始化 的 模型调用数据库
    # re = Lists.books1.all()   # 通过在模型中 定义 管理器 调用数据库，books1 相当于 模型的一个变量
    re = Lists.books2.all()     # 通过在模型中 定义 管理器 调用数据库，books2 相当于 模型的一个变量
    return re
    # response3 = Lists.objects.get(id=1)
    # return response3
    # return 'haha'






# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")