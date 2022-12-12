import scrapy
import scraper_helper as sh


class currSpider(scrapy.Spider):
    name = 'curr'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_circulating_currencies']
    custom_settings = {
        'LOG_LEVEL': 'WARN'
    }

    def parse(self, response):
        for link in response.css('//table[1]/tbody/tr/td[2]/a').css('::attr(href)').getall():
            yield scrapy.Request(response.urljoin(link), callback=self.save_page)

    def save_page(self, response):
        with open('./output/'+response.url.split("/")[-1]+".html", "wb") as f:
            f.write(response.body)
        print('.',end='',flush=True)


if __name__ == '__main__':
    sh.run_spider(currSpider)
