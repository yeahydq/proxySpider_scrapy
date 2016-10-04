#coding:utf-8
__author__ = 'dick'

import urllib2
import urllib

user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/38.0.2125.111 Safari/537.36")

request_header = {
    "User-Agent": user_agent,  # 伪装成浏览器访问
}

url="http://ip.chinaz.com/getip.aspx"
proxy_host = "http://218.72.172.72:8888"  # 随便添加了账户名和密码，只是为了防止填写账户名密码暂停的情况
proxy_host = "http://171.38.100.107:8123"  # 随便添加了账户名和密码，只是为了防止填写账户名密码暂停的情况
# req = urllib2.Request(url, headers=request_header)
# req.set_proxy(proxy_host,"http")
try:
    # response = urllib2.urlopen(req)
    response = urllib.urlopen(url, proxies={"http": proxy_host})

    # if response.getcode() != 200:
    #
    if response.getcode() != 200:
        print "fail"
        response.read()
    else:
        print "ok"
    content = response.read().decode("utf-8")
    print content
except Exception, e:
    print proxy_host, 'bad proxy'
