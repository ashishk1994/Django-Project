import sys
import os
c=os.getcwd()
os.chdir("myweb")
d=os.getcwd()
os.chdir(c)
sys.path.insert(0, d)
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.conf import settings
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from multiprocessing import Process
from scrapy.settings import CrawlerSettings
from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher
def stop_reactor():
        reactor.stop()
def setup_crawler(spider_name):
	mySettings = {'LOG_ENABLED': True, 'ITEM_PIPELINES': 'aqaq.aqaq.pipelines.JsonWithEncodingPipeline'} 
	settings.overrides.update(mySettings)
	crawlerProcess = CrawlerProcess(settings)
	crawler = Crawler(settings)
	crawler.configure()
	crawler.crawl(spider_name)
	dispatcher.connect(stop_reactor, signal=signals.spider_closed)
	crawler.start()

log.start(loglevel=log.DEBUG)
crawler = Crawler(CrawlerSettings())
crawler.configure()
mySettings = {'LOG_ENABLED': True, 'ITEM_PIPELINES': 'aqaq.pipelines.JsonWithEncodingPipeline'} 
settings.overrides.update(mySettings)
crawlerProcess = CrawlerProcess(settings)
from aqaq.aqaq.spiders.spider import aqaqspider
spider = aqaqspider(domain='aqaq.com')
setup_crawler(spider)
#from aqaq.aqaq.spiders.spider2 import DmozSpider
#spider=DmozSpider(domain='shoptiques.com')
#setup_crawler(spider)
result = reactor.run()
print result
log.msg("------------>Running stoped")

	
