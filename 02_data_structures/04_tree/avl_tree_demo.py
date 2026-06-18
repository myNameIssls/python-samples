"""平衡二叉树（AVL Tree）示例

本文件演示 AVL 树的完整实现：
- AVL 树：最早提出的自平衡二叉搜索树
- 特点：任意节点的左右子树高度差（平衡因子）不超过 1
- 平衡因子：左子树高度 - 右子树高度，范围为 {-1, 0, 1}

平衡调整（旋转操作）：
- LL 型（右旋）：在左子树的左节点上插入
- RR 型（左旋）：在右子树的右节点上插入
- LR 型（左旋+右旋）：在左子树的右节点上插入
- RL 型（右旋+左旋）：在右子树的左节点上插入

时间复杂度：所有操作都是 O(log n)
"""


# ==================== AVL 树节点类 ====================
class AVLNode:
    """AVL 树节点"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1    # 节点高度（叶子节点高度为 1）


# ==================== AVL 树类 ====================
class AVLTree:
    """AVL 树（自平衡二叉搜索树）"""

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __len__(self):
        return self._get_size(self.root)

    def _get_size(self, node):
        if node is None:
            return 0
        return 1 + self._get_size(node.left) + self._get_size(node.right)

    # ==================== 高度相关 ====================
    def _get_height(self, node):
        """获取节点高度"""
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        """更新节点高度"""
        if node is None:
            return
        node.height = 1 + max(
            self._get_height(node.left),
            self._get_height(node.right)
        )

    def _get_balance(self, node):
        """获取节点平衡因子（左子树高度 - 右子树高度）"""
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # ==================== 旋转操作 ====================
    def _right_rotate(self, y):
        """
        右旋（LL 型和 LR 型调整）
        y: 失衡节点
              y                x
             / \              / \
            x   T3   -->     T1  y
           / \                  / \
          T1  T2              T2  T3
        """
        x = y.left
        T2 = x.right

        # 执行旋转
        x.right = y
        y.left = T2

        # 更新高度（注意：先更新 y，再更新 x）
        self._update_height(y)
        self._update_height(x)

        return x    # 返回新的根节点

    def _left_rotate(self, x):
        """
        左旋（RR 型和 RL 型调整）
        x: 失衡节点
            x                y
           / \              / \
          T1  y    -->     x   T3
             / \          / \
            T2  T3       T1  T2
        """
        y = x.right
        T2 = y.left

        # 执行旋转
        y.left = x
        x.right = T2

        # 更新高度
        self._update_height(x)
        self._update_height(y)

        return y    # 返回新的根节点

    def _rebalance(self, node):
        """平衡调整"""
        if node is None:
            return node

        # 更新当前节点高度
        self._update_height(node)

        # 获取平衡因子
        balance = self._get_balance(node)

        # LL 型：右旋
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # LR 型：先左旋后右旋
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # RR 型：左旋
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # RL 型：先右旋后左旋
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # ==================== 插入操作 ====================
    def insert(self, value):
        """插入节点（插入后自动平衡）"""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """递归插入"""
        # 1. 执行标准 BST 插入
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # BST 不允许重复值
            return node

        # 2. 向上回溯时更新高度并平衡
        return self._rebalance(node)

    def _insert_iterative(self, value):
        """迭代插入（更高效）"""
        new_node = AVLNode(value)

        if self.is_empty():
            self.root = new_node
            return

        parent = None
        current = self.root

        # 1. 找到插入位置
        while current:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return    # 不允许重复值

        # 2. 插入节点
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        # 3. 向上回溯平衡
        current = new_node
        while current:
            self._update_height(current)
            balance = self._get_balance(current)

            if abs(balance) > 1:
                current = self._rebalance(current)

                # 更新父节点的指针
                if parent:
                    if current.value < parent.value:
                        parent.left = current
                    else:
                        parent.right = current
                else:
                    self.root = current
                break

            current = parent
            if parent:
                parent = parent.parent if hasattr(parent, 'parent') else None

    # ==================== 查找操作 ====================
    def search(self, value):
        """查找值为 value 的节点"""
        current = self.root

        while current:
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
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    def find_max(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node

    # ==================== 删除操作 ====================
    def delete(self, value):
        """删除节点（删除后自动平衡）"""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """递归删除"""
        if node is None:
            return None

        # 1. 找到要删除的节点
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # 找到目标节点
            # 情况 1：叶子节点
            if node.left is None and node.right is None:
                return None
            # 情况 2：只有一个子节点
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # 情况 3：有两个子节点，用后继替换
            successor = self.find_min(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        # 2. 平衡调整
        return self._rebalance(node)

    # ==================== 遍历操作 ====================
    def inorder(self):
        """中序遍历（有序序列）"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is None:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    def preorder(self):
        """前序遍历"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

    def level_order(self):
        """层序遍历"""
        if self.root is None:
            return []

        from collections import deque
        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    # ==================== 可视化 ====================
    def __str__(self):
        if self.is_empty():
            return "Empty AVL Tree"

        lines = []
        self._print_tree(self.root, "", True, lines)
        return "\n".join(lines)

    def _print_tree(self, node, prefix, is_last, lines):
        if node is None:
            return

        balance = self._get_balance(node)
        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{node.value} (h={node.height}, b={balance})")

        new_prefix = prefix + ("    " if is_last else "│   ")

        children = []
        if node.left:
            children.append((node.left, False))
        if node.right:
            children.append((node.right, True))

        for i, (child, _) in enumerate(children):
            is_last_child = (i == len(children) - 1)
            self._print_tree(child, new_prefix, is_last_child, lines)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("平衡二叉树（AVL Tree）测试")
    print("=" * 60)

    avl = AVLTree()

    # 插入节点（演示平衡过程）
    print("\n1. 依次插入节点，观察平衡调整:")
    values = [10, 20, 30, 40, 50, 25]

    for v in values:
        avl.insert(v)
        print(f"   插入 {v}: 中序={avl.inorder()}, 层序={avl.level_order()}")

    print("\n2. AVL 树结构:")
    print("   (h=高度, b=平衡因子)")
    print(avl)

    # 基本信息
    print(f"\n3. 树信息:")
    print(f"   节点数量: {len(avl)}")
    print(f"   最小节点: {avl.find_min().value}")
    print(f"   最大节点: {avl.find_max().value}")

    # 遍历
    print(f"\n4. 遍历结果:")
    print(f"   中序遍历 (有序): {avl.inorder()}")
    print(f"   前序遍历: {avl.preorder()}")
    print(f"   层序遍历: {avl.level_order()}")

    # 查找
    print(f"\n5. 查找操作:")
    print(f"   查找 30: {'找到' if avl.contains(30) else '未找到'}")
    print(f"   查找 35: {'找到' if avl.contains(35) else '未找到'}")

    # 删除
    print(f"\n6. 删除操作:")
    avl.delete(30)
    print(f"   删除 30 后: {avl.inorder()}")
    print(avl)
