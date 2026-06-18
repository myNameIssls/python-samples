"""二叉树基础示例

本文件演示二叉树（Binary Tree）的基础知识：
- 二叉树：每个节点最多有两个子节点（左子节点、右子节点）
- 树结构：根（root）在顶部，叶子（leaf）在底部

基本概念：
- 根节点（Root）：树的顶层节点
- 子节点（Child）：某个节点下面的节点
- 父节点（Parent）：某个节点上面的节点
- 叶子节点（Leaf）：没有子节点的节点
- 子树（Subtree）：树中的任意节点及其所有后代
"""


# ==================== 二叉树节点类 ====================
class TreeNode:
    """二叉树节点"""

    def __init__(self, value):
        self.value = value      # 节点的值
        self.left = None        # 左子节点
        self.right = None       # 右子节点

    def __repr__(self):
        return f"TreeNode({self.value})"


# ==================== 二叉树类 ====================
class BinaryTree:
    """二叉树类"""

    def __init__(self):
        self.root = None        # 根节点

    def is_empty(self):
        """判断树是否为空"""
        return self.root is None

    def size(self):
        """返回树的节点数量"""
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        """递归计算节点数量"""
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def height(self):
        """返回树的高度（深度）"""
        return self._calc_height(self.root)

    def _calc_height(self, node):
        """递归计算节点高度"""
        if node is None:
            return -1    # 空树高度为 -1，单节点树高度为 0
        return 1 + max(self._calc_height(node.left), self._calc_height(node.right))

    # ==================== 遍历方法 ====================
    def preorder(self):
        """前序遍历（Preorder）：根 -> 左 -> 右"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

    def inorder(self):
        """中序遍历（Inorder）：左 -> 根 -> 右"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is None:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    def postorder(self):
        """后序遍历（Postorder）：左 -> 右 -> 根"""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is None:
            return
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    def level_order(self):
        """层序遍历（Level Order）：按层次从上到下遍历（使用队列）"""
        if self.is_empty():
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

    # ==================== 树的构建 ====================
    def build_from_list(self, values):
        """从列表构建完全二叉树（层序插入）"""
        if not values:
            return

        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 左子节点
            if i < len(values):
                node.left = TreeNode(values[i])
                queue.append(node.left)
                i += 1

            # 右子节点
            if i < len(values):
                node.right = TreeNode(values[i])
                queue.append(node.right)
                i += 1

    def __str__(self):
        """返回树的字符串表示"""
        if self.is_empty():
            return "Empty Tree"

        lines = []
        self._print_tree(self.root, "", True, lines)
        return "\n".join(lines)

    def _print_tree(self, node, prefix, is_last, lines):
        """递归打印树结构"""
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
    from collections import deque

    print("=" * 50)
    print("二叉树基础测试")
    print("=" * 50)

    # 手动构建一棵树
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6

    tree = BinaryTree()
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.right = TreeNode(6)

    # 打印树结构
    print("\n树结构:")
    print(tree)

    # 基本信息
    print(f"\n树信息:")
    print(f"  节点数量: {tree.size()}")
    print(f"  树高度: {tree.height()}")

    # 四种遍历方式
    print(f"\n遍历结果:")
    print(f"  前序遍历 (根-左-右): {tree.preorder()}")
    print(f"  中序遍历 (左-根-右): {tree.inorder()}")
    print(f"  后序遍历 (左-右-根): {tree.postorder()}")
    print(f"  层序遍历 (按层):     {tree.level_order()}")

    # 从列表构建树
    print("\n从列表 [1,2,3,4,5,6,7] 构建的树:")
    tree2 = BinaryTree()
    tree2.build_from_list([1, 2, 3, 4, 5, 6, 7])
    print(tree2)
