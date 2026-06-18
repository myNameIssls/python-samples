"""Requests 网络请求示例

本文件演示 Requests 库的基本使用：
- Requests：Python 最流行的 HTTP 客户端库，用于发送网络请求
- 可以发送 GET、POST、PUT、DELETE 等各种 HTTP 请求

安装命令：pip install requests
"""

import json    # 内置库，用于处理 JSON 数据

# try...except：异常处理，捕获 import 失败的情况
try:
    import requests    # 导入 Requests 库
except ImportError:
    # 如果导入失败（即没有安装），提示用户安装
    print("请先安装 requests: pip install requests")
    exit(1)    # 退出程序


def main():
    # ==================== 发送 GET 请求 ====================
    # httpbin.org：一个测试网站，返回请求的相关信息
    url = "https://httpbin.org/get"

    # 请求参数：类似 URL 中的 ?name=Python&version=3.8
    params = {"name": "Python", "version": "3.8"}

    # requests.get()：发送 GET 请求
    # timeout=10：请求超时时间（秒），避免请求卡住
    response = requests.get(url, params=params, timeout=10)

    # response.status_code：HTTP 状态码
    # 200 表示成功，404 表示页面不存在，500 表示服务器错误
    print(f"状态码: {response.status_code}")

    # ==================== 处理响应 ====================
    # 只有请求成功时才处理响应
    if response.status_code == 200:
        # response.json()：将响应内容解析为 Python 字典
        data = response.json()

        # 打印响应的 URL（服务器收到的完整 URL）
        print(f"请求的 URL: {data['url']}")

        # json.dumps()：将 Python 对象格式化为 JSON 字符串
        # ensure_ascii=False：不转义中文字符
        # indent=2：缩进 2 个空格，使输出更易读
        print(f"参数: {json.dumps(data['args'], ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()
