from collections import deque

def DFSpost_recursively(root):

    if root:
        left = []
        right = []
        if root.left:
            left = DFSpost_recursively(root.left)
        if root.right:
            right = DFSpost_recursively(root.right)
        return ( left + right + [root] )
    else:
        return ( [] )
