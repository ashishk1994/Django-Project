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
    name = "dk"
    allowed_domains = ["donnakaran.com"]
    start_urls = ["http://www.donnakaran.com/shop-ready-to-wear/dresses/","http://www.donnakaran.com/shop-ready-to-wear/dresses/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/dresses/#/?s=12&p=3","http://www.donnakaran.com/shop-ready-to-wear/dresses/#/?s=12&p=4","http://www.donnakaran.com/shop-ready-to-wear/cashmere-and-sweaters/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/cashmere-and-sweaters/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/cashmere-and-sweaters/#/?s=12&p=3","http://www.donnakaran.com/shop-ready-to-wear/tops/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/tops/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/jackets-and-outerwear/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/jackets-and-outerwear/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/evening/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/evening/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/runway/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/runway/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/modern-icons/#/?s=12&p=5","http://www.donnakaran.com/shop-ready-to-wear/modern-icons/#/?s=12&p=4","http://www.donnakaran.com/shop-ready-to-wear/modern-icons/#/?s=12&p=3","http://www.donnakaran.com/shop-ready-to-wear/modern-icons/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/modern-icons/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/cashmere-collection/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/cashmere-collection/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/casual-luxe/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/casual-luxe/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/pre-fall-2013/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/pre-fall-2013/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/fall-2013/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/fall-2013/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/resort-2014/#/?s=12&p=2","http://www.donnakaran.com/shop-ready-to-wear/resort-2014/#/?s=12&p=1","http://www.donnakaran.com/shop-ready-to-wear/resort-2014/#/?s=12&p=3","http://www.donnakaran.com/shop-ready-to-wear/resort-2014/#/?s=12&p=4"]
    
    def parse(self, response):
	hxs = HtmlXPathSelector(response)
       	sites= hxs.select('//div[@class="fixer"]/div[1]/ul/li/div[2]')

	for site in sites:
       		name=site.select('a/@href').extract()
		print name
		a.append(name)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write("http://www.donnakaran.com"+str(i)[3:-2].rstrip('\n')+os.linesep)
			yield Request("http://www.donnakaran.com"+str(i)[3:-2].rstrip('\n'),callback=self.parser)			
	f.close()

    def parser(self,response):
	hxs = HtmlXPathSelector(response)
        sites= hxs.select('//div[@id="container"]')
        items = []
        for site in sites:
		item=aqaqItem()
		item['source']=response.url
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="partial-look_viewer"]/div[1]/div[1]/img/@src').extract())
		if image_urls=='':
			image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="partial-product_viewer"]/div[1]/div[1]/img/@src').extract())
		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")

		
		title=hxs.select('//div[@class="partial-product_info"]/h1[@class="product-name"]//text()').extract()
		s=''
		for k in title:
			s=s+k
		if s=="":
			title=hxs.select('//div[@class="partial-look_info"]/h1[@class="look-name"]//text()').extract()
			s=''
			for k in title:
				s=s+k
		item['title']=s.encode("utf-8")

		

		size= hxs.select('//li[@class="option option-size"]/ul/li/a/@title').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")

		cost =  hxs.select('//ul[@class="price-set"]/li[1]/span[1]/text()').extract()
		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
		if len(l)!=0:
			l=l[0]
                s=''
                for i in l:
                        s=s+i
		item['cost']=s.encode("utf-8")

		desc =  hxs.select('//ul[@class="price-set"]/li[1]/span[1]/text()').extract()
		s=''
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")

		color =   hxs.select('//ul[@class="option-value-set"]/li/a/img/@alt').extract()
		s=''
		for k in color:
			s=s+k
		item['color']=s.encode("utf-8")
		item['fabric']="Not available"
		item['fit']="Not available"
		item['advertiser']="donnakaran"
		item['currency']="AmericanDollar"	
		if title==[]:
			item['title']="Not available"
				
		if desc==[]:
			item['desc']="Not available"
		
		if color=="[]" or item['color']=="":
			item['color']="Not availabale"
		
		if image_urls==[]:
			item['image_urls']=="Not available"
		item['type_dress']= "Not available"
		if item['size']=='':
			item['size']='Not available'
		
		if item['fabric']=='':
			item['fabric']='Not available'
		
		if item['fit']=='':
			item['fit']="Not available"
		item['category']="female"
		if item['category']=='':
			item['category']="Not available"
		
		if item['type_dress']=='':
			item['type_dress']="General"	

		#items.append(item)
                return item
	
	

