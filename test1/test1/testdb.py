from django.http import HttpResponse

from TestModel.models import Test

# 自定义的表  Bool_list
from Book.models import Lists


def bookdb():
    re = Lists.objects.all()
    return re
    # response3 = Lists.objects.get(id=1)
    # return response3
    # return 'haha'






# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")