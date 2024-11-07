import numpy as np
import random

def ant_colony_optimization(matrix, num_ants=10, num_iterations=100, alpha=1.0, beta=2.0, evaporation_rate=0.5, initial_pheromone=1.0):
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

    for iteration in range(num_iterations):
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

    # Возвращаем лучший найденный путь и его длину
    return best_path + [best_path[0]], best_length


class AntColony:
    def tsp(self, matrix, num_ants=10, num_iterations=100, alpha=1.0, beta=2.0, evaporation_rate=0.5, initial_pheromone=1.0):
        return ant_colony_optimization(matrix, num_ants, num_iterations, alpha, beta, evaporation_rate, initial_pheromone)


# Тестирование метода муравьев
if __name__ == "__main__":
    matrix = [
        [0, 2.5, 0.3],
        [2.5, 0, 4],
        [0.3, 4, 0]
    ]
    ant_colony_search = AntColony()
    route, dist = ant_colony_search.tsp(matrix)
    print(f"Маршрут: {route}, Длина: {dist}")

    matrix = [
        [0, 2, 1, 2],
        [2, 0, 4, 2],
        [1, 4, 0, 3],
        [2, 2, 3, 0]
    ]
    route, dist = ant_colony_search.tsp(matrix)
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

    route, dist = ant_colony_search.tsp(distance_matrix)
    print(f"Маршрут: {route}, Длина: {dist}")
