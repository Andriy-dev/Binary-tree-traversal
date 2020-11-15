from collections import deque

def DFSinorder(root):
    traversal_queue = deque()
    result_queue = deque()

    node = root

    while True:

        if node:
            traversal_queue.append(node)
            node = node.left
    
        elif traversal_queue:
            node = traversal_queue.pop()
            result_queue.append(node)

            node = node.right
        else:
            break

    return(result_queue)
