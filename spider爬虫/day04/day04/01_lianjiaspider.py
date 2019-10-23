import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent

class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'
        self.blag = 1

    # 随机headers
    def get_headers(self):
        agent = UserAgent().random
        headers = { 'User-Agent':agent }
        return headers

    # 请求函数
    def get_html(self,url):
        if self.blag <= 3:
            try:
                res = requests.get(
                    url,
                    headers=self.get_headers(),
                    timeout=5
                )
                html = res.content.decode()
                return html
            except Exception as e:
                print('Retry')
                self.blag += 1
                self.get_html(url)


    # 解析提取数据
    def parse_html(self,url):
        html = self.get_html(url)
        # html要么为正常内容,要么为None
        if html:
            p = etree.HTML(html)
            # 基准xpath表达式 - 30个房源节点对象列表
            h_list = p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            for h in h_list:
                item = {}
                # 名称
                name_list = h.xpath('.//a[@data-el="region"]/text()')
                item['name'] = name_list[0] if name_list else None
                # 户型+面积+方位+精装
                info_list = h.xpath('.//div[@class="houseInfo"]/text()')  # ['三室 | 92 | ']
                if info_list:
                    L = info_list[0].split('|')
                    if len(L) == 5:
                        item['model'] = L[1].strip()
                        item['area'] = L[2].strip()
                        item['direction'] = L[3].strip()
                        item['perfect'] = L[4].strip()
                    else:
                        item['model'] = item['area'] = item['direction'] = item['perfect'] = None
                else:
                    item['model'] = item['area'] = item['direction'] = item['perfect'] = None
                # 楼层+区域+总价+单价
                floor_list = h.xpath('.//div[@class="positionInfo"]/text()')
                item['floor'] = floor_list[0].strip() if floor_list else None

                address_list = h.xpath('.//div[@class="positionInfo"]/a/text()')
                item['address'] = address_list[0].strip() if address_list else None

                total_list = h.xpath('.//div[@class="totalPrice"]/span/text()')
                item['total'] = total_list[0].strip() if total_list else None

                unit_list = h.xpath('.//div[@class="unitPrice"]/span/text()')
                item['unit'] = unit_list[0].strip() if unit_list else None

                print(item)

    # 入口函数
    def run(self):
        for i in range(1,101):
            url = self.url.format(i)
            self.parse_html(url)
            time.sleep(random.randint(1,3))
            # 每抓取1页要初始化self.blag
            self.blag = 1

if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()


















