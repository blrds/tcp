import numpy as np
import random

def self_learning_random_search(matrix, start, iterations=1000, learning_rate=0.05):
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

    for iteration in range(iterations):
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

    # Возвращаем лучший найденный путь и его длину
    return best_path + [start], best_length


class SelfLearningRandomSearch:
    def tsp(self, matrix, start=0, iterations=1000, learning_rate=0.05):
        return self_learning_random_search(matrix, start, iterations, learning_rate)


# Тестирование алгоритма
if __name__ == "__main__":
    matrix = [
        [0, 2.5, 0.3],
        [2.5, 0, 4],
        [0.3, 4, 0]
    ]
    learning_search = SelfLearningRandomSearch()
    route, dist = learning_search.tsp(matrix)
    print(f"Маршрут: {route}, Длина: {dist}")

    matrix = [
        [0, 2, 1, 2],
        [2, 0, 4, 2],
        [1, 4, 0, 3],
        [2, 2, 3, 0]
    ]
    route, dist = learning_search.tsp(matrix)
    print(f"Маршрут: {route}, Длина: {dist}")
