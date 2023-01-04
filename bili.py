import requests
import json

# 登录接口
url_login = 'https://passport.bilibili.com/api/v2/oauth2/login'

# 动态接口
url_dynamic = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history'

# 登录参数
data = {
    'username': 'zh',
    'password': 'mm'
}

# 登录
res = requests.post(url_login, data=data)
res_json = json.loads(res.text)
print(res_json)
# 获取access_token
access_token = res_json['data']['token_info']['access_token']

# 动态参数
params = {
    'host_uid': '227561303',
    'access_key': access_token
}

# 获取动态
res = requests.get(url_dynamic, params=params)
res_json = json.loads(res.text)

# 获取动态列表
dynamic_list = res_json['data']['cards']

# 打印动态列表
for dynamic in dynamic_list:
    print(dynamic['desc']['dynamic'])