"""NumPy 数值计算示例

本文件演示 NumPy 库的基本使用：
- NumPy：Python 科学计算的基础库，提供了高效的数组对象和数学函数
- 核心数据结构：ndarray（N 维数组）

安装命令：pip install numpy
"""

import numpy as np    # 导入 NumPy 库，简称 np（约定俗成的写法）


def main():
    # ==================== 创建数组 ====================
    # np.array()：将 Python 列表转换为 NumPy 数组
    arr = np.array([1, 2, 3, 4, 5])    # 创建一维数组
    print(f"数组: {arr}")                        # 输出：[1 2 3 4 5]

    # ==================== 数组属性 ====================
    # shape：数组的形状（各维度的长度）
    # dtype：数组元素的数据类型
    print(f"形状: {arr.shape}, 类型: {arr.dtype}")
    # 输出：形状: (5,), 类型: int64

    # ==================== 统计函数 ====================
    # np.mean()：计算平均值
    print(f"平均值: {np.mean(arr)}")

    # np.std()：计算标准差
    # :.4f 表示保留 4 位小数
    print(f"标准差: {np.std(arr):.4f}")

    # ==================== 二维数组（矩阵）====================
    # 创建二维数组（2 行 3 列）
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n矩阵:\n{matrix}")
    # 输出：
    # [[1 2 3]
    #  [4 5 6]]

    # 矩阵转置：行变列，列变行
    print(f"矩阵转置:\n{matrix.T}")
    # 输出：
    # [[1 4]
    #  [2 5]
    #  [3 6]]

    # 矩阵求和
    print(f"矩阵求和: {matrix.sum()}")


if __name__ == "__main__":
    main()
