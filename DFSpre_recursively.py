from collections import deque

def DFSpre_recursively(root):

    if root:
        left = []
        right = []
        if root.left:
            left = DFSpre_recursively(root.left)
        if root.right:
            right = DFSpre_recursively(root.right)
        return ( [root] + left + right )
    else:
        return ( [] )
