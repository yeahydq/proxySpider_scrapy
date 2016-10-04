#coding:utf-8
#!/usr/bin/env python
__author__ = 'dick'

import random
from proxySpider_scrapy.db import SQLiteHelper

'''
这个类主要用于产生随机代理
'''
class RandomProxy(object):


    def __init__(self):#初始化一下数据库连接
        self.db_helper = SQLiteHelper()
        self.count =self.db_helper.selectCount()

    def process_request(self, request, spider):
        '''
        在请求上添加代理
        :param request:
        :param spider:
        :return:
        '''
        idList = range(1,self.count+1)
        id = random.choice(idList)
        result = self.db_helper.selectOne('proxys','id=\'1\'','')
        print result
        self.db_helper.close()
        # request.meta['proxy'] =settings.HTTP_PROXY
        # HTTP_PROXY ='http://127.0.0.1:8123'#使用Tor

if __name__=="__main__":
    s = RandomProxy()
    print s.process_request()[0]
    # print s.selectAll()