"""二叉树示例

本文件演示二叉树（Binary Tree）数据结构：
- 二叉树：每个节点最多有两个子节点（左子节点、右子节点）
- 遍历方式：前序、中序、后序（都是深度优先遍历 DFS）

生活类比：组织架构图、族谱
树结构：根（root）在顶部，叶子（leaf）在底部
"""


# ==================== 树节点类（TreeNode）====================
class TreeNode:
    """二叉树的节点"""

    def __init__(self, value):
        # value：节点的值
        self.value = value
        # left：左子节点，初始为 None
        self.left = None
        # right：右子节点，初始为 None
        self.right = None


# ==================== 二叉树类（BinaryTree）====================
class BinaryTree:
    """二叉树类"""

    def __init__(self, root):
        # root：树的根节点
        self.root = TreeNode(root)

    def inorder(self, node, result=None):
        """中序遍历：左子树 -> 根节点 -> 右子树"""
        # result：用于存储遍历结果的列表
        if result is None:
            result = []        # 避免多次调用时共享同一个列表

        if node:
            # 1. 递归遍历左子树
            self.inorder(node.left, result)
            # 2. 访问根节点
            result.append(node.value)
            # 3. 递归遍历右子树
            self.inorder(node.right, result)

        return result

    def preorder(self, node, result=None):
        """前序遍历：根节点 -> 左子树 -> 右子树"""
        if result is None:
            result = []

        if node:
            # 1. 访问根节点
            result.append(node.value)
            # 2. 递归遍历左子树
            self.preorder(node.left, result)
            # 3. 递归遍历右子树
            self.preorder(node.right, result)

        return result

    def postorder(self, node, result=None):
        """后序遍历：左子树 -> 右子树 -> 根节点"""
        if result is None:
            result = []

        if node:
            # 1. 递归遍历左子树
            self.postorder(node.left, result)
            # 2. 递归遍历右子树
            self.postorder(node.right, result)
            # 3. 访问根节点
            result.append(node.value)

        return result


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 构建一棵二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    tree = BinaryTree(1)           # 创建根节点，值为 1
    tree.root.left = TreeNode(2)   # 左子节点，值为 2
    tree.root.right = TreeNode(3)  # 右子节点，值为 3
    tree.root.left.left = TreeNode(4)   # 2 的左子节点
    tree.root.left.right = TreeNode(5)  # 2 的右子节点

    # 测试三种遍历方式
    print(f"中序遍历: {tree.inorder(tree.root)}")   # 左 -> 根 -> 右：4, 2, 5, 1, 3
    print(f"前序遍历: {tree.preorder(tree.root)}")   # 根 -> 左 -> 右：1, 2, 4, 5, 3
    print(f"后序遍历: {tree.postorder(tree.root)}")  # 左 -> 右 -> 根：4, 5, 2, 3, 1
