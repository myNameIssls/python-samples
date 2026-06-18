"""栈与队列示例

本文件演示两种经典数据结构：
- 栈（Stack）：后进先出（LIFO = Last In First Out）
- 队列（Queue）：先进先出（FIFO = First In First Out）

生活类比：
- 栈：叠盘子，只能从最上面拿
- 队列：排队买奶茶，先来的先买
"""


# ==================== 栈（Stack）====================
class Stack:
    """栈类：后进先出的数据结构"""

    def __init__(self):
        # 初始化空列表，用于存储栈中的元素
        # Python 不需要提前声明变量，直接赋值即可创建属性
        self.items = []

    def push(self, item):
        """入栈：将元素压入栈顶"""
        # append() 在列表末尾添加元素，栈顶就在列表末尾
        self.items.append(item)

    def pop(self):
        """出栈：从栈顶弹出元素"""
        # 先检查栈是否为空
        if not self.is_empty():
            # pop() 默认删除并返回列表末尾元素，正好是栈顶
            return self.items.pop()
        # 如果栈为空，抛出异常
        raise IndexError("栈为空")

    def is_empty(self):
        """判断栈是否为空"""
        # len() 获取列表长度，为 0 则表示栈空
        return len(self.items) == 0

    def peek(self):
        """查看栈顶元素：返回但不删除"""
        if not self.is_empty():
            # 负索引 -1 表示列表最后一个元素（栈顶）
            return self.items[-1]


# ==================== 队列（Queue）====================
class Queue:
    """队列类：先进先出的数据结构"""

    def __init__(self):
        # 初始化空列表
        self.items = []

    def enqueue(self, item):
        """入队：将元素添加到队尾"""
        # append() 在列表末尾添加，队尾在列表末尾
        self.items.append(item)

    def dequeue(self):
        """出队：从队头移除元素"""
        if not self.is_empty():
            # pop(0) 删除并返回列表第一个元素（队头）
            return self.items.pop(0)
        raise IndexError("队列为空")

    def is_empty(self):
        """判断队列是否为空"""
        return len(self.items) == 0


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试栈：后进先出
    stack = Stack()
    for item in ["A", "B", "C"]:     # 依次入栈 A、B、C
        stack.push(item)
    # 出栈顺序：C、B、A（最后进去的最先出来）
    print("栈弹出顺序:", stack.pop(), stack.pop(), stack.pop())

    # 测试队列：先进先出
    queue = Queue()
    for item in ["1号", "2号", "3号"]:  # 依次入队 1号、2号、3号
        queue.enqueue(item)
    # 出队顺序：1号、2号、3号（最先进去的最先出来）
    print("队列出队顺序:", queue.dequeue(), queue.dequeue(), queue.dequeue())
