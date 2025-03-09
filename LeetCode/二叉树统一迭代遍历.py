from typing import Optional


# 节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点的值
        self.left = left  # 节点的左孩子
        self.right = right  # 节点的右孩子


# 前序遍历：中、左、右
def preordertraversal(root: Optional[TreeNode]) -> list[int]:
    if not root:  # 当根节点为空时，直接返回
        return []

    stack = [root]  # 栈结构：保存遍历过程的节点
    result = []  # 最终输出的遍历顺序

    while stack:  # 当栈不为空时，继续遍历
        node = stack.pop()  # 出栈一个节点
        if node:  # 该节点不为空时，加入其孩子节点。由于栈是先进后出，所以要先将右节点入栈，然后是左节点，最后是中间节点
            if node.right:
                stack.append(node.right)  # 右边节点入栈，
            if node.left:
                stack.append(node.left)  # 左边节点入栈
            stack.append(node)  # 中间节点入栈
            stack.append(None)  # 标志：遇见None就说明出栈中间节点了
        else:  # 该节点为空，再出栈一个元素，并将其加入到最终的result中
            node = stack.pop()
            result.append(node.val)

    return result


# 中序遍历：左、中、右
def inordertraversal(root: Optional[TreeNode]) -> list[int]:
    if not root:  # 当根节点为空时，直接返回
        return []

    stack = [root]  # 栈结构：保存遍历过程的节点
    result = []  # 最终输出的遍历顺序

    while stack:  # 当栈不为空时，继续遍历
        node = stack.pop()  # 出栈一个节点
        if node:  # 该节点不为空时，加入其孩子节点。此处是中序遍历，所以要换一下加入栈的顺序。所以要先将右节点入栈，然后是中间节点，最后是左节点。
            if node.right:
                stack.append(node.right)  # 右节点入栈
            stack.append(node)  # 中间节点入栈
            stack.append(None)  # 标志：遇见None就说明出栈中间节点了
            if node.left:
                stack.append(node.left)  # 左结点入栈
        else:  # 该节点为空，再出栈一个元素，并将其加入到最终的result中
            node = stack.pop()
            result.append(node.val)
    return result


# 后序遍历：左、右、中
def postordertraversal(root: Optional[TreeNode]) -> list[int]:
    if not root:  # 当根节点为空时，直接返回
        return []

    stack = [root]  # 栈结构：保存遍历过程的节点
    result = []  # 最终输出的遍历顺序

    while stack:  # 当栈不为空时，继续遍历
        node = stack.pop()  # 出栈一个节点
        if node:  # 该节点不为空时，加入其孩子节点。此处是后序遍历，所以要换一下加入栈的顺序。所以要先将中间节点入栈，然后是右节点，最后是左节点。
            stack.append(node)  # 中间节点入栈
            stack.append(None)  # 标志：遇见None就说明出栈中间节点了

            if node.right:
                stack.append(node.right)  # 右节点入栈
            if node.left:
                stack.append(node.left)  # 左结点入栈
        else:  # 该节点为空，再出栈一个元素，并将其加入到最终的result中
            node = stack.pop()
            result.append(node.val)
    return result

"""
颜色标记法，也可以进行统一迭代遍历：
    使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
    如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
    如果遇到的节点为灰色，则将节点的值输出。
    https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/25220/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
"""

if __name__ == "__main__":
    # 这里手动创建一棵树
    tree_list = [0, 1, 2, 3, 4]

    root = TreeNode(tree_list[0])  # 节点1
    node_1 = TreeNode(tree_list[1])  # 节点2
    node_2 = TreeNode(tree_list[2])  # 节点3
    node_3 = TreeNode(tree_list[3])  # 节点4
    node_4 = TreeNode(tree_list[4])  # 节点5

    root.left, root.right = node_1, node_2
    node_1.left, node_1.right = node_3, node_4

    # 前序遍历
    pre_result = preordertraversal(root)
    print("前序遍历结果：", pre_result)

    # 中序遍历
    in_result = inordertraversal(root)
    print("中序遍历结果：", in_result)

    # 前序遍历
    post_result = postordertraversal(root)
    print("后序遍历结果：", post_result)