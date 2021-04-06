
# from data_structure import BinaryTree
# from set_data_structure import set_BinaryTree
# s = [1,2,2,3,4,4,3]
#
# tree = set_BinaryTree(s)
# print(tree)
#
# class Solution:
#     def isSymmetric(self, root: BinaryTree) -> bool:
#
#         if not root:
#             return True
#
#         result = [root]
#         while result:
#             l = len(result)
#             stack = []
#             for i in range(l):
#                 root = result.pop(0)
#                 list = [root.left,root.right]
#                 for root in list:
#                     if root:
#                         result.append(root)
#                         val = root.val
#                         if stack and stack[-1] == val:
#                             stack.pop()
#                         else:
#                             stack.append(val)
#                     else:
#                         val = None
#                         if stack and stack[-1] == val:
#                             stack.pop()
#                         else:
#                             stack.append(val)
#
#             if len(stack)!=0:
#                 return False
#         return True
#
# q = Solution()
# a = q.isSymmetric(tree)
# print(a)


Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class auxiliary():
    def __init__(self, val, side):
        self.val = val
        self.side = side


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        res = [root]

        while root:

            temp = []
            k = len(res)

            for _ in range(k):
                root = res.pop(0)
                if root.left:
                    res.append(root.left)
                    t = auxiliary(root.left.val, "l")
                    temp.append(t)

                if root.right:
                    res.append(root.right)
                    t = auxiliary(root.right.val, "r")
                    temp.append(t)

            while temp:
                temp_len = len(temp)
                if temp_len == 1:
                    return False

                temp_r = temp_len - 1
                temp_l = 0
                if temp[temp_l].val == temp[temp_r].val and temp[temp_l].side != temp[temp_r].side:
                    continue
                else:
                    return False
        return True