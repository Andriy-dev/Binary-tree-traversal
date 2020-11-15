from collections import deque

def DFSpre(root):
    traversal_queue = deque()
    result_queue = deque()
    traversal_queue.append(root)

    while traversal_queue:
        node = traversal_queue.pop()
        result_queue.appendleft(node)
        if node.right:
             traversal_queue.append(node.right)            
        if node.left:
            traversal_queue.append(node.left)

    return(reversed(result_queue))
