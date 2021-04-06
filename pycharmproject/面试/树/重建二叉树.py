
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val



class Solution:

    def buildTree(self, preorder, inorder):
        if inorder:

            ind = inorder.index(preorder.pop(0))

            root = TreeNode(inorder[ind])

            root.left = self.buildTree(preorder, inorder[0:ind])

            root.right = self.buildTree(preorder, inorder[ind + 1:])

            return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

s = Solution()
a = s.buildTree(preorder,inorder)
print(a)



class Solution:

    def buildTree(self, preorder, inorder):

        if preorder:
            index = inorder.index(preorder.pop(0))

            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder,inorder[:index])
            root.right = self.buildTree(preorder,inorder[index:])

            return root