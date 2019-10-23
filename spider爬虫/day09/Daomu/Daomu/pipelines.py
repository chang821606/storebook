# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class DaomuPipeline(object):
    def process_item(self, item, spider):
        # title: 盗墓笔记1-七星鲁王宫
        # name : 七星鲁王 第一章 血尸
        # content: 小说内容
        # 创建对应文件夹
        directory = '/home/tarena/novel/{}/'.format(item['title'])
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = '/home/tarena/novel/{}/{}.txt'.format(item['title'],item['name'])

        with open(filename,'w') as f:
            f.write(item['content'])

        return item








