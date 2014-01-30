from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
a=[]
from aqaq.aqaq.items import aqaqItem
import os
import urlparse
import ast
import re
class aqaqspider(BaseSpider):
    name = "inkfruit"
    allowed_domains = ["inkfruit.com"]
    start_urls = [
		"http://www.inkfruit.com/womens-tops?misc_ref_code=menu_womens-tops",		
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//section[@id="content"]/section[@id="catalog"]')
	for site in sites:
                name=site.select('div[@class="item"]/a/@href').extract()
		for i in name:
			a.append(i)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write( "http://www.inkfruit.com" + str(i) + os.linesep)
			yield Request("http://www.inkfruit.com" + str(i).rstrip('\n'),callback=self.parsed)
			
	f.close()
    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
       	sites=hxs.select('//body')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="inkfruit"
		item['currency']="Rupees"
		item['source']=response.url	
		s=''
        	title= hxs.select('//section[@id="main-area"]/section[@id="size-selection-bar"]/div[@class="details"]/span//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		#print title,source
		
		cost=hxs.select('//section[@id="main-area"]/section[@id="content"]/section[@id="action-area"]/label[@class="visible"]//text()').extract()
		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
                s=''
                for i in l:
                        s=s+i
		item['cost']=int(s.encode("utf-8"))
		type_dress=hxs.select('//section[@id="main-area"]/section[@id="content"]/div[@id="breadcrumbs"]/a[4]//text()').extract()
		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
		category=hxs.select('//section[@id="main-area"]/section[@id="content"]/div[@id="breadcrumbs"]/a[2]//text()').extract()
		s=''
		for k in category:
			s=s+k
		item['category']=s.encode("utf-8")
		
		size=hxs.select('//section[@id="main-area"]/section[@id="size-selection-bar"]/ul[@class="sizes visible reset-ul"]/li//text()').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		
		
		fabric=hxs.select('//section[@id="main-area"]/section[@id="content"]/section[@id="movable-column"]/section[@id="product-detail"]/label[@class="care"]/section[@id="washcare"]//ul/li//text()').extract()
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")

		
		s=''
		d=''
		flag=0
		desc=hxs.select('//section[@id="main-area"]/section[@id="content"]/section[@id="movable-column"]/section[@id="product-detail"]/p//text()').extract()
		for k in desc:
			s=s+k
				
		item['desc']=s.encode("utf-8")
		
		fit=hxs.select('//section[@id="main-area"]/section[@id="content"]/section[@id="movable-column"]/section[@id="product-detail"]//text()').extract()

		s=''
		for k in fit:
			s=s+k
		item['fit']=s
	 	color=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/div[@id="colours"]/ul/li/a/img/@src').extract()
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")
		
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="contents"]/div[@class="left_col"]/div[@class="product-img-box"]/div[@class="media-container"]/a/@href').extract())
		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")
		
		if title==[]:
			item['title']="Not available"
		
		if item['cost']=="[]" or item['cost']==[]:
			item['cost']=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/div[@class="price-container"]/p[@class="special-price"]/span[@class="price"]//text()').extract()
		
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
		
		if item['category']=='':
			item['category']="Not available"
		if item['type_dress']=='':
			item['type_dress']="General"
		
		item.save()
		return item
			

