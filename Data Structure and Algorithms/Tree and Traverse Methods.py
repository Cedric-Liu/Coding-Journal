class Node(object):
    """Node"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """Tree"""
    def _init_(self):
        self.root = Node()
        sefl.myQueue = []


