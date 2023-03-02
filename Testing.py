from heap import *

a = Heap()

a.insert(4)
a.insert(1)
a.insert(3)
a.insert(2)
a.insert(16)
a.insert(9)
a.insert(10)
a.insert(14)
a.insert(8)
a.insert(7)

node = 5

#print("Parent: ", a.parent(node))
#print("Current Node: ", a.current(node))
#print("Left child value: ", a.left(node))
#print("Right child value: ", a.right(node))

a.printHeap()

print("###")

#a.buildMaxHeap()
a.maxHeapSort()

print("Sorted: ")

for i in a.sorted:
    print(i)

#print("New heap:")

#a.printHeap()

print("Number of elements: ", a.size())

"""
if a.hasLeftChild(node):
    print(str(a.current(node)) + " has a left child")
else:
    print(str(a.current(node)) + " has no left child")
"""

#a.printHeap()
