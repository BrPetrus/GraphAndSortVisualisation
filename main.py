import tkinter
import visualise_sort
from algorithms import heapsort
from algorithms import insertionsort
from algorithms import quicksort
from app import App

root = tkinter.Tk()

app = App(root, [1024, 768])

#sortframe = tkinter.Frame()

#vs = visualise_sort.VisualiseSort([quicksort.Quicksort, quicksort.Quicksort_random, heapsort.HeapSort, insertionsort.InsertionSort], ['Quicksort', 'Random pivot quicksort', 'Heapsort', 'Insertionsort'], root, 100, dimensions=[1024, 700])
#vs.start()

print('Mainloop')
#b = tkinter.Button(text='OK', command=vs.removethis)
#b.grid(row=1, column=0)
root.mainloop()
