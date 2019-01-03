"""
Heap Data Structure
heap is essentially an array-like binary search tree
each parent has two children and children always are greater/smaller (follow some rules) than the parent
the heap data structure is filled in order
parent "i" has two children "2i + 1" and "2i + 2"
get the root node: move the last item to the root and check if the heap property is still conserved or not
"""
import heapq
# the library is also an implementation of heap data structure

CAPACITY = 10


class Heap:
    def __init__(self):
        self.heap = [0] * CAPACITY
        self.heap_size = 0

    def insert(self, data):
        if self.heap_size == CAPACITY:
            return
        self.heap[self.heap_size] = data
        self.heap_size += 1
        self.fixup(self.heap_size - 1)

    def fixup(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] < self.heap[index]:
            self.swap(parent_index, index)
            self.fixup(parent_index)

    def swap(self, parent_index, index):
        self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]

    def get_max(self):
        return self.heap[0]

    def poll(self):
        max = self.get_max()
        self.swap(0,self.heap_size-1)
        self.heap_size -= 1
        self.fixdown(0)
        return max

    def fixdown(self,index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if left < self.heap_size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < self.heap_size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(largest,index)
            self.fixdown(largest)

    def heap_sort(self):
        size = self.heap_size
        for i in range(size):
            max = self.poll()
            print(max)

if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)
    heap.insert(10)
    heap.insert(40)
    heap.insert(30)
    heap.insert(41)
    heap.insert(42)

    print(heap.heap)
    heap.heap_sort()