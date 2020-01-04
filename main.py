# import tkinter
# canvas = tkinter.Canvas(bg='black', height=1000, width=1000)
# canvas.pack()
# canvas.mainloop()
import visualise_sort
from algorithms import heapsort

vs = visualise_sort.VisualiseSort(heapsort.HeapSort)
vs.run()


