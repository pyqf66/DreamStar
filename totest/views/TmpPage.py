#!/usr/bin/env python
# coding=utf-8
###########################################
# File: TmpPage.py
# Desc: 临时页面视图层
# Author: 张羽锋
# History: 2016/01/01 张羽锋 新建
###########################################

from django.template import RequestContext
from django.shortcuts import render_to_response
import logging

logger = logging.getLogger("DreamStar.app")


# 临时页面
def tmp_page(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("tmp.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
