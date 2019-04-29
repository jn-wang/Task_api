from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32,verbose_name="用户名")
    pwd = models.CharField(max_length=64,verbose_name="密码")
    email = models.EmailField()
    sex_choices = (
        (1, '男'),
        (2, '女'),
        (3, '妖'),
    )
    sex = models.IntegerField(verbose_name="性别",choices=sex_choices,default=3)
    birthday = models.DateTimeField('用户生日', default=timezone.now)
    school = models.CharField(max_length=64,verbose_name="学校",null=True)
    major = models.CharField(max_length=64,verbose_name="专业",null=True)
    tel = models.CharField(max_length=64,verbose_name="电话",null=True)

class UserToken(models.Model):
    user = models.OneToOneField(to="UserInfo",on_delete=True)
    token = models.CharField(max_length=64)

class User_information(models.Model):
    user = models.OneToOneField(to="UserInfo",on_delete=True)
    newtime = models.DateTimeField('用户注册日期', default=timezone.now)

class Task(models.Model):
    taskname = models.CharField(max_length=64,verbose_name="任务名称")
    publisher = models.CharField(max_length=32,verbose_name="发布人")
    receiver = models.CharField(max_length=32,verbose_name="领取人",default='暂无')
    brokerage = models.FloatField(max_length=16,verbose_name="平台佣金",default=0)
    service_fee = models.FloatField(max_length=16,verbose_name="个人佣金")
    create_time = models.DateTimeField('任务创建时间',default=timezone.now)
    first_time = models.DateTimeField('任务领取时间',default=timezone.now)
    last_time = models.DateTimeField('任务结束时间',default=timezone.now)
    get_status_choices = (
        (0,'待领取'),
        (1, '已领取'),
    )
    completion_status_choices = (
        (0,'未完成'),
        (1, '已完成'),
        (2, '任务失败'),
    )
    get_status = models.IntegerField(verbose_name="任务领取状态", choices=get_status_choices,default=0)
    completion_status = models.IntegerField(verbose_name="任务完成状态", choices=completion_status_choices,default=0)