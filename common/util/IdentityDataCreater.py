# coding=utf-8
###########################################
# File: InterfaceDataProcessing.py
# Desc: 身份数据生成器
# Author: zhangyufeng
# History: 2015/11/21 zhangyufeng 新建
###########################################
import os
import random
from datetime import date
from datetime import timedelta
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DC_PATH = BASE_DIR + "\districtcode.txt"
logger = logging.getLogger("DreamStar.app")


# 随机生成身份证号
def get_district_code():
    try:
        with open(DC_PATH) as file:
            data = file.read()
            district_list = data.split('\n')
        for node in district_list:
            # print node
            if node[10:11] != ' ':
                state = node[10:].strip()
            if node[10:11] == ' ' and node[12:13] != ' ':
                city = node[12:].strip()
            if node[10:11] == ' ' and node[12:13] == ' ':
                district = node[14:].strip()
                code = node[0:6]
                code_list.append({"state": state, "city": city, "district": district, "code": code})
    except Exception as e:
        logger.error(e)
        logger.exception(u"地区字典读取错误如下:")


def gennerator():
    try:
        global code_list
        code_list = []
        if not code_list:
            get_district_code()
        id = code_list[random.randint(0, len(code_list))]['code']  # 地区项
        id = id + str(random.randint(1930, 2013))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  # ，顺序号简单处理
        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5',
                      '9': '3', '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
            id = id + check_code[str(count % 11)]  # 算出校验码
            return id
    except Exception as e:
        logger.error(e)
        logger.exception(u"身份证生成错误如下:")
