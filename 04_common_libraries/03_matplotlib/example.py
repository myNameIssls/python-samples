"""Matplotlib 数据可视化示例

运行前请确保已安装: pip install matplotlib
"""

import matplotlib.pyplot as plt


def main():
    months = ["1月", "2月", "3月", "4月", "5月", "6月"]
    sales = [120, 150, 180, 140, 200, 230]

    plt.figure(figsize=(8, 5))
    plt.plot(months, sales, marker="o", linewidth=2)
    plt.title("月度销售趋势")
    plt.xlabel("月份")
    plt.ylabel("销售额（万元）")
    plt.grid(True, alpha=0.3)
    plt.savefig("/workspace/04_common_libraries/03_matplotlib/sales_chart.png")
    print("图表已保存到 sales_chart.png")


if __name__ == "__main__":
    main()
