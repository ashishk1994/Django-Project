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
    name = "walls"
    allowed_domains = ["wallis.co.uk"]
    start_urls = ["http://www.wallis.co.uk/en/wluk/category/dresses-265974/view-all-dresses-266009#pageSize=200&catalogId=33058&viewAllFlag=false&sort_field=Relevance&langId=-1&beginIndex=1&storeId=12557&parent_categoryId=209167&categoryId=215487",
"http://www.wallis.co.uk/en/wluk/category/petite-265975/view-all-petite-clothing-266014#pageSize=200&catalogId=33058&viewAllFlag=false&sort_field=Relevance&langId=-1&beginIndex=1&storeId=12557&parent_categoryId=209168&categoryId=215493",
"http://www.wallis.co.uk/en/wluk/category/party-shop-2412906/christmas-party-dresses-2413530#pageSize=200&catalogId=33058&viewAllFlag=false&sort_field=Relevance&langId=-1&beginIndex=1&storeId=12557&parent_categoryId=283995&categoryId=1457622"]
    
    def parse(self, response):
	hxs = HtmlXPathSelector(response)
       	sites= hxs.select('//div[@id="wrapper_page_content"]/div[@class="wrapper_product_list cf cols_4"]/div/ul/li/a/@href').extract()

	for site in sites:
       		name=site
		print name
		a.append(name)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write("htt"+str(i)[3:].rstrip('\n')+os.linesep)
			yield Request("htt"+str(i)[3:].rstrip('\n'),callback=self.parser)			
	f.close()

    def parser(self,response):
	hxs = HtmlXPathSelector(response)
	print response
        sites= hxs.select('//div[@id="wrapper_outer"]')
        items = []
        for site in sites:
		item=aqaqItem()
		item['source']=response.url
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="product_viewer cf"]/div[2]/div[1]/a/@href').extract())
	

		s=''
		for k in image_urls:
			s=s+k
		item['image_urls']=s.encode("utf-8")

		
		title=hxs.select('//div[@class="sp_10 product_column_2"]/div[1]/h1/text()').extract()
		s=''
		for k in title:
			s=s+k
		item['title']=s.encode("utf-8")

		cost =  hxs.select('//li[@class="now_price product_price"]/span/text()').extract()
		s=''
		for k in cost:
			s=s+k
		if s=='':
			cost =  hxs.select('//li[@class="product_price"]/span/text()').extract()
			for k in cost:
				s+=k
		l=re.findall("(\d[0-9]*)",s)
		l=l[0]
	        s=''
		for i in l:
			s=s+i
		item['cost']=int(s.encode("utf-8"))
		
		color = hxs.select('//li[@class="product_colour"]/span/text()').extract()
		s=''
		for k in color:
			s=s+k
		item['color']=s.encode("utf-8")


		item['advertiser']="wallis"
		item['currency']="Euro"	
		if title==[]:
			item['title']="Not available"
				
	
		item['desc']="Not available"
		
		if color=="[]" or item['color']=="":
			item['color']="Not availabale"
		
		if image_urls==[]:
			item['image_urls']=="Not available"
		item['type_dress']= "Not available"
		item['size']='Not available'
		
		item['fabric']='Not available'
		
		item['fit']="Not available"
		item['category']="female"
		
		item['type_dress']="General"	
		item.save()
		#items.append(item)
                return item
