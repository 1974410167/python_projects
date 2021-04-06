


class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f"<val:{self.val},left:{self.left},right:{self.right}>"


class NAryTree:
    """
    children is a list
    """
    def __init__(self,val):
        self.val = val
        self.children = None

class LinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None


