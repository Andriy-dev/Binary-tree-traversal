'''
Bread First Search (BFS):
    We scan through the tree level by level, following the order of height, from top to bottom.
    The nodes on higher level would be visited before the ones with lower levels.
'''

def BFS(root):
    if root is None:
        return
    nodes = [ root ]
    out = []
    while nodes:
        tmp = []
        for node in nodes:
            out.append(node)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        nodes = tmp
    return(out)

