"""查找算法示例"""


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    data = [11, 12, 22, 25, 64, 90]
    target = 25
    print(f"线性查找 {target}: 索引 = {linear_search(data, target)}")
    print(f"二分查找 {target}: 索引 = {binary_search(data, target)}")
