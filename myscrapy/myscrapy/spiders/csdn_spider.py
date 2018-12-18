import scrapy


class CsdnSpider(scrapy.Spider):
    name = 'csdn_spider'
    allowed_domains = ["dmoz.net"]
    start_urls = [
        "http://www.csdn.net/"
    ]

    def parse(self, response):
        print response.url
        print response.body
