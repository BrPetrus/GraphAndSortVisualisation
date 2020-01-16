import tkinter
import visualise_sort
from algorithms import heapsort
from algorithms import insertionsort
from algorithms import quicksort


class App():
    def __init__(self, root, dimensions):
        self.root = root

        # Menu
        self.menu_frame = tkinter.Frame(self.root, width=dimensions[0], height=dimensions[1])
        # Place menu
        self.menu_frame.grid(row=0, column=0)

        # Create checkboxes for each algorithm
        self.checkbuttons = []

        # Heapsort
        var_heapsort = tkinter.StringVar()
        box_heapsort = tkinter.Checkbutton(self.menu_frame, text='Heapsort', onvalue='Heapsort', offvalue='', variable=var_heapsort)
        self.checkbuttons.append([var_heapsort, box_heapsort])
        # Quicksort
        var_quicksort = tkinter.StringVar()
        box_quicksort = tkinter.Checkbutton(self.menu_frame, text='Quicksort', onvalue='Quicksort', offvalue='', variable=var_quicksort)
        self.checkbuttons.append([var_quicksort, box_quicksort])
        # Quicksort with random pivot
        var_quicksort_rand = tkinter.StringVar()
        box_quicksort_rand = tkinter.Checkbutton(self.menu_frame, text='Quicksort with random pivot', offvalue='', variable=var_quicksort_rand)
        self.checkbuttons.append([var_quicksort_rand, box_quicksort_rand])
        # Inserion sort
        var_insertionsort = tkinter.StringVar()
        box_insertionsort = tkinter.Checkbutton(self.menu_frame, text='Insertion sort', onvalue='Insertion sort', offvalue='', variable=var_insertionsort)
        self.checkbuttons.append([var_insertionsort, box_insertionsort])

        # Delay slider
        self.delay_scale = tkinter.Scale(self.menu_frame, from_=1, to=100, orient='horizontal')
        self.delay_scale.set(20)

        # Start button
        self.startbutton = tkinter.Button(self.menu_frame, text='Start', command=self.start)

        print(self.checkbuttons[:][0])
        # Place stuff inside the frame
        i = 0
        for sort_stuff in self.checkbuttons[:]:
            sort_stuff[1].grid(row=i, column=0, sticky='w')
            i += 1
        self.delay_scale.grid(row=i, column=0)
        i += 1
        self.startbutton.grid(row=i, column=0)

    def start(self):
        pass
