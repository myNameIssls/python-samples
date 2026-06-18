"""Matplotlib 数据可视化示例

本文件演示 Matplotlib 库的基本使用：
- Matplotlib：Python 最流行的数据可视化库
- 可以绘制折线图、柱状图、饼图、散点图等各种图表

安装命令：pip install matplotlib
"""

import matplotlib.pyplot as plt    # 导入 Matplotlib 的 pyplot 模块，简称 plt


def main():
    # ==================== 准备数据 ====================
    # x 轴数据：月份
    months = ["1月", "2月", "3月", "4月", "5月", "6月"]
    # y 轴数据：销售额（万元）
    sales = [120, 150, 180, 140, 200, 230]

    # ==================== 创建图表 ====================
    # plt.figure()：创建图表窗口
    # figsize=(宽度, 高度)：设置图表大小（单位：英寸）
    plt.figure(figsize=(8, 5))

    # plt.plot()：绘制折线图
    # x 轴数据，y 轴数据
    # marker="o"：每个数据点显示圆圈标记
    # linewidth=2：线条宽度
    plt.plot(months, sales, marker="o", linewidth=2)

    # ==================== 设置图表元素 ====================
    plt.title("月度销售趋势")        # 图表标题
    plt.xlabel("月份")              # x 轴标签
    plt.ylabel("销售额（万元）")    # y 轴标签
    plt.grid(True, alpha=0.3)      # 显示网格线，alpha=0.3 表示透明度

    # ==================== 保存图表 ====================
    # plt.savefig()：保存图表到文件
    # 必须在 show() 之前调用，否则可能保存空白图片
    plt.savefig("/workspace/04_common_libraries/03_matplotlib/sales_chart.png")
    print("图表已保存到 sales_chart.png")


if __name__ == "__main__":
    main()
