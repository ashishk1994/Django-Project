from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
a=[]
b=[]
from aqaq.aqaq.items import aqaqItem
import os
import urlparse
import ast
import re
class aqaqspider(BaseSpider):
    name = "jabong"
    allowed_domains = ["jabong.com"]
    start_urls = [
	"http://www.jabong.com/women/clothing/womens-tops/",
	"http://www.jabong.com/women/clothing/women-ethnic-wear/womens-kurtas-and-kurtis/",
	"http://www.jabong.com/women/clothing/womens-dresses/",
	"http://www.jabong.com/women/clothing/women-ethnic-wear/womens-sarees/",
	"http://www.jabong.com/women/clothing/womens-tunics/",
	"http://www.jabong.com/women/clothing/women-winter-wear/",
	"http://www.jabong.com/women/clothing/women-trousers-and-shorts/womens-leggings/",
	]

    def parse(self, response):
        k=response.url.split("/")[-1]


	hxs = HtmlXPathSelector(response)
        sites=hxs.select('//div[@id="content"]/section[@class="full-width pt5 mt10"]/div[@class="right-content fr"]/div[@class="box box-bgcolor"]/section[@class="full-width sorted-by-product mt10 p-list"]/ul[@id="productsCatalog"]/li')
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

#	f=open("next","w+")
#	next_page=hxs.select('//div[@id="Brand"]/ul[@id="facet_brand"]/li/@data-brand-key').extract()
#	for i in next_page:
#		s=response.url.split("/")
#		if i not in b:
#			if s[-1]=="":
#				b.append(i)
#				f.write(i + os.linesep)
#       			yield Request(response.url + i,callback=self.parse)
#	f.close()

    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
	sites=hxs.select('//div[@id="content"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="jabong"
		item['currency']="Rs"
		item['source']=response.url	
		s=''
        	title=hxs.select('//div[@class="prd-brand"]/div[@class="fl ml10 c666 prd-brand-detail"]/span//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		
		cost=hxs.select('//div[@id="price_div"]/span[@id="before_price"]/span[2]/span[1]//text()').extract()

		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
                s=''
                for i in l:
                        s=s+i

		item['cost']=s.encode("utf-8")
		print item['cost'],item['title']
		type_dress= hxs.select('//div[@class="breadcrumbs fs12 l-hght26"]/a[4]/@title').extract()

		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
		item['category']="Female"
		
		size=hxs.select('//div[@id="OptionsSingleDefault"]/div[@class="mt10"]/ul[@id="listProductSizes"]/li//text()').extract()

		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		color=hxs.select('//table[@class="c999 fs12 mt10 f-bold"]/tr[2]/td[2]//text()').extract()
		s=''
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")
		
		fit=hxs.select('//table[@class="c999 fs12 mt10 f-bold"]/tr[6]/td[2]//text()').extract()


		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		
		fabric=hxs.select('//table[@class="c999 fs12 mt10 f-bold"]/tr[1]/td[2]//text()').extract()

		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")

		
		s=''
		desc= hxs.select('//div[@id="productInfo"]/p[1]//text()').extract()
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		
		s=''
	 	
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@id="prdbig"]/ul[@class="imageview-slider"]/li[1]/img/@src').extract())
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
			item['category']="Not available"
		#if item['type_dress']=='':
		#	item['type_dress']="General"
		print item['title']	
		item.save()
#item.save()
		return item
						

