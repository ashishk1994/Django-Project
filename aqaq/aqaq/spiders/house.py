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
    name = "house"
    allowed_domains = ["houseoffraser.co.uk"]
    start_urls = [
	"http://www.houseoffraser.co.uk/women%27s+designer+dresses/301,default,sc.html"	
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//div[@id="pageBackground"]/div[1]/div[@id="productSearchRefinementsAjaxContainer"]/div[1]/div[@class="wrapperColumn"]/div[@class="mainColumn"]/ol[@class="productListing clearfix"]/li')
	for site in sites:
                name=site.select('a[@class="productImage"]/@href').extract()
		a.append(name)
		print a

	f=open("url","w+")
	for i in a:
		if str(i)=='[]':
			pass;
		else:
			f.write(str(i)[3:-2].rstrip('\n')+os.linesep)
			yield Request(str(i)[3:-2].rstrip('\n'),callback=self.parsed)
			
	f.close()
	
	next_page=hxs.select('//div[@id="pageBackground"]/div[1]/div[@id="productSearchRefinementsAjaxContainer"]/div[1]/div[@class="wrapperColumn"]/div[@class="mainColumn"]/div[@class="pagination "][2]/div[@class="paginationNumbers"]/a[@class="pager nextPage"]/@href').extract()[0]
	if next_page: 
        	yield Request(urlparse.urljoin(response.url, next_page), self.parse)

    def parsed(self,response):
	hxs = HtmlXPathSelector(response)
	sites=hxs.select('//div[@id="pageBackground"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="houseoffraser"
		item['currency']="Euro"
		item['source']=response.url	
		s=''
        	title=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@id="productTitle"]/h1/span[2]//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		#print title,source
		
		cost=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@class="productDetails clearfix"]/span[@id="productPriceContainer"]/p[@class="price"]//text()').extract()

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
			cost=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@class="productDetails clearfix"]/span[@id="productPriceContainer"]/p[@class="priceNow"]//text()').extract()
			for k in cost:
				s=s+k
			l=re.findall("(\d[0-9]*)",s)
			l=l[0]
			s=''
			for i in l:
				s=s+i

		item['cost']=s.encode("utf-8")
		type_dress=hxs.select('//div[@id="pageContainer"]/ol[@class="breadcrumbs clearfix"]/li[3]/a[@itemprop="breadcrumb"]//text()').extract()

		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
#category=
#		hxs.select('//div[@id="pageContainer"]/ol[@class="breadcrumbs clearfix"]/li[2]//text()').extract()

#		s=''
#		for k in category:
#			s=s+k
		item['category']="Female"
		
		size=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@class="productRefinement"]/div[@class="tabInner clearfix"]/div[@id="configuration"]/form[1]/div[@id="newSizeSwatches"]/ul[@class="sizeSelector"]/li//text()').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		
		fit=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@class="tabs"]/div[@id="psiTab1"]/span[@itemprop="description"]/li//text()').extract()

		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		
		fabric=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@class="tabs"]/div[@id="psiTab1"]/span[@itemprop="description"]/ul/li//text()').extract()
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")

		
		s=''
		desc=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@class="tabs"]/div[@id="psiTab1"]/span[@itemprop="description"]//text()').extract()
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		
		s=''
	 	color=hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@class="col col-10"]/div[@class="middleColumn"]/div[@class="productRefinement"]/div[@class="tabInner clearfix"]/div[@id="configuration"]/form[1]/div[@class="productRefinement"]/div[@id="colourRefinementTitle"]/h2/span[@id="selectedColourValue"]//text()').extract()

		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")
		
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@class="wrapperColumn"]/div[@class="col col-15"]/div[@id="imagesColumn"]/div[@id="productSlidesWrapper"]/div[@id="productSlides"]/img[1]/@src').extract())
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
			

