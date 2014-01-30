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
    name = "promod"
    allowed_domains = ["promod.eu"]
    start_urls = [
	"http://www.promod.eu/women/tops/page-O2.html",
	"http://www.promod.eu/women/tops/page-O2P2.html","http://www.promod.eu/women/tops/page-O2P3.html","http://www.promod.eu/women/tops/page-O2P4.html","http://www.promod.eu/women/tops/page-O2P5.html","http://www.promod.eu/women/dresses/page-O2.html","http://www.promod.eu/women/dresses/page-O2P2.html","http://www.promod.eu/women/dresses/page-O2P3.html","http://www.promod.eu/women/knitwear/page-O2.html","http://www.promod.eu/women/knitwear/page-O2P2.html","http://www.promod.eu/women/knitwear/page-O2P3.html","http://www.promod.eu/women/knitwear/page-O2P4.html","http://www.promod.eu/women/shirts---tunics/page-O2.html","http://www.promod.eu/women/shirts---tunics/page-O2P2.html","http://www.promod.eu/women/shirts---tunics/page-O2P3.html","http://www.promod.eu/women/jackets/page-O2.html","http://www.promod.eu/women/jackets/page-O2P2.html","http://www.promod.eu/women/trousers/page-O2.html","http://www.promod.eu/women/trousers/page-O2P2.html","http://www.promod.eu/women/jeans/page-O2.html","http://www.promod.eu/women/cropped-trousers---shorts/page-O2.html","http://www.promod.eu/women/leggings/page-O2.html","http://www.promod.eu/women/skirts/page-O2.html","http://www.promod.eu/women/skirts/page-O2P2.html","http://www.promod.eu/women/coats/page-O2.html","http://www.promod.eu/women/footwear/page-O2.html","http://www.promod.eu/women/accessories/page-O2.html","http://www.promod.eu/women/accessories/page-O2P2.html","http://www.promod.eu/women/accessories/page-O2P3.html","http://www.promod.eu/women/jewellery/page-O2.html","http://www.promod.eu/women/jewellery/page-O2P2.html","http://www.promod.eu/women/fragrances/page-O2.html",
		
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites=hxs.select('//div[@id="resultatsSearch"]/div[@class="bande_produits"]/div[@class="bloc_produit"]')
	for site in sites:
                name=site.select('a[@class="search_product"]/@href').extract()
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
	sites=hxs.select('//div[@id="global"]')
   	items=[]
        for site in sites:
		item=aqaqItem()
		item['advertiser']="promod"
		item['currency']="Euro"
		item['source']=response.url	
		s=''
        	title=hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_2"]/h1//text()').extract()
		for k in title:
			k.decode('string_escape')
			s=s+k
		item['title']=s.encode("utf-8")
		#print title,source
		
		cost=hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_2"]/div[@id="encart_fiche"]/div[@id="fp_middle"]/div[@id="prix"]/span[@class="actuel"]/span//text()').extract()
		s=''
		for k in cost:
			s=s+k
		l=re.findall("(\d[0-9]*)",s)
		if l:
			l=l[0:2]
                s=''
                for i in l:
                        s=s+i
		item['cost']=s.encode("utf-8")
		type_dress=hxs.select('//div[@id="ariane"]/div[@id="ariane_navig"]/a[4]//text()').extract()
		s=''
		for k in type_dress:
			s=s+k
		item['type_dress']=s.encode("utf-8")
#		category=hxs.select('//div[@id="ariane"]/div[@id="ariane_navig"]/a[2]//text()').extract()
#		s=''
#		for k in category:
#			s=s+k
		item['category']="Female"
		
		size=hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_2"]/div[@id="encart_fiche"]/div[@id="taille"]/div[@id="chx_taille"]/div[@id="bloc_taille_"]/p[@class="det_2"]/a//text()').extract()
		s=''
		for k in size:
			s=s+k
			s=s+','
		item['size']=s.encode("utf-8")
		
		fit=hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_2"]/div[@id="texte_fiche"]/ul[@class="liste_caract"]/li[2]//text()').extract()
		s=''
		for k in fit:
			s=s+k
		item['fit']=s.encode("utf-8")
		
		fabric=hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_2"]/div[@id="texte_fiche"]/ul[@class="liste_caract"]/li[3]//text()').extract()
		s=''
		for k in fabric:
			s=s+k
		item['fabric']=s.encode("utf-8")

		
		s=''
		desc=hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_2"]/div[@id="texte_fiche"]/h2//text()').extract()
		for k in desc:
			s=s+k
		item['desc']=s.encode("utf-8")
		
		s=''
	 	color=hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_2"]/div[@id="texte_fiche"]/ul[@class="liste_caract_2"]/li[1]//text()').extract()
		for k in color:
			s=s+k
			s=s+','
		item['color']=s.encode("utf-8")
		
		image_urls=map(lambda src: urlparse.urljoin(response.url,src),hxs.select('//div[@id="page"]/div[@class="fiche_produit"]/form[1]/div[1]/div[@id="fiche_1"]/div[@id="cadre_visuel"]/a[@id="lien_grand_visuel"]/span[@id="grand_visuel_span"]/img/@src').extract())
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
		print item['title']	
		item.save()
		return item
			

