# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CCSpiderItem(scrapy.Item):
    symbol = scrapy.Field()
    date = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    volume = scrapy.Field()
    market_cap = scrapy.Field()
