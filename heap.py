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
    root = None
    size = 0

    def Insert(self, r):
        if root == None:
            root = r

    def PrintHeap(self, r):

        if r.left != None:
            print(r.left.value)

        if r.right != None:
            print(r.right.value)

        # def Heapify(self):
        # Heapify
