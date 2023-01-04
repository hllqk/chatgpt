# 写python爬虫bilibili视频的代码
# -*- coding: utf-8 -*-
import requests
import json

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

# 请求地址
url = 'https://api.bilibili.com/x/web-interface/view'

# 请求参数
params = {
    'aid': '99999999'
}

# 发送请求
response = requests.get(url, params=params, headers=headers)

# 解析json
json_data = json.loads(response.text)

# 获取视频标题
title = json_data['data']['title']

# 获取视频播放地址
video_url = '无法获取'

# 获取视频封面
cover = json_data['data']['pic']

# 获取视频播放量
view = json_data['data']['stat']['view']

# 获取视频点赞数
like = json_data['data']['stat']['like']

# 获取视频弹幕数
danmaku = json_data['data']['stat']['danmaku']

# 获取视频收藏数
favorite = json_data['data']['stat']['favorite']

# 获取视频分享数
share = json_data['data']['stat']['share']

# 获取视频评论数
reply = json_data['data']['stat']['reply']

# 获取视频up主id
mid = json_data['data']['owner']['mid']

# 获取视频up主名称
name = json_data['data']['owner']['name']

# 打印信息
print('标题：', title)
print('播放地址：', video_url)
print('封面：', cover)
print('播放量：', view)
print('点赞数：', like)
print('弹幕数：', danmaku)
print('收藏数：', favorite)
print('分享数：', share)
print('评论数：', reply)
print('up主id：', mid)
print('up主名称：', name)