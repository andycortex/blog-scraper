from scrapy import Request, FormRequest
import json
import scrapy


class QuotesLoginPostSpider(scrapy.Spider):
    name = 'quotes_login_post'
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        print(f'Got response from {response.url}')
        token = response.css('[name="csrf_token"] ::attr(value)').get() # response.xpath('//*[@name="csrf_token"]/@value').get()/
        
        data = {
            'csrf_token': token,
            'username': 'andrea',
            'password': 'andrea',
        }

        headers = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

        # logout = response.xpath('//a[text()="Logout]')

        # print('BASE_URL POST',FormRequest.from_response(response, formdata = data))
        json.dumps(data)
        result = Request(response.url, body = json.dumps(data), method = 'POST', headers=headers)
        print(result)
