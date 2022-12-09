from scrapy.http import TextResponse
import requests
import scraper_helper as sh
import scrapy


class SfmaDetailsSpider(scrapy.Spider):
    name = 'sfma_details'
    start_urls = ['https://sfma.org.sg/member/members-directory']

    def parse(self, response):
        print(f'Got response from {response.url}')

        links = response.css('#myList a::attr(href)').extract()[:1]
        for link in links:
            page_url = response.urljoin(link)
            resp = requests.get(page_url)
            resp = TextResponse(body=resp.content, url=page_url)
            title = resp.css('h6::text').getall()
            address = resp.xpath('//div[@class="min-vh-100 container-fluid bg-white pb-3"]/p[1]/text()').getall()
            address = ', '.join([sh.cleanup(x) for x in address])
            phonenumber = resp.xpath('//strong[text()="Tel:"]/../text()').getall()
            email = resp.xpath('//strong[text()="Email:"]/../text()').getall()
            website = resp.xpath('//strong[text()="Website:"]/../text()').getall()
            name = resp.css('.text-sfma ::text').get()

            yield {
                'name': name,
                'title': title,
                'address': address,
                'phonenumber': phonenumber,
                'email': email,
                'website': website,
            }