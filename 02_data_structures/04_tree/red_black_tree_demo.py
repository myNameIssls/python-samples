"""红黑树（Red-Black Tree）示例

本文件演示红黑树的完整实现：
- 红黑树：一种自平衡的二叉搜索树
- 通过节点颜色和旋转操作保持近似平衡

红黑树的 5 个性质：
1. 每个节点要么是红色，要么是黑色
2. 根节点是黑色
3. 所有叶子节点（NIL）是黑色
4. 红色节点的子节点必须是黑色（不能有连续红色）
5. 从任意节点到其每个叶子节点的路径上，黑色节点数量相同

时间复杂度：所有操作都是 O(log n)

与 AVL 树的比较：
- AVL：查找更快（更严格平衡），但插入/删除时旋转更多
- 红黑树：插入/删除更快（近似平衡），实际应用中更常用
"""


# ==================== 颜色常量 ====================
BLACK = True
RED = False


# ==================== 红黑树节点类 ====================
class RBNode:
    """红黑树节点"""

    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        color_str = "B" if self.color == BLACK else "R"
        return f"RBNode({self.value},{color_str})"


# ==================== 红黑树类 ====================
class RedBlackTree:
    """红黑树类"""

    def __init__(self):
        # 使用 NIL 哨兵节点，简化边界处理
        self.NIL = RBNode(value=None, color=BLACK)
        self.root = self.NIL
        self.size = 0

    def is_empty(self):
        return self.root == self.NIL

    def __len__(self):
        return self.size

    # ==================== 辅助方法 ====================
    def _is_red(self, node):
        """判断节点是否为红色"""
        return node is not self.NIL and node.color == RED

    def _is_black(self, node):
        """判断节点是否为黑色"""
        return node is self.NIL or node.color == BLACK

    def _get_uncle(self, node):
        """获取叔节点"""
        if node.parent is None:
            return self.NIL
        grandparent = node.parent.parent
        if grandparent is None:
            return self.NIL
        if node.parent == grandparent.left:
            return grandparent.right
        return grandparent.left

    def _get_sibling(self, node):
        """获取兄弟节点"""
        if node.parent is None:
            return self.NIL
        if node == node.parent.left:
            return node.parent.right
        return node.parent.left

    def _rotate_left(self, x):
        """
        左旋
              x                y
             / \              / \
            T1  y    -->     x   T3
               / \          / \
              T2  T3        T1  T2
        """
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _rotate_right(self, y):
        """
        右旋
              y                x
             / \              / \
            x   T3    -->    T1  y
           / \                  / \
          T1  T2              T2  T3
        """
        x = y.left
        y.left = x.right

        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    # ==================== 插入修复 ====================
    def _insert_fixup(self, node):
        """
        插入修复：保持红黑树性质
        违反性质的情况：
        1. 当前节点是红色，父节点也是红色
        2. 叔节点也是红色（LLr/RLr 型）
        3. 叔节点是黑色，当前节点是内孙子（LRb/RBb 型）
        4. 叔节点是黑色，当前节点是外孙子（LLb/RBb 型）
        """
        while node.parent and self._is_red(node.parent):
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                # 情况 1：叔节点是红色
                if self._is_red(uncle):
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    # 情况 2：叔节点是黑色，当前节点是右孩子
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    # 情况 3：叔节点是黑色，当前节点是左孩子（外孙子）
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_right(node.parent.parent)
            else:
                # 对称情况：父节点是祖父的右子节点
                uncle = node.parent.parent.left
                if self._is_red(uncle):
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._rotate_left(node.parent.parent)

        # 保持性质 2：根节点必须是黑色
        self.root.color = BLACK

    # ==================== 插入操作 ====================
    def insert(self, value):
        """插入值为 value 的节点"""
        new_node = RBNode(value)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        # 1. 找到插入位置
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            elif new_node.value > current.value:
                current = current.right
            else:
                return    # 不允许重复值

        # 2. 插入节点
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        # 3. 修复红黑树性质
        self._insert_fixup(new_node)
        self.size += 1

    # ==================== 查找操作 ====================
    def search(self, value):
        """查找值为 value 的节点"""
        current = self.root

        while current != self.NIL:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def contains(self, value):
        return self.search(value) is not None

    # ==================== 找最小/最大节点 ====================
    def find_min(self, node=None):
        if node is None:
            node = self.root
        if node == self.NIL:
            return None
        while node.left != self.NIL:
            node = node.left
        return node

    def find_max(self, node=None):
        if node is None:
            node = self.root
        if node == self.NIL:
            return None
        while node.right != self.NIL:
            node = node.right
        return node

    # ==================== 删除修复 ====================
    def _delete_fixup(self, x):
        """
        删除修复：保持红黑树性质
        x：替代被删除节点的子节点（可能为 NIL）
        """
        while x != self.root and self._is_black(x):
            if x == x.parent.left:
                sibling = x.parent.right
                # 兄弟节点是红色
                if self._is_red(sibling):
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._rotate_left(x.parent)
                    sibling = x.parent.right

                # 兄弟节点是黑色，且两个侄子都是黑色
                if (self._is_black(sibling.left) and self._is_black(sibling.right)):
                    sibling.color = RED
                    x = x.parent
                else:
                    # 兄弟的右侄子黑色，左侄子红色
                    if self._is_black(sibling.right):
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self._rotate_right(sibling)
                        sibling = x.parent.right

                    # 兄弟节点设为与父节点相同的颜色
                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.right.color = BLACK
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                # 对称情况
                sibling = x.parent.left
                if self._is_red(sibling):
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._rotate_right(x.parent)
                    sibling = x.parent.left

                if self._is_black(sibling.left) and self._is_black(sibling.right):
                    sibling.color = RED
                    x = x.parent
                else:
                    if self._is_black(sibling.left):
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self._rotate_left(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.left.color = BLACK
                    self._rotate_right(x.parent)
                    x = self.root

        x.color = BLACK

    # ==================== 删除操作 ====================
    def _transplant(self, u, v):
        """用 v 替换 u"""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, value):
        """删除值为 value 的节点"""
        z = self.search(value)
        if z == self.NIL or z is None:
            return False

        y = z
        y_original_color = y.color

        if z.left == self.NIL:
            # 情况 1：左子节点为空
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            # 情况 2：右子节点为空
            x = z.left
            self._transplant(z, z.left)
        else:
            # 情况 3：两个子节点都不为空
            y = self.find_min(z.right)
            y_original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        # 如果删除的是黑色节点，需要修复
        if y_original_color == BLACK:
            self._delete_fixup(x)

        self.size -= 1
        return True

    # ==================== 遍历操作 ====================
    def inorder(self, node=None, result=None):
        """中序遍历（有序序列）"""
        if node is None:
            node = self.root
        if result is None:
            result = []

        if node != self.NIL:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)

        return result

    def preorder(self, node=None, result=None):
        """前序遍历"""
        if node is None:
            node = self.root
        if result is None:
            result = []

        if node != self.NIL:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

        return result

    def level_order(self):
        """层序遍历"""
        if self.is_empty():
            return []

        from collections import deque
        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            if node != self.NIL:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)

        return result

    # ==================== 可视化 ====================
    def __str__(self):
        if self.is_empty():
            return "Empty Red-Black Tree"

        lines = []
        self._print_tree(self.root, "", True, lines)
        return "\n".join(lines)

    def _print_tree(self, node, prefix, is_last, lines):
        if node == self.NIL:
            return

        color_str = "B" if node.color == BLACK else "R"
        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{node.value}({color_str})")

        new_prefix = prefix + ("    " if is_last else "│   ")

        children = []
        if node.left != self.NIL:
            children.append((node.left, False))
        if node.right != self.NIL:
            children.append((node.right, True))

        for i, (child, _) in enumerate(children):
            is_last_child = (i == len(children) - 1)
            self._print_tree(child, new_prefix, is_last_child, lines)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("红黑树（Red-Black Tree）测试")
    print("=" * 60)

    rbt = RedBlackTree()

    # 插入节点
    print("\n1. 插入节点:")
    values = [7, 3, 18, 10, 22, 8, 11]
    for v in values:
        rbt.insert(v)
        print(f"   插入 {v}: 中序={rbt.inorder()}, 层序={rbt.level_order()}")

    print("\n2. 红黑树结构:")
    print("   (B=黑色, R=红色)")
    print(rbt)

    # 基本信息
    print(f"\n3. 树信息:")
    print(f"   节点数量: {len(rbt)}")
    print(f"   最小节点: {rbt.find_min().value}")
    print(f"   最大节点: {rbt.find_max().value}")

    # 遍历
    print(f"\n4. 遍历结果:")
    print(f"   中序遍历 (有序): {rbt.inorder()}")
    print(f"   前序遍历: {rbt.preorder()}")
    print(f"   层序遍历: {rbt.level_order()}")

    # 查找
    print(f"\n5. 查找操作:")
    print(f"   查找 10: {'找到' if rbt.contains(10) else '未找到'}")
    print(f"   查找 15: {'找到' if rbt.contains(15) else '未找到'}")

    # 删除
    print(f"\n6. 删除操作:")
    rbt.delete(10)
    print(f"   删除 10 后:")
    print(f"   中序: {rbt.inorder()}")
    print(rbt)
