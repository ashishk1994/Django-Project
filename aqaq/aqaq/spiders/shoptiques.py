from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from aqaq.items import aqaqItem
#from shoptiques2.items import ShoptiquesItem

import os
import urlparse
import ast
import re
a=[]

class DmozSpider(BaseSpider):
    name = "shoptiques2"
    allowed_domains = ["shoptiques.com"]
    start_urls = ["http://www.shoptiques.com/categories/clothing","http://www.shoptiques.com/categories/clothing?max=90&offset=90","http://www.shoptiques.com/categories/clothing?max=90&offset=180","http://www.shoptiques.com/categories/clothing?max=90&offset=270","http://www.shoptiques.com/categories/clothing?max=90&offset=360","http://www.shoptiques.com/categories/clothing?max=90&offset=450","http://www.shoptiques.com/categories/clothing?max=90&offset=540","http://www.shoptiques.com/categories/clothing?max=90&offset=630","http://www.shoptiques.com/categories/clothing?max=90&offset=720","http://www.shoptiques.com/categories/clothing?max=90&offset=810","http://www.shoptiques.com/categories/clothing?max=90&offset=900"]
    def parse(self, response):
	hxs = HtmlXPathSelector(response)
       	sites= hxs.select('//div[@class="product with-swatches  listproduct"]')
	for site in sites:
       		name=site.select('div[@class="productImageHolder"]/a/@href').extract()
		#print name
		a.append(name)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write("http://www.shoptiques.com"+str(i)[3:-2].rstrip('\n')+os.linesep)
			yield Request("http://www.shoptiques.com"+str(i)[3:-2].rstrip('\n'),callback=self.parser)			
	f.close()
    def parser(self,response):
	hxs = HtmlXPathSelector(response)
        sites= hxs.select('//div[@class="product-show"]')
        items = []
        for site in sites:
		item=aqaqItem()
		item['source']=response.url
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="image-gallery"]/div[1]/ul[1]/li[1]/a/@href').extract())
		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")

		item['image_urls']
		title=hxs.select('//title//text()').extract()
		s=''
		for k in title:
			s=s+k
		item['title']=s.encode("utf-8")
		color=hxs.select('//div[@id="variant-container"]/div[1]/div[1]/div[1]/a//text()').extract()
		s=''
		for k in color:
			s=s+k
			s=s+','
		l=re.findall("(\d[0-9]*)",s)
                s=''
                for i in l:
                        s=s+i

		item['color']=s.encode("utf-8")
		size=hxs.select('//div[@id="variant-container"]/div[1]/div[2]/div[1]/div[1]/a//text()').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		desc=hxs.select('//div[@class="accordion"]/div[1]/div[2]/div[1]/p[2]//text()').extract()
		s=''
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		fit=hxs.select('//div[@class="accordion"]/div[2]/div[2]/div[1]/span[1]//text()').extract()
		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		fabric=hxs.select('//div[@class="accordion"]/div[@class="accordion-group"]/div[@id="collapseOne"]/div[1]/p[3]//text()').extract()
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")
		type_dress = hxs.select('//div[@id="product-show"]/div[1]/div[@class="left-panel"]/ul[1]/li[2]//text()').extract()
		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")

		item['cost']="Not available"
		item['advertiser']="shoptiques"
		item['currency']="AmericanDollar"	
		if title==[]:
			item['title']="Not available"
				
		if desc==[]:
			item['desc']="Not available"
		
		if color=="[]" or item['color']=="":
			item['color']="Not availabale"
		
		if image_urls==[]:
			item['image_urls']=="Not available"
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
		item.save()
    		return item
		#items.append(item)
#return item
	
	
