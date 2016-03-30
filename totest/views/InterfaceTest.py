#!/usr/bin/env python
# coding=utf-8
###########################################
# File: InterfaceTestTreegrid.py
# Desc: 接口测试视图层
# Author: 张羽锋
# History: 2016/01/01 张羽锋 新建
###########################################

from django.template import RequestContext
from django.shortcuts import render_to_response
from totest.models import HttpInterfaceInfo
import simplejson
from django.http.response import HttpResponse
from common.util.HttpUrlConnection import HttpUrlConnection
from common.util.InterfaceDataProcessing import InterfaceDataProcessing
import logging

logger = logging.getLogger("DreamStar.app")


# 功能菜单视图接口
def interface_test_treegrid(request):
    try:
        # 获取链接的参数
        interface_code_data = request.GET.get('interfaceCode')
        logger.info(interface_code_data)
        interface_info_data = HttpInterfaceInfo.objects.get(interface_code=interface_code_data)
        logger.info(interface_code_data)
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("interfaceTestTreegrid.html", {"interfaceInfoData": interface_info_data},
                                  context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 获得接口测试方法下拉框
def interface_test_method_json_response(request):
    try:
        interface_test_method_json_list = [{
            "id": 0,
            "text": "GET"
        }, {
            "id": 1,
            "text": "POST"
        }]
        interface_test_method_json_str = simplejson.dumps(interface_test_method_json_list)
        return HttpResponse(interface_test_method_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 接口请求
def interface_test_form(request):
    try:
        global received_json_interface_code
        if request.method == 'POST':
            received_json_url = request.POST.get("testUrl")
            received_json_interface_code = request.POST.get("interfaceCodeValue")
            received_json_data = request.POST.get("effectRow")
            received_json_dict = simplejson.loads(received_json_data)
            headers_dict = {"Content-type": "application/json"}

        elif request.method == 'GET':
            received_json_url = request.GET.get("testUrl")
            received_json_interface_code = request.GET.get("interfaceCodeValue")
            received_json_data = request.GET.get("effectRow")
            logger.debug(received_json_data)
            received_json_dict = simplejson.loads(received_json_data)
            headers_dict = {}
        secretkey_value = HttpInterfaceInfo.objects.get(interface_code=received_json_interface_code).secretkey
        logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        processing_data_object = InterfaceDataProcessing(received_json_interface_code, received_json_dict,
                                                         secretkey_value)
        logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # 进行是否满足InterfaceDataProcessing数据处理字典的判断
        if processing_data_object.processing() != 0:
            received_json_dict = processing_data_object.processing()
        http_oject = HttpUrlConnection(received_json_url, method=request.method, parameters=received_json_dict,
                                       headers=headers_dict)
        result = http_oject.request()
        return HttpResponse(result)
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
