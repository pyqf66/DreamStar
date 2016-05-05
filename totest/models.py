# coding=utf-8
###########################################
# File: models.py
# Desc: 数据层
# Author: 张羽锋
# History: 2015/11/02 张羽锋 新建
###########################################
from django.db import models


# 功能菜单-测试接口设置表
class HttpInterfaceInfo(models.Model):
    interface_id = models.AutoField(primary_key=True)
    interface_name = models.CharField(max_length=50)
    interface_code = models.CharField(max_length=50)
    http_interface = models.CharField(max_length=300)
    params = models.TextField()
    secretkey = models.CharField(max_length=50)


# 省份表
class AddressProvince(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=40)


# 城市表

class AddressCity(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=40)
    province_code = models.CharField(max_length=6)


# 地区表
class AddressTown(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=40)
    city_code = models.CharField(max_length=6)


# crmMock基础数据表
class CrmmockInfo(models.Model):
    id = models.AutoField(primary_key=True)
    crmuri = models.CharField(max_length=255)
    crmcode = models.CharField(max_length=32)


# crmMock消费数据表
class CrmmockPaydata(models.Model):
    id = models.AutoField(primary_key=True)
    card_no = models.CharField(max_length=255)
    paylog = models.CharField(max_length=2048)
    crmcode = models.CharField(max_length=32)
    growthlevel = models.CharField(max_length=32)
    growthvalue = models.CharField(max_length=32)
    crmmemberid = models.CharField(max_length=32,null=True)
