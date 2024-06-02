import requests

url = "https://api.cloudflare.com/client/v4/ips"

# 发送 GET 请求
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 请求成功，获取响应内容
    data = response.json()
    print(data)
    print("helloword")
else:
    # 请求失败，打印错误信息
    print("请求失败:", response.status_code)