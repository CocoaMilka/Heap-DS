from heap import *

a = Heap()

a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)

node = 5

#print("Parent: ", a.parent(node))
#print("Current Node: ", a.current(node))
#print("Left child value: ", a.left(node))
#print("Right child value: ", a.right(node))

a.printHeap()

a.buildMaxHeap()

print("New heap:")

a.printHeap()

print("Number of elements: ", a.size())

"""
if a.hasLeftChild(node):
    print(str(a.current(node)) + " has a left child")
else:
    print(str(a.current(node)) + " has no left child")
"""

#a.printHeap()
