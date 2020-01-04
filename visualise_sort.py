import threading
import random


class VisualiseSort():
    def __init__(self, sorting_algorithm_class):
        self.threadLock = threading.Lock()
        self.sorting_algorithm_class = sorting_algorithm_class

        # Generate array
        self.arr = [i for i in range(10)]

        # Shuffle array
        N = 5
        for i in range(N):
            j, k = random.randint(0, 9), random.randint(0, 9)
            self.arr[j], self.arr[k] = self.arr[k], self.arr[j]

    def run(self):
        # Run sort function
        self.thread = self.sorting_algorithm_class(self.threadLock, self.arr)
        self.thread.start()
        print(type(self.thread))

        while self.thread.isAlive():
            # self.threadLock.acquire()
            # self.thread.join()
            self.threadLock.acquire()
            print('Drawin')
            self.thread.release()
            print(self.thread.array)


        print('[~] Done sorting')
        # print(self.arr)

    def draw(self):
        pass
