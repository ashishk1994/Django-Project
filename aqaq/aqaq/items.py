# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem

from apple3.models import Person

class aqaqItem(DjangoItem):
    django_model=Person
    pass
