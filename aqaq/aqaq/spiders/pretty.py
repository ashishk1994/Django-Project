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
    name = "pretty"
    allowed_domains = ["prettysecrets.com"]
    start_urls = [
	"http://prettysecrets.com/apparel-clothes/tops",
"http://prettysecrets.com/apparel-clothes/dresses?p=1",
"http://prettysecrets.com/apparel-clothes/dresses?p=2"


	]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//div[@class="grid"]/div[@id="catalog-layered-list"]/table[@id="product_grid_container"]/tr/td')

	for site in sites:
                name=site.select('a[@class="product-name"]/@href').extract()
		for i in name:
			a.append(i)
		print a

	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write(str(i).rstrip('\n')+os.linesep)
			yield Request(str(i).rstrip('\n'),callback=self.parsed)
			
	f.close()
	
	#next_page=hxs.select('//div[@id="pageNumbersTop"]/div[@id="topPages"]/ul[@id="bottomPages"]/li[@id="bottomRightArrow"]/div[1]/a[1]/@href').extract()[0]
	#if next_page: 
        #	yield Request(urlparse.urljoin(response.url, next_page), self.parse)

    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
	sites=hxs.select('//div[@id="container"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="prettysecrets"
		item['currency']="Rs"
		item['source']=response.url	
		s=''
        	title=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/h1[1]//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		
		cost=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@class="grid_7 alpha"]/form[1]/div[@class="decision"]/div[@class="price-box"]/span[@class="regular-price"]/span[@class="price"]//text()').extract()


		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
                s=''
                for i in l:
                        s=s+i
		if s=='':
			cost=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@class="grid_7 alpha"]/form[1]/div[@class="decision"]/div[@class="price-box"]/p[@class="special-price"]/span[@class="price"]//text()').extract()
			for k in cost:
				s=s+k
			l=re.findall("(\d[0-9]*)",s)
			s=''
			for i in l:
				s=s+i

		item['cost']=int(s.encode("utf-8"))
		print item['cost'],item['title']
		
		size=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@id="detailsAccordion"]/div[@id="longDescriptionContainer"]/div[@class="long-description"]/p[2]//text()').extract()

		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		color=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@id="detailsAccordion"]/div[@id="detailsContainer"]/table[1]/tbody[1]/tr[3]/td[1]//text()').extract()

		s=''
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")
		
		fit=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@id="detailsAccordion"]/div[@id="longDescriptionContainer"]/div[@class="long-description"]/p[3]//text()').extract()


		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		
		fabric=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@id="detailsAccordion"]/div[@id="detailsContainer"]/table[1]/tbody[1]/tr[4]/td[1]//text()').extract()

		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")

		type_dress=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@id="detailsAccordion"]/div[@id="detailsContainer"]/table[1]/tbody[1]/tr[5]/td[1]//text()').extract()
		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
		s=''
		desc=hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-info"]/div[@class="grid"]/div[@id="detailsAccordion"]/div[@id="longDescriptionContainer"]/div[@class="long-description"]/p[1]//text()').extract()

		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		
		s=''
	 	
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@id="matter"]/div[@id="product-header"]/div[@id="product-media"]/a[@class="product-image primary cloud-zoom"]/@href').extract())
		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")
		item['category']="Female"		
		if title==[]:
			item['title']="Not available"
		
		if item['cost']=="[]" or item['cost']==[]:
			item['cost']="Not available"
		
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
		#if item['type_dress']=='':
		#	item['type_dress']="General"
		print item['title']	
		item.save()
		return item
			

