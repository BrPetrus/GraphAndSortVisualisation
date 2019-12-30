def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapify(arr, n, i):
    largest = i
    l = 2*i+1   # left child
    r = 2*i+2   # right child

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)


def build_heap(arr, n):
    i = len(arr)//2-1
    while i > -1:
        heapify(arr, n, i)
        i -= 1


def heapsort(arr):
    # build a max-heap
    build_heap(arr, len(arr))
    n = len(arr)
    for i in range(n-1, -1, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [1, 4, 2, 5, 3]
    print(arr)
    heapsort(arr)
    print(arr)
