"""双向链表（Doubly Linked List）示例

本文件演示双向链表数据结构的完整实现：
- 双向链表：每个节点包含数据、指向前一个节点的指针、指向后一个节点的指针
- 特点：可以从两个方向遍历，支持双向查找
- 与单向链表的区别：每个节点多了一个 prev 指针

基本操作：
- 头部插入、尾部插入、指定位置插入
- 头部删除、尾部删除、指定位置删除
- 反向显示、查找
"""


# ==================== 双向链表节点类 ====================
class DNode:
    """双向链表节点"""

    def __init__(self, data):
        # data：节点存储的数据
        self.data = data
        # prev：指向前一个节点的指针
        self.prev = None
        # next：指向后一个节点的指针
        self.next = None

    def __repr__(self):
        return f"DNode({self.data})"


# ==================== 双向链表类 ====================
class DoublyLinkedList:
    """双向链表类"""

    def __init__(self):
        # head：链表的头节点
        self.head = None
        # tail：链表的尾节点（方便尾部操作）
        self.tail = None
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
        new_node = DNode(data)

        if self.is_empty():
            # 空链表：头尾都指向新节点
            self.head = self.tail = new_node
        else:
            # 非空：将新节点插入到头节点前面
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def append(self, data):
        """尾部插入：在链表末尾添加新节点"""
        new_node = DNode(data)

        if self.is_empty():
            # 空链表：头尾都指向新节点
            self.head = self.tail = new_node
        else:
            # 非空：将新节点插入到尾节点后面
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def insert_at(self, index, data):
        """指定位置插入：在 index 位置插入新节点"""
        if index < 0 or index > self.length:
            raise IndexError("索引越界")

        if index == 0:
            self.prepend(data)
            return

        if index == self.length:
            self.append(data)
            return

        # 找到插入位置的节点
        new_node = DNode(data)
        if index < self.length / 2:
            # 从头开始找（插入位置在前半部分）
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # 从尾开始找（插入位置在后半部分，更快）
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        # 在 current 前插入新节点
        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

        self.length += 1

    # ==================== 删除操作 ====================
    def remove_first(self):
        """删除头节点"""
        if self.is_empty():
            raise IndexError("链表为空，无法删除")

        if self.head == self.tail:
            # 只有一个节点
            self.head = self.tail = None
        else:
            # 有多个节点：将头节点向后移动
            self.head = self.head.next
            self.head.prev = None

        self.length -= 1

    def remove_last(self):
        """删除尾节点"""
        if self.is_empty():
            raise IndexError("链表为空，无法删除")

        if self.head == self.tail:
            # 只有一个节点
            self.head = self.tail = None
        else:
            # 有多个节点：将尾节点向前移动
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1

    def remove_at(self, index):
        """删除指定位置的节点"""
        if self.is_empty():
            raise IndexError("链表为空，无法删除")

        if index < 0 or index >= self.length:
            raise IndexError("索引越界")

        if index == 0:
            self.remove_first()
            return

        if index == self.length - 1:
            self.remove_last()
            return

        # 找到要删除的节点
        if index < self.length / 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        # 删除节点：跳过 current
        current.prev.next = current.next
        current.next.prev = current.prev

        self.length -= 1

    # ==================== 查找操作 ====================
    def find(self, data):
        """查找数据所在位置"""
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

        if index < self.length / 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        return current.data

    # ==================== 显示与转换 ====================
    def display(self):
        """正向显示链表"""
        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        return " <-> ".join(elements)

    def display_reverse(self):
        """反向显示链表"""
        elements = []
        current = self.tail

        while current:
            elements.append(str(current.data))
            current = current.prev

        return " <-> ".join(elements)

    def __str__(self):
        return f"DoublyLinkedList({self.display()})"


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("双向链表（Doubly Linked List）测试")
    print("=" * 50)

    dll = DoublyLinkedList()

    # 尾部插入
    print("\n1. 尾部插入: A, B, C")
    dll.append("A")
    dll.append("B")
    dll.append("C")
    print(f"   正向: {dll}")
    print(f"   反向: {dll.display_reverse()}")

    # 头部插入
    print("\n2. 头部插入: Z")
    dll.prepend("Z")
    print(f"   {dll}")

    # 指定位置插入
    print("\n3. 位置 2 插入: X")
    dll.insert_at(2, "X")
    print(f"   {dll}")

    # 获取元素
    print("\n4. 获取元素:")
    print(f"   位置 0: {dll.get(0)}")
    print(f"   位置 3: {dll.get(3)}")

    # 删除头节点
    print("\n5. 删除头节点")
    dll.remove_first()
    print(f"   {dll}")

    # 删除尾节点
    print("\n6. 删除尾节点")
    dll.remove_last()
    print(f"   {dll}")

    # 删除指定位置
    print("\n7. 删除位置 1")
    dll.remove_at(1)
    print(f"   {dll}")

    print(f"\n8. 最终结果: {dll}, 长度: {dll.size()}")
