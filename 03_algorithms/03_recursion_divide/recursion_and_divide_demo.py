"""递归与分治示例

本文件演示递归和分治策略：
- 递归（Recursion）：函数调用自身来解决问题
- 分治（Divide and Conquer）：将大问题分解为小问题，分别解决后合并结果

递归三要素：
1. 基本情况（Base Case）：递归终止条件
2. 递归调用：函数调用自身
3. 递推公式：将问题逐步分解
"""


# ==================== 阶乘（Factorial）====================
def factorial(n):
    """计算 n 的阶乘：n! = n * (n-1) * (n-2) * ... * 1"""
    # 基本情况：n <= 1 时返回 1
    if n <= 1:
        return 1

    # 递归调用：n! = n * (n-1)!
    return n * factorial(n - 1)


# ==================== 斐波那契数列（Fibonacci）====================
def fibonacci(n):
    """计算斐波那契数列第 n 项：
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2)
    """
    # 基本情况
    if n <= 1:
        return n    # n=0 返回 0，n=1 返回 1

    # 递归调用：当前项 = 前两项之和
    return fibonacci(n - 1) + fibonacci(n - 2)


# ==================== 归并排序（Merge Sort）- 分治策略 ====================
def merge_sort(arr):
    """归并排序：分治策略的典型应用"""
    # 基本情况：数组长度 <= 1，无需排序
    if len(arr) <= 1:
        return arr

    # 分解：将数组分成两半
    mid = len(arr) // 2                          # 中间索引
    left = merge_sort(arr[:mid])                 # 左半部分递归排序
    right = merge_sort(arr[mid:])                # 右半部分递归排序

    # 合并：将两个有序数组合并为一个有序数组
    return merge(left, right)


def merge(left, right):
    """合并两个有序数组"""
    result = []    # 存储合并结果
    i = j = 0      # i 遍历左数组，j 遍历右数组

    # 比较两个数组的元素，按顺序放入结果数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 处理剩余元素
    result.extend(left[i:])     # extend() 将列表中的所有元素添加到结果中
    result.extend(right[j:])

    return result


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print(f"5! = {factorial(5)}")
    print(f"斐波那契数列前8项: {[fibonacci(i) for i in range(8)]}")
    print(f"归并排序: {merge_sort([38, 27, 43, 3, 9, 82, 10])}")
