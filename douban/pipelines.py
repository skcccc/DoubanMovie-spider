# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlrd
import xlwt

class DoubanPipeline(object):
    def __init__(self):
        self.workbook = xlwt.Workbook()
        self.sheet = self.workbook.add_sheet("Sheet1")
        self.i = 0
        self.n = 0

        pass

    def process_item(self, item, spider):

        
        def process_info(self):
            replace_name = [' ', '导演:', '编剧:', '主演:', '类型:', '制片国家/地区:', '语言:', '上映日期:', '片长:', '又名:']
            
            movie_name = item['movie_name']
            movie_info = item['movie_info']
            movie_score = item['movie_score']
            
            for i in replace_name:
                movie_info = movie_info.replace(str(i), '')

            movie_info = movie_info.split('\n')

            while '' in movie_info:
                movie_info.remove('')
            
            movie_item = {}
            movie_item['name'] = movie_name
            movie_item['score'] = movie_score
            movie_item['director'] = movie_info[0]
            movie_item['screenwriter'] = movie_info[1]
            movie_item['role'] = movie_info[2]
            movie_item['type'] = movie_info[3]
            movie_item['country'] = movie_info[4]
            movie_item['language'] = movie_info[5]
            movie_item['date'] = movie_info[6]
            movie_item['length'] = movie_info[7]
            return movie_item

        info = process_info(self)

        #self.n = 1
        self.i +=1
        self.sheet.write(self.i, self.n, info['name'])
        self.sheet.write(self.i, self.n+1, info['type'])
        self.sheet.write(self.i, self.n+2, info['director'])
        self.sheet.write(self.i, self.n+3, info['screenwriter'])
        self.sheet.write(self.i, self.n+4, info['country'])
        self.sheet.write(self.i, self.n+5, info['language'])
        self.sheet.write(self.i, self.n+6, info['date'])
        self.sheet.write(self.i, self.n+7, info['length'])
        self.sheet.write(self.i, self.n+8, info['score'])
        # self.sheet.write(self.i, self.n+9, info['name'])



        return item

    def close_spider(self, spider):
        self.workbook.save('电影列表.xls')

    def open_spider(self, spider):
        self.sheet.write(0, 0, '电影')
        self.sheet.write(0, 1, '类型')
        self.sheet.write(0, 2, '导演')
        self.sheet.write(0, 3, '编剧')
        self.sheet.write(0, 4, '国家/地区')
        self.sheet.write(0, 5, '语言')
        self.sheet.write(0, 6, '上映日期')
        self.sheet.write(0, 7, '片长')
        self.sheet.write(0, 8, '评分')
