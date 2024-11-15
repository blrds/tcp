import numpy as np
import random
import threading
import time

def self_learning_random_search(self, matrix, start, iterations=1000, learning_rate=0.05):
    n = len(matrix)
    
    # Матрица вероятностей для рёбер. Изначально все вероятности одинаковы.
    edge_influence = np.ones((n, n))
    
    # Лучший путь и его длина
    best_path = None
    best_length = float('inf')

    def calculate_path_length(path):
        """Вычисляет длину пути."""
        length = 0
        for i in range(len(path) - 1):
            length += matrix[path[i]][path[i + 1]]
        length += matrix[path[-1]][path[0]]  # Возвращаемся к начальной точке
        return length
    
    def iter(best_path, best_length, edge_influence):
        # Генерация случайного пути с учётом влияния рёбер
        current_path = [start]
        unvisited = set(range(n)) - {start}
        
        # Направленно выбираем узлы на основе матрицы влияния
        while unvisited:
            last_node = current_path[-1]
            # Выбираем следующий узел с учетом вероятности, основанной на edge_influence
            next_node = random.choices(
                list(unvisited),
                weights=[edge_influence[last_node][node] for node in unvisited],
                k=1
            )[0]
            current_path.append(next_node)
            unvisited.remove(next_node)
        
        # Вычисляем длину нового пути
        current_length = calculate_path_length(current_path)
        
        # Если новый путь лучше, запоминаем его и усиливаем влияние рёбер
        if current_length < best_length:
            best_length = current_length
            best_path = current_path
            
            # Усиливаем влияние рёбер, которые входят в лучший путь
            for i in range(len(current_path) - 1):
                edge_influence[current_path[i]][current_path[i + 1]] *= (1 - learning_rate)
            edge_influence[current_path[-1]][current_path[0]] *= (1 - learning_rate)

        else:
            # Ослабляем влияние рёбер, если решение не улучшилось
            for i in range(len(current_path) - 1):
                edge_influence[current_path[i]][current_path[i + 1]] *= (1 + learning_rate)
            edge_influence[current_path[-1]][current_path[0]] *= (1 + learning_rate)
        return best_path, best_length, edge_influence

    if iterations != -1 :
        for _ in range(iterations):
            best_path, best_length, edge_influence = iter(best_path, best_length, edge_influence)
    else :
        self.stopped = False
        i = 100 * n
        while not self.stopped and i > 0:
            time.sleep(0.01)
            best_path, best_length1, edge_influence = iter(best_path, best_length, edge_influence)
            if best_length == best_length1 :
                i=i-1
            else:
                i = 100 * n
                best_length = best_length1
            self.final_path = [start] + list(best_path) + [start]
            self.final_res = best_length

    # Возвращаем лучший найденный путь и его длину
    return best_path + [start], best_length


class SelfLearningRandomSearch(threading.Thread):
    def __init__(self, matrix, start = 0, iterations = 1000, learning_rate = 0.5):
        threading.Thread.__init__(self)
        self.final_path = []
        self.final_res = float('inf')
        self.stopped = True
        self.matrix=matrix
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.s= start

    def run(self):
        return self_learning_random_search(self, self.matrix, self.s, self.iterations, self.learning_rate)

