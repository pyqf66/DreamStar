# coding=utf-8
###########################################
# File: readConfig.py
# Desc: 读取配置文件工具类
# Author: zhangyufeng
# History: 2015/10/13 zhangyufeng 新建
###########################################
from ConfigParser import SafeConfigParser
import os
import logging


class ReadConfig:
    u'''
        conf.ini和config.conf配置文件路径不可更改
    '''

    global logger
    logger = logging.getLogger("DreamStar.app")

    def __init__(self):
        try:
            current_dir = os.getcwd()
            self.__ini_config_file = current_dir + "\\config\\" + "config.ini"
            self.__conf_config_file = current_dir + "\\config\\" + "config.conf"
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 读取windows ini配置文件
    # 配置文件格式
    #   [table]
    #   key=value
    def ini_data(self, label, key):
        try:
            config = SafeConfigParser()
            config.read(self.__config_file)
            return config.get(label, key)
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 读取linux配置文件
    # 配置文件格式
    #   key=value
    def conf_data(self, key):
        try:
            config_file = open(self.__conf_config_file, 'r')
            result = config_file.readlines()
            result_deal_list = []
            key_value_list = []
            for i in result:
                result_deal_list.append(i.strip('\n'))
            for j in result_deal_list:
                key_value_list.append(j.split('='))
            result_dict = dict(key_value_list)
            return result_dict[key]
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")
