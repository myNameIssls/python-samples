"""函数定义与调用示例

本文件演示 Python 中函数的定义和使用：
- 普通函数：使用 def 关键字定义
- 参数传递：位置参数、默认参数
- 可变参数：*args 接收任意数量的位置参数
- lambda 表达式：创建匿名函数
"""


# ==================== 简单函数 ====================
# def 函数名(参数): 定义一个函数
# return 返回值

def greet(name):
    """问候函数：根据名字返回问候语"""
    return f"你好, {name}!"


def add(a, b):
    """加法函数：返回两个数的和"""
    return a + b


# ==================== 带默认参数的函数 ====================
# *args：可变参数，接收任意数量的位置参数，以元组形式存储
# operation="sum"：默认参数，如果不传则使用默认值 "sum"

def calculate(*args, operation="sum"):
    """
    计算函数：根据 operation 执行不同运算

    参数:
        *args: 任意数量的数字
        operation: 运算类型，"sum"(求和) / "max"(最大值) / "min"(最小值)

    返回:
        计算结果
    """
    if operation == "sum":
        return sum(args)          # sum() 是 Python 内置函数，计算总和
    if operation == "max":
        return max(args)          # max() 是 Python 内置函数，计算最大值
    if operation == "min":
        return min(args)          # min() 是 Python 内置函数，计算最小值
    return None                   # operation 不合法时返回 None


# ==================== lambda 表达式（匿名函数）====================
# lambda 参数: 表达式
# 创建一个简单的匿名函数，计算平方
square = lambda x: x * x


# ==================== 函数调用 ====================
print(greet("Python"))                              # 调用 greet 函数
print(f"3 + 5 = {add(3, 5)}")                       # 调用 add 函数
print(f"计算和: {calculate(1, 2, 3, 4, 5)}")        # 使用可变参数，默认 operation="sum"
print(f"计算最大值: {calculate(1, 2, 3, 4, 5, operation='max')}")  # 指定 operation 为 "max"
print(f"4 的平方: {square(4)}")                       # 调用 lambda 函数
