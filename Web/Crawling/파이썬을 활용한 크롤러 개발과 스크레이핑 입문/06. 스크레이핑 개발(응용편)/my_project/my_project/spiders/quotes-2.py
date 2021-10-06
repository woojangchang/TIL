import scrapy
from scrapy.spiders import CrawlSpider

from my_project.items import Quote

class QuotesSpider(CrawlSpider):
    """Quote 아이템을 수집하는 크롤러"""
    
    name = 'quotes-2'
    allowed_domains = ['quotes.toscrape.com']
    
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/'
        ]

        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
        """또는
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        """

    def parse(self, response):
        """크롤링한 페이지에서 Item을 스크레이핑"""
        for i, quote_html in enumerate(response.css('div.quote')):
            if i > 2:
                raise scrapy.exceptions.CloseSpider(reason='abort')
            item = Quote()
            item['author'] = quote_html.css('small.author::text').get()
            item['text'] = quote_html.css('span.text::text').get()
            item['tags'] = quote_html.css('div.tags a.tag::text').getall()
            yield item
