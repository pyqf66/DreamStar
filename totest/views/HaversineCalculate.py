#!/usr/bin/env python
# coding=utf-8
###########################################
# File: HaversineCalculate.py
# Desc: 经纬度计算视图层
# Author: 张羽锋
# History: 2016/01/01 张羽锋 新建
###########################################

from django.template import RequestContext
from django.shortcuts import render_to_response
import simplejson
from django.http.response import HttpResponse
from math import radians, cos, sin, asin, sqrt
import logging

logger = logging.getLogger("DreamStar.app")


# 经纬度工具视图接口
def haversine_calculate(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("haversineCalculate.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 计算经纬度的两点距离
def calculate_haversine(request):
    try:
        # 经度1，纬度1，经度2，纬度2 （十进制度数）  
        # Calculate the great circle distance between two points  
        # on the earth (specified in decimal degrees) 
        lon1 = float(request.POST.get("aLongitude"))
        lat1 = float(request.POST.get("aLatitude"))
        lon2 = float(request.POST.get("bLongitude"))
        lat2 = float(request.POST.get("bLatitude"))
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        logger.info(lat2)
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # 将十进制度数转化为弧度  
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine公式  
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里  
        return HttpResponse(simplejson.dumps(c * r))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
