# 从上到下打印二叉树，每一层打印一行
from 平衡二叉树 import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        list = []
        vals = []
        if not root:
            return list
        list.append(root)
        vals.append([root.val])
        while list:
                temp = []
                for i in range(len(list)):
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