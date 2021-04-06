import scrapy
from ..items import YellowItem
class ye_vi(scrapy.Spider):

    name = "xixi"

    start_urls = [
        "https://www.32de1e56b1cd.com/xiazai/list-%E4%BA%9A%E6%B4%B2%E7%94%B5%E5%BD%B1-1.html"
    ]

    def parse(self, response):

        detail_urls = response.xpath("//div[@id='tpl-img-content']//a/@href").getall()
        for i in detail_urls:
            print("--"*30)
            yield response.follow(i,callback=self.parse_url)

        next_page = response.xpath('//div[@class="pagination"]//a[@title="下一页"]/@href').get()
        if next_page is not None:
            print("="*50)
            yield response.follow(next_page, callback=self.parse)

    def parse_url(self,response):

        down_url = response.xpath("//div[@class='panel']//a[@class='btn btn-sm btn-default downlink_btn c_white']/@href").get()

        print(down_url)