# coding=utf-8
###########################################
# File: data_generation_urls.py
# Desc: 数据生成控制层
# Author: 张羽锋
# History: 2016/01/02 张羽锋 新建
###########################################
"""DreamStar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

urlpatterns = [
    url(r'^generation/mobilePhoneCreater', 'totest.views.cellphone_number_creater'),
    url(r'^generation/createMobilePhone', 'totest.views.create_cellphone_number'),
    url(r'^generation/identityGennerator$', 'totest.views.identity_gennerator'),
    url(r'^generation/identityGenneratorRandom', 'totest.views.identity_gennerator_random'),
    url(r'^generation/identityGenneratorCreater', 'totest.views.identity_gennerator_creater'),
    url(r'^generation/haversineCalculate', 'totest.views.haversine_calculate'),
    url(r'^generation/calculateHaversine', 'totest.views.calculate_haversine'),
    url(r'^generation/getProvince', 'totest.views.get_province'),
    url(r'^generation/getCity', 'totest.views.get_city'),
    url(r'^generation/getTown', 'totest.views.get_town'),
    url(r'^generation/getSexData', 'totest.views.get_sex_data'),
]
