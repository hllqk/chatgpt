
import requests
import re
from bs4 import BeautifulSoup

# 登录
username = '你的账号'
password = '你的密码'
data = {
    'pixiv_id': username,
    'password': password,
    'captcha': '',
    'g_recaptcha_response': '',
    'source': 'pc',
    'ref': 'wwwtop_accounts_index',
    'return_to': 'https://www.pixiv.net/'
}
session = requests.Session()
login_url = 'https://accounts.pixiv.net/login'
response = session.post(login_url, data=data)

# 获取收藏页面
fav_url = 'https://www.pixiv.net/bookmark.php'
response = session.get(fav_url)

# 从收藏页面获取所有图片的url
soup = BeautifulSoup(response.text, 'html.parser')
img_urls = [img.get('data-src') for img in soup.find_all('img', {'class': '_thumbnail ui-scroll-view'})]

# 从图片url中获取原图的url
original_img_urls = []
for img_url in img_urls:
    response = session.get(img_url)
    original_img_urls.append(re.findall(r'https://i.pximg.net/img-original/.*?\.(.*?)&', response.text)[0])

# 格式化输出
for img_url in original_img_urls:
    print(img_url)