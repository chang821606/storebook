# **Day10回顾**

## **settings.py常用变量**

```python
# 1、设置日志级别

# 2、保存到日志文件(不在终端输出)

# 3、设置数据导出编码(主要针对于json文件)
FEED_EXPORT_ENCODING='utf-8'
# 4、非结构化数据存储路径
IMAGES_STORE='/home/tarena/so/images/'
IMAGES_STORE='D:\\SO\\images'
# 5、设置User-Agent
USER_AGENT='Mozilla/5.0'
# 6、设置最大并发数(默认为16)
CONCURRENT_REQUEST=16
# 7、下载延迟时间(每隔多长时间请求一个网页)
DOWNLOAD_DELAY=0.5
# 8、请求头
DEFAULT_REQUEST_HEADERS={}
# 9、添加项目管道

# 10、添加下载器中间件
11
COOKIE_ENABLED=False|True
```

## **非结构化数据抓取**

```python
1、spider
   yield item['链接']
2、pipelines.py
   from scrapy.pipelines.images import ImagesPipeline
   import scrapy
   class TestPipeline(ImagesPipeline):
      def get_media_requests(self,item,info):
            yield scrapy.Request(url=item['url'],meta={'item':item['name']})
      def file_path(self,request,response=None,info=None):
            name = request.meta['item']
            filename = name
            return filename
3、settings.py
   IMAGES_STORE = 'D:\\Spider\\images'
```

## **scrapy.Request()**

```python
# 参数
1、url
2、callback
3、headers
4、meta ：传递数据,定义代理
5、dont_filter ：是否忽略域组限制 - 默认False,检查allowed_domains['']
#不检查:dont_filter=True
6、cookies
cookies={}
# request属性
1、request.url
2、request.headers
3、request.meta  
4、request.method  scrapy.request(method="get")
# response属性
1、response.url
2、response.text
3、response.body  json
4、response.meta
5、response.encoding
```

## **设置中间件**

**随机User-Agent**

```python
# 1、middlewares.py - headers属性
class RandomUaDownloaderMiddleware(object):
      def process_request(self,request,spider)
        request.headers['User-Agent']=agent
# 2、settings.py 
DOWNLOADER_MIDDLEWARES = {'xxx.middlewares.xxx':300}
```

**随机代理**

```python
# 1、middlewares.py - meta属性
class RandomProxyDownloaderMiddleware(object):
    def process_request(self,request,spider):
    	request.META['proxy']=proxy
        
    def process_exception(self,request,xxx):
    	return request   
    
        
# 2、settings.py
DOWNLOADER_MIDDLEWARES = {'xxx.middlewares.xxx':200}
```

# **Day11笔记**

## **分布式爬虫**

### **分布式爬虫介绍**

- **原理**

```python
多台主机共享1个爬取队列
```

- **实现** 

```python
重写scrapy调度器(scrapy_redis模块)
```

- **为什么使用redis**

```python
1、Redis基于内存,速度快
2、Redis非关系型数据库,Redis中集合,存储每个request的指纹
3、scrapy_redis安装
	sudo pip3 install scrapy_redis
```

## **scrapy_redis详解**

- **GitHub地址**

  ```python
  https://github.com/rmax/scrapy-redis
  ```

- **settings.py说明**

  ```python
  # 重新指定调度器: 启用Redis调度存储请求队列
  SCHEDULER = "scrapy_redis.scheduler.Scheduler"
  
  # 重新指定去重机制: 确保所有的爬虫通过Redis去重
  DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
  
  # 不清除Redis队列: 暂停/恢复/断点续爬/增量爬取
  SCHEDULER_PERSIST = True
  
  # 优先级队列 （默认）
  SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
  #可选用的其它队列
  # 先进先出队列
  SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
  # 后进先出队列
  SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
  
  # redis管道
  ITEM_PIPELINES = {
      #真正把数据库存入到redis数据库
      'scrapy_redis.pipelines.RedisPipeline': 300
  }
  
  #指定连接到redis时使用的端口和地址
  REDIS_HOST = 'localhost'
  REDIS_PORT = 6379
  ```

## **腾讯招聘分布式改写**

### **1、正常项目数据抓取（非分布式）**

### **2、改写为分布式（同时存入redis）**

**1、settings.py**

```python
# 1、使用scrapy_redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 2、使用scrapy_redis的去重机制
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 3、是否清除请求指纹,True:不清除 False:清除（默认）
SCHEDULER_PERSIST = True
# 4、(非必须)在ITEM_PIPELINES中添加redis管道
'scrapy_redis.pipelines.RedisPipeline': 200
# 5、定义redis主机地址和端口号
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
```

#### **改写为分布式（同时存入mysql）**

- **修改管道**

```python
ITEM_PIPELINES = {
   'Tencent.pipelines.TencentPipeline': 300,
   # 'scrapy_redis.pipelines.RedisPipeline': 200
   'Tencent.pipelines.TencentMysqlPipeline':200,
}
```

- **清除redis数据库**

```python
flushdb
```

- **代码拷贝一份到分布式中其他机器，两台或多台机器同时执行此代码**

## **腾讯招聘分布式改写- 方法二**

- **使用redis_key改写**

  ```python
  # 第一步: settings.py无须改动
  settings.py和上面分布式代码一致
  # 第二步:tencent.py
  from scrapy_redis.spiders import RedisSpider
  class TencentSpider(RedisSpider):
      # 1. 去掉start_urls
      # 2. 定义redis_key
      redis_key = 'tencent:spider'
      def parse(self,response):
          pass
  # 第三步:把代码复制到所有爬虫服务器，并启动项目
  # 第四步
    到redis命令行，执行LPUSH命令压入第一个要爬取的URL地址
    >LPUSH tencent:spider 第1页的URL地址
  
  # 项目爬取结束后无法退出，如何退出？
  setting.py
  CLOSESPIDER_TIMEOUT = 3600
  # 到指定时间(3600秒)时,会自动结束并退出
  ```

## **scrapy - post请求**

- **方法+参数**

```python
scrapy.FormRequest(
    url=posturl,
    formdata=formdata,
    callback=self.parse
)
```

- **有道翻译案例实现**

**1、创建项目+爬虫文件**

```python

```

**2、items.py**

```python

```

**3、youdao.py**

```python

```

**4、settings.py**

```python

```

**scrapy添加cookie的三种方式**

```python
# 1、修改 settings.py 文件
1、COOKIES_ENABLED = False  # 取消注释，表示启用cookie,使用变量中Cookie值
2、DEFAULT_REQUEST_HEADERS = {}   添加Cookie

# 2、爬虫文件 - 利用cookies参数
COOKIES_ENABLED = TRUE  # 启用Cookie,使用Request()方法中cookies参数
def start_requests(self):
    yield scrapy.Request(url=url,cookies={},callback=xxx)
    
# 3、DownloadMiddleware设置中间件
COOKIES_ENABLED = TRUE # 启用Cookie,使用Request()方法中cookies参数
def process_request(self,request,spider):
    request.cookies={}
```

## **机器视觉与tesseract**

### **作用**

```python
处理图形验证码
```

### **三个重要概念**

- **OCR**

```python
# 定义
OCR: 光学字符识别(Optical Character Recognition)
# 原理
通过扫描等光学输入方式将各种票据、报刊、书籍、文稿及其它印刷品的文字转化为图像信息，再利用文字识别技术将图像信息转化为电子文本
```

- **tesserct-ocr**

```python
OCR的一个底层识别库（不是模块，不能导入）
# Google维护的开源OCR识别库
```

- **pytesseract**

```python
Python模块,可调用底层识别库
# 对tesseract-ocr做的一层Python API封装
```

### **安装tesseract-ocr**

- **Ubuntu**

```python
sudo apt-get install tesseract-ocr 
```

- **Windows**

```python
1、下载安装包
2、添加到环境变量(Path)
```

- **测试**

```python
# 终端 | cmd命令行
tesseract xxx.jpg 文件名
```

### **安装pytesseract**

- 安装

```python
sudo pip3 install pytesseract
```

- 使用

  #离线安装步骤

  1.官网下载安装包  xxx.tar.gz

  2.解压;tar -zxvf xxx.tar.gz

  3.cd 解压后的文件夹 readme 和 setup .py

  4.sudo python3 setup.py install

  111111111111111111111111111111111111111111111111111111

- import pytesseract

  from PIL import Image

  img=Image.open('xxx.jpg')

  code=pytesseract.image_to_string(img)

  code 是字符串

  识别率低原因     看他训练的数据tessdata  机器训练的数据有多么高

  11111111111111111111111111111111111111111111111111111

- 爬取网站思路（验证码）

```python
1、获取验证码图片
2、使用PIL库打开图片
3、使用pytesseract将图片中验证码识别并转为字符串
4、将字符串发送到验证码框中或者某个URL地址
```

### **在线打码平台**

- **为什么使用在线打码**

```python
tesseract-ocr识别率很低,文字变形、干扰，导致无法识别验证码
```

- **云打码平台使用步骤**

```python
1、下载并查看接口文档
2、调整接口文档，调整代码并接入程序测试
3、真正接入程序，在线识别后获取结果并使用
```

- **破解云打码网站验证码**

  **1、下载并调整接口文档，封装成函数，打码获取结果**

```python

```
​	**2、访问云打码网站，获取验证码并在线识别**

```python

```

## **Fiddler抓包工具**

- **配置Fiddler**

```python
# 添加证书信任
1、Tools - Options - HTTPS
   勾选 Decrypt Https Traffic 后弹出窗口，一路确认
# 设置只抓取浏览器的数据包
2、...from browsers only
# 设置监听端口（默认为8888）
3、Tools - Options - Connections
# 配置完成后重启Fiddler（重要）
4、关闭Fiddler,再打开Fiddler
```

- **配置浏览器代理**

```python
1、安装Proxy SwitchyOmega插件
2、浏览器右上角：SwitchyOmega->选项->新建情景模式->AID1901(名字)->创建
   输入 ：HTTP://  127.0.0.1  8888
   点击 ：应用选项
3、点击右上角SwitchyOmega可切换代理
```

- **Fiddler常用菜单**

```python
1、Inspector ：查看数据包详细内容
   整体分为请求和响应两部分
2、常用菜单
   Headers ：请求头信息
   WebForms: POST请求Form表单数据 ：<body>
   GET请求查询参数: <QueryString>
   Raw
   将整个请求显示为纯文本
```

## **移动端app数据抓取**

**方法1 - 手机 + Fiddler**

```python
设置方法见文件夹 - 移动端抓包配置
```

**方法2 - F12浏览器工具**

**有道翻译手机版破解案例**

```python

```

## **爬虫总结**

```python
# 1、什么是爬虫
  爬虫是请求网站并提取数据的自动化程序

# 2、robots协议是什么
  爬虫协议或机器人协议,网站通过robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取

# 3、爬虫的基本流程
  1、请求得到响应
  2、解析
  3、保存数据

# 4、请求
  1、urllib
  2、requests
  3、scrapy

# 5、解析
  1、re正则表达式
  2、lxml+xpath解析
  3、json解析模块

# 6、selenium+browser

# 7、常见反爬策略
  1、Headers : 最基本的反爬手段，一般被关注的变量是UserAgent和Referer，可以考虑使用浏览器中
  2、UA ： 建立User-Agent池,每次访问页面随机切换
  3、拉黑高频访问IP
     数据量大用代理IP池伪装成多个访问者,也可控制爬取速度
  4、Cookies
     建立有效的cookie池，每次访问随机切换
  5、验证码
    验证码数量较少可人工填写
    图形验证码可使用tesseract识别
    其他情况只能在线打码、人工打码和训练机器学习模型
  6、动态生成
    一般由js动态生成的数据都是向特定的地址发get请求得到的，返回的一般是json
  7、签名及js加密
    一般为本地JS加密,查找本地JS文件,分析,或者使用execjs模块执行JS
  8、js调整页面结构
  9、js在响应中指向新的地址

# 8、scrapy框架的运行机制

# 9、分布式爬虫的原理
  多台主机共享一个爬取队列
```

