import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
import asyncio
#用python多线程下载txt文件里的多行图片链接，并使用协程
async def download_image(url):
    r = requests.get(url)
    image_name = url.split('/')[-1]
    with open('./images/' + image_name, 'wb') as f:
        f.write(r.content)

def run(url):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_image(url))

if __name__ == '__main__':
    with open('urls.txt', 'r') as f:
        urls = f.readlines()
    pool = ThreadPool(4)
    pool.map(run, urls)
    pool.close()
    pool.join()