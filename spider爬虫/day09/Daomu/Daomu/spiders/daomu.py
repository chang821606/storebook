# -*- coding: utf-8 -*-
'''标题+标题+内容'''
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']
	
    def parse(self, response):
	#提取文件 text()|@htef|content()
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomuItem()#
            # item['title']: 盗墓笔记1-七星鲁王宫  选择器get()
            item['title'] = a.xpath('./text()').get()
            link = a.xpath('./@href').get()
            # 把link交给调度器入队列
            yield scrapy.Request(
                url=link,
                # meta: 不同解析函数间传递数据
                meta={'item':item},
                callback=self.parse_two_html
            )

    # 解析二级页面
    def parse_two_html(self,response):
        # 获取item
        item = response.meta['item']
        # article_list: [节点对象1,节点对象2]
        article_list = response.xpath('//article')
        for article in article_list:
            # item['name']: "七星鲁王 第一章 血尸"
            name = article.xpath('./a/text()').get()
            two_link = article.xpath('./a/@href').get()
            # 交给调度器
            yield scrapy.Request(
                url=two_link,
                meta={'item':item,'name':name},
                callback=self.parse_three_page
            )

    def parse_three_page(self,response):
        # 获取item
        item = response.meta['item']
        item['name'] = response.meta['name']
        # con_list: ['段落1','段落2','']
        con_list = response.xpath('//article[@class="article-content"]//p/text()').extract()#重点

        item['content'] = '\n'.join(con_list)
        #交给管道
        yield item




