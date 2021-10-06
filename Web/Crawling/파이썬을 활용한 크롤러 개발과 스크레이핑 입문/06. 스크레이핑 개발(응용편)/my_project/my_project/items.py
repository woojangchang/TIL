# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Quote(scrapy.Item):
    """격언 아이템"""
    author = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
