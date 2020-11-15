from collections import deque

def DFSpost(root):
    traversal_queue = deque()
    result_queue = deque()
    traversal_queue.append(root)

    while traversal_queue:
        node = traversal_queue.pop()
        result_queue.append(node)
        if node.left:
            traversal_queue.append(node.left)
        if node.right:
            traversal_queue.append(node.right)

    return(reversed(result_queue))
