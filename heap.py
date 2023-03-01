# Man I wish I could do this in C++ >.>

class Node:

    # Member Variables
    left = None
    right = None
    value = None

    # Parameterized Constructor
    def __init__(self, v):
        self.value = v


class Heap:

    # Member Variables
    heap = []
    size = 0

    # Insert element to end of heap
    def Insert(self, x):
        heap.append(x)
        size += 1

    # Removes last element in heap
    def Remove(self):
        heap.pop()
        size -= 1
