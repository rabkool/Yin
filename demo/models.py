from django.db import models


# Create your models here.

class UserInfoDemo(models.Model):
    userId = models.CharField(primary_key=True, max_length=20, verbose_name='userId')
    userName = models.CharField(blank=True, max_length=20, verbose_name='userName')
    passWord = models.CharField(blank=True, max_length=20, verbose_name='passWord')
    userAge = models.CharField(blank=True, max_length=3, verbose_name='userAge')
    userMail = models.CharField(blank=True, max_length=20, verbose_name='userMail')

    class Meta:
        managed = False
        db_table = 'UserInfoDemo'


class UserDemo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'UserDemo'
