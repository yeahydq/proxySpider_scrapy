#coding:utf-8
import scrapy
import requests


from proxySpider_scrapy.db.db_helper import DB_Helper
from proxySpider_scrapy.detect.detect_proxy import Detect_Proxy
from proxySpider_scrapy.detect.detect_manager import Detect_Manager
from proxySpider_scrapy.items import ProxyItem

'''
这个类的作用是将代理数据进行爬取
'''
class ProxySpider(scrapy.Spider):
    name = 'proxy'
    start_urls = ["http://www.xicidaili.com/nn/"]
    allowed_domains = []
    db_helper = DB_Helper()
    detecter = Detect_Manager(5)
    Page_Start = 1
    Page_End = 4
    headers = {
        "Accept:text/html": "application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        # "Cookie:_gat=1": "PHPSESSID=3e37j0485m37s56h1rrlo6mci6; 647564024=56deyEog4Ho1%2FyRtYYkl4NcAqzshg9DUihgM05%2B1; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1475299357457; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1475200552,1475291867; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1475299358; _ga=GA1.2.698006203.1475200552",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    }
    def make_requests_from_url(self, url):
        return scrapy.http.Request(url, headers=self.headers)
        #return requests.get(url=url, headers=self.headers)
        # r = requests.get(url=url, headers=config.HEADER, timeout=config.TIMEOUT, proxies=proxies)

    def parse(self, response):
        '''
        解析出其中的ip和端口
        :param response:
        :return:
        '''

        trs = response.xpath('//tr[@class="odd" or @class=""]')
        for tr in trs:
            item = ProxyItem()
            tds = tr.xpath('./td/text()').extract()
            for td in tds:
                content = td.strip()
                if len(content)>0:
                    if content.isdigit():
                        item['port'] = content
                        print 'ip:',item['ip']
                        print 'port:',item['port']
                        break
                    if content.find('.')!= -1:
                        item['ip'] = content
            yield item
        if self.Page_Start < self.Page_End:
            new_url = self.start_urls[0]+str(self.Page_Start)
            self.Page_Start += 1
            yield scrapy.Request(new_url,headers=self.headers,callback=self.parse)

