"""变量与数据类型示例

本文件演示 Python 中最基础的数据类型：
- 字符串（str）：文本数据
- 整数（int）：整数值
- 浮点数（float）：小数
- 布尔值（bool）：True/False
"""


# ==================== 变量声明与赋值 ====================
# 变量不需要提前声明类型，直接赋值即可使用
# Python 是动态类型语言，变量的类型由赋值决定

name = "Alice"       # 字符串：用双引号或单引号包裹的文本
age = 25             # 整数：没有小数点的数字
height = 1.75        # 浮点数：带小数点的数字
is_student = True    # 布尔值：True（真）或 False（假）


# ==================== 类型查看 ====================
# 使用 type() 函数可以查看变量的数据类型

print(f"姓名: {name}, 类型: {type(name)}")
# f-string（格式化字符串）：在引号前加 f，可以在 {} 中直接插入变量
# type(name) 返回 "Alice" 这个变量的数据类型

print(f"年龄: {age}, 类型: {type(age)}")
print(f"身高: {height}, 类型: {type(height)}")
print(f"学生: {is_student}, 类型: {type(is_student)}")
