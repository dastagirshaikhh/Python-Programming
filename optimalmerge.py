# class Heap():
#     def __init__(self):
#         self.h = []
#     def parent(self, index):
#         if index > 0:
#             return (index - 1) // 2
#     def lchild(self, index):
#         return (2 * index) + 1
#     def rchild(self, index):
#         return (2 * index) + 2
#     def addItem(self, item):
#         self.h.append(item)
#         if len(self.h) == 1:
#             return
#         index = len(self.h) - 1
#         parent = self.parent(index)
#         while index > 0 and item < self.h[parent]:
#             self.h[index], self.h[parent] = self.h[parent], self.h[index]
#             index = parent
#             parent = self.parent(index)
#     def deleteItem(self):
#         length = len(self.h)
#         self.h[0], self.h[length-1] = self.h[length-1], self.h[0]
#         deleted = self.h.pop()
#         self.moveDownHeapify(0)
#         return deleted
#     def moveDownHeapify(self, index):
#         lc, rc = self.lchild(index), self.rchild(index)
#         length, smallest = len(self.h), index
#         if lc < length and self.h[lc] <= self.h[smallest]:
#             smallest = lc
#         if rc < length and self.h[rc] <= self.h[smallest]:
#             smallest = rc
#         if smallest != index:
#             self.h[smallest], self.h[index] = self.h[index], self.h[smallest]
#         self.moveDownHeapify(smallest)
#     def increaseItem(self, index, value):
#         if value <= self.h[index]:
#             return 
#         self.h[index] = value
#         self.moveDownHeapify(index)
# class OptimalMergePattern():
#     def __init__(self, n, items):
#         self.n = n
#         self.items = items
#         self.heap = Heap()
#     def optimalMerge(self):
#         if self.n <= 0:
#             return 0
#         if self.n == 1:
#             return self.items[0]
#         for _ in self.items:
#             self.heap.addItem(_)
#         count = 0
#         while len(self.heap.h) != 1:
#             tmp = self.heap.deleteItem()
#             count += (tmp + self.heap.h[0])
#             self.heap.increaseItem(0, tmp + self.heap.h[0])
#         return count
# if __name__ == '__main__':
#     OMP = OptimalMergePattern(15, [12, 13, 14, 15, 16, 17])
#     ans = OMP.optimalMerge()
#     print(ans)


# Practical 9.1
# Implementation of Optimal Merge Pattern
class Heap():
    def __init__(self):
        self.h = []
    def parent(self, index):
        if index > 0:
            return (index - 1) // 2
    def lchild(self, index):
        return (2 * index) + 1
    def rchild(self, index):
        return (2 * index) + 2
    def addItem(self, item):
        self.h.append(item)
        if len(self.h) == 1:
            return
        index = len(self.h) - 1
        parent = self.parent(index)
        while index > 0 and item < self.h[parent]:
            self.h[index], self.h[parent] = self.h[parent], item
            index = parent
            parent = self.parent(index)
    def deleteItem(self):
        length = len(self.h)
        self.h[0], self.h[length-1] = self.h[length-1], self.h[0]
        deleted = self.h.pop()
        self.moveDownHeapify(0)
        return deleted
    def moveDownHeapify(self, index):
        lc, rc = self.lchild(index), self.rchild(index)
        length, smallest = len(self.h), index
        if lc < length and self.h[lc] <= self.h[smallest]:
            smallest = lc
        if rc < length and self.h[rc] <= self.h[smallest]:
            smallest = rc
        if smallest != index:
            self.h[smallest], self.h[index] = self.h[index], self.h[smallest]
            self.moveDownHeapify(smallest)
heapObj = Heap()
heapObj.addItem(3)
heapObj.addItem(4)
heapObj.addItem(9)
heapObj.addItem(5)
heapObj.addItem(2)
print(heapObj.deleteItem())
print(heapObj.deleteItem())
print(heapObj.deleteItem())
