# 写python爬虫github某个用户所有仓库
import requests
import json

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}

# 请求url
url = "https://api.github.com/users/{username}/repos"

# 替换{username}为你想要查询的用户名
username = "hllqk"

# 发送请求
response = requests.get(url.format(username=username),headers=headers)

# 获取json格式的响应数据
data = response.json()

# 遍历获取仓库名
for item in data:
    print(item['name'])