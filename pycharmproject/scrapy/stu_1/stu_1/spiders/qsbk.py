import scrapy
from scrapy.http.response.text import TextResponse
from scrapy.selector.unified import SelectorList
from ..items import QsbkItem
class QsbkSpider(scrapy.Spider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    start_urls = [
        "https://www.qiushibaike.com/text/page/1/"
    ]

    def parse(self, response):
        base_xpath = response.xpath("//div[@class='author clearfix']//a//h2/text()").getall()
        for author in base_xpath:
            item = QsbkItem(author=author)
            yield item
        # content = response.xpath("//div[@class='content']/span/text()").getall()
        # print(content)
        # print(type(content))

        next_page = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if next_page is not None:
            print('+'*40)
            print(next_page)
            yield response.follow(next_page,callback=self.parse)
