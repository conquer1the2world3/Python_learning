import json
import requests
# from utils import json_format

def do_search(base_url, api_key, user_id=None, subject_name=None, recursive=True, parent_id=None):
    url = f"{base_url}/Items/{parent_id}"
    headers = {"Authorization": f"MediaBrowser Token=\"{api_key}\""}
    params = {
        "userId": user_id,
        "enableImages": False,
        "recursive": recursive,
        "searchTerm": subject_name,
        "fields": "CanDownload",
        "parentId": parent_id
    }

    response = requests.get(url, headers=headers, params=params)

    print(json_format(response.json()))  # 输出响应信息

    return response.json()



def json_format(data):
    data = data
    # 使用 json.dumps() 格式化数据并打印
    formatted_data = json.dumps(data, ensure_ascii=False, indent=4)
    print(formatted_data)

def fetch(subject_name=None):
    res = do_search(base_url, api_key, subject_name=subject_name)
    # print(json_format(res))
    for i in res["Items"]:
        # 如果是系列   
        if i["Type"] == "Series":
            print("是系列："+i["Name"])
            do_search(base_url, api_key, parent_id=i["Id"])
        # 如果是季度
        elif i["Type"] == "Season":
            print("是季度："+i["Name"])
            fetch(do_search(base_url, api_key, parent_id=i["Id"]))
        # 如果是剧集
        elif i["Type"] == "Episode":
            print("是剧集："+i["Name"])
        else:
            print("不符合要求:"+i["Name"])

base_url="http://127.0.0.1:8096"
api_key="8ea4dba65e6446bc81104e5001d6714c"
user_id="bd89c7976f8345e7bbf071299c4b7c20"
parent_id="dca8fd13b808d072d7c42444aa7aa571"
# subject_name="悠哉日常大王"
# subject_name="派对浪客诸葛孔明"
# subject_name="ようこそ実力至上主義の教室へ"
# do_search(base_url, api_key, subject_name=subject_name)
# do_search(base_url, api_key, parent_id="dca8fd13b808d072d7c42444aa7aa571")
# fetch("派对浪客诸葛孔明")
do_search(base_url, api_key, user_id=user_id, parent_id=parent_id)