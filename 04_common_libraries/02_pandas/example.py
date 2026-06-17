"""Pandas 数据处理示例

运行前请确保已安装: pip install pandas
"""

import pandas as pd


def main():
    data = {
        "姓名": ["小明", "小红", "小刚"],
        "年龄": [20, 21, 19],
        "成绩": [85, 92, 78],
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    print(f"\n平均年龄: {df['年龄'].mean():.2f}")
    print(f"平均成绩: {df['成绩'].mean():.2f}")
    print("\n按成绩排序:")
    print(df.sort_values("成绩", ascending=False))


if __name__ == "__main__":
    main()
