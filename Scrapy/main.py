import scrapy

class ArticleSpider(scrapy.Spider):
    name = "articles"

    start_urls = [
        'https://example.com',
    ]

    def parse(self, response):
        for article in response.css('div.article'):
            title = article.css('div.title::text').get()
            yield {
                'title': title,
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

