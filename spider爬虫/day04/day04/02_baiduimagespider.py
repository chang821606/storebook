import requests
from lxml import etree
import time
import random
from urllib import parse

class BaiduImageSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'
        # IE的User-Agent返回数据最标准
        # 如果各种检查后数据下不来,考虑使用IE的User-Agent尝试
        self.headers = { 'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)' }

    # 功能函数 - 获取html
    def get_html(self,url,params=None):
        html = requests.get(
            url=url,
            params=params,
            headers=self.headers
        ).content.decode('utf-8','ignore')
        return html

    # 功能函数2 - xpath解析
    def xpath_func(self,html,xpath_bds):
        p = etree.HTML(html)
        r_list = p.xpath(xpath_bds)
        return r_list

    # 解析+提取
    def parse_html(self,one_url,params):
        one_html = self.get_html(one_url,params)
        xpath_bds = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        # t_list: ['/p/2323','/p/2323222']
        t_list = self.xpath_func(one_html,xpath_bds)
        for t in t_list:
            t_link = 'http://tieba.baidu.com' + t
            # 保存图片
            self.save_image(t_link)

    # 给定1个帖子链接,把帖子中所有图片下载到本地
    def save_image(self,t_link):
        t_html = self.get_html(t_link)
        # 图片+视频xpath,使用xpath的或： 图片xpath | 视频xpath
        xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        # img_list: ['src1','src2','src3']
        img_list = self.xpath_func(t_html,xpath_bds)
        for img in img_list:
            img_html = requests.get(
                url=img,
                headers=self.headers
            ).content
            filename = img[-10:]
            with open(filename,'wb') as f:
                f.write(img_html)

            print('%s下载成功' % filename)
            time.sleep(random.uniform(0,2))

    def run(self):
        name = input('请输入贴吧名:')
        begin = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        for page in range(begin,end+1):
            pn = (page-1)*50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            self.parse_html(self.url,params)


if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()






















