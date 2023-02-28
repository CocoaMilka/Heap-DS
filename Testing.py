from heap import *

a = Node(1)
b = Node(2)
c = Node(3)

d = Node(4)
e = Node(5)

a.left = b
a.right = c

b.left = d
b.right = e

print("Left child value: ", a.left.value)
print("Right child value: ", a.right.value)

print("Left child value: ", b.left.value)
print("Right child value: ", b.right.value)

h = Heap()

h.root = a

h.PrintHeap(h.root)
