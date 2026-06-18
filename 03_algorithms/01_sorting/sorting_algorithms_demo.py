"""排序算法示例

本文件演示三种经典排序算法：
- 冒泡排序（Bubble Sort）：时间复杂度 O(n²)，简单但效率低
- 选择排序（Selection Sort）：时间复杂度 O(n²)，比冒泡排序交换次数少
- 快速排序（Quick Sort）：时间复杂度 O(n log n)，效率高，常用
"""


# ==================== 冒泡排序（Bubble Sort）====================
def bubble_sort(arr):
    """冒泡排序：比较相邻元素，每轮把最大元素"冒泡"到末尾"""
    n = len(arr)                              # 获取数组长度

    # 外层循环：需要执行 n-1 轮
    for i in range(n - 1):
        # 内层循环：每轮比较次数递减
        for j in range(n - 1 - i):
            # 如果前一个元素大于后一个元素，交换位置
            if arr[j] > arr[j + 1]:
                # Python 特有的交换语法：不需要临时变量
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ==================== 选择排序（Selection Sort）====================
def selection_sort(arr):
    """选择排序：每轮选择最小元素放到已排序序列的末尾"""
    n = len(arr)

    for i in range(n):
        # 假设当前位置是最小值的索引
        min_idx = i

        # 在未排序部分找到最小元素的索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 将找到的最小元素与当前位置交换
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# ==================== 快速排序（Quick Sort）====================
def quick_sort(arr):
    """快速排序：选择基准元素，分治递归排序"""
    # 递归终止条件：数组长度 <= 1
    if len(arr) <= 1:
        return arr

    # 选择基准元素（pivot）：使用中间元素
    pivot = arr[len(arr) // 2]

    # 分区操作：将数组分为三部分
    left = [x for x in arr if x < pivot]     # 小于基准的放左边
    middle = [x for x in arr if x == pivot]   # 等于基准的放中间
    right = [x for x in arr if x > pivot]     # 大于基准的放右边

    # 递归排序左右部分，然后合并
    return quick_sort(left) + middle + quick_sort(right)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11, 90]    # 测试数据

    print(f"原始数据: {data}")
    print(f"冒泡排序: {bubble_sort(data.copy())}")    # copy() 避免修改原数组
    print(f"选择排序: {selection_sort(data.copy())}")
    print(f"快速排序: {quick_sort(data.copy())}")
