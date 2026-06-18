"""NumPy 数值计算示例

运行前请确保已安装: pip install numpy
"""

import numpy as np


def main():
    arr = np.array([1, 2, 3, 4, 5])
    print(f"数组: {arr}")
    print(f"形状: {arr.shape}, 类型: {arr.dtype}")
    print(f"平均值: {np.mean(arr)}")
    print(f"标准差: {np.std(arr):.4f}")

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n矩阵:\n{matrix}")
    print(f"矩阵转置:\n{matrix.T}")
    print(f"矩阵求和: {matrix.sum()}")


if __name__ == "__main__":
    main()
