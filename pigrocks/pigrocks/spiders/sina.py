import scrapy


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["sina.com"]
    start_urls = ["https://sina.com"]

    def parse(self, response):
        pass
