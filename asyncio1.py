import asyncio
import aiohttp
from bs4 import BeautifulSoup
#用python使用协程爬虫关于丛雨的bing搜索结果
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://cn.bing.com/search?q=丛雨'
    html = await fetch(url)
    soup = BeautifulSoup(html, 'lxml')
    results = soup.find_all('li', class_='b_algo')

    for result in results:
        title = result.find('h2')
        description = result.find('p')
        print(title.text)
        print(description.text)
        print('-' * 20)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())