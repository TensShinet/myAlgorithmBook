class MaxHeap:
    def __init__(self):
        self.heap = [None]
        self.length = 0

    def insert(self, e):
        self.length += 1
        self.heap += [e]
        self.bubble_up(self.length)

    def bubble_up(self, idx):
        parent = idx // 2
        while parent > 0 and self.heap[parent] < self.heap[idx]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx, parent = parent, parent // 2

    def delete(self):
        if self.length < 1:
            return None
        minm = self.heap[1]
        self.heap[1],  self.heap[self.length] = self.heap[self.length], self.heap[1]
        self.length -= 1
        self.heap.pop(-1)
        self.bubble_down(1)
        return minm

    def bubble_down(self, idx):
        parent = idx
        child = 2 * idx
        while child <= self.length:
            if child < self.length and self.heap[child] < self.heap[child+1]:
                child += 1
            if self.heap[parent] >= self.heap[child]:
                break
            else:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            parent = child
            child *= 2


def main():
    N = 10000
    h = MaxHeap()

    for i in range(N, 0, -1):
        h.insert(i)

    for i in range(N):
        print(h.delete())

main()