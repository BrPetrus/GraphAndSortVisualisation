from abc import ABC, abstractmethod
import queue


class Sort(ABC):
    def __init__(self, array):
        self.array = array.copy()
        self.steps = queue.Queue()

    @abstractmethod
    def sort(self):
        pass

    def swap(self, i, j):
        self.steps.put((i, j))
        self.array[i], self.array[j] = self.array[j], self.array[i]
