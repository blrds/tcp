import numpy as np
import random
import math

def simulated_annealing(matrix, start, initial_temp=1000, cooling_rate=0.995, iterations=1000):
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

    for iteration in range(iterations):
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

    # Возвращаем лучший найденный путь и его длину
    return best_path + [best_path[0]], best_length


class Annealing:
    def tsp(self, matrix, start=0, initial_temp=1000, cooling_rate=0.995, iterations=1000):
        return simulated_annealing(matrix, start, initial_temp, cooling_rate, iterations)


# Тестирование метода выжигания
if __name__ == "__main__":
    matrix = [
        [0, 2.5, 0.3],
        [2.5, 0, 4],
        [0.3, 4, 0]
    ]
    annealing_search = Annealing()
    route, dist = annealing_search.tsp(matrix)
    print(f"Маршрут: {route}, Длина: {dist}")

    matrix = [
        [0, 2, 1, 2],
        [2, 0, 4, 2],
        [1, 4, 0, 3],
        [2, 2, 3, 0]
    ]
    route, dist = annealing_search.tsp(matrix)
    print(f"Маршрут: {route}, Длина: {dist}")

    distance_matrix = [
        [0, 328, 259, 180, 314, 294, 269, 391],
        [328, 0, 83, 279, 107, 131, 208, 136],
        [259, 83, 0, 257, 70, 86, 172, 152],
        [180, 279, 257, 0, 190, 169, 157, 273],
        [314, 107, 70, 190, 0, 25, 108, 182],
        [294, 131, 86, 169, 25, 0, 84, 158],
        [269, 208, 172, 157, 108, 84, 0, 140],
        [391, 136, 152, 273, 182, 158, 140, 0],
    ]

    route, dist = annealing_search.tsp(distance_matrix)
    print(f"Маршрут: {route}, Длина: {dist}")
