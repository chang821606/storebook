# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=0']
    offset = 0

    # response为start_urls中的响应对象
    def parse(self, response):
        # 基准xpath,匹配电影信息的dd节点对象列表
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 给items.py中的类:MaoyanItem()实例化
        item = MaoyanItem()
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').get()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get()

            yield item

        if self.offset < 90:
            self.offset += 10
            url = 'https://maoyan.com/board/4?offset=' + str(self.offset)
            # 把url地址交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )







