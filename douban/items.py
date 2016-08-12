# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_info = scrapy.Field()
    movie_score = scrapy.Field()

    # movie_director = scrapy.Field()
    # movie_writer = scrapy.Field()

    pass
