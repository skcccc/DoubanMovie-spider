# -*- coding: utf-8 -*-

import scrapy
from douban.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domain = ["douban.com"]
    start_urls = []
    # start_urls = [
    #     "https://movie.douban.com/subject_search?search_text=The+Secret+Life+of+Walter+Mitty",
    #     "https://movie.douban.com/subject_search?search_text=The+Boat+That+Rocked"



    # ]

    def start_requests(self):
        readfile = open('filmname.txt', 'r')
        url_head = "http://movie.douban.com/subject_search?search_text="
        try:
            for line in readfile:
                self.start_urls.append(url_head + line)

            for url in self.start_urls:
                yield self.make_requests_from_url(url)

        finally:
             readfile.close()

    def parse(self, response):
  
        sel = response.xpath('//ul/li')
        url = sel.xpath('//*[@id="content"]/div/div[1]/div[2]/table[1]/tr/td[1]/a/@href').extract()[0]
        yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = DoubanItem()
        for sel in response.xpath('//ul/li'):
            
            item['movie_name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0]

            info = sel.xpath('//*[@id="info"]')
            item['movie_info'] = info.xpath('string(.)').extract()[0]

            item['movie_score'] = sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()[0]

            # director = sel.xpath('//*[@id="info"]/span[1]/span[2]')
            # item['movie_director'] = director.xpath('string(.)').extract()[0]

            # writer = sel.xpath('//*[@id="info"]/span[2]/span[2]')
            # item['movie_writer'] = movie_writer.xpath('string(.)').extract()[0]

        yield item
