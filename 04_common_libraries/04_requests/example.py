"""Requests 网络请求示例

运行前请确保已安装: pip install requests
"""

import json

try:
    import requests
except ImportError:
    print("请先安装 requests: pip install requests")
    exit(1)


def main():
    url = "https://httpbin.org/get"
    params = {"name": "Python", "version": "3.8"}

    response = requests.get(url, params=params, timeout=10)
    print(f"状态码: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"请求的 URL: {data['url']}")
        print(f"参数: {json.dumps(data['args'], ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()
