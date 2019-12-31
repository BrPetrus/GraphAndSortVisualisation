import threading


class HeapSort(threading.Thread):
    def __init__(self, threadID, name, canvas, array):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.canvas = canvas
        self.array = array

    def run(self):
        pass

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def heapify(self, n, i):
        largest = i
        left = 2*i+1   # left child
        right = 2*i+2   # right child

        if left < n and self.array[left] > self.array[largest]:
            largest = left
        if right < n and self.array[right] > self.array[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapify(n, largest)

    def build_heap(self, n):
        i = len(self.array)//2-1
        while i > -1:
            self.heapify(n, i)
            i -= 1

    def heapsort(self):
        # build a max-heap
        self.build_heap(len(self.array))
        n = len(self.array)
        for i in range(n-1, -1, -1):
            self.swap(0, i)
            self.heapify(i, 0)


if __name__ == "__main__":
    arr = [1, 4, 2, 5, 3]
    print(arr)
    hs = HeapSort(0, 'Heapsort', None, arr)
    hs.heapsort()
    print(arr)
