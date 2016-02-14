from django.test import TestCase

# from traceback import format_tb
# from traceback import format_exc
# from traceback import format_exception
# from traceback import format_exception_only
# from traceback import format_list
# import traceback
# import logging
# import sys
# logger=logging.getLogger("DreamStar.app")
# 
# try:
#     raise
# except Exception as e:
#     logger.error(format_tb(e.__traceback__)[0])

# Create your tests here.

test = "CrmMemberID=141659805&startDate=2015-10-21&endDate=2016-01-19&hasOrder=0"


def urldecoded(data):
    data_list_first = data.split("&")
    data_list_second = list()
    for tmp in data_list_first:
        data_list_second.append(tmp.split("="))
    result = dict()
    for i in data_list_second:
        result[i[0]] = i[1]
    return result


print(urldecoded(test))
