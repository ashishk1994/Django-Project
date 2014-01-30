from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    	title=models.CharField(max_length=250,unique=True)
	cost=models.IntegerField()
	desc=models.TextField(blank=True)
	color=models.CharField(max_length=1000)
	image_urls=models.CharField(max_length=1000)
	source=models.CharField(max_length=250,unique=True)
	category=models.CharField(max_length=1000)
	size=models.TextField(blank=True)
	fit=models.CharField(max_length=1000)
	fabric=models.CharField(max_length=1000)
	type_dress=models.CharField(max_length=1000)
	currency=models.CharField(max_length=1000)
	advertiser=models.CharField(max_length=1000)
	def __unicode__(self):
	     	return self.title

class foroccasion(models.Model):
    	occasions=models.CharField(max_length=2000)
	def __unicode__(self):
	     	return self.occasions
	
class forstyle(models.Model):
    	style=models.CharField(max_length=2000)
	def __unicode__(self):
	     	return self.style

class forbodytype(models.Model):
    	bodytype=models.CharField(max_length=2000)
	def __unicode__(self):
	     	return self.bodytype

class  Input(models.Model):
	tabbody=[
	    	("apple","apple"),
	    	("pear/triangle","pear/triangle"),
	    	("hourglass","hourglass"),
	    	("rectangle","rectangle"),
	    	("inverted triangle","invered triangle")
    	]
    	tabstyle=[
		("vintage","vintage"),
		("sophisticated","sophisticated"),
		("chic","chic"),
		("bone","bone"),
		("edgy","edgy")
    	]

	apparelid=models.IntegerField(blank=True)
#apparelid=models.ForeignKey('Person')
	#apparelid=models.CharField(max_length=100,blank=True)
#userid=models.IntegerField()
	userid=models.CharField(max_length=140)
	occassion=models.ManyToManyField(foroccasion)
	bodytype=models.ManyToManyField(forbodytype)
	style=models.ManyToManyField(forstyle)
    	def __unicode__(self):
	    	return self.userid
class comment(models.Model):
	userid=models.CharField(max_length=140)
	apparelid=models.IntegerField(blank=True)
	desc=models.TextField(blank=True)
 	def __unicode__(self):
	    	return self.userid

    	

