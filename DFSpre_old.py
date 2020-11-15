from collections import deque

def DFSpre(root):
    left_queue = deque()
    right_queue = deque()
    left_queue.append(root)
    result=[]

    while left_queue or right_queue:
        if left_queue:
            node = left_queue.pop()
            result.append(node.data)
            if node.left:
                left_queue.append(node.left)
            if node.right:
                right_queue.append(node.right)
        else:
            node = right_queue.pop()
            result.append(node.data)
            if node.left:
                left_queue.append(node.left)
            if node.right:
                right_queue.append(node.right)
    return(result)
