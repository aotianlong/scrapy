import scrapy


class PigdotrocksSpider(scrapy.Spider):
    name = "pigdotrocks"
    allowed_domains = ["pig.rocks"]
    start_urls = ["https://pig.rocks"]

    def parse(self, response):
        pass
