# coding=utf-8
#用python爬取bing和baidu有关二次元动漫图片链接并逐行添加到TXT
import requests
import json

# 搜索关键字
keyword = '二次元动漫'

# bing api
url = 'https://www.bing.com/images/async?q={}&async=content&first=0&count=35&dgst=ro&IID=images.1&SFX=2&IG=9C37A2F6F2D44A7F9D5E8F8CED38D8F4&CW=1364&CH=766&CT=&S=1&ensearch=1&scenario=ImageBasicHover'.format(keyword)

# 发送请求
res = requests.get(url).text
print(res)

# 解析json
data = json.loads(res)

# 打开文件
f = open('二次元动漫图片链接.txt','w+')

# 获取图片链接
for item in data['items']:
    f.write(item['contentUrl']+'\n')

# 关闭文件
f.close()