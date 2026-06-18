"""单向循环链表（Singly Circular Linked List）示例

本文件演示单向循环链表数据结构的完整实现：
- 单向循环链表：尾节点的 next 指向头节点，形成一个环
- 特点：没有 None 终点，可以无限遍历
- 应用场景：约瑟夫问题、循环调度、时间片轮转

与单向链表的区别：
- 单向链表：尾节点.next = None
- 单向循环链表：尾节点.next = head
"""


# ==================== 节点类 ====================
class Node:
    """单向循环链表节点"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


# ==================== 单向循环链表类 ====================
class SinglyCircularLinkedList:
    """单向循环链表类"""

    def __init__(self):
        self.head = None
        self.tail = None    # 保存尾节点，方便 O(1) 尾部操作
        self.length = 0

    # ==================== 判空与长度 ====================
    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    # ==================== 插入操作 ====================
    def append(self, data):
        """尾部插入：新节点的 next 指向头节点"""
        new_node = Node(data)

        if self.is_empty():
            # 空链表：新节点指向自己
            new_node.next = new_node
            self.head = self.tail = new_node
        else:
            # 非空：新节点指向头节点，尾节点指向新节点
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, data):
        """头部插入：新节点指向原头节点，尾节点指向新节点"""
        new_node = Node(data)

        if self.is_empty():
            new_node.next = new_node
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
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

        new_node = Node(data)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        # 如果插入位置是尾部，更新 tail
        if current == self.tail:
            self.tail = new_node

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
            # 多个节点：尾节点跳过头节点，头节点后移
            self.tail.next = self.head.next
            self.head = self.head.next

        self.length -= 1

    def remove_last(self):
        """删除尾节点"""
        if self.is_empty():
            raise IndexError("链表为空")

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            # 找到倒数第二个节点
            current = self.head
            while current.next != self.tail:
                current = current.next
            # 删除尾节点
            current.next = self.head    # 新尾节点指向头节点
            self.tail = current

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

        # 找到要删除节点的前一个节点
        current = self.head
        for _ in range(index - 1):
            current = current.next

        # 删除节点
        current.next = current.next.next

        # 如果删除的是尾节点
        if current.next == self.head:
            self.tail = current

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
            if current == self.head:    # 遍历一圈后回到头节点
                break

        return -1

    def get(self, index):
        """获取指定位置的元素"""
        if self.is_empty():
            raise IndexError("链表为空")

        if index < 0 or index >= self.length:
            raise IndexError("索引越界")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    # ==================== 遍历与显示 ====================
    def display(self):
        """显示链表（会标注循环）"""
        if self.is_empty():
            return "Empty"

        elements = []
        current = self.head

        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        return " -> ".join(elements) + " -> (回到头部)"

    def traverse(self, steps=None):
        """
        遍历链表
        - steps=None：从头遍历一圈
        - steps=N：遍历 N 个节点
        """
        if self.is_empty():
            return []

        result = []
        current = self.head

        if steps is None:
            # 遍历一圈
            while True:
                result.append(current.data)
                current = current.next
                if current == self.head:
                    break
        else:
            # 遍历指定步数
            for _ in range(steps):
                result.append(current.data)
                current = current.next

        return result

    def __str__(self):
        return f"SinglyCircularLL({self.display()})"


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("单向循环链表（Singly Circular Linked List）测试")
    print("=" * 50)

    scll = SinglyCircularLinkedList()

    # 尾部插入
    print("\n1. 尾部插入: 1, 2, 3")
    scll.append(1)
    scll.append(2)
    scll.append(3)
    print(f"   {scll}")

    # 头部插入
    print("\n2. 头部插入: 0")
    scll.prepend(0)
    print(f"   {scll}")

    # 指定位置插入
    print("\n3. 位置 2 插入: 5")
    scll.insert_at(2, 5)
    print(f"   {scll}")

    # 遍历演示
    print("\n4. 遍历演示:")
    print(f"   遍历一圈: {scll.traverse()}")
    print(f"   遍历 5 步: {scll.traverse(5)}")

    # 查找
    print("\n5. 查找:")
    print(f"   查找 2: 位置 {scll.find(2)}")
    print(f"   获取位置 3: {scll.get(3)}")

    # 删除
    print("\n6. 删除操作:")
    scll.remove_first()
    print(f"   删除头节点: {scll}")
    scll.remove_last()
    print(f"   删除尾节点: {scll}")
    scll.remove_at(1)
    print(f"   删除位置 1: {scll}")

    print(f"\n7. 最终结果: {scll}, 长度: {scll.size()}")
