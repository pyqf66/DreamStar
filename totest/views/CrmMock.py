#!/usr/bin/env python
# coding=utf-8
###########################################
# File: crmMock.py
# Desc: crmMock视图层
# Author: 张羽锋
# History: 2015/12/28 张羽锋 新建
###########################################
from common.util.HttpUrlConnection import HttpUrlConnection
from common.util.InterfaceDataProcessing import InterfaceDataProcessing
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
import simplejson
import json
import datetime
from totest.models import CrmmockInfo
from totest.models import CrmmockPaydata
from common.util.CrmDict import *
import logging

logger = logging.getLogger("DreamStar.app")


# crmMock设置页面
def crmmock_interface(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("crmMock.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 功能菜单-crmmock接口设置数据接口
def crmmock_paydata_json_response(request):
    try:
        paging_data = request.GET
        logger.info(paging_data)
        page = paging_data.get("page")
        logger.info(page)
        rows = paging_data.get("rows")
        logger.info(rows)
        crmmock_paydata_json_data = CrmmockPaydata.objects.all()
        crmmock_paydata_json_list = []
        index_num = 0
        # 数据库读取数据并插入字典
        for i in crmmock_paydata_json_data.order_by("-id"):
            crmmock_paydata_json_list.append({})
            crmmock_paydata_json_list[index_num]["id"] = i.id
            crmmock_paydata_json_list[index_num]["card_no"] = i.card_no
            crmmock_paydata_json_list[index_num]["paylog"] = i.paylog
            crmmock_paydata_json_list[index_num]["crmcode"] = i.crmcode
            crmmock_paydata_json_list[index_num]["growthlevel"] = i.growthlevel
            crmmock_paydata_json_list[index_num]["growthvalue"] = i.growthvalue
            index_num = index_num + 1
        paging_object = Paginator(crmmock_paydata_json_list, rows)
        results = paging_object.page(page).object_list
        logger.info("===========================================================")
        logger.info(type(results))
        logger.info(results)
        total_Records = paging_object.count
        crmmock_paydata_json_str = simplejson.dumps({"totalRecord": total_Records, "results": results})
        logger.info({"totalRecord": total_Records, "results": results})
        return HttpResponse(crmmock_paydata_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


# 功能菜单-crmmock接口设置数据处理
def crmdata_setting(request):
    try:
        result = "success!!!"
        # 接收json数据
        if request.method == 'POST':
            received_json_data = request.POST.get("effectRow")
            data_list = simplejson.loads(received_json_data.encode("utf-8"))
            if "inserted" in data_list:
                for i in list(simplejson.loads(data_list["inserted"])):
                    # 增加数据，如果是欧亚会员卡则请求crm并把CrmMemberID插入库
                    if i["crmcode"] == "oyjt":
                        des_card = i["card_no"]
                        crmmember_ID_url = "http://wap.oysd.cn/Info/WeChatCustomerInfo/" + des_card
                        logger.info(crmmember_ID_url)
                        httpObject = HttpUrlConnection(crmmember_ID_url)
                        crmmember_ID_result = httpObject.request().json()
                        logger.info(crmmember_ID_result)
                        logger.info(type(crmmember_ID_result))
                        crmmock_paydata_db = CrmmockPaydata(card_no=i["card_no"], paylog=i["paylog"],
                                                            crmcode=i["crmcode"], growthlevel=i["growthlevel"],
                                                            growthvalue=i["growthvalue"],
                                                            crmmemberid=crmmember_ID_result["WCC"]["CrmMemberID"])
                    else:
                        crmmock_paydata_db = CrmmockPaydata(card_no=i["card_no"], paylog=i["paylog"],
                                                            crmcode=i["crmcode"], growthlevel=i["growthlevel"],
                                                            growthvalue=i["growthvalue"])
                    crmmock_paydata_db.save()
            if "deleted" in data_list:
                for i in list(simplejson.loads(data_list["deleted"])):
                    # 删除数据
                    CrmmockPaydata.objects.get(id=i["id"]).delete()
            if "updated" in data_list:
                for i in list(simplejson.loads(data_list["updated"])):
                    # 更新数据，同时更新CrmMemberID
                    if i["crmcode"] == "oyjt":
                        des_card = i["card_no"]
                        crmmember_ID_url = "http://wap.oysd.cn/Info/WeChatCustomerInfo/" + des_card
                        logger.info(crmmember_ID_url)
                        httpObject = HttpUrlConnection(crmmember_ID_url)
                        crmmember_ID_result = httpObject.request().json()
                        logger.info(crmmember_ID_result)
                        logger.info(type(crmmember_ID_result))
                        CrmmockPaydata.objects.filter(id=i["id"]).update(id=i["id"], card_no=i["card_no"],
                                                                     paylog=i["paylog"], crmcode=i["crmcode"],
                                                                     growthlevel=i["growthlevel"],
                                                                     growthvalue=i["growthvalue"], crmmemberid=
                                                                     crmmember_ID_result["WCC"]["CrmMemberID"])
                    result = simplejson.dumps(result, ensure_ascii=False)
                    return HttpResponse(result)
                else:
                    result = "error!!!"
                    result = simplejson.dumps(result, ensure_ascii=False)
                    return HttpResponse(result)
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")

# 烟台大悦城crm接口模拟
@csrf_exempt
def ytdyc_crm(request):
    try:
        if request.method == "POST":
            try:
                crmdata = simplejson.loads(request.body.decode("utf-8"))
                logger.info(type(crmdata))
                logger.info(
                    ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>crmdata=" + request.body.decode(
                        "utf-8"))
                logger.info(crmdata["method"])
                logger.info(
                    ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>requestMethod=" + request.method)
                # 数据库中获取配置
                crmurl_object = CrmmockInfo.objects.filter(crmcode="ytdyc")
                crmdata_object = CrmmockPaydata.objects.filter(crmcode="ytdyc", card_no=crmdata["args"]["card_no"])
                crmurl = list(crmurl_object)[0].crmuri
                logger.debug(crmurl)
            except:
                logger.exception("基础数据错误：")
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>crmUri=" + crmurl)
            # 满足条件则生成mock数据
            if crmdata["method"] == "GetVipPayLog":
                logger.info(crmdata["method"])
                dt = crmdata["dt"]
                sign = crmdata["sign"]
                args_dict = crmdata["args"]
                card_no = args_dict["card_no"]
                paydata = dict()
                paydata["errno"] = 0
                paydata["errmsg"] = "OK"
                paydata["dt"] = dt
                paydata["sign"] = sign
                paydata["args"] = list()
                # 判断获取的请求中的卡号是否存在于已配置的卡号列表
                if list(crmdata_object):
                    try:
                        # 数据库读取设置好的支付记录
                        for j in list(crmdata_object.filter(card_no=crmdata["args"]["card_no"])):
                            logger.info(j.paylog)
                            paylog_dict = simplejson.loads(j.paylog)
                            logger.info(paylog_dict)
                        paylog_data_list = paylog_dict["data"]
                        if len(paylog_data_list) == 1:
                            # 设置了建卡时间但未设置消费记录
                            paydata = {"errno": 0, "errmsg": "没找到相关记录，请确认", "args": None}
                        else:
                            # 设置了建卡时间并设置了消费记录
                            jointdate = paylog_dict["data"][0]
                            for k in range(len(paylog_data_list) - 1):
                                num = k + 1
                                salesamt = paylog_data_list[num][0]
                                datetime_str_buy = paylog_data_list[num][1]
                                # 调用大悦城数据Dict
                                args_data = ytdycDict(card_no, jointdate, salesamt, datetime_str_buy)
                                paydata["args"].append(args_data)
                                logger.info(paydata)
                        return HttpResponse(simplejson.dumps(paydata, ensure_ascii=False))
                    except:
                        logger.exception("自设定卡号mock异常:")
                else:
                    try:
                        # 无支付记录的给予默认值
                        yesterday_date = str(datetime.date.today() - datetime.timedelta(days=1))
                        TIME_STR_REGISTER = " 10:59:59"
                        TIME_STR_BUY = " 11:59:59"
                        datetime_str_register = yesterday_date + TIME_STR_REGISTER
                        datetime_str_buy = yesterday_date + TIME_STR_BUY
                        SALESAMT = "600.0000"
                        # 调用大悦城数据Dict
                        args_data = ytdycDict(card_no, datetime_str_register, SALESAMT, datetime_str_buy)
                        paydata["args"].append(args_data)
                    except:
                        logger.exception("非自设定卡号mock异常")
                return HttpResponse(simplejson.dumps(paydata, ensure_ascii=False))
            # 不满足条件则直接请求真实crm接口
            headers_dict = {"Content-type": "application/json"}
            logger.info(crmdata)
            httpObject = HttpUrlConnection(crmurl, method="POST", parameters=crmdata, headers=headers_dict)
            result = httpObject.request()
            if crmdata["method"] == "GetVipCard" and list(crmdata_object):
                try:
                    # 数据库读取设置好的支付记录
                    for j in list(crmdata_object.filter(card_no=crmdata["args"]["card_no"])):
                        growthlevel = j.growthlevel
                        growthvalue = j.growthvalue
                        logger.info(growthlevel)
                    result_dict = simplejson.loads(result.text)
                    result_dict["args"]["growthlevel"] = growthlevel
                    result_dict["args"]["growthvalue"] = growthvalue
                    result = simplejson.dumps(result_dict, ensure_ascii=False)
                except:
                    logger.exception("成长值mock错误：")
        # 非POST请求返回
        else:
            resultDict = {"error": "1", "msg": "不提供POST以外的请求数据"}
            result = simplejson.dumps(resultDict, ensure_ascii=False)
        return HttpResponse(result)
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")

# 欧亚集团crm接口模拟
@csrf_exempt
def oyjt_crm(request, rest_api):
    try:
        crmdata = dict()
        logger.debug(request.body.decode("utf-8"))
        # 判断是json数据还是application/x-www-form-urlencoded请求数据
        if request.body.decode("utf-8") != "":
            if "&" in request.body.decode("utf-8"):
                crmdata = InterfaceDataProcessing.urldecoded(request.body.decode("utf-8"))
                logger.info(crmdata)
                logger.info(crmdata["CrmMemberID"])
            else:
                crmdata = simplejson.loads(request.body.decode("utf-8"))
                logger.info(crmdata)
                logger.info(crmdata["CrmMemberID"])
        # 数据库中获取配置
        crmurl_object = CrmmockInfo.objects.filter(crmcode="oyjt")
        crmurl = list(crmurl_object)[0].crmuri
        logger.info(crmurl)
        logger.info(rest_api)
        logger.info(request.body)
        logger.info(request.body.decode("utf-8"))
        logger.info(request.method)
        logger.info(request.method)
        # 获取rest链接参数
        crmapi = rest_api
        # 拼接真正请求的url
        crm_rest_absapi = crmurl + "/" + rest_api
        logger.info(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>crm_rest_absapi=" + crm_rest_absapi)
        logger.info(request.method)
        if request.method == "POST":
            crmdata_object = CrmmockPaydata.objects.filter(crmcode="oyjt", crmmemberid=crmdata["CrmMemberID"])
            # 获取消费记录
            if crmapi == "Info/GetCrmHyxfjl":
                paydata_detail = dict()
                paydata_detail["Msg"] = ""
                paydata_detail["Bl"] = True
                paydata_detail["Infos"] = list()
                paydata_detail["Info"] = dict()
                paydata_total = dict()
                paydata_total["Msg"] = ""
                paydata_total["Bl"] = True
                paydata_total["Info"] = dict()
                paydata = dict()
                paydata["1"] = paydata_total
                paydata["0"] = paydata_detail
                logger.info(crmdata["CrmMemberID"])
                if list(crmdata_object):
                    try:
                        # 数据库读取设置好的支付记录
                        paylog_dict = dict()
                        logger.debug(paylog_dict)
                        for j in list(crmdata_object):
                            logger.info("++++++++++++++++++++++++++++++++++++")
                            logger.info(j.paylog)
                            paylog_dict = simplejson.loads(j.paylog.encode("utf-8"))
                            logger.info(paylog_dict)
                        paylog_data_list = paylog_dict["data"]
                        logger.info(paylog_data_list)
                    except:
                        logger.exception("支付记录获取错误：")
                    if len(paylog_data_list) == 1:
                        # 设置了建卡时间但未设置消费记录
                        paydata_detail = {"Infos": [], "Info": {"shopCount": "0", "shopSumMoney": None}, "Msg": "",
                                          "Bl": True}
                        paydata_total = {"Info": {"shopCount": "0", "shopSumMoney": None}, "Msg": "", "Bl": True}
                        paydata["0"] = paydata_detail
                        paydata["1"] = paydata_total
                    else:
                        # 设置了建卡时间并设置了消费记录
                        k = 0
                        for k in range(len(paylog_data_list) - 1):
                            num = k + 1
                            amount = paylog_data_list[num][0]
                            logger.info(amount)
                            orderDate = paylog_data_list[num][1]
                            logger.info(orderDate)
                            # 调用大悦城数据Dict
                            info_data = oyjtDict(amount, orderDate)
                            paydata_detail["Infos"].append(info_data)
                            logger.info(paydata_detail)
                    if len(paydata_detail["Infos"]) != 0:
                        shopCount = len(paydata_detail["Infos"])
                        shopSumMoney = float(0)
                        i = 0
                        for i in range(len(paydata_detail["Infos"])):
                            shopSumMoney = shopSumMoney + float(paydata_detail["Infos"][i]["amount"])
                        paydata_detail["Info"]["shopCount"] = str(shopCount)
                        paydata_detail["Info"]["shopSumMoney"] = str(shopSumMoney)
                        paydata_total["Info"]["shopCount"] = str(shopCount)
                        paydata_total["Info"]["shopSumMoney"] = str(shopSumMoney)

                else:
                    # 无支付记录的给予默认值
                    yesterday_date = str(datetime.date.today() - datetime.timedelta(days=1))
                    TIME_STR_BUY = " 11:59:59"
                    orderDate = yesterday_date + TIME_STR_BUY
                    AMOUNT = "600.00"
                    # 调用欧亚数据Dict
                    info_data = oyjtDict(AMOUNT, orderDate)
                    logger.info(info_data)
                    paydata_detail["Infos"].append(info_data)
                    logger.info(paydata_detail)
                    logger.info(paydata)
                    logger.info(paydata[crmdata["hasOrder"]])
                    logger.info(simplejson.dumps(paydata[crmdata["hasOrder"]]))
                    paydata_detail["Info"]["shopCount"] = str(1)
                    paydata_detail["Info"]["shopSumMoney"] = str(AMOUNT)
                    paydata_total["Info"]["shopCount"] = str(1)
                    paydata_total["Info"]["shopSumMoney"] = str(AMOUNT)
                    logger.info(simplejson.dumps(paydata_total))
                return HttpResponse(simplejson.dumps(paydata[crmdata["hasOrder"]], ensure_ascii=False))
            # 不满足条件则直接请求真实crm接口
            headers_dict = {"Content-type": "application/x-www-form-urlencoded"}
            logger.info(crmdata)
            httpObject = HttpUrlConnection(crm_rest_absapi, method="POST", parameters=crmdata, headers=headers_dict)
            result = httpObject.request()

        if request.method == "GET":
            try:
                crmdata_object = CrmmockPaydata.objects.filter(crmcode="oyjt")
                httpObject = HttpUrlConnection(crm_rest_absapi, method="GET")
                logger.info("+++++++++++++++++++++++++++++++++++++")
                result = httpObject.request().json()
                logger.debug(type(result))
                logger.debug(result)
                resultDict = result
                # 获取会员卡信息，其他接口数据直接返回result
                if "Info/MembershipCardBasicInfo" in crmapi and resultDict["Mcb"] != None:
                    logger.debug(resultDict["Mcb"]["CardID"])
                    logger.debug(list(crmdata_object.filter(card_no=resultDict["Mcb"]["CardID"])))
                    if list(crmdata_object.filter(card_no=resultDict["Mcb"]["CardID"])):
                        # 数据库读取设置好的支付记录
                        paylog_dict = dict()
                        for j in list(crmdata_object.filter(card_no=resultDict["Mcb"]["CardID"])):
                            logger.info(j.paylog)
                            paylog_dict = simplejson.loads(j.paylog.encode("utf-8"))
                            logger.info(paylog_dict)
                        # 获取数据库中配置的建卡时间
                        createDate = paylog_dict["data"][0]
                        # 只更改正常获取crm信息中的建卡时间,欧亚没时分秒
                        resultDict["Mcb"]["CreateDate"] = createDate.split(" ")[0]
                        return HttpResponse(simplejson.dumps(resultDict, ensure_ascii=False))
            except:
                logger.exception("GET方法错误：")
            result = simplejson.dumps(resultDict, ensure_ascii=False)
            logger.info(result)
        return HttpResponse(result)
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")

def query_cardno(request):
    try:
        paging_data = request.GET
        logger.info(paging_data)
        crmno_condition = paging_data.get("crmNoCondition")
        logger.info(crmno_condition)
        page = paging_data.get("page")
        logger.info(page)
        rows = paging_data.get("rows")
        logger.info(rows)
        crmmock_paydata_json_data = CrmmockPaydata.objects.all()
        crmmock_paydata_json_list = []
        index_num = 0
        # 数据库读取数据并插入字典
        for i in crmmock_paydata_json_data.filter(card_no__icontains=crmno_condition).order_by("-id"):
            crmmock_paydata_json_list.append({})
            crmmock_paydata_json_list[index_num]["id"] = i.id
            crmmock_paydata_json_list[index_num]["card_no"] = i.card_no
            crmmock_paydata_json_list[index_num]["paylog"] = i.paylog
            crmmock_paydata_json_list[index_num]["crmcode"] = i.crmcode
            index_num = index_num + 1
        paging_object = Paginator(crmmock_paydata_json_list, rows)
        results = paging_object.page(page).object_list
        logger.info("===========================================================")
        logger.info(type(results))
        logger.info(results)
        total_Records = paging_object.count
        crmmock_paydata_json_str = simplejson.dumps({"totalRecord": total_Records, "results": results})
        logger.info({"totalRecord": total_Records, "results": results})
        logger.info(crmmock_paydata_json_str)
        return HttpResponse(crmmock_paydata_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
