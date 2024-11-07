import numpy as np
import random

def guided_random_search(matrix, start = 0, iterations = 1000, influence_rate=0.2):
    n = len(matrix)
    best_path = np.random.permutation([x for x in range(n) if x != start])
    best_length = float('inf')
    
    def calculate_path_length(path):
        length = 0
        prev = start
        for node in path:
            length += matrix[prev][node]
            prev = node
        length += matrix[prev][start]  # Замыкаем цикл
        return length

    best_length = calculate_path_length(best_path)

    # Матрица для накопления информации о "хороших" рёбрах
    edge_influence = np.ones((n, n))

    for _ in range(iterations):
        new_path = best_path.copy()

        # Эвристика: более вероятно изменить ребра с низкой эффективностью
        for i in range(len(new_path) - 1):
            if random.random() < influence_rate:  # Вероятность смены направления
                current_node = new_path[i]
                next_node = new_path[i + 1]

                # Переход к узлу, который реже использовался или менее выгоден
                potential_nodes = [node for node in range(n) if node != current_node and node not in new_path[:i+1] and node != start]
                #print(f"a{i} {potential_nodes} {new_path}")
                if potential_nodes:
                    # Используем эвристику: выбираем узел с минимальной ценностью ребра
                    next_node = min(potential_nodes, key=lambda node: matrix[current_node][node] * edge_influence[current_node][node])
                changer=new_path[i + 1]
                changer_id=np.where(new_path == next_node)[0][0]
                new_path[changer_id]=changer
                new_path[i + 1] = next_node

        new_length = calculate_path_length(new_path)

        # Если новый путь лучше, обновляем лучший и обновляем влияние рёбер
        if new_length < best_length:
            best_length = new_length
            best_path = new_path
            # Обновляем влияние: "хорошие" рёбра усиливаются
            for i in range(len(best_path) - 1):
                edge_influence[best_path[i]][best_path[i + 1]] *= 0.9  # Уменьшаем влияние
            edge_influence[len(best_path) - 1][0] *= 0.9

    return [start] + list(best_path) + [start], best_length


class GuidedRandomSearch:
    def tsp(self, matrix, start=0, iterations=1000, influence_rate=0.2):
        return guided_random_search(matrix, start, iterations, influence_rate)


# Тестирование направленного случайного поиска
guided_search = GuidedRandomSearch()

matrix = [
    [0, 2.5, 0.3],
    [2.5, 0, 4],
    [0.3, 4, 0]
]
route, dist = guided_search.tsp(matrix)
print(f"Маршрут: {route}, Длина: {dist}")

matrix = [
    [0, 2, 1, 2],
    [2, 0, 4, 2],
    [1, 4, 0, 3],
    [2, 2, 3, 0]
]
route, dist = guided_search.tsp(matrix)
print(f"Маршрут: {route}, Длина: {dist}")

matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]
route, dist = guided_search.tsp(matrix)
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

route, dist = guided_search.tsp(distance_matrix)
print(f"Маршрут: {route}, Длина: {dist}")
