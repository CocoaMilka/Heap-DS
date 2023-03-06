from heap import *

array = [1, 7, 8, 9, 10, 12, 5, 1, 5, 2, 5, 7, 12, 19]

a = Heap(array)

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

#a.printHeap()
