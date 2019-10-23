from threading import Thread
import random
import requests

# 功能: 随机向8000或8001发1个请求
def get_request():
    url1 = 'http://127.0.0.1:8000/test_cors'
    url2 = 'http://127.0.0.1:8001/test_cors'
    url = random.choice([url1,url2])
    # 发请求 - 在浏览器地址栏输入url地址,敲回车
    requests.get(url)

t_list = []

for i in range(30):
    t = Thread(target=get_request)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()





















