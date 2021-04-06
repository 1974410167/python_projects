# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Stu1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class YellowItem(scrapy.Item):
    url = scrapy.Field()


class QsbkItem(scrapy.Item):
    author = scrapy.Field()