import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class fist_bookSpider(CrawlSpider):
    name = 'fist_book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        all_headings = response.xpath('//h1/text()').getall()
        
        for heading in all_headings:
            yield {
                'text': heading,
                'page': response.url
            }
