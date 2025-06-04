import json

def json_format(data):
    data = data
    # 使用 json.dumps() 格式化数据并打印
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)
