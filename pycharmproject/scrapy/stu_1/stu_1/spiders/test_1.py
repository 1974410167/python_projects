
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/"
    ]
    def parse(self, response):
        abouts = response.xpath("//div[@class='quote']//span//a/@href").getall()
        for about in abouts:
            print("$"*40)
            yield response.follow(about,callback=self.aboutparse)

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            print("+"*40)
            yield response.follow(next_page,callback=self.parse)

    def aboutparse(self,response):
        author = response.xpath("//div[@class='author-details']//h3/text()").get()
        print("#"*40)
        print(author)
        yield {author:author}

