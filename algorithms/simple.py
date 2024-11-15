import numpy as np
import threading
import time

def simple_random_search(self, matrix, start):
    n = len(matrix)
    min_path = []
    min_length = float('inf')
    begin = 0
    if start != -1 :
    # Выполняем случайные перестановки для пути
        for _ in range(start):  # Количество случайных попыток
            path = np.random.permutation([x for x in range(n) if x != begin])
            current_length = 0
            prev = begin
            for node in path:
                current_length += matrix[prev][node]
                prev = node
            current_length += matrix[prev][begin]  # Замыкаем путь, возвращаемся к начальной точке
            
            if current_length < min_length:
                min_length = current_length
                min_path = [begin] + list(path) + [begin]
    else:
        self.stopped = False
        i = 100 * n
        while not self.stopped and i > 0:
            time.sleep(0.01)
            path = np.random.permutation([x for x in range(n) if x != begin])
            current_length = 0
            prev = begin
            for node in path:
                current_length += matrix[prev][node]
                prev = node
            current_length += matrix[prev][begin]  # Замыкаем путь, возвращаемся к начальной точке
            
            if current_length < min_length:
                min_length = current_length
                min_path = [begin] + list(path) + [begin]
                self.final_path = min_path
                self.final_res = min_length
                i = 100 * n
            else :
                i=i-1
        self.stopped = True
    return min_path, min_length


class SimpleRandomSearch(threading.Thread):
    def __init__(self, matrix, start):
        threading.Thread.__init__(self)
        self.final_path = []
        self.final_res = float('inf')
        self.stopped = True
        self.matrix=matrix
        self.s= start

    def run(self):
        return simple_random_search(self, self.matrix, self.s)