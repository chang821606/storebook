# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    # start_urls = ['https://maoyan.com/board/4?offset=0']

    # 重写scrapy的start_requests()方法
    # 拼接所有地址,交给调度器入队列
    def start_requests(self):
        for offset in range(0,91,10):
            url = 'https://maoyan.com/board/4?offset=' + str(offset)
            # 交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse_html
            )

    # response为start_urls中的响应对象
    def parse_html(self, response):
        # 基准xpath,匹配电影信息的dd节点对象列表
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 给items.py中的类:MaoyanItem()实例化

        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()

            yield item









