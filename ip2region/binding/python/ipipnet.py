#coding=utf-8
import requests
for i in xrange(1003):
    r= requests.get("http://freeapi.ipip.net/118.28.8.8")
    print r.text
