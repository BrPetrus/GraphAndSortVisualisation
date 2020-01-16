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
        self.menu_frame.option_add('*Font', 'Courier 20')
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
        box_quicksort_rand = tkinter.Checkbutton(self.menu_frame, text='Quicksort with random pivot', onvalue='Quicksort with random pivot', offvalue='', variable=var_quicksort_rand)
        self.checkbuttons.append([var_quicksort_rand, box_quicksort_rand])
        # Inserion sort
        var_insertionsort = tkinter.StringVar()
        box_insertionsort = tkinter.Checkbutton(self.menu_frame, text='Insertion sort', onvalue='Insertion sort', offvalue='', variable=var_insertionsort)
        self.checkbuttons.append([var_insertionsort, box_insertionsort])

        # Button to get back to menu
        self.button_to_menu = tkinter.Button(text='Back', command=self.back_to_menu)
        # Delay slider
        self.delay_scale = tkinter.Scale(self.menu_frame, from_=1, to=300, orient='horizontal')
        self.delay_scale.set(20)

        # Start button
        self.startbutton = tkinter.Button(self.menu_frame, text='Start', command=self.start)

        # Title
        self.label_title = tkinter.Label(self.menu_frame, text='Sort visualisation', font='Arial 40 bold')

        # Place stuff inside the frame
        self.label_title.grid(row=0, column=0)
        i = 1
        for sort_stuff in self.checkbuttons[:]:
            sort_stuff[1].grid(row=i, column=0, sticky='w')
            i += 1
        tkinter.Label(self.menu_frame, text='Delay in ms', font='Arial 15').grid(row=i, column=0)
        i += 1
        self.delay_scale.grid(row=i, column=0)
        i += 1
        self.startbutton.grid(row=i, column=0)

    def start(self):
        self.menu_frame.grid_forget()
        self.button_to_menu.grid(row=1, column=0)

        algs = {'Quicksort': quicksort.Quicksort, 'Heapsort': heapsort.HeapSort, 'Insertion sort': insertionsort.InsertionSort, 'Quicksort with random pivot': quicksort.Quicksort_random}

        # Determine which algoritms were selected
        algs_list = []
        names_list = []
        for var, checkbox in self.checkbuttons:
            print(var.get())
            value = var.get()
            if value in algs:
                algs_list.append(algs[value])
                names_list.append(value)

        self.vs = visualise_sort.VisualiseSort(algs_list, names_list, self.root, 100, [1024, 700], int(self.delay_scale.get()))
        self.vs.start()

    def back_to_menu(self):
        self.vs.removethis()
        self.button_to_menu.grid_forget()
        self.menu_frame.grid()
