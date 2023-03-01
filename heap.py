# Man I wish I could do this in C++ >.>

import math


class Heap:

    # Member Variables
    heap = []
    numElements = 0

    # Insert element to end of heap
    def insert(self, x):
        self.heap.append(x)
        self.numElements += 1

    # Removes last element in heap
    def remove(self):
        self.heap.pop()
        self.numElements -= 1

    # Accessors
    def parent(self, x):
        return self.heap[math.floor((x - 1) / 2)]

    def left(self, x):
        return self.heap[(2 * x) + 1]

    def right(self, x):
        return self.heap[(2 * x) + 2]

    def size(self):
        return self.numElements

    def printHeap(self):
        for i in range(self.numElements):
            if i == 0:
                print(self.heap[i])
            print(str(self.left(i)) + " " + str(self.right(i)))
