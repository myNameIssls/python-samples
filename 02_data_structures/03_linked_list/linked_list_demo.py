"""单链表示例

本文件演示链表（Linked List）数据结构：
- 链表：由节点（Node）组成，每个节点包含数据和指向下一个节点的指针
- 特点：插入/删除效率高（O(1)），但随机访问效率低（O(n)）
- 与数组的区别：数组在内存中是连续存储，链表是分散存储
"""


# ==================== 节点类（Node）====================
class Node:
    """节点类：链表的基本单元"""

    def __init__(self, data):
        # data：节点存储的数据
        self.data = data
        # next：指向下一个节点的指针，初始为 None（表示没有下一个节点）
        self.next = None


# ==================== 链表类（LinkedList）====================
class LinkedList:
    """单链表类"""

    def __init__(self):
        # head：链表的头节点，初始为 None（空链表）
        self.head = None

    def append(self, data):
        """在链表末尾添加节点"""
        # 1. 创建新节点
        new_node = Node(data)

        # 2. 如果链表为空，直接将新节点设为头节点
        if self.head is None:
            self.head = new_node
            return

        # 3. 如果链表不为空，遍历到尾节点
        current = self.head
        while current.next:           # while current.next != None
            current = current.next    # 移动到下一个节点
        # 循环结束后，current 指向尾节点

        # 4. 将尾节点的 next 指向新节点
        current.next = new_node

    def display(self):
        """将链表转换为字符串显示"""
        elements = []     # 用于存储所有节点的数据
        current = self.head

        # 遍历链表
        while current:    # while current != None
            elements.append(str(current.data))
            current = current.next

        # 用 " -> " 连接所有元素，表示链表的结构
        return " -> ".join(elements)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 创建链表
    linked_list = LinkedList()

    # 依次添加节点
    linked_list.append(1)    # 链表：1
    linked_list.append(2)    # 链表：1 -> 2
    linked_list.append(3)    # 链表：1 -> 2 -> 3

    # 显示链表
    print(f"链表:", linked_list.display())
