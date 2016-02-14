#!/usr/bin/env python
# coding=utf-8
###########################################
# File: Index.py
# Desc: 首页视图层
# Author: 张羽锋
# History: 2016/01/01 张羽锋 新建
###########################################

from django.template import RequestContext
from django.shortcuts import render_to_response
import simplejson
from django.http.response import HttpResponse
import logging

logger = logging.getLogger("DreamStar.app")


# 主页接口
def index(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("index.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 功能菜单json数据接口
def interface_test_treegrid_json_response(request):
    try:
        interface_test_treegrid_json_list = [{
            "id": 1,
            "text": "http接口",
            "children": [{
                "text": "快递信息查询接口",
                "attributes": {
                    "url": "/interfaceTest/treegrid?interfaceCode=kdxxcx"
                }
            }, {
                "text": "烟台大悦城CRM解绑接口",
                "attributes": {
                    "url": "/interfaceTest/treegrid?interfaceCode=ytdyccrmcancel"
                }
            }]
        }, {
            "id": 2,
            "text": "数据生成工具",
            "children": [{
                "text": "手机号生成器",
                "attributes": {
                    "url": "/testTool/generation/mobilePhoneCreater"
                }
            }, {
                "text": "身份证生成器",
                "attributes": {
                    "url": "/testTool/generation/identityGenneratorCreater"
                }
            }, {
                "text": "经纬度距离计算器",
                "attributes": {
                    "url": "/testTool/generation/haversineCalculate"
                }
            }]
        }, {
            "id": 3,
            "text": "结果统计",
            "children": [{
                "text": "临时页面 ",
                "attributes": {
                    "url": "/tmpPage"
                }
            }]
        }, {
            "id": 4,
            "text": "参数设置",
            "children": [{
                "text": "接口测试设置",
                "attributes": {
                    "url": "/parameters/config/settings/interfaceSettingsTreegrid"
                }
            }, {
                "text": "crmMock测试设置",
                "attributes": {
                    "url": "/parameters/config/crmmock/crmMockInterface"
                }
            }, {
                "text": "crm信息设置",
                "attributes": {
                    "url": "/parameters/config/crmmock/crmSettingsPage"
                }
            }]
        }]
        interface_test_treegrid_json_str = simplejson.dumps(interface_test_treegrid_json_list)
        return HttpResponse(interface_test_treegrid_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
