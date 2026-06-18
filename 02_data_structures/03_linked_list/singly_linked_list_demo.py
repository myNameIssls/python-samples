"""单向链表（Singly Linked List）示例

本文件演示单向链表数据结构的完整实现：
- 链表：由节点（Node）组成，每个节点包含数据和指向下一个节点的指针
- 特点：插入/删除效率高（O(1)），但随机访问效率低（O(n)）
- 与数组的区别：数组在内存中是连续存储，链表是分散存储

基本操作：
- 头部插入、尾部插入、指定位置插入
- 头部删除、尾部删除、指定位置删除
- 查找、获取长度、判断是否为空
"""


# ==================== 节点类（Node）====================
class Node:
    """单向链表节点"""

    def __init__(self, data):
        # data：节点存储的数据
        self.data = data
        # next：指向下一个节点的指针，初始为 None
        self.next = None

    def __repr__(self):
        """调试时显示节点信息"""
        return f"Node({self.data})"


# ==================== 单向链表类 ====================
class SinglyLinkedList:
    """单向链表类"""

    def __init__(self):
        # head：链表的头节点，初始为 None（空链表）
        self.head = None
        # length：记录链表长度，避免每次遍历计算
        self.length = 0

    # ==================== 判空与长度 ====================
    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def size(self):
        """返回链表长度"""
        return self.length

    # ==================== 插入操作 ====================
    def prepend(self, data):
        """头部插入：在链表开头添加新节点"""
        # 1. 创建新节点
        new_node = Node(data)
        # 2. 新节点的 next 指向原来的头节点
        new_node.next = self.head
        # 3. 将新节点设为头节点
        self.head = new_node
        # 4. 长度加 1
        self.length += 1

    def append(self, data):
        """尾部插入：在链表末尾添加新节点"""
        # 1. 创建新节点
        new_node = Node(data)

        # 2. 如果链表为空，直接设为头节点
        if self.head is None:
            self.head = new_node
        else:
            # 3. 遍历到尾节点
            current = self.head
            while current.next:           # while current.next != None
                current = current.next
            # 4. 将尾节点的 next 指向新节点
            current.next = new_node

        self.length += 1

    def insert_at(self, index, data):
        """指定位置插入：在 index 位置插入新节点"""
        # 检查索引合法性
        if index < 0 or index > self.length:
            raise IndexError("索引越界")

        # 如果在头部插入
        if index == 0:
            self.prepend(data)
            return

        # 找到插入位置的前一个节点
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        # 插入新节点
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    # ==================== 删除操作 ====================
    def remove_first(self):
        """删除头节点"""
        if self.is_empty():
            raise IndexError("链表为空，无法删除")

        # 将头节点指向下一个节点
        self.head = self.head.next
        self.length -= 1

    def remove_last(self):
        """删除尾节点"""
        if self.is_empty():
            raise IndexError("链表为空，无法删除")

        # 如果只有一个节点
        if self.head.next is None:
            self.head = None
        else:
            # 遍历到倒数第二个节点
            current = self.head
            while current.next.next:      # 找到倒数第二个节点
                current = current.next
            # 删除最后一个节点
            current.next = None

        self.length -= 1

    def remove_at(self, index):
        """删除指定位置的节点"""
        if self.is_empty():
            raise IndexError("链表为空，无法删除")

        if index < 0 or index >= self.length:
            raise IndexError("索引越界")

        # 如果删除头节点
        if index == 0:
            self.remove_first()
            return

        # 找到要删除节点的前一个节点
        current = self.head
        for _ in range(index - 1):
            current = current.next

        # 删除节点：让前一个节点指向下一个节点
        current.next = current.next.next
        self.length -= 1

    # ==================== 查找操作 ====================
    def find(self, data):
        """查找数据所在位置，返回第一个匹配的索引，未找到返回 -1"""
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    def get(self, index):
        """获取指定位置的元素"""
        if index < 0 or index >= self.length:
            raise IndexError("索引越界")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    # ==================== 显示与转换 ====================
    def display(self):
        """显示链表：head -> node1 -> node2 -> ... -> None"""
        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements) + " -> None"

    def __str__(self):
        """print() 时调用"""
        return f"SinglyLinkedList({self.display()})"

    def __repr__(self):
        """调试时调用"""
        return self.__str__()


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("单向链表（Singly Linked List）测试")
    print("=" * 50)

    # 创建链表
    ll = SinglyLinkedList()
    print(f"\n1. 创建空链表: {ll}")
    print(f"   是否为空: {ll.is_empty()}, 长度: {ll.size()}")

    # 尾部插入
    print("\n2. 尾部插入 10, 20, 30")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print(f"   {ll}")

    # 头部插入
    print("\n3. 头部插入 5")
    ll.prepend(5)
    print(f"   {ll}")

    # 指定位置插入
    print("\n4. 在位置 2 插入 15")
    ll.insert_at(2, 15)
    print(f"   {ll}")

    # 获取元素
    print("\n5. 获取元素:")
    print(f"   位置 0: {ll.get(0)}")
    print(f"   位置 3: {ll.get(3)}")

    # 查找元素
    print("\n6. 查找元素:")
    print(f"   查找 20: 位置 {ll.find(20)}")
    print(f"   查找 99: 位置 {ll.find(99)}")

    # 删除头节点
    print("\n7. 删除头节点")
    ll.remove_first()
    print(f"   {ll}")

    # 删除尾节点
    print("\n8. 删除尾节点")
    ll.remove_last()
    print(f"   {ll}")

    # 删除指定位置
    print("\n9. 删除位置 1")
    ll.remove_at(1)
    print(f"   {ll}")

    print(f"\n10. 最终结果: {ll}, 长度: {ll.size()}")
