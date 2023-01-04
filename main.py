# chatgpt提问：写python爬虫bing每日壁纸的代码
import requests
import os

url = 'https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

response = requests.get(url).json()
image_url = response['images'][0]['url']
image_url = 'https://bing.com' + image_url

response = requests.get(image_url)



with open('bing_wallpaper.jpg','wb') as file:
    file.write(response.content)