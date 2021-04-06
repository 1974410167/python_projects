
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return abs(self.depth(root.left)-self.depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self,root:TreeNode):
        if not root:
            return 0

        return max(self.depth(root.left),self.depth(root.right))+1


