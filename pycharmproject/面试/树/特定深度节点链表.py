from set_data_structure import set_BinaryTree
from data_structure import LinkedList as ListNode,BinaryTree as TreeNode

s = [1,2,3,4,5,None,7,8]
tree = set_BinaryTree(s)

print(tree)

class Solution:
    def listOfDepth(self, tree):
        if not tree:
            return []
        list1 = [tree]
        x = ListNode(tree.val)
        vals = [[x]]
        while list1:
            L = len(list1)
            temp = []
            for _ in range(L):

                root = list1.pop(0)

                if root.left:
                    temp.append(root.left.val)
                    list1.append(root.left)

                if root.right:
                    temp.append(root.right.val)
                    list1.append(root.right)

            head = ListNode(None)
            cur = head
            while temp:
                cur.next = ListNode(temp.pop(0))
                cur = cur.next
            if head.next:
                vals.append(head.next)

        return vals
q = Solution()
q1 = q.listOfDepth(tree)
print(q1)