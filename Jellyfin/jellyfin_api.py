import requests
from requests.auth import HTTPBasicAuth

# 替换为你的 Jellyfin 服务器地址、用户名和密码
jellyfin_server = 'http://127.0.0.1:8096'
username = 'zfsjlll'
password = 'yyt010324'

# 构建 API 请求的 URL
api_url = f'{jellyfin_server}/Users/Public'  # 这是一个公共 API 端点的示例

# 使用 requests.get 方法发送 GET 请求，并使用 HTTPBasicAuth 添加基本身份验证
response = requests.get(api_url, auth=HTTPBasicAuth(username, password))

# 检查响应状态码
if response.status_code == 200:
    print('请求成功！')
    # 打印返回的数据
    print(response.json())
else:
    print(f'请求失败，状态码：{response.status_code}')