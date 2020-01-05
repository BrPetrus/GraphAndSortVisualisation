import tkinter
import visualise_sort
from algorithms import heapsort

canvas = tkinter.Canvas(bg='black', height=1000, width=1000)
canvas.pack()


vs = visualise_sort.VisualiseSort(heapsort.HeapSort, canvas, 1000, (1000, 1000))
vs.start()

canvas.mainloop()
