"""查找算法示例

本文件演示两种查找算法：
- 线性查找（Linear Search）：逐个检查，时间复杂度 O(n)
- 二分查找（Binary Search）：折半查找，时间复杂度 O(log n)
  注意：二分查找要求数组有序！
"""


# ==================== 线性查找（Linear Search）====================
def linear_search(arr, target):
    """线性查找：逐个遍历数组查找目标元素"""
    # enumerate()：同时获取元素的索引和值
    for i, value in enumerate(arr):
        if value == target:
            return i    # 找到目标，返回索引
    return -1           # 未找到，返回 -1


# ==================== 二分查找（Binary Search）====================
def binary_search(arr, target):
    """二分查找：在有序数组中查找目标元素（递归实现）"""
    # 初始化左右边界
    left = 0              # 左边界（起始索引）
    right = len(arr) - 1  # 右边界（结束索引）

    # 当左边界 <= 右边界时，继续查找
    while left <= right:
        # 计算中间位置（向下取整）
        mid = (left + right) // 2

        if arr[mid] == target:
            # 找到目标，返回索引
            return mid
        elif arr[mid] < target:
            # 目标在右半部分，缩小左边界
            left = mid + 1
        else:
            # 目标在左半部分，缩小右边界
            right = mid - 1

    # 未找到目标
    return -1


# ==================== 测试代码 ====================
if __name__ == "__main__":
    data = [11, 12, 22, 25, 64, 90]    # 有序数组
    target = 25                          # 要查找的目标

    print(f"线性查找 {target}: 索引 = {linear_search(data, target)}")
    print(f"二分查找 {target}: 索引 = {binary_search(data, target)}")
