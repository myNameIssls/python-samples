"""序列数据结构示例：列表、元组、字典、集合"""

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(f"列表: {numbers}")
print(f"切片 [1:4]: {numbers[1:4]}")

coordinates = (10.5, 20.3)
x, y = coordinates
print(f"元组解包: x={x}, y={y}")

student = {"name": "小明", "age": 18, "major": "计算机"}
student["grade"] = "A"
for key, value in student.items():
    print(f"{key}: {value}")

colors = {"red", "blue", "green", "red"}
print(f"集合（自动去重）: {colors}")
print(f"共有 {len(colors)} 种颜色")
