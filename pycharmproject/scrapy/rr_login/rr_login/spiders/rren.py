# -*- coding: utf-8 -*-
import scrapy


class RrenSpider(scrapy.Spider):
    name = 'rren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        pass
