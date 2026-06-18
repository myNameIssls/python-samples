"""Pandas 数据处理示例

本文件演示 Pandas 库的基本使用：
- Pandas：用于数据分析的库，提供了 DataFrame（数据框）数据结构
- DataFrame：类似 Excel 表格的二维数据结构，有行有列

安装命令：pip install pandas
"""

import pandas as pd    # 导入 Pandas 库，简称 pd（约定俗成的写法）


def main():
    # ==================== 创建 DataFrame ====================
    # DataFrame：Pandas 的核心数据结构，类似于 Excel 表格
    # 用字典创建，键是列名，值是列数据
    data = {
        "姓名": ["小明", "小红", "小刚"],    # 列：字符串类型
        "年龄": [20, 21, 19],              # 列：整数类型
        "成绩": [85, 92, 78],              # 列：整数类型
    }

    # pd.DataFrame()：将字典转换为 DataFrame
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)    # 打印表格
    # 输出：
    #     姓名  年龄  成绩
    # 0  小明   20    85
    # 1  小红   21    92
    # 2  小刚   19    78

    # ==================== 数据统计 ====================
    # df['列名']：选取某一列
    # .mean()：计算平均值
    print(f"\n平均年龄: {df['年龄'].mean():.2f}")    # :.2f 保留 2 位小数
    print(f"平均成绩: {df['成绩'].mean():.2f}")

    # ==================== 数据排序 ====================
    # df.sort_values()：按指定列排序
    # by="列名"：指定排序列
    # ascending=True/False：升序/降序
    print("\n按成绩排序:")
    print(df.sort_values("成绩", ascending=False))    # 降序排列


if __name__ == "__main__":
    main()
