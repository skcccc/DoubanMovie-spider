# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        #self.file = open('film.txt', 'w')
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
        print(info['name'], info['score'], info['director'], info['screenwriter'], info['type'], info['country'], info['language'], info['date'], info['length'])

        return item
