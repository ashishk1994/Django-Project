from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from aqaq.aqaq.items import aqaqItem

import os
import urlparse
import ast
import re
a=[]

class DmozSpider(BaseSpider):
    name = "flipkart"
    allowed_domains = ["flipkart.com","flixcart.com"]
    start_urls = ["http://www.flipkart.com/womens-clothing/pr?p%5B%5D=sort%3Dpopularity&sid=2oq%2Cc1r#jumpTo=0|15",
    	"http://www.flipkart.com/womens-clothing/biba~brand/pr?sid=2oq%2Cc1r&otracker=hp_nmenu_sub_women_1_Biba",
    	"http://www.flipkart.com/womens-clothing/dresses-skirts/pr?p[]=sort%3Dpopularity&sid=2oq%2Cc1r%2Cxzt",
    	"http://www.flipkart.com/womens-clothing/jeans-shorts/pr?sid=2oq,c1r,uuk&otracker=ch_vn_womensclot_filter_Categories_Jeans%20%26%20Shorts"]
    
    def parse(self, response):
	hxs = HtmlXPathSelector(response)
       	sites= hxs.select('//div[@class="pu-visual-section"]')
	for site in sites:
       		name=site.select('a/@href').extract()
		print name
		a.append(name)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write("http://www.flipkart.com"+str(i)[3:-2].rstrip('\n')+os.linesep)
			yield Request("http://www.flipkart.com"+str(i)[3:-2].rstrip('\n'),callback=self.parser)			
	f.close()
	next_page=hxs.select('//div[@id="pagination"]/a/@href').extract()
	next_page=next_page[0]
	print next_page
	if next_page:
		yield Request(urlparse.urljoin(response.url, next_page),callback=self.parse)
    def parser(self,response):
	hxs = HtmlXPathSelector(response)
        sites= hxs.select('//div[@id="fk-mainbody-id"]')
        items = []
        for site in sites:
		item=aqaqItem()
		desc=[]
		item['source']=response.url
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//span[@id="main-image-id"]/div[1]/div[1]/img/@src').extract())
	

		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")

		
		title=hxs.select('//div[@class="mprod-summary-title fksk-mprod-summary-title"]/h1/text()').extract()
		s=''
		for k in title:
			s=s+k
		item['title']=s.encode("utf-8")

		color=hxs.select('//div[@class="sectionImage paletteImage"]/a/div/div/@title').extract()
		s=''
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")

		size=hxs.select('//div[@class="multiselect-item "]/text()').extract()
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		
		s=''
		cost=hxs.select('//div[@class="prices"]/meta[@itemprop="price"]/@content').extract()
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
		s=''
		for i in l:
			s=s+i


			
		item['cost']=int(s.encode("utf-8"))

		item['advertiser']="flipkart"
		item['currency']="IndianRupees"	
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
		
		item['fabric']='Not available'
		
		item['fit']="Not available"
		item['category']="female"
		
		item['type_dress']="General"	
		item.save()
		#items.append(item)
                return item
	
	
	
