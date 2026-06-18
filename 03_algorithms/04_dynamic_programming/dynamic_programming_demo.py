"""动态规划示例

本文件演示动态规划（Dynamic Programming）的经典问题：
- 动态规划：将复杂问题分解为子问题，避免重复计算
- 核心思想：存储子问题的解（记忆化），从子问题构建原问题的解
- 适用条件：最优子结构 + 重叠子问题

核心概念：
- 状态（State）：问题的局部解
- 状态转移方程（Transition）：如何从子问题推导当前问题
- DP 表：存储子问题解的表格
"""


# ==================== 爬楼梯问题（Climbing Stairs）====================
def climb_stairs(n):
    """爬楼梯问题：
    有 n 级台阶，每次可以爬 1 级或 2 级，问有多少种爬法？

    分析：
    - n=1: 1 种 (1)
    - n=2: 2 种 (1+1, 2)
    - n=3: 3 种 (1+1+1, 1+2, 2+1)
    - n=4: 5 种 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
    规律：F(n) = F(n-1) + F(n-2)，斐波那契数列！
    """
    # 基本情况
    if n <= 2:
        return n

    # 创建 DP 表
    dp = [0] * (n + 1)    # 索引 0 到 n，共 n+1 个元素
    dp[1] = 1             # 1 级台阶有 1 种爬法
    dp[2] = 2             # 2 级台阶有 2 种爬法

    # 状态转移：F(n) = F(n-1) + F(n-2)
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ==================== 0/1 背包问题（Knapsack）====================
def knapsack(weights, values, capacity):
    """0/1 背包问题：
    有 n 件物品，每件物品有重量和价值，背包容量为 capacity
    求：在不超过容量的情况下，能获得的最大价值

    特点：每件物品只能选一次（0/1 选择）

    DP 状态定义：
    dp[i][w] = 前 i 件物品，容量为 w 时的最大价值

    状态转移：
    - 如果不选第 i 件：dp[i][w] = dp[i-1][w]
    - 如果选第 i 件：dp[i][w] = values[i-1] + dp[i-1][w-weights[i-1]]
    - dp[i][w] = max(不选, 选)
    """
    n = len(weights)

    # 创建 DP 表：(n+1) x (capacity+1) 的二维数组
    # 初始化为 0，表示没有物品或容量为 0 时价值为 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填表
    for i in range(1, n + 1):           # 遍历物品（1 到 n）
        for w in range(1, capacity + 1):  # 遍历容量（1 到 capacity）
            # 检查当前物品是否能装入背包
            if weights[i - 1] <= w:
                # 能装入：选择价值更大的方案
                dp[i][w] = max(
                    dp[i - 1][w],                                        # 不选第 i 件
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]        # 选第 i 件
                )
            else:
                # 不能装入：只能不选
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 爬楼梯测试
    print(f"爬 5 级楼梯: {climb_stairs(5)} 种方法")

    # 背包问题测试
    weights = [2, 3, 4, 5]    # 物品重量
    values = [3, 4, 5, 6]     # 物品价值
    capacity = 8              # 背包容量
    print(f"背包最大价值: {knapsack(weights, values, capacity)}")
