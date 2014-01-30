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
    name = "saks"
    allowed_domains = ["saksfifthavenue.com"]
    start_urls = [
	"http://www.saksfifthavenue.com/Women-s-Apparel/Dresses/shop/_/N-52flor/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Tops-and-Tees/shop/_/N-52floo/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Sweaters/shop/_/N-52g463/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Jackets-and-Vests/shop/_/N-52fzyx/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Outerwear/shop/_/N-52floy/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Denim/shop/_/N-52flov/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Pants-and-Shorts/shop/_/N-52flot/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Leggings/shop/_/N-52ib4o/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Skirts/shop/_/N-52flos/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Suits/shop/_/N-52ft07/Ne-6lvnb5",
	"http://www.saksfifthavenue.com/Women-s-Apparel/Leather-and-Faux-Leather/shop/_/N-52jh20/Ne-6lvnb5",
	
		
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//div[@id="saksContainer"]/div[@id="saksBody"]/div[@id="pa-content-wrap"]/div[@id="pa-right-content"]')
	for site in sites:
                name=site.select('div[@id="product-container"]/div/div[@class="product-text"]/a/@href').extract()
		for i in name:
			a.append(i)
	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write(str(i)+os.linesep)
			yield Request(str(i).rstrip('\n'),callback=self.parsed)
			
	f.close()
#	next_page=hxs.select('//div[@id="saksContainer"]/div[@id="saksBody"]/div[@id="pa-content-wrap"]/div[@id="pa-right-content"]/div[@class="pagination-container"]/ol[@class="pa-page-number"]/li/a[@class="next"]/@href').extract()[0]
	#print next_page
#	if next_page: 
#		next_page= "http://www.saksfifthavenue.com" + next_page 
#       	yield Request(urlparse.urljoin(response.url, next_page), self.parse)

    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
	sites=hxs.select('//div[@id="saksBody"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="saksfifthavenue"
		item['currency']="Rs"
		item['source']=response.url	
		s=''
        	title=hxs.select('//table[@class="newskin"]/tr[1]/td[1]/div[@class="pdp-item-container clearfix  "]/div[@class="pdp-reskin-right-container "]/div[@class="pdp-reskin-general-info"]/h2[@class="description"]//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		type_dress=hxs.select('//table[@class="newskin"]/tr[1]/td[1]/div[@class="pdp-item-container clearfix  "]/div[@class="pdp-reskin-right-container "]/div[@class="pdp-reskin-general-info"]/h1[@class="brand"]//text()').extract()
		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
		print title,type_dress
		size=hxs.select('//table[@class="newskin"]/tr[1]/td[1]/div[@class="pdp-item-container clearfix  "]/div[@class="pdp-reskin-right-container "]/div[@class="pdp-reskin-size-color clearfix"]/table[1]/tr[1]/div[@class="dropdown-container "]/div[@class="dropdown-helper"]/select[1]/option/@data-product-size').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")		
		color=hxs.select('//table[@class="newskin"]/tr[1]/td[1]/div[@class="pdp-item-container clearfix  "]/div[@class="pdp-reskin-right-container "]/div[@class="pdp-reskin-size-color clearfix"]/table[1]/tr[1]/div[@class="dropdown-container "]/div[@class="dropdown-helper"]/select[1]/option/@data-colorname').extract()
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")

		s=''
		desc=hxs.select('//div[@class="productCopy-container"]/table[1]/tr[1]/td[1]/span[@class="pdp-reskin-detail-content"]/p[1]//text()').extract()
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		item['category']="Female"
		
		fabric=hxs.select('//div[@class="productCopy-container"]/table[1]/tr[1]/td[1]/span[@class="pdp-reskin-detail-content"]/ul[1]/li//text()').extract()
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")
		
		fit=hxs.select('//div[@class="productCopy-container"]/table[1]/tr[1]/td[1]/div[@class="reskin-fitmodel-container"]/div[@class="reskin-ft-shown"]//text()').extract()
		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")

		cost=hxs.select('//div[@class="pdp-reskin-addtobag"]/table[@class="reskin-price-container"]/tr[1]/td[@class="clearfix"]/div[@class="reskin-regular-price-container"]/span[@class="product-price"]//text()').extract()
		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*[.])",s)
		print l
		l=l[-1]
		s=''
		for k in l:
			s=s+k
		s=s[:-1]
		s=s[1:]
		item['cost']=int(s.encode("utf-8"))
	
		
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="flashContent"]/object[1]/object[1]/a[1]/img/@src').extract())
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
		if item['type_dress']=='':
			item['type_dress']="General"
		print item['title']	
		item.save()
		return item
			

