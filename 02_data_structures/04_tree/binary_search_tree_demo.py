"""二叉搜索树（Binary Search Tree）示例

本文件演示二叉搜索树（BST）的完整实现：
- 二叉搜索树：左子树所有节点 < 根节点 < 右子树所有节点
- 特点：查找、插入、删除的平均时间复杂度为 O(log n)
- 应用：快速查找、有序数据存储、字典树

基本操作：
- 插入、查找、删除
- 找最小值、找最大值
- 前驱、后继
"""


# ==================== 二叉搜索树节点类 ====================
class BSTNode:
    """二叉搜索树节点"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None    # 父节点指针，方便删除操作

    def __repr__(self):
        return f"BSTNode({self.value})"


# ==================== 二叉搜索树类 ====================
class BinarySearchTree:
    """二叉搜索树类"""

    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.root is None

    def __len__(self):
        return self.size

    # ==================== 查找操作 ====================
    def search(self, value):
        """
        查找值为 value 的节点
        返回值：找到返回节点，未找到返回 None
        """
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
        """判断树中是否包含值为 value 的节点"""
        return self.search(value) is not None

    # ==================== 插入操作 ====================
    def insert(self, value):
        """插入值为 value 的节点"""
        new_node = BSTNode(value)

        if self.is_empty():
            self.root = new_node
            self.size += 1
            return new_node

        current = self.root

        while True:
            if value < current.value:
                # 插入到左子树
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                # 插入到右子树（注意：BST 允许重复值插入右子树）
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right

        self.size += 1
        return new_node

    # ==================== 查找极值 ====================
    def find_min(self, node=None):
        """查找最小节点（最左边的节点）"""
        if node is None:
            node = self.root

        if node is None:
            return None

        while node.left:
            node = node.left

        return node

    def find_max(self, node=None):
        """查找最大节点（最右边的节点）"""
        if node is None:
            node = self.root

        if node is None:
            return None

        while node.right:
            node = node.right

        return node

    def find_min_node(self):
        """返回树的最小节点"""
        return self.find_min(self.root)

    def find_max_node(self):
        """返回树的最大节点"""
        return self.find_max(self.root)

    # ==================== 删除操作 ====================
    def delete(self, value):
        """
        删除值为 value 的节点
        三种情况：
        1. 叶子节点：直接删除
        2. 只有一个子节点：用子节点替代
        3. 有两个子节点：用后继节点替代
        """
        node = self.search(value)

        if node is None:
            return False    # 未找到

        # 获取待删除节点的父节点
        parent = node.parent

        # 情况 1：叶子节点
        if node.left is None and node.right is None:
            self._replace_child(parent, node, None)

        # 情况 2a：只有右子节点
        elif node.left is None:
            self._replace_child(parent, node, node.right)

        # 情况 2b：只有左子节点
        elif node.right is None:
            self._replace_child(parent, node, node.left)

        # 情况 3：有两个子节点
        else:
            # 找到后继节点（右键树的最小节点）
            successor = self.find_min(node.right)
            successor_value = successor.value

            # 递归删除后继节点
            self.delete(successor.value)

            # 用后继节点的值替换当前节点
            node.value = successor_value

        self.size -= 1
        return True

    def _replace_child(self, parent, old_child, new_child):
        """将父节点的子节点替换"""
        if parent is None:
            self.root = new_child
        elif parent.left == old_child:
            parent.left = new_child
        else:
            parent.right = new_child

        if new_child:
            new_child.parent = parent

    # ==================== 前驱与后继 ====================
    def predecessor(self, value):
        """查找值为 value 的节点的前驱（中序遍历中的前一个节点）"""
        node = self.search(value)
        if node is None:
            return None

        # 情况 1：有左子树，前驱是左子树的最大节点
        if node.left:
            return self.find_max(node.left)

        # 情况 2：没有左子树，沿父节点向上找
        current = node
        while current.parent:
            if current.parent.right == current:
                return current.parent
            current = current.parent

        return None

    def successor(self, value):
        """查找值为 value 的节点的后继（中序遍历中的后一个节点）"""
        node = self.search(value)
        if node is None:
            return None

        # 情况 1：有右子树，后继是右子树的最小节点
        if node.right:
            return self.find_min(node.right)

        # 情况 2：没有右子树，沿父节点向上找
        current = node
        while current.parent:
            if current.parent.left == current:
                return current.parent
            current = current.parent

        return None

    # ==================== 遍历操作 ====================
    def inorder(self):
        """中序遍历（得到有序序列）"""
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

    def postorder(self):
        """后序遍历"""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is None:
            return
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    # ==================== 可视化 ====================
    def __str__(self):
        if self.is_empty():
            return "Empty BST"

        lines = []
        self._print_tree(self.root, "", True, lines)
        return "\n".join(lines)

    def _print_tree(self, node, prefix, is_last, lines):
        if node is None:
            return

        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{node.value}")

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
    print("=" * 50)
    print("二叉搜索树（Binary Search Tree）测试")
    print("=" * 50)

    bst = BinarySearchTree()

    # 插入节点
    print("\n1. 插入节点: 50, 30, 70, 20, 40, 60, 80")
    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)
    print(bst)

    # 基本信息
    print(f"\n2. 树信息:")
    print(f"   节点数量: {len(bst)}")
    print(f"   最小节点: {bst.find_min_node().value}")
    print(f"   最大节点: {bst.find_max_node().value}")

    # 遍历
    print(f"\n3. 遍历结果:")
    print(f"   中序遍历 (有序): {bst.inorder()}")
    print(f"   前序遍历: {bst.preorder()}")
    print(f"   后序遍历: {bst.postorder()}")

    # 查找
    print(f"\n4. 查找操作:")
    print(f"   查找 40: {'找到' if bst.contains(40) else '未找到'}")
    print(f"   查找 45: {'找到' if bst.contains(45) else '未找到'}")

    # 前驱与后继
    print(f"\n5. 前驱与后继:")
    print(f"   节点 50 的前驱: {bst.predecessor(50).value if bst.predecessor(50) else 'None'}")
    print(f"   节点 50 的后继: {bst.successor(50).value if bst.successor(50) else 'None'}")

    # 删除
    print(f"\n6. 删除操作:")
    print(f"   删除前 (中序): {bst.inorder()}")
    bst.delete(30)    # 删除有两个子节点的节点
    print(f"   删除 30 后 (中序): {bst.inorder()}")
    print(bst)
