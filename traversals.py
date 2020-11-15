from def_tree import Node
from def_tree import print_tree
from collections import deque
from BFS import BFS
from DFSpre import DFSpre
from DFSpost import DFSpost
from DFSinorder_recursively import DFSinorder_recursively
from DFSinorder import DFSinorder
from DFSpre_recursively import DFSpre_recursively
from DFSpost_recursively import DFSpost_recursively

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)


print_tree(root)

print("BFS traversal             ",[ node.data for node in BFS(root)                   ],"expected 4 2 6 1 3 5 7")

print("DFS preorder              ",[ node.data for node in DFSpre(root)                ],"expected 4 2 1 3 6 5 7")
print("DFS preorder recursively  ",[ node.data for node in DFSpre_recursively(root)    ],"expected 4 2 1 3 6 5 7")

print("DFS postorder             ",[ node.data for node in DFSpost(root)               ],"expected 1 3 2 5 7 6 4")
print("DFS postorder recursively ",[ node.data for node in DFSpost_recursively(root)   ],"expected 1 3 2 5 7 6 4")

print("DFS inorder               ",[ node.data for node in DFSinorder(root)            ],"expected 1 2 3 4 5 6 7") 
print("DFS inorder recursively   ",[ node.data for node in DFSinorder_recursively(root)],"expected 1 2 3 4 5 6 7")


