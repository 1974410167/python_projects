# -*- coding: utf-8 -*-
import scrapy
from ..items import MvtpItem

class MvspiderSpider(scrapy.Spider):
    name = 'mvspider'

    allowed_domains = ['desk.zol.com.cn']

    start_urls = ['http://desk.zol.com.cn/meinv/hot_1.html']

    def parse(self, response):
        details = response.xpath("//a[@class='pic']/@href").getall()
        for detail in details:
            yield response.follow(detail,callback=self.parse_detail)

        main_next_page = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if main_next_page is not None:
            yield response.follow(main_next_page,callback=self.parse)

    def parse_detail(self,response):

        image_urls = response.xpath("//img[@id='bigImg']/@src").getall()

        item = MvtpItem(image_urls=image_urls)
        yield item

        detail_next_page = response.xpath("//a[@id='pageNext']/@href").get()
        false_url = 'javascript:;'
        if detail_next_page is not None and false_url not in detail_next_page:
            yield response.follow(detail_next_page,callback=self.parse_detail)

