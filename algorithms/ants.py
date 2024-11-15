import numpy as np
import random
import threading
import time

def ant_colony_optimization(self, matrix, num_ants=10, iterations=100, alpha=1.0, beta=2.0, evaporation_rate=0.5, initial_pheromone=1.0):
    n = len(matrix)
    
    # Инициализация феромонов на всех рёбрах
    pheromone = np.full((n, n), initial_pheromone)
    best_path = None
    best_length = float('inf')

    def calculate_path_length(matrix, path):
        """Вычисляет длину пути для данного порядка узлов."""
        length = 0
        for i in range(len(path) - 1):
            length += matrix[path[i]][path[i + 1]]
        length += matrix[path[-1]][path[0]]  # Возвращаемся к начальной точке
        return length

    def iter(best_path, best_length, pheromone):
        all_paths = []
        all_lengths = []

        # Каждый муравей создает свой путь
        for ant in range(num_ants):
            path = [random.randint(0, n-1)]
            while len(path) < n:
                current_node = path[-1]
                unvisited_nodes = [node for node in range(n) if node not in path]
                
                # Расчёт вероятностей для выбора следующего узла
                probabilities = []
                for next_node in unvisited_nodes:
                    pheromone_level = pheromone[current_node][next_node] ** alpha
                    visibility = (1.0 / matrix[current_node][next_node]) ** beta
                    probabilities.append(pheromone_level * visibility)
                
                # Нормализация вероятностей
                total = sum(probabilities)
                probabilities = [p / total for p in probabilities]
                
                # Выбор следующего узла на основе вероятности
                next_node = random.choices(unvisited_nodes, weights=probabilities, k=1)[0]
                path.append(next_node)

            # Добавляем путь в список всех путей муравьёв
            all_paths.append(path)
            path_length = calculate_path_length(matrix, path)
            all_lengths.append(path_length)

            # Обновляем лучший путь
            if path_length < best_length:
                best_length = path_length
                best_path = path

        # Испарение феромонов
        pheromone *= (1 - evaporation_rate)

        # Обновление феромонов на основе пройденных путей
        for i, path in enumerate(all_paths):
            path_length = all_lengths[i]
            pheromone_deposit = 1.0 / path_length  # Количество феромона обратно пропорционально длине пути
            for j in range(len(path) - 1):
                pheromone[path[j]][path[j + 1]] += pheromone_deposit
            pheromone[path[-1]][path[0]] += pheromone_deposit  # Замыкаем путь

        return best_path, best_length, pheromone

    if iterations != -1 :
        for iteration in range(iterations):
            best_path, best_length, pheromone = iter(best_path, best_length, pheromone)
    else :
        self.stopped = False
        i = 100 * n
        while not self.stopped and i > 0:
            time.sleep(0.01)
            best_path, best_length1, pheromone = iter(best_path, best_length, pheromone)
            if best_length == best_length1 :
                i=i-1
            else:
                i = 100 * n
                best_length = best_length1
            self.final_path = best_path + [best_path[0]]
            self.final_res = best_length


    # Возвращаем лучший найденный путь и его длину
    return best_path + [best_path[0]], best_length


class AntColony(threading.Thread):
    def __init__(self, matrix, num_ants=10, iterations=100, alpha=1.0, beta=2.0, evaporation_rate=0.5, initial_pheromone=1.0):
        threading.Thread.__init__(self)
        self.final_path = []
        self.final_res = float('inf')
        self.stopped = True
        self.matrix=matrix
        self.ants=num_ants
        self.iter = iterations
        self.a=alpha
        self.b=beta
        self.vape=evaporation_rate
        self.pher=initial_pheromone

    def run(self):
        return ant_colony_optimization(self, self.matrix, self.ants, self.iter, self.a, self.b, self.vape, self.pher)
