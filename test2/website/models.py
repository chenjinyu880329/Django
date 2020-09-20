# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class WebsiteBookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    bread = models.IntegerField()
    bcommet = models.IntegerField()
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'website_bookinfo'


class WebsiteCeshi(models.Model):
    name = models.CharField(max_length=50)
    sex = models.IntegerField()
    addr = models.TextField()
    age = models.IntegerField()
    pub_date = models.DateTimeField()
    addtime = models.DateTimeField(db_column='addTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'website_ceshi'


#############################
# 管理器


class WebsiteChenjinyuManager(models.Manager):
    def get_queryset(self):  # 自定义管理师 有过滤作用
        return super(WebsiteChenjinyuManager, self).get_queryset().filter(status=True)


class WebsiteChenjinyu(models.Model):
    chen = models.CharField(max_length=50)
    jin = models.TextField()
    yu = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'website_chenjinyu'
    # 两种方式
    books1 = models.Manager()
    books2 = WebsiteChenjinyuManager()

#############################


class WebsiteHeroinfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.IntegerField()
    hcontent = models.CharField(max_length=1000)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'website_heroinfo'


class WebsiteYu(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'website_yu'
