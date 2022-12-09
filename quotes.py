import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/random']

    def parse(self, response):
        print(f'Got response from {response.url}')

        item = {
            'author': response.css('.author::text').get(),
            'quotes': response.css('.text::text').get(),
            'tags': response.css('.tag::text').getall(),
        }

        yield item
