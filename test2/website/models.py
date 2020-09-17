from django.db import models


# Create your models here.
class Yu(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)


class Ceshi(models.Model):
    name = models.CharField(max_length=50)
    sex = models.BooleanField(default=False)
    addr = models.TextField(null=False)
    age = models.IntegerField(default=0)
    createTime = models.DateTimeField(db_column='pub_date')
    addTime = models.DateTimeField(default=False)

