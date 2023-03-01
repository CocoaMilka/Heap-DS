from heap import *

a = Node(1)

b = Node(2)
c = Node(3)

d = Node(4)
e = Node(5)

f = Node(6)
g = Node(7)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

print("Left child value: ", a.left.value)
print("Right child value: ", a.right.value)

print("Left child value: ", b.left.value)
print("Right child value: ", b.right.value)

h = Heap()

h.root = a

h.PrintHeap(h.root)
