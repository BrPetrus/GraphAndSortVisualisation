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
