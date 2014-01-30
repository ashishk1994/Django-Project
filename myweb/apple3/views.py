# Create your views here.
from apple3.forms import *
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext,loader
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from apple3.models import Person,Input,comment,forbodytype,foroccasion,forstyle
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User
import sys
import os

pur=os.getcwd()
def call(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
#dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.flipkart import DmozSpider
	spider = DmozSpider(domain='flipkart.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')
def call4(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
#		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.aqa import aqaqspider
	spider = aqaqspider(domain='aqaq.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call6(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.pretty import aqaqspider
	spider = aqaqspider(domain='prettysecrets.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call8(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.blooming import aqaqspider
	spider = aqaqspider(domain='bloomingdales.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call9(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.house import aqaqspider
	spider = aqaqspider(domain='houseoffraser.co.uk')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call10(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
#		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.flipkart import DmozSpider
	spider = DmozSpider(domain='flipkart.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call11(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
#		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.jabong import aqaqspider
	spider = aqaqspider(domain='jabong.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call12(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
#		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.infruit import aqaqspider
	spider = aqaqspider(domain='inkfruit.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call13(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
#		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.wallis import DmozSpider
	spider = DmozSpider(domain='wallis.co.uk')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')


def call14(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.promod import aqaqspider
	spider = aqaqspider(domain='promod.eu')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call15(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.saks import aqaqspider
	spider = aqaqspider(domain='saksfifthavenue.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call16(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.zlz import DmozSpider
	spider = DmozSpider(domain='zlz.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')

def call17(request):
    	os.chdir(pur)
	ma=os.getcwd()
	print ma
	os.chdir("..")
	c=os.getcwd()
	os.chdir("myweb")
	d=os.getcwd()
	os.chdir(c)
	sys.path.insert(0, d)
	sys.path.insert(0,c)
	print os.getcwd()
	os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
	from twisted.internet import reactor
	from scrapy.crawler import Crawler
	from scrapy.settings import CrawlerSettings
	from scrapy import log, signals
	from scrapy.xlib.pydispatch import dispatcher
	def stop_reactor():
	        reactor.stop()
		os.chdir(ma)
	def setup_crawler(spider_name):
		crawler = Crawler(CrawlerSettings())
		crawler.configure()
		crawler.crawl(spider_name)
		dispatcher.connect(stop_reactor, signal=signals.spider_closed)
		crawler.start()
	
	log.start(loglevel=log.DEBUG)
	crawler = Crawler(CrawlerSettings())
	crawler.configure()
	from aqaq.aqaq.spiders.myntra import aqaqspider
	spider = aqaqspider(domain='myntra.com')
	setup_crawler(spider)
	#from aqaq.aqaq.spiders.spider2 import DmozSpider
	#spider=DmozSpider(domain='shoptiques.com')
	#setup_crawler(spider)
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")			
    	return HttpResponseRedirect('/')



def index(request):
    	user=request.user
    	if user.is_anonymous:
		a=0
	if request.user.is_active and request.user.is_authenticated:
		a=1
		   	
    	template=loader.get_template('apple3/index.html')
	context=RequestContext(request,{
			'a':a,
		}
		)
    	return HttpResponse(template.render(context))
@login_required
def dress(request):
	insta=Input.objects.filter(userid=request.user.username)
	inst=[]
	for i in insta:
	    inst.append(i.apparelid)
    	cat=0
    	im=[0,1,2]
    	k=0
	ln=[]
	image=Person.objects.all()
	paginator=Paginator(image,50)
    	page=request.GET.get('page')
	try:
		images=paginator.page(page)
    	except PageNotAnInteger:
		images=paginator.page(1)
    	except EmptyPage:
		images=paginator.page(paginator.num_pages)
    	for i in range(images.start_index(),images.end_index()+1):
	    ln.append(int(i)-1)
	lst=[]
	for i in range(1,paginator.num_pages):
	    lst.append(int(i))
	template=loader.get_template('apple3/dress2.html')
	context=RequestContext(request,{
				   	    'image':image,
					    'k':k,
					    'im':im,
					    'ln':ln,
					    'images':images,
					    'lst':lst,
					    'paginator':paginator,
					    'cat':cat,
					    'inst':inst,
					}
				)
	return HttpResponse(template.render(context))

@login_required
def title(request,title_id):
    	cur=0
	cur=Person.objects.get(pk=title_id)
	sz=str(cur.size)
	sz=sz.split(',')
	fsz=[]
	for i in sz:
	   s=""
	   for j in range(0,len(i)):
	    if i[j]!='U' and i[j]!='K' and i[j]!=',':
	    	s+=i[j]
	   fsz.append(s)
	lsz=len(fsz)
    	if request.method == 'POST':# If the form has been submitted...
        	form=UserForm(request.POST)# A form bound to the POST data
        	if form.is_valid(): # All validation rules pass
			form.cleaned_data
			new=form.save(commit=False)
    			new.userid=request.user
			new.save()
    			form.save_m2m()
			return HttpResponseRedirect('/')
    	else:
        	form = UserForm() # An unbound form"""
    	template=loader.get_template('apple3/title.html')
	context=RequestContext(request,{
			'cur':cur,
			'sz':fsz,
			'lsz':lsz,
			'form':form,
		}
		)
    	return HttpResponse(template.render(context))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required    
def male(request,flag):
	insta=Input.objects.filter(userid=request.user.username)
	inst=[]
	for i in insta:
	    inst.append(i.apparelid)
    	fl=0
	if flag:
		if flag=='1':
    			image=Person.objects.filter(Q(category="male")|Q(category="Male")).order_by('title')
    		elif flag=='2':
    			image=Person.objects.filter(Q(category="male")|Q(category="Male")).order_by('-cost')
    		elif flag=='3':
    			image=Person.objects.filter(Q(category="male")|Q(category="Male")).order_by('cost')
    		elif flag=='4':
    			image=Person.objects.filter(Q(category="male")|Q(category="Male"),advertiser='aqaq')
    		elif flag=='5':
    			image=Person.objects.filter(Q(category="male")|Q(category="Male"),advertiser='Shoptiques')
    		elif flag=='6':
    			image=Person.objects.filter(Q(category="male")|Q(category="Male"),advertiser='prettysecrets')

	else:
    		image=Person.objects.filter(Q(category="male")|Q(category="Male"))
	if(len(image))==0:
	    fl=1
    	cat=1
	im=[0,1,2]
    	k=1
	ln=[]
#image=Person.objects.all()[:109]
	paginator=Paginator(image,30)
    	page=request.GET.get('page')
	try:
		images=paginator.page(page)
    	except PageNotAnInteger:
		images=paginator.page(1)
    	except EmptyPage:
		images=paginator.page(paginator.num_pages)
	for i in range(images.start_index(),images.end_index()+1):
	    ln.append(int(i)-1)
	lst=[]
	for i in range(1,paginator.num_pages):
	    lst.append(int(i))
	template=loader.get_template('apple3/dress2.html')
	context=RequestContext(request,{
				   	    'image':image,
					    'k':k,
					    'im':im,
					    'ln':ln,
					    'images':images,
					    'lst':lst,
					    'paginator':paginator,
					    'cat':cat,
					    'fl':fl,
					    'inst':inst,
					    }
				)
	return HttpResponse(template.render(context))
@login_required
def female(request,flag):
	insta=Input.objects.filter(userid=request.user.username)
	inst=[]
	for i in insta:
	    inst.append(i.apparelid)
    	cat=2
	fl=0
	if flag:
		print flag
		if flag=='1':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female")).order_by('title')
    		elif flag=='2':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female")).order_by('-cost')
    		elif flag=='3':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female")).order_by('cost')
    		elif flag=='4':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='aqaq')
    		elif flag=='5':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='Shoptiques')
    		elif flag=='6':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='prettysecrets')
    		elif flag=='7':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='Donnakaran')
    		elif flag=='8':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='bloomingdale')
    		elif flag=='9':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='houseoffraser')
    		elif flag=='10':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='flipkart')	
    		elif flag=='11':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='jabong')
    		elif flag=='12':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='inkfruit')
    		elif flag=='13':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='wallis')
    		elif flag=='14':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='promod')
    		elif flag=='15':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='saksfifthavenue')  		
    		elif flag=='16':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='ZLZ')  		
    		elif flag=='17':
    			image=Person.objects.filter(Q(category="female")|Q(category="Female"),advertiser='myntra')  		
	else:
	    	flag='0'
		print 0
    		image=Person.objects.filter(Q(category="female")|Q(category="Female"))
    	if(len(image)==0):
	    	fl=1
    	im=[0,1,2]
    	k=1
	ln=[]
#image=Person.objects.all()[:109]
	paginator=Paginator(image,20)
    	page=request.GET.get('page')
	try:
		images=paginator.page(page)
    	except PageNotAnInteger:
		images=paginator.page(1)
    	except EmptyPage:
		images=paginator.page(paginator.num_pages)
	for i in range(images.start_index(),images.end_index()+1):
	    ln.append(int(i)-1)
	lst=[]
	for i in range(1,paginator.num_pages):
	    lst.append(int(i))
	template=loader.get_template('apple3/dress2.html')
	context=RequestContext(request,{
				   	    'image':image,
					    'k':k,
					    'im':im,
					    'ln':ln,
					    'images':images,
					    'lst':lst,
					    'paginator':paginator,
		    			    'cat':cat,
					    'fl':fl,
					    'inst':inst,
					    'flag':flag,
					    }
				)
	return HttpResponse(template.render(context))
 
def add_tag(request,title_id):
    	use=User.objects.all()
    	a={}
    	for i in use:
		b=[]
    		bodytag=[]
    		styletag=[]
    		occasiontag=[]
		tag=forbodytype.objects.filter(input__userid=i.username,input__apparelid=title_id)
		for j in tag:
			bodytag.append(j.bodytype)
    		tag=forstyle.objects.filter(input__userid=i.username,input__apparelid=title_id)
		for j in tag:
			styletag.append(j.style)
		tag=foroccasion.objects.filter(input__userid=i.username,input__apparelid=title_id)
		for j in tag:
			occasiontag.append(j.occasions)
    		b.append(bodytag)
    		b.append(styletag)
    		b.append(occasiontag)
    		if bodytag:
    			a[i.username]=b
		elif styletag:
    			a[i.username]=b
		elif occasiontag:
    			a[i.username]=b
    	if request.method == 'POST':# If the form has been submitted...
        	form=UserForm(request.POST)# A form bound to the POST data
        	if form.is_valid(): # All validation rules pass
			form.cleaned_data
			new=form.save(commit=False)
    			new.userid=request.user.username
    			new.apparelid=title_id
    			new.save()
    			form.save_m2m()
			return HttpResponseRedirect('/')
    	else:
        	form = UserForm() # An unbound form"""
	template=loader.get_template('apple3/add_tag.html')
	context=RequestContext(request,{
						'id':title_id,
						'user':request.user.username,
						'form':form,
						'a':a,
					}
				)
	return HttpResponse(template.render(context))

def edit_tag(request,title_id):
	inst=Input.objects.get(apparelid=title_id,userid=request.user.username)
   	apple_obj=Input.objects.filter(bodytype__bodytype='apple')
    	'''hour_obj=Input.objects.filter(bodytype__bodytype='hourglass')
   	inverted_obj=Input.objects.filter(bodytype__bodytype='inverted triangle')
   	bone_obj=Input.objects.filter(style__style='bone')
   	chic_obj=Input.objects.filter(style__style='chic')
   	edgy_obj=Input.objects.filter(style__style='edgy')
   	soph_obj=Input.objects.filter(style__style='sophisticated')
   	vintage_obj=Input.objects.filter(style__style='vintage')
   	party_obj=Input.objects.filter(style__style='party')'''
    	use=User.objects.all()
    	a={}
    	for i in use:
		b=[]
    		bodytag=[]
    		styletag=[]
    		occasiontag=[]
		tag=forbodytype.objects.filter(input__userid=i.username,input__apparelid=title_id)
		for j in tag:
			bodytag.append(j.bodytype)
    		tag=forstyle.objects.filter(input__userid=i.username,input__apparelid=title_id)
		for j in tag:
			styletag.append(j.style)
		tag=foroccasion.objects.filter(input__userid=i.username,input__apparelid=title_id)
		for j in tag:
			occasiontag.append(j.occasions)
    		b.append(bodytag)
    		b.append(styletag)
    		b.append(occasiontag)
    		if bodytag:
    			a[i.username]=b
		elif styletag:
    			a[i.username]=b
		elif occasiontag:
    			a[i.username]=b
	print a
	if request.method=='POST':
		form=ShowForm(request.POST,instance=inst)
		if form.is_valid():
		    new=form.save()
		    return HttpResponseRedirect('/')
	else:
	    	form=ShowForm(instance=inst)
	template=loader.get_template('apple3/edit_tag.html')
	context=RequestContext(request,{
						'id':title_id,
						'user':request.user.username,
						'form':form,
						'inst':inst,
						'a':a,
					}
				)
	return HttpResponse(template.render(context))
def comment_view(request,title_id):
    	ob=comment.objects.filter(apparelid=title_id)
    	if request.method=='POST':
		form=commentForm(request.POST)
		if form.is_valid():
		    new=form.save(commit=False)
		    new.userid=request.user.username
		    new.apparelid=title_id
		    new.save()
		    return HttpResponseRedirect('/')
	else:
	    	form=commentForm()
	template=loader.get_template('apple3/comment.html')
	context=RequestContext(request,{
					'form':form,
					'obj':ob,
				       }
			      )
	return HttpResponse(template.render(context))

