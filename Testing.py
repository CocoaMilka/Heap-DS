from heap import *

a = Heap()

a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)

print("Parent: ", a.parent(2))
print("Left child value: ", a.left(2))
print("Right child value: ", a.right(2))

print("Number of elements: ", a.size())

a.printHeap()
