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
    name = "aqaq"
    allowed_domains = ["aqaq.com"]
    start_urls = [
"http://www.aqaq.com/list/female/new-in?limit=all","http://www.aqaq.com/list/female/dresses?limit=all","http://www.aqaq.com/list/female/jumpsuits?limit=all","http://www.aqaq.com/list/female/tops?limit=all","http://www.aqaq.com/list/female/jackets?limit=all","http://www.aqaq.com/list/female/skirts?limit=all","http://www.aqaq.com/list/female/trousers?limit=all","http://www.aqaq.com/list/female/jewellery?limit=all","http://www.aqaq.com/list/female/accessories?limit=all","http://www.aqaq.com/list/female/aq-aq-pop-shop?limit=all","http://www.aqaq.com/list/female/aq-aq-aw13-preview?limit=all","http://www.aqaq.com/list/female/private-benjamin?limit=all","http://www.aqaq.com/list/female/take-the-plunge?limit=all","http://www.aqaq.com/list/male/new-in?limit=all","http://www.aqaq.com/list/male/idol-magazine-picks?limit=all","http://www.aqaq.com/list/male/mono-chrome?limit=all","http://www.aqaq.com/list/male/techno-print?limit=all","http://www.aqaq.com/list/male/eldorado?limit=all","http://www.aqaq.com/list/male/platoon?limit=all","http://www.aqaq.com/list/male/aq-aq-re-genesis?limit=all","http://www.aqaq.com/list/male/shorts?limit=all","http://www.aqaq.com/list/male/trousers?limit=all","http://www.aqaq.com/list/male/denim?limit=all","http://www.aqaq.com/list/male/denim?limit=all","http://www.aqaq.com/list/male/outerwear?limit=all","http://www.aqaq.com/list/male/sweatshirts?limit=all","http://www.aqaq.com/list/male/shirts?limit=all","http://www.aqaq.com/list/male/t-shirts?limit=all",
                        "http://www.aqaq.com/list/female/view-all?limit=all",
			"http://www.aqaq.com/list/male/view-all?limit=all",
			"http://www.aqaq.com/list/male/sale?limit=all",
			"http://www.aqaq.com/list/male/sale?limit=all"
		
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//ul[@class="list"]/li')
	for site in sites:
                name=site.select('a[@class="product-name"]/@href').extract()
		a.append(name)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write(str(i)[3:-2]+os.linesep)
			yield Request(str(i)[3:-2].rstrip('\n'),callback=self.parsed)
			
	f.close()
    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
       	sites=hxs.select('//div[@class="contents"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="aqaq"
		item['currency']="Euro"
		item['source']=response.url	
		s=''
        	title=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/h1//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		#print title,source
		
		cost=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/div[@class="price-container"]/span[@class="regular-price"]/span[@class="price"]//text()').extract()
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
			cost=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/div[@class="price-container"]/p[@class="special-price"]/span[@class="price"]//text()').extract()
			s=''
			for k in cost:
				s+=k
			l=re.findall("(\d[0-9]*)",s)
			l=l[0]
			s=''
			for i in l:
				s=s+i
			print s
		item['cost']=int(s.encode("utf-8"))
		type_dress=	hxs.select('//div[@class="breadcrumbs-container"]/ul[@class="breadcrumbs"]/li[3]/a/span/text()').extract()
		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
		category=hxs.select('//div[@class="breadcrumbs-container"]/ul[@class="breadcrumbs"]/li[2]/a/span/text()').extract()
		s=''
		for k in category:
			s=s+k
		item['category']=s.encode("utf-8")
		
		size=hxs.select('//div[@class="input-box"]/select[@name="super_attribute[127]"]/option/@val').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		
		fit=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/div[@id="tabs"]/div[@id="info-tab"]/dl/dd[1]//text()').extract()		
		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		
		fabric=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/div[@id="tabs"]/div[@id="info-tab"]/dl/dd[2]//text()').extract()		
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")

		
		s=''
		desc=hxs.select('//div[@class="contents"]/div[@class="right_col"]/div[@class="form"]/div[@class="row-block"]/p//text()').extract()
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		
		s=''
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
			

