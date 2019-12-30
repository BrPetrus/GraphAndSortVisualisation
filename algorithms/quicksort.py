import random


def quicksort(arr, p, r, rand=False):
    if p < r:
        if rand:
            q = partition_rand(arr, p, r)
        else:
            q = partition(arr, p, r)    # partition
        quicksort(arr, p, q-1)      # sort left
        quicksort(arr, q+1, r)      # sort right


def partition(arr, p, r):
    x = arr[r]  # pivot's value
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]  # put pivot into the correct position
    return i+1


def partition_rand(arr, p, r):
    piv = random.randrange(p, r)  # choose pivot randomly
    arr[piv], arr[r] = arr[r], arr[piv]  # exchange with the last element
    x = arr[r]  # pivot's value
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]  # put pivot into the correct position
    return i+1


if __name__ == "__main__":
    arr = [2, 1, 3, 4, 8, 5]
    quicksort(arr, 0, 5)
    print(arr)
