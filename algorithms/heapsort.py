from . import sort


class HeapSort(sort.Sort):
    def __init__(self, array):
        super().__init__(array)

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

    def _build_heap(self, n):
        i = len(self.array)//2-1
        while i > -1:
            self.heapify(n, i)
            i -= 1

    def sort(self):
        # build a max-heap
        self._build_heap(len(self.array))
        n = len(self.array)
        for i in range(n-1, -1, -1):
            self.swap(0, i)
            self.heapify(i, 0)
        return self.steps  # returns the steps


if __name__ == "__main__":
    arr = [1, 4, 2, 5, 3]
    print(arr)
    hs = HeapSort(arr)
    print(hs.sort())
    print(hs.array)
