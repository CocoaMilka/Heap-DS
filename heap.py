# Man I wish I could do this in C++ >.>

import math


class Heap:

    # Member Variables
    heap = []
    numElements = 0

    sorted = []

    def __init__(self, array):
        for i in array:
            self.insert(i)

    # Insert element to end of heap
    def insert(self, x):
        self.heap.append(x)
        self.numElements += 1

    # Removes last element in heap
    def remove(self):
        self.heap.pop()
        self.numElements -= 1

    def hasLeftChild(self, x):
        if (2 * x) + 1 > self.numElements:
            return False;
        return True;

    def hasRightChild(self, x):
        if (2 * x) + 2 > self.numElements:
            return False;
        return True;

    # Operators

    def maxHeapify(self, x):

        left = self.getLeftIndex(x)
        right = self.getRightIndex(x)

        if (left < self.numElements) and (self.heap[left] > self.heap[x]):
            largest = left
        else:
            largest = x
        if (right < self.numElements) and (self.heap[right] > self.heap[largest]):
            largest = right
        if largest != x:

            # Funky swapping magic syntax
            self.heap[x], self.heap[largest] = self.heap[largest], self.heap[x]

            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(math.floor(self.numElements / 2), -1, -1):
            self.maxHeapify(i)

    def maxHeapSort(self):
        self.buildMaxHeap()

        for i in range(self.numElements - 1, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.numElements -= 1
            self.maxHeapify(0)

            self.sorted.insert(0, self.heap[i])

    # Accessors
    def current(self, x):
        return self.heap[x]

    def parent(self, x):
        return self.heap[math.floor((x - 1) / 2)]

    # Return value of Children

    def left(self, x):
        return self.heap[(2 * x) + 1]

    def right(self, x):
        return self.heap[(2 * x) + 2]

    def size(self):
        return self.numElements

    # Return Index of Children

    def getLeftIndex(self, x):
        return (2 * x) + 1

    def getRightIndex(self, x):
        return (2 * x) + 2

    def printHeap(self):
        for i in range(self.numElements):
            print(self.heap[i])
