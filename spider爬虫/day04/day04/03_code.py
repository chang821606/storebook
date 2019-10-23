import requests
from lxml import etree

class CodeSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1906/14Spider/'
        # web客户端验证参数
        self.auth = ('tarenacode','code_2013')

    def save_file(self):
        html = requests.get(
            url=self.url,
            auth=self.auth
        ).text
        print(html)
        p = etree.HTML(html)
        # href_list: ['../','day01/','day01.zip']
        href_list = p.xpath('//a/@href')
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar'):
                self.download(href)

    def download(self,href):
        file_url = self.url + href
        html = requests.get(
            url=file_url,
            auth=self.auth
        ).content
        with open(href,'wb') as f:
            f.write(html)

        print(href,'下载成功')

if __name__ == '__main__':
    spider = CodeSpider()
    spider.save_file()























