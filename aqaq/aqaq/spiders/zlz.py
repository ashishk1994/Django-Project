from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from aqaq.items import aqaqItem

import os
import urlparse
import ast
import re
a=[]

class DmozSpider(BaseSpider):
    name = "zlz"
    allowed_domains = ["zlz.com"]
    start_urls = ["http://zlz.com/dress_l178_45","http://zlz.com/tops_l163","http://zlz.com/bottoms_l233","http://zlz.com/dress_l178","http://zlz.com/bottoms_l233_2","http://zlz.com/bottoms_l233_3","http://zlz.com/bottoms_l233_4","http://zlz.com/bottoms_l233_5","http://zlz.com/bottoms_l233_6","http://zlz.com/bottoms_l233_7","http://zlz.com/bottoms_l233_8","http://zlz.com/bottoms_l233_9","http://zlz.com/bottoms_l233_10","http://zlz.com/bottoms_l233_11","http://zlz.com/bottoms_l233_12","http://zlz.com/bottoms_l233_13","http://zlz.com/bottoms_l233_14","http://zlz.com/bottoms_l233_15","http://zlz.com/bottoms_l233_16","http://zlz.com/bottoms_l233_17","http://zlz.com/dress_l178_2","http://zlz.com/dress_l178_3","http://zlz.com/dress_l178_4","http://zlz.com/dress_l178_5","http://zlz.com/dress_l178_6","http://zlz.com/dress_l178_7","http://zlz.com/dress_l178_8","http://zlz.com/dress_l178_9","http://zlz.com/dress_l178_10","http://zlz.com/dress_l178_11","http://zlz.com/dress_l178_12","http://zlz.com/dress_l178_13","http://zlz.com/dress_l178_14","http://zlz.com/dress_l178_15","http://zlz.com/dress_l178_16","http://zlz.com/dress_l178_17","http://zlz.com/dress_l178_18","http://zlz.com/dress_l178_19","http://zlz.com/dress_l178_20","http://zlz.com/dress_l178_21","http://zlz.com/dress_l178_22","http://zlz.com/dress_l178_23","http://zlz.com/dress_l178_24","http://zlz.com/dress_l178_25","http://zlz.com/dress_l178_26","http://zlz.com/dress_l178_27","http://zlz.com/dress_l178_28","http://zlz.com/dress_l178_29","http://zlz.com/dress_l178_30","http://zlz.com/dress_l178_31","http://zlz.com/dress_l178_32","http://zlz.com/dress_l178_33","http://zlz.com/dress_l178_34","http://zlz.com/dress_l178_35","http://zlz.com/dress_l178_36","http://zlz.com/dress_l178_37","http://zlz.com/dress_l178_38","http://zlz.com/dress_l178_39","http://zlz.com/dress_l178_40","http://zlz.com/dress_l178_41","http://zlz.com/dress_l178_42","http://zlz.com/dress_l178_43","http://zlz.com/dress_l178_44","http://zlz.com/dress_l178_45","http://zlz.com/dress_l178_46","http://zlz.com/dress_l178_47","http://zlz.com/dress_l178_48","http://zlz.com/dress_l178_49","http://zlz.com/dress_l178_50"]
    
    def parse(self, response):
	hxs = HtmlXPathSelector(response)
       	sites= hxs.select('//div[@class="name"]')
	for site in sites:
       		name=site.select('a/@href').extract()
		print name
		a.append(name)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write("http://www.zlz.com/"+str(i)[3:-2].rstrip('\n')+os.linesep)
			yield Request("http://www.zlz.com/"+str(i)[3:-2].rstrip('\n'),callback=self.parser)			
	f.close()

    def parser(self,response):
	hxs = HtmlXPathSelector(response)
        sites= hxs.select('//div[@id="wrapper"]')
        items = []
        for site in sites:
		item=aqaqItem()
		item['source']=response.url
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="product2"]/div[@class="mainimg"]/div[1]/div[1]/img/@src').extract())
	

		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")

		
		title=hxs.select('//div[@class="product3"]/div[1]/form/h1/text()').extract()
		s=''
		for k in title:
			s=s+k
		item['title']=s.encode("utf-8")

		

		size=hxs.select('//ul[@class="sizeselect clearfix"]/li/text()').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")

	 	cost=hxs.select('//li[@class="mm_price value"]/span/text()').extract()
		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
		s=''
		for i in l:
			s=s+i
		item['cost']=int(s.encode("utf-8"))
		
		
		type_dress = hxs.select('//div[@class="bread"]/a[3]/@title').extract()
		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")

		item['advertiser']="ZLZ"
		item['currency']="AmericanDollar"	
		if title==[]:
			item['title']="Not available"
				
		item['desc']="Not available"
		
		item['color']="Not availabale"
		
		if image_urls==[]:
			item['image_urls']=="Not available"
		if item['size']=='':
			item['size']='Not available'
		
		item['fabric']='Not available'
		
		item['fit']="Not available"
		item['category']="female"
		item['category']="Not available"
		
		if item['type_dress']=='':
			item['type_dress']="General"	
		item.save()
		#items.append(item)
                return item
	
	

