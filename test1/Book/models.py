from django.db import models

# Create your models here.


class Lists(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Chen(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Jin(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Yu(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

