import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = ['http://scrapeit.home.blog']

    def parse(self, response):
        blogs = response.css('article')
        for blog in blogs:
            title = blog.css('.entry-title a::text').get(),
            summary = blog.css('p:nth-child(1)::text').get(),
            author = blog.css('.author.vcard a::text').get(),
            date = blog.css('.entry-date.published::text').get(),
            category = blog.css('.cat-links a::text').getall(),
            tags = blog.css('.tags-links a::text').getall(),

            yield {
                'title':title,
                'summary':summary,
                'author':author,
                'date':date,
                'category':category,
                'tags':tags,
            }