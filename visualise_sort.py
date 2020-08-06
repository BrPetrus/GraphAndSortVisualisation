import random
import tkinter


class VisualiseSort():
    def __init__(self, sort_classes, sort_classes_names, root, num, dimensions, delay):
        self.num = num
        self.dimensions = dimensions
        self.root = root
        self.delay = delay

        # Generate array
        self.arr = [i for i in range(num)]

        # Shuffle arr
        N = len(self.arr)*100
        for _ in range(N):
            j, k = random.randint(0, num-1), random.randint(0, num-1)
            self.arr[j], self.arr[k] = self.arr[k], self.arr[j]

        # Instantiate the classes and create an array copy for each sorting object
        self.sort_objects = []
        self.arrays = []
        for i, _class in enumerate(sort_classes):
            self.sort_objects.append([_class(self.arr), sort_classes_names[i]])
            self.arrays.append(self.arr.copy())

        # Create a sepparate canvas for each sorting algorithm
        self.frame = tkinter.Frame(self.root, width=dimensions[0], height=dimensions[1])
        # Height and width of each canvas
        self.canvas_height = (self.dimensions[1]-50)/len(sort_classes)
        self.canvas_width = (self.dimensions[0])
        self.frame.grid(row=0, column=0, sticky='n')
        self.canvases = []
        for i in range(len(sort_classes)):
            canvas = tkinter.Canvas(self.frame, width=self.canvas_width,
                                    height=self.canvas_height, bg='black')
            canvas.grid(row=i, column=0, sticky='n')
            self.canvases.append(canvas)

        self.last_selected = [None]*len(sort_classes)

    def start(self):
        # Run sort functions and get steps
        self.steps = []
        for obj, name in self.sort_objects:
            self.steps.append(obj.sort())
        print('[~] Done sorting')
        # Draw all canvases
        self.draw()
        # Start animation
        self.root.after(3000, self.run)

        # is the frame destroyed?
        self.is_frame_destroyed = False

    def run(self):
        if not self.is_frame_destroyed:
            run = False
            for i in range(len(self.sort_objects)):
                # If there are still unprocessed steps
                if self.steps[i].empty() is False:
                    swap = self.steps[i].get()
                    # Perform swap
                    self.arrays[i][swap[0]], self.arrays[i][swap[1]] = self.arrays[i][swap[1]], self.arrays[i][swap[0]]
                    self.last_selected[i] = [swap[0], swap[1]]
                    run = True
            self.draw()
            self.last_selected = [None]*len(self.sort_objects)
            if run:
                self.root.after(self.delay, self.run)

    def draw(self):
        # For each canvas
        for i, canvas in enumerate(self.canvases):
            canvas.delete('all')

            # Maximum value
            max = self.num-1

            # width of each column
            width = self.canvas_width/self.num
            k = (self.canvas_height-15)/max

            # draw columns
            x = 0
            for j, value in enumerate(self.arrays[i]):
                if self.last_selected is not None and self.last_selected[i] is not None and j in self.last_selected[i]:
                    fill = 'yellow'
                else:
                    fill = 'white'
                canvas.create_rectangle(x, self.canvas_height,
                                        x+width,
                                        self.canvas_height-(k*value),
                                        fill=fill, width=2)
                x += width

            # name of the algorthm
            canvas.create_text(10, 5, text=self.sort_objects[i][1], font='Arial', anchor='nw', fill='gray')

    def removethis(self):
        self.is_frame_destroyed = True
        self.frame.destroy()
