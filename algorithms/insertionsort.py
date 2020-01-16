from . import sort


class InsertionSort(sort.Sort):
    def __init__(self, array):
        super().__init__(array)

    def sort(self):
        for step in range(1, len(self.array)):
            key = self.array[step]
            j = step - 1
            while j >= 0 and key < self.array[j]:
                self.swap(j, j+1)
                j -= 1
            #arr[j+1] = key
        return self.steps


def insertionsort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    arr = [6, 3, 2, 1, 8]
    insertionsort(arr)
    print(arr)
