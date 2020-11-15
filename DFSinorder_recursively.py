from collections import deque

def DFSinorder_recursively(root):

    if root:
        left = []
        right = []
        if root.left:
            left = DFSinorder_recursively(root.left)
        if root.right:
            right = DFSinorder_recursively(root.right)
        return ( left + [root] + right )
    else:
        return ( [] )
