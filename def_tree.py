class Node():
    def __init__(self,n=None):
        self.data = n
        self.left = None
        self.right = None

def print_tree(root):
    if root is None:
        return None
    nodes = [root]
    final_out = []
    while nodes:
        tmp = []
        out = []
        for node in nodes:
            if node:
                if node.left:
                    tmp.append(node.left)
                else:
                    tmp.append(None)
                if node.right:
                    tmp.append(node.right)
                else:
                    tmp.append(None)
                out.append(str(node.data).center(3))
            else:
                out.append(" . ")
        if any(nodes):
            final_out.append(" ".join(out))
        nodes = tmp
    max_len = len(final_out[-1])
    for s in final_out:
        print(s.center(max_len))
