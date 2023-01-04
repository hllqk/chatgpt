# 提问：写python爬虫www.shui.tk的所有文章
# 有bug懒得修了
import requests
from bs4 import BeautifulSoup

# 爬取www.shui.tk的所有文章

def get_article_urls(url):
    # 获取文章url
    response = requests.get(url,verify=False)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    # 找到文章的列表
    article_list = soup.find('article', class_='article-item')
    # 找到所有文章的url
    article_urls = [item.find('a')['href'] for item in article_list.find_all('post-link')]
    return article_urls

def get_article_content(url):
    # 获取文章内容
    response = requests.get(url,verify=False)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    # 找到文章内容
    article_content = soup.find('div', class_='entry-content').text
    return article_content

def main():
    url = 'https://www.shui.tk/'
    article_urls = get_article_urls(url)
    # for article_url in article_urls:
    #     article_content = get_article_content(article_url)
    #     print(article_content)

if __name__ == '__main__':
    main()