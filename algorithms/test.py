import heapsort as hs
import quicksort as qs
import insertionsort as ins
import random
import time

start = time.time()
n = random.randrange(0, 100000)
arr = [random.randrange(0, 100000) for x in range(n)]
arr1 = arr.copy()  # Heapsort
arr2 = arr.copy()  # Quicksort with random pivot
arr3 = arr.copy()  # Quicksort with fixed pivot
arr4 = arr.copy()  # Insertion sort
print("[~] Generating {:} numbers took {:} s".format(n, time.time()-start))

start = time.time()
hs.heapsort(arr1)
print("[~] Heapsort took {:} s".format(time.time()-start))

start = time.time()
qs.quicksort(arr2, 0, len(arr2)-1, True)
print("[~] Quicksort with random pivot took {:} s".format(time.time()-start))

start = time.time()
qs.quicksort(arr3, 0, len(arr2)-1)
print("[~] Quicksort took {:} s".format(time.time()-start))

start = time.time()
ins.insertionsort(arr4)
print("[~] Insertion sort took {:} s".format(time.time()-start))
