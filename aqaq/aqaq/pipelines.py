from scrapy import log
import json
import codecs
from apple3.models import Person
a=[]
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('aqaq.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
	if item['title']:
		a.append(item['title'])		
		delete_item=Person.objects.filter(title=item['title'])
		if delete_item:
			delete_item=delete_item[0]
			delete_item.cost=item['cost']
			delete_item.size=item['size']
			delete_item.color=item['color']
			delete_item.fit=item['fit']
			delete_item.fabric=item['fabric']
	 		delete_item.save()
		else:
		    item.save()

#	k=Person.objects.filter(advertiser=item['advertiser'])
#	for i in k:
#	    if i.title not in a:
#	    	i.delete()
#delete_item.delete()
    def spider_closed(self, spider):
	delete_item=Person.objects.filter(advertiser='bloomingdale')
        for i in delete_item:
	    if i not in a:
	    	i.delete()
	self.file.close()
