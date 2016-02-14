#!/usr/bin/env python
# coding=utf-8
###########################################
# File: IdentityGenneratorCreater.py
# Desc: 身份证生成器视图层
# Author: 张羽锋
# History: 2016/01/01 张羽锋 新建
###########################################

from django.template import RequestContext
from django.shortcuts import render_to_response
from totest.models import AddressProvince
from totest.models import AddressCity
from totest.models import AddressTown
import simplejson
from django.http.response import HttpResponse
import random
from datetime import date
from datetime import timedelta
import logging

logger = logging.getLogger("DreamStar.app")


# 身份证生成页面
def identity_gennerator_creater(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("genneratorCreater.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 生成身份证
def identity_gennerator(request):
    try:
        received_json_towncode_data = str(request.POST.get("townCodeData"))
        received_json_birthdaydate_data = str(request.POST.get("birthdayDateData").replace("-", ""))
        # 地区项 
        id = received_json_towncode_data + received_json_birthdaydate_data
        # 顺序号简单处理 
        id = id + str(random.randint(100, 300))
        i = 0
        count = 0
        # 权重项 
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
            # 算出校验码
        id = id + checkcode[str(count % 11)]
        return HttpResponse(simplejson.dumps(str(id)))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 随机生成身份证
def identity_gennerator_random(request):
    try:
        towncode_code_object = AddressTown.objects.all()
        codelist = []
        for var in towncode_code_object:
            codelist.append(var.code)
        # 地区项     
        id = codelist[random.randint(0, len(codelist))]
        # 年份项 
        id = id + str(random.randint(1930, 2013))
        # 月份和日期项 
        da = date.today() + timedelta(days=random.randint(1, 366))
        id = id + da.strftime('%m%d')
        # 顺序号简单处理 
        id = id + str(random.randint(100, 300))
        i = 0
        count = 0
        # 权重项 
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
            # 算出校验码
        id = id + checkcode[str(count % 11)]
        return HttpResponse(simplejson.dumps(str(id)))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 获得性别
def get_sex_data(request):
    try:
        sex_data_list = [{
            "id": 1,
            "text": "男"
        }, {
            "id": 2,
            "text": "女"
        }]
        sex_data_json_str = simplejson.dumps(sex_data_list)
        return HttpResponse(sex_data_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 获取省数据
def get_province(request):
    try:
        province_data_object = AddressProvince.objects.all()
        province_data_json_list = []
        i = 0
        for var in province_data_object:
            province_data_json_list.append({})
            province_data_json_list[i]["id"] = var.code
            province_data_json_list[i]["text"] = var.name
            i = i + 1
        return HttpResponse(simplejson.dumps(province_data_json_list))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 获取市数据
def get_city(request):
    try:
        province_name_param = request.GET.get("provinceName")
        province_code_param = AddressProvince.objects.get(name=province_name_param).code
        city_data_object = AddressCity.objects.all().filter(province_code=province_code_param)
        city_data_json_list = []
        i = 0
        for var in list(city_data_object):
            city_data_json_list.append({})
            city_data_json_list[i]["id"] = var.code
            city_data_json_list[i]["text"] = var.name
            i = i + 1
        return HttpResponse(simplejson.dumps(city_data_json_list))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 获取区数据
def get_town(request):
    try:
        city_name_param = request.GET.get("cityName")
        city_code_param = AddressCity.objects.get(name=city_name_param).code
        town_data_object = AddressTown.objects.all().filter(city_code=city_code_param)
        town_data_json_list = []
        i = 0
        for var in list(town_data_object):
            town_data_json_list.append({})
            town_data_json_list[i]["id"] = var.code
            town_data_json_list[i]["text"] = var.name
            i = i + 1
        return HttpResponse(simplejson.dumps(town_data_json_list))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
