# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaodaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
    baidu = scrapy.Field()
    baidu_code = scrapy.Field()
    tianyi = scrapy.Field()
    tianyi_code = scrapy.Field()
    
