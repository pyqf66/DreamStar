#!/usr/bin/env python
# coding=utf-8
###########################################
# File: crmSettings.py
# Desc: crmSetting视图层
# Author: 张羽锋
# History: 2016/01/05 张羽锋 新建
###########################################
from common.util.HttpUrlConnection import HttpUrlConnection
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
import simplejson
import datetime
from totest.models import CrmmockInfo
import logging

logger = logging.getLogger("DreamStar.app")


# crm信息设置页面
def crm_settings_page(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("crmSettings.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 功能菜单-crmmock接口设置数据接口
def crm_settings_json_response(request):
    try:
        paging_data = request.GET
        logger.info(paging_data)
        page = paging_data.get("page")
        logger.info(page)
        rows = paging_data.get("rows")
        logger.info(rows)
        crm_settings_json_data = CrmmockInfo.objects.all()
        crm_settings_json_list = []
        index_num = 0
        # 数据库读取数据并插入字典
        for i in crm_settings_json_data.order_by("-id"):
            crm_settings_json_list.append({})
            crm_settings_json_list[index_num]["id"] = i.id
            crm_settings_json_list[index_num]["crmuri"] = i.crmuri
            crm_settings_json_list[index_num]["crmcode"] = i.crmcode
            index_num = index_num + 1
        paging_object = Paginator(crm_settings_json_list, rows)
        results = paging_object.page(page).object_list
        logger.info("===========================================================")
        logger.info(type(results))
        logger.info(results)
        total_Records = paging_object.count
        crm_settings_json_str = simplejson.dumps({"totalRecord": total_Records, "results": results})
        return HttpResponse(crm_settings_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 功能菜单-crmmock接口设置数据处理
def crm_setting(request):
    try:
        result = "success!!!"
        # 接收json数据
        if request.method == 'POST':
            received_json_data = request.POST.get("effectRow")
            data_list = simplejson.loads(received_json_data.encode("utf-8"))
            if "inserted" in data_list:
                for i in list(simplejson.loads(data_list["inserted"])):
                    # 增加数据
                    crm_settings_db = CrmmockInfo(crmuri=i["crmuri"], crmcode=i["crmcode"])
                    crm_settings_db.save()
            if "deleted" in data_list:
                for i in list(simplejson.loads(data_list["deleted"])):
                    # 删除数据
                    CrmmockInfo.objects.get(id=i["id"]).delete()
            if "updated" in data_list:
                for i in list(simplejson.loads(data_list["updated"])):
                    # 更新数据
                    CrmmockInfo.objects.filter(id=i["id"]).update(id=i["id"], crmuri=i["crmuri"], crmcode=i["crmcode"])
            result = simplejson.dumps(result)
            return HttpResponse(result)
        else:
            result = "error!!!"
            result = simplejson.dumps(result)
            return HttpResponse(result)
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
