# Scrapy settings for aqaq project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#


BOT_NAME = 'aqaq'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['aqaq.spiders']
NEWSPIDER_MODULE = 'aqaq.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
			'aqaq.pipelines.JsonWithEncodingPipeline']

import sys
import os
c=os.getcwd()
os.chdir("../../../myweb")
d=os.getcwd()
os.chdir(c)
sys.path.insert(0, d)

# Setting up django's settings module name.
# This module is located at /home/rolando/projects/myweb/myweb/settings.py.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'


