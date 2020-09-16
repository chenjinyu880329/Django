from django.db import models


# Create your models here.


class ListsManager(models.Manager):
    def get_queryset(self):
        return super(ListsManager, self).get_queryset().filter('id > 2')

    def create(self, name):
        b = Lists()
        b.name = name
        return b


class Lists(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    # 管理器  如果定义  Meta 就是 访问 Lists 表  不是 Book_Lists表
    # class Meta:
    #     db_table = 'Lists'
    books1 = models.Manager()
    books2 = ListsManager()


class Chen(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Jin(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Yu(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
