class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        list1 = []
        def dfs(root):
            if not root:
                return

            list1.append(root.val)
            dfs(root.left)
            dfs(root.right)

        list1 = dfs(A)
        # list2 = dfs(B)

        return list1
        # print(list2)
s = Solution()
a = s.isSubStructure()
print(a)
