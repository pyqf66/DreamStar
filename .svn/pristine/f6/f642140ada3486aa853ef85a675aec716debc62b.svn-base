#!/usr/bin/env python
# coding=utf-8
###########################################
# File: MobilephoneCreater.py
# Desc: 手机号生成器视图层
# Author: 张羽锋
# History: 2015/01/01 张羽锋 新建
###########################################

from django.template import RequestContext
from django.shortcuts import render_to_response
import simplejson
from django.http.response import HttpResponse
import random
import logging

logger = logging.getLogger("DreamStar.app")


# 功能菜单-手机号生成功能页面视图接口
def cellphone_number_creater(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("mobilePhoneCreater.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 随机手机号生成
def create_cellphone_number(request):
    try:
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        mobile_phone = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        return HttpResponse(simplejson.dumps(mobile_phone))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
