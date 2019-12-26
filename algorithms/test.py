import heapsort as hs
import random

n = random.randrange(0, 1000000)
arr = [x for x in range(n)]

hs.heapsort(arr)
#print(arr)
