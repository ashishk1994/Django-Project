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
    name = "myntra"
    allowed_domains = ["myntra.com"]
    start_urls = [
	"http://www.myntra.com/women-dresses",
"http://www.myntra.com/women-shirts-tops-tees",
"http://www.myntra.com/women-sweaters-sweatshirts",
"http://www.myntra.com/women-shrugs-jackets",
"http://www.myntra.com/women-jeans-jeggings",
"http://www.myntra.com/women-shorts-skirts",
"http://www.myntra.com/women-leggings-capris",
"http://www.myntra.com/women-trousers",


	]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//div[@id="mk-search-results"]/ul[@class="mk-cf"]/li')

	for site in sites:
                name=site.select('a[@class="clearfix"]/@href').extract()
		for i in name:
			a.append(response.url + i)
		print a

	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write(str(i).rstrip('\n')+os.linesep)
			yield Request(str(i).rstrip('\n'),callback=self.parsed)
			
	f.close()
	
	next_page=hxs.select('//a[@class="mk-more-products-link btn normal-btn"]/@href').extract()[0]
	if next_page: 
		if next_page!="":
	       		yield Request(urlparse.urljoin(response.url, next_page), self.parse)

    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
	sites=hxs.select('//div[@class="mk-body mynt-layout-new"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="myntra"
		item['currency']="Rs"
		item['source']=response.url	
		s=''
        	title=hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-product-shop mk-cf"]/div[@class="mk-product-guide mk-f-right "]/div[@id="mk-filler"]/div[@class="mk-zoom-hide"]/h1[1]//text()').extract()

		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		cost=hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-product-shop mk-cf"]/div[@class="mk-product-guide mk-f-right "]/div[@id="mk-filler"]/div[@class="mk-zoom-hide"]/h3[@class="red"]/meta[@itemprop="price"]/@content').extract()

		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
                s=''
                for i in l:
                        s=s+i
		item['cost']=int(s.encode("utf-8"))
		size=hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-product-shop mk-cf"]/div[@class="mk-product-guide mk-f-right "]/div[@id="mk-filler"]/div[@class="mk-zoom-hide"]/div[@class="mk-product-option-cont"]/div[@class="mk-custom-drop-down mk-size-drop mk-size-drop-pdp"]/div[@class="flat-size-options"]/div[@class="options"]//text()').extract()
		s=''

		for k in size:
			if k!='\n' and k!='\r' and k!=' ':
				s=s+k
				s=s+','

		l=re.findall('[a-z0-9]+',s)
		s=''
		for k in l:
			s=s+k
			s=s+' '
		item['size']=s.encode("utf-8")	
		s=''
		desc=hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-pdpv1-description"]/ul[@class="mk-pdpv1-product-helper mk-cf"]/li[@itemprop="description"]/p//text()').extract()

		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		
		fabric=hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-pdpv1-description"]/ul[@class="mk-pdpv1-product-helper mk-cf"]/li[7]/p//text()').extract()
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")
		fit=hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-pdpv1-description"]/ul[@class="mk-pdpv1-product-helper mk-cf"]/li[9]/p//text()').extract()


		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		s=''
		type_dress=hxs.select('//div[@class="mk-pdp-carousel-breadcrumbs mk-location-breadcrumbs  mk-pdpv1-carousel-breadcrumbs"]/div[4]/a//text()').extract()
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
		color=hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-product-shop mk-cf"]/div[@class="mk-product-guide mk-f-right "]/div[@id="mk-filler"]/div[@class="mk-zoom-hide"]/div[@class="mk-product-option-cont"]/div[@class="mk-colour rs-carousel"]/ul[@class="rs-carousel-runner mk-cf"]/li/a/img/@title').extract()
		s=''
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="mk-cf"]/div[@id="mk-product-page"]/div[@class="mk-product-shop mk-cf"]/div[@class="mk-product-media mk-f-left"]/div[@class="mk-more-views rs-carousel mk-f-left"]/ul[@class="rs-carousel-runner"]/li[@class="rs-carousel-item img-selected"]/a/@href').extract())
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
		if item['type_dress']=='':
			item['type_dress']="General"
		print item['title'],item['type_dress']	
		item.save()
		return item
			

