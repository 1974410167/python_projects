list = [5,4,8,11,0,13,4,7,2,0,0,0,0,1]

from set_data_structure import set_BinaryTree

tree = set_BinaryTree(list)


def hasPathSum(root, sum):
    if not root:
        return False
    list = []
    list.append(root)
    while list:
        for _ in range(len(list)):
            root = list.pop(0)
            if root.left:
                list.append(root.left)
                root.left.val += root.val
            if root.right:
                list.append(root.right)
                root.right.val += root.val
            if not root.right and root.left and root.val == sum:
                return True
    return False

q = hasPathSum(tree,22)
print(q)