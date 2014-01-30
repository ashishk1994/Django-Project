import sys
import os
os.chdir("../..")
c=os.getcwd()
os.chdir("myweb")
d=os.getcwd()
os.chdir(c)
sys.path.insert(0, d)
sys.path.insert(0,c)
print os.getcwd()
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import CrawlerSettings
from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher
def stop_reactor():
        reactor.stop()
def setup_crawler(spider_name):
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	crawler.crawl(spider_name)
	dispatcher.connect(stop_reactor, signal=signals.spider_closed)
	crawler.start()

log.start(loglevel=log.DEBUG)
crawler = Crawler(CrawlerSettings())
crawler.configure()
from aqaq.aqaq.spiders.spider import DmozSpider
spider = DmozSpider(domain='zlz.com')
setup_crawler(spider)
#from aqaq.aqaq.spiders.spider2 import DmozSpider
#spider=DmozSpider(domain='shoptiques.com')
#setup_crawler(spider)
result = reactor.run()
print result
log.msg("------------>Running stoped")
