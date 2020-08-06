import random
from . import sort


class Quicksort(sort.Sort):
    def __init__(self, array):
        super().__init__(array)

    def sort(self):
        self.quicksort(0, len(self.array)-1)
        return self.steps

    def quicksort(self, p, r):
        if p < r:
            q = self.partition(p, r)    # partition
            self.quicksort(p, q-1)      # sort left
            self.quicksort(q+1, r)      # sort right

    def partition(self, p, r):
        x = self.array[r]  # pivot's value
        i = p-1
        for j in range(p, r):
            if self.array[j] <= x:
                i += 1
                self.swap(i, j)
        self.swap(i+1, r)
        return i+1


class Quicksort_random(Quicksort):
    def __init__(self, array):
        super().__init__(array)

    def partition(self, p, r):
        piv = random.randrange(p, r)  # choose pivot randomly
        # exchange with the last element
        self.swap(piv, r)
        x = self.array[r]  # pivot's value
        i = p-1
        for j in range(p, r):
            if self.array[j] <= x:
                i += 1
                self.swap(i, j)
        # put pivot into the correct position
        self.swap(i+1, r)
        return i+1


if __name__ == "__main__":
    arr = [2, 1, 3, 4, 8, 5]
    quicksort(arr, 0, 5)
    print(arr)
