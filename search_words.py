import scrapy
import pandas as pd
url = "https://vplates.com.au/vplatesapi/checkcombo?vehicleType=car&combination={}"

class SearchWordsSpider(scrapy.Spider):
    name = 'search_words'

    def start_request(self):
        df = pd.read_csv('input.csv')
        for word in df['search'].tolist():
            yield scrapy.Request(url.format(word), cb_kwargs={'word': word})

    def parse(self, response, word):
        result = response.json().get("success")
        yield { 
            'word': word,
            'Availability': 'Yes' if result else 'No'
        }
