import numpy as np
import random
import math
import threading
import time

def simulated_annealing(self, matrix, start, initial_temp=1000, cooling_rate=0.995, iterations=1000):
    n = len(matrix)

    def calculate_path_length(matrix, path):
        """Вычисляет длину пути для данного порядка узлов."""
        length = 0
        for i in range(len(path) - 1):
            length += matrix[path[i]][path[i + 1]]
        length += matrix[path[-1]][path[0]]  # Замыкаем цикл, возвращаясь к начальной точке
        return length

    # Начальный случайный путь
    current_path = list(range(n))
    random.shuffle(current_path)
    current_length = calculate_path_length(matrix, current_path)

    # Сохраняем лучший путь и его длину
    best_path = current_path[:]
    best_length = current_length
    
    temperature = initial_temp

    def iter(best_path, best_length, current_path, current_length, temperature):
         # Создаём новый путь, меняя два случайных узла
        new_path = current_path[:]
        i, j = random.sample(range(n), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        
        # Вычисляем длину нового пути
        new_length = calculate_path_length(matrix, new_path)
        
        # Решение о принятии нового пути
        if new_length < current_length:
            # Принимаем новый путь, если он короче
            current_path = new_path
            current_length = new_length
            
            # Обновляем лучший путь
            if new_length < best_length:
                best_path = new_path
                best_length = new_length
        else:
            # Принимаем более длинный путь с вероятностью, зависящей от температуры
            delta = new_length - current_length
            acceptance_probability = math.exp(-delta / temperature)
            if random.random() < acceptance_probability:
                current_path = new_path
                current_length = new_length

        # Охлаждаем температуру
        temperature *= cooling_rate
        return best_path, best_length, current_path, current_length, temperature

    if iterations != -1 :
        for _ in range(iterations):
            best_path, best_length, current_path, current_length, temperature = iter(best_path, best_length, current_path, current_length, temperature)
    else :
        self.stopped = False
        i = 1000 * n
        while not self.stopped and i > 0:
            time.sleep(0.01)
            best_path, best_length1, current_path, current_length, temperature = iter(best_path, best_length, current_path, current_length, temperature)
            if best_length == best_length1 :
                i=i-1
            else:
                i = 1000 * n
                best_length = best_length1
            self.final_path = best_path + [best_path[0]]
            self.final_res = best_length

    # Возвращаем лучший найденный путь и его длину
    return best_path + [best_path[0]], best_length


class Annealing(threading.Thread):
    def __init__(self, matrix, start=0, initial_temp=1000, cooling_rate=0.995, iterations=1000):
        threading.Thread.__init__(self)
        self.final_path = []
        self.final_res = float('inf')
        self.stopped = True
        self.matrix=matrix
        self.iterations = iterations
        self.initial_temp = initial_temp
        self.cooling_rate=cooling_rate
        self.s= start

    def run(self):
        return simulated_annealing(self, self.matrix, self.s, self.initial_temp, self.cooling_rate, self.iterations)
