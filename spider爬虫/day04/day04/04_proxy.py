import requests

url = 'http://httpbin.org/get'
headers = { 'User-Agent':'Mozilla/5.0' }
# 定义代理
proxies = {
    'http':'http://101.27.20.150:61234',
    'https':'https://101.27.20.150:61234'
}
html = requests.get(
    url=url,
    proxies=proxies,
    headers=headers
).text

print(html)








