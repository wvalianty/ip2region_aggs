#coding=utf-8
from ip2Region import Ip2Region
searcher = Ip2Region("/tmp/delete/ip2region/data/ip2region.db")
ip = "1.1.1.1"
data = searcher.binarySearch(ip)
print "%s|%s " % (data["city_id"], data["region"])
