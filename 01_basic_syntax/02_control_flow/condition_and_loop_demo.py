"""条件语句与循环示例"""

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print(f"分数 {score} 的等级是: {grade}")

for i in range(1, 6):
    print(f"第 {i} 次循环")

count = 3
while count > 0:
    print(f"倒计时: {count}")
    count -= 1
