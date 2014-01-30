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
    name = "blooming"
    allowed_domains = ["bloomingdales.com"]
    start_urls = [
	"http://www1.bloomingdales.com/shop/womens-apparel/blazers-jackets?id=1001521",
#"http://www1.bloomingdales.com/shop/womens-apparel/cashmere-shop?id=1000658",
#"http://www1.bloomingdales.com/shop/womens-apparel/coats?id=1001520",
#"www1.bloomingdales.com/shop/womens-apparel/denim?id=5545",
#"http://www1.bloomingdales.com/shop/womens-apparel/dresses?id=21683",
"http://www1.bloomingdales.com/shop/womens-apparel/tops-tees?id=5619"


	]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//div[@id="bl_main_container"]/div[@class="bl_main"]/div[@id="bl_hp_main"]/div[@class="bl_mainContent_no_bottom_padding"]/div[@id="catSplash"]/div[1]/div[@class="row"]/div[@class="columned"]/div[1]/div[@id="macysGlobalLayout"]/div[@id="thumbnails"]/div[@class="productThumbnail showQuickView"]/div[@class="shortDescription"]')

	for site in sites:
                name=site.select('a/@href').extract()
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
	
	next_page=hxs.select('//div[@id="pageNumbersTop"]/div[@id="topPages"]/ul[@id="bottomPages"]/li[@id="bottomRightArrow"]/div[1]/a[1]/@href').extract()[0]
	if next_page: 
        	yield Request(urlparse.urljoin(response.url, next_page), self.parse)

    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
	sites=hxs.select('//div[@class="bl_main"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="bloomingdale"
		item['currency']="Dollar"
		item['source']=response.url	
		s=''
        	title=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@class="pdp_right"]/div[@id="productDescription"]/div[@class="pdp_productInfo"]/div[@class="pdp_descriptionAndPrice"]/h1//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		
		cost=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@class="pdp_right"]/div[@id="productDescription"]/div[@class="pdp_productInfo"]/div[@class="pdp_descriptionAndPrice"]/div[1]/div[@id="PriceDisplay"]/div[1]/div[@class="priceSale"]/div[@class="singleTierPrice"]/span[1]//text()').extract()

		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
		if l:
			l=l[0]
		s=''
		for i in l:
			s=s+i
		if s=='':
			cost=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@class="pdp_right"]/div[@id="productDescription"]/div[@class="pdp_productInfo"]/div[@class="pdp_descriptionAndPrice"]/div[1]/div[@id="PriceDisplay"]/div[1]/div[@class="priceSale"]/div[@class="singleTierPrice"]/span[2]//text()').extract()
			for k in cost:
				s=s+k
			l=re.findall("(\d[0-9]*)",s)
			if l:
				l=l[0]
			s=''
			for i in l:
				s=s+i
		print cost	
		item['cost']=int(s.encode("utf-8"))

		print item['cost'],item['title']
		l=response.url.split('/')

		#s=''
		#for k in type_dress:
		#	s=s+k
		#item['type_dress']=s.encode("utf-8")
		if re.search("Jacket",item['title']):
			item['type_dress']="Jackets"
		elif re.search("Blazer",item['title']):
			item['type_dress']="Blazers"
		elif re.search("Cashmere",item['title']):
			item['type_dress']="Cashmere"
		elif re.search("Coat",item['title']):
			item['type_dress']="Coat"
		elif re.search("Jeans",item['title']):
			item['type_dress']="Jeans"
		elif re.search("Dress",item['title']):
			item['type_dress']="Dresses"
		elif re.search("Top",item['title']):
			item['type_dress']="Top"
		else:
			item['type_dress']="Not Available"
		item['category']="Female"
		
		size=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@class="pdp_right"]/div[@id="productDescription"]/div[@class="pdp_member_area"]/div[@class="pdp_member_colorSize"]/div[@class="pdp_member_size"]/div[2]/div[1]/ul[1]/li//text()').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		color=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@class="pdp_right"]/div[@id="productDescription"]/div[@class="pdp_member_area"]/div[@class="pdp_member_colorSize"]/div[@class="pdp_member_color"]/div[@id="colorHeadersDiv"]/span[2]//text()').extract()
		s=''
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")
		
		fit=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@id="pdp_tabs"]/div[@id="pdp_tabs_body"]/div[@id="pdp_tabs_body_details"]/div[@id="pdp_tabs_body_left"]/ul[1]/li//text()').extract()

		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		
		fabric=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@id="pdp_tabs"]/div[@id="pdp_tabs_body"]/div[@id="pdp_tabs_body_details"]/div[@id="pdp_tabs_body_left"]/ul[1]/li//text()').extract()
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")

		
		s=''
		desc=hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@id="pdp_tabs"]/div[@id="pdp_tabs_body"]/div[@id="pdp_tabs_body_details"]/div[@id="pdp_tabs_body_left"]/ul[1]/li//text()').extract()
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		
		s=''
	 	
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@id="pdp_main"]/div[1]/div[@class="pdp_container"]/div[@class="pdp_left"]/div[@id="pdp_left_image"]/div[@id="zoomerDiv"]/img/@src').extract())
		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")
		
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
			item['category']="Female"
		#if item['type_dress']=='':
		#	item['type_dress']="General"
		print item['title']	
		item.save()
		return item
			

