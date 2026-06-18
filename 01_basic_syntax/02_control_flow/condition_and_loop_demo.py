"""条件语句与循环示例

本文件演示 Python 中的控制流语句：
- 条件语句：if / elif / else
- for 循环：遍历已知次数
- while 循环：条件满足时重复执行
"""


# ==================== 条件语句 ====================
# 成绩分级：根据分数判断等级

score = 85  # 定义一个变量表示分数

# if...elif...else：依次检查条件，第一个满足的执行
if score >= 90:          # 如果分数 >= 90
    grade = "A"          # 等级为 A
elif score >= 80:        # 否则如果分数 >= 80
    grade = "B"          # 等级为 B
elif score >= 60:        # 否则如果分数 >= 60
    grade = "C"          # 等级为 C
else:                    # 以上都不满足
    grade = "D"          # 等级为 D

print(f"分数 {score} 的等级是: {grade}")


# ==================== for 循环 ====================
# range(start, end)：生成从 start 到 end-1 的整数序列
# 语法：range(起始值, 结束值) 结束值不包含

for i in range(1, 6):           # i 从 1 循环到 5（不包含 6）
    print(f"第 {i} 次循环")


# ==================== while 循环 ====================
# while：当条件为 True 时重复执行循环体

count = 3            # 初始化计数器
while count > 0:     # 当 count > 0 时继续循环
    print(f"倒计时: {count}")
    count -= 1       # 每次循环将 count 减 1，避免无限循环
