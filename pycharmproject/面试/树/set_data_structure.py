
from data_structure import BinaryTree,NAryTree,LinkedList
list = [5,4,8,11,None,13,4,7,2,None,None,None,None,1]
# 建立二叉树
def set_BinaryTree(list):
    if not list:
        return []

    temp = []
    root = BinaryTree(list.pop(0))
    mm = root
    temp.append(root)

    while list:
        for _ in range(len(temp)):
            root = temp.pop(0)
            # poplist前首先判断，若list已经为空，直接返回根节点mm
            if list:
                t = list.pop(0)
            else:
                return mm
            left = BinaryTree(t)
            root.left = left
            temp.append(root.left)

            # poplist前首先判断，若list已经为空，直接返回根节点mm
            if list:
                t1 = list.pop(0)
            else:
                return mm
            right = BinaryTree(t1)
            root.right = right
            temp.append(root.right)

    return mm


# 层次遍历二叉树
def bfs_tree(root):
    if not root:
        return []
    list = []
    vals = []

    list.append(root)
    vals.append([root.val])

    while list:
        temp = []
        for _ in range(len(list)):

            root = list.pop(0)
            if root.left:
                list.append(root.left)
                temp.append(root.left.val)

            if root.right:
                list.append(root.right)
                temp.append(root.right.val)
        if temp:
            vals.append(temp)
    return vals


# 前序遍历二叉树(深度优先DFS)
def pre_order_traversal(root):

    if not root:
        return []
    vals = []
    def dfs(root):
        if not root:
            return

        vals.append(root.val)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return vals



# 中遍历二叉树(深度优先DFS)
def InOrdeTraversal(root):

    if not root:
        return []
    vals = []
    def dfs(root):
        if not root:
            return

        dfs(root.left)
        vals.append(root.val)
        dfs(root.right)

    dfs(root)
    return vals



# 后序遍历二叉树(深度优先DFS)
def PostOrderTraversal(root):

    if not root:
        return []
    vals = []
    def dfs(root):
        if not root:
            return

        dfs(root.left)
        dfs(root.right)
        vals.append(root.val)

    dfs(root)
    return vals



"""
list : [1, 2, 3, 4, 5, 6, 7]
list转换为二叉树 : <val:1,left:<val:2,left:<val:4,left:None,right:None>,right:<val:5,left:None,right:None>>,right:<val:3,left:<val:6,left:None,right:None>,right:<val:7,left:None,right:None>>>
层次遍历二叉树,每一行嵌套list : [[1], [2, 3], [4, 5, 6, 7]]
前序遍历二叉树 : [1, 2, 4, 5, 3, 6, 7]
中续遍历二叉树 : [4, 2, 5, 1, 6, 3, 7]
后序遍历二叉树 : [4, 5, 2, 6, 7, 3, 1]
"""



