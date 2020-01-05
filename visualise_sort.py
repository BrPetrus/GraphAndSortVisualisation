import random
import tkinter
import time


class VisualiseSort():
    def __init__(self, sorting_algorithm_class, canvas, num=100, dimensions=(400, 400)):
        self.sorting_algorithm_class = sorting_algorithm_class
        self.num = num
        self.dimensions = dimensions
        self.canvas = canvas

        # Generate array
        self.arr = [i for i in range(num)]

        # Shuffle arr
        N = len(self.arr)*100
        for _ in range(N):
            j, k = random.randint(0, num-1), random.randint(0, num-1)
            self.arr[j], self.arr[k] = self.arr[k], self.arr[j]

    def start(self):
        # Run sort function
        self.sorting_algorithm_class = self.sorting_algorithm_class(self.arr)
        self.steps = self.sorting_algorithm_class.heapsort()
        print('[~] Done sorting')
        self.draw()
        self.canvas.after(5000, self.run)

    def run(self):
        if self.steps.empty() is False:
            step = self.steps.get()
            self.arr[step[0]], self.arr[step[1]] = self.arr[step[1]], self.arr[step[0]]
            self.draw()
            self.canvas.after(5, self.run)

    def draw(self):
        self.canvas.delete('all')

        # min max values
        max = self.num-1
        min = 0

        # width of each column
        width = self.dimensions[0]//self.num
        k = self.dimensions[1]/max

        # draw columns
        x = 0
        for value in self.arr:
            self.canvas.create_rectangle(x, self.dimensions[1], x+width, self.dimensions[1]-(k*value), fill='white', width=0)
            x += width
