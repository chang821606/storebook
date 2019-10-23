# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['time'],item['star'])
        return item


# 存储mysql数据库的管道
import pymysql
from .settings import *

class MaoyanMysqlPipeline(object):
    def open_spider(self,spider):
        # 爬虫项目启动时执行1次,一般用于数据库连接
        self.db = pymysql.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PWD,
                database=MYSQL_DB,
                charset=MYSQL_CHARSET
            )
        self.cursor = self.db.cursor()
        print('openspider方法')

    def process_item(self,item,spider):
        # 把数据存入到数据库
        ins = 'insert into filmtab values(%s,%s,%s)'
        L = [
            item['name'],item['star'],item['time']
        ]
        self.cursor.execute(ins,L)
        self.db.commit()

        return item

    def close_spider(self,spider):
        # 爬虫项目结束时只执行1次
        self.cursor.close()
        self.db.close()
        print('closespider方法')

# 流程:
# 1. settings.py中定义常用变量
# 2. pipelines.py中写存入数据库代码
# 3. setting.py中开启对应管道

import pymongo

class MaoyanMongoPipeline(object):
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(
            MONGO_HOST,MONGO_PORT
        )
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self,item,spider):
        info = dict(item)
        self.myset.insert_one(info)

        return item













