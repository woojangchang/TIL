import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from my_project.items import Quote

class QuotesSpider(CrawlSpider):
    """Quote 아이템을 수집하는 크롤러"""
    
    name = 'quotes-3'
    allowed_domains = ['quotes.toscrape.com']

    rules = (
        Rule(LinkExtractor(allow=r'.*'), callback='parse_start_url', follow=True),
    )
    
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/'
        ]

        return [scrapy.Request(url=url) for url in urls]
        """또는
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        """

    def parse_start_url(self, response):
        """start_urls 아래의 다른 페이지도 스크레이핑"""
        return self.parse(response)

    def parse(self, response):
        """크롤링한 페이지에서 Item을 스크레이핑"""
        items = []
        for i, quote_html in enumerate(response.css('div.quote')):
            if i > 1:
                return items
            item = Quote()
            item['author'] = quote_html.css('small.author::text').get()
            item['text'] = quote_html.css('span.text::text').get()
            item['tags'] = quote_html.css('div.tags a.tag::text').getall()
            items.append(item)
