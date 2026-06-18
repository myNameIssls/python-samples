"""函数定义与调用示例"""


def greet(name):
    return f"你好, {name}!"


def add(a, b):
    return a + b


def calculate(*args, operation="sum"):
    if operation == "sum":
        return sum(args)
    if operation == "max":
        return max(args)
    if operation == "min":
        return min(args)
    return None


square = lambda x: x * x

print(greet("Python"))
print(f"3 + 5 = {add(3, 5)}")
print(f"计算和: {calculate(1, 2, 3, 4, 5)}")
print(f"计算最大值: {calculate(1, 2, 3, 4, 5, operation='max')}")
print(f"4 的平方: {square(4)}")
