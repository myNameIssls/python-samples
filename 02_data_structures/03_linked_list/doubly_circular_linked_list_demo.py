"""双向循环链表（Doubly Circular Linked List）示例

本文件演示双向循环链表数据结构的完整实现：
- 双向循环链表：头节点的 prev 指向尾节点，尾节点的 next 指向头节点
- 特点：可以从两个方向循环遍历

与双向链表的区别：
- 双向链表：head.prev = None, tail.next = None
- 双向循环链表：head.prev = tail, tail.next = head
"""


# ==================== 双向循环链表节点类 ====================
class DCNode:
    """双向循环链表节点"""

    def __init__(self, data):
        self.data = data
        self.prev = None   # 指向前一个节点
        self.next = None   # 指向后一个节点

    def __repr__(self):
        return f"DCNode({self.data})"


# ==================== 双向循环链表类 ====================
class DoublyCircularLinkedList:
    """双向循环链表类"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ==================== 判空与长度 ====================
    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    # ==================== 插入操作 ====================
    def append(self, data):
        """尾部插入"""
        new_node = DCNode(data)

        if self.is_empty():
            # 空链表：首尾相接
            new_node.prev = new_node
            new_node.next = new_node
            self.head = self.tail = new_node
        else:
            # 插入到尾节点后面
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, data):
        """头部插入"""
        new_node = DCNode(data)

        if self.is_empty():
            new_node.prev = new_node
            new_node.next = new_node
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def insert_at(self, index, data):
        """指定位置插入"""
        if index < 0 or index > self.length:
            raise IndexError("索引越界")

        if index == 0:
            self.prepend(data)
            return

        if index == self.length:
            self.append(data)
            return

        new_node = DCNode(data)

        # 选择更短的遍历方向
        if index <= self.length / 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index - 1, -1):
                current = current.prev

        # 在 current 前插入
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

        self.length += 1

    # ==================== 删除操作 ====================
    def remove_first(self):
        """删除头节点"""
        if self.is_empty():
            raise IndexError("链表为空")

        if self.head == self.tail:
            # 只有一个节点
            self.head = self.tail = None
        else:
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = self.head.next

        self.length -= 1

    def remove_last(self):
        """删除尾节点"""
        if self.is_empty():
            raise IndexError("链表为空")

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev

        self.length -= 1

    def remove_at(self, index):
        """删除指定位置的节点"""
        if self.is_empty():
            raise IndexError("链表为空")

        if index < 0 or index >= self.length:
            raise IndexError("索引越界")

        if index == 0:
            self.remove_first()
            return

        if index == self.length - 1:
            self.remove_last()
            return

        # 找到要删除的节点
        if index <= self.length / 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        # 删除节点
        current.prev.next = current.next
        current.next.prev = current.prev

        self.length -= 1

    # ==================== 查找操作 ====================
    def find(self, data):
        """查找数据，返回第一个匹配的索引"""
        if self.is_empty():
            return -1

        current = self.head
        index = 0

        while True:
            if current.data == data:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break

        return -1

    def get(self, index):
        """获取指定位置的元素"""
        if self.is_empty():
            raise IndexError("链表为空")

        if index < 0 or index >= self.length:
            raise IndexError("索引越界")

        if index <= self.length / 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        return current.data

    # ==================== 遍历与显示 ====================
    def display(self):
        """正向显示链表"""
        if self.is_empty():
            return "Empty"

        elements = []
        current = self.head

        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        return " <-> ".join(elements)

    def display_reverse(self):
        """反向显示链表"""
        if self.is_empty():
            return "Empty"

        elements = []
        current = self.tail

        while True:
            elements.append(str(current.data))
            current = current.prev
            if current == self.tail:
                break

        return " <-> ".join(elements)

    def traverse(self, steps=None, reverse=False):
        """
        遍历链表
        - steps=None：遍历一圈
        - steps=N：遍历 N 个节点
        - reverse=True：反向遍历
        """
        if self.is_empty():
            return []

        result = []

        if not reverse:
            current = self.head
            if steps is None:
                while True:
                    result.append(current.data)
                    current = current.next
                    if current == self.head:
                        break
            else:
                for _ in range(steps):
                    result.append(current.data)
                    current = current.next
        else:
            current = self.tail
            if steps is None:
                while True:
                    result.append(current.data)
                    current = current.prev
                    if current == self.tail:
                        break
            else:
                for _ in range(steps):
                    result.append(current.data)
                    current = current.prev

        return result

    def __str__(self):
        display_str = self.display()
        return f"DoublyCircularLL({display_str})"


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("双向循环链表（Doubly Circular Linked List）测试")
    print("=" * 50)

    dcll = DoublyCircularLinkedList()

    # 尾部插入
    print("\n1. 尾部插入: A, B, C")
    dcll.append("A")
    dcll.append("B")
    dcll.append("C")
    print(f"   正向: {dcll}")
    print(f"   反向: {dcll.display_reverse()}")

    # 头部插入
    print("\n2. 头部插入: Z")
    dcll.prepend("Z")
    print(f"   {dcll}")

    # 指定位置插入
    print("\n3. 位置 2 插入: X")
    dcll.insert_at(2, "X")
    print(f"   {dcll}")

    # 遍历演示
    print("\n4. 遍历演示:")
    print(f"   正向遍历一圈: {dcll.traverse()}")
    print(f"   正向遍历 5 步: {dcll.traverse(5)}")
    print(f"   反向遍历一圈: {dcll.traverse(reverse=True)}")
    print(f"   反向遍历 5 步: {dcll.traverse(5, reverse=True)}")

    # 查找和获取
    print("\n5. 查找与获取:")
    print(f"   查找 B: 位置 {dcll.find('B')}")
    print(f"   获取位置 2: {dcll.get(2)}")

    # 删除操作
    print("\n6. 删除操作:")
    dcll.remove_first()
    print(f"   删除头节点: {dcll}")
    dcll.remove_last()
    print(f"   删除尾节点: {dcll}")
    dcll.remove_at(1)
    print(f"   删除位置 1: {dcll}")

    print(f"\n7. 最终结果: {dcll}, 长度: {dcll.size()}")
