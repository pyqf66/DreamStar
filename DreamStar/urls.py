#coding=utf-8
###########################################
# File: urls.py
# Desc: 总控制层
# Author: 张羽锋
# History: 2015/11/02 张羽锋 新建
###########################################
from totest.urls import parameters_config_urls, data_generation_urls, interface_test_urls

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
from django.conf.urls import include, url
from django.contrib import admin
from DreamStar import settings

urlpatterns =[ 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tmpPage$', "totest.views.tmp_page"),
    url(r'^interfaceTest/', include(interface_test_urls)),
    url(r'^testTool/', include(data_generation_urls)),
    url(r'^parameters/config/', include(parameters_config_urls)),
    url(r'^index/$', 'totest.views.index'),
    url(r'^index/interfaceTestTreegridJsonResponse.json$', 'totest.views.interface_test_treegrid_json_response'),
    url(r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATICFILES_DIRS}),
]
