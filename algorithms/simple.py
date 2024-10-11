import numpy as np

def simple_random_search(matrix, start):
    n = len(matrix)
    min_path = []
    min_length = float('inf')
    begin = 0

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

    return min_path, min_length


class SimpleRandomSearch:
    def tsp(self, matrix, start=1000):
        return simple_random_search(matrix, start)


# Тестирование метода простого случайного поиска
simple_search = SimpleRandomSearch()

matrix = [
    [0, 2.5, 0.3],
    [2.5, 0, 4],
    [0.3, 4, 0]
]
route, dist = simple_search.tsp(matrix)
print(f"Маршрут: {route}, Длина: {dist}")

matrix = [
    [0, 2, 1, 2],
    [2, 0, 4, 2],
    [1, 4, 0, 3],
    [2, 2, 3, 0]
]
route, dist = simple_search.tsp(matrix)
print(f"Маршрут: {route}, Длина: {dist}")

matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]
route, dist = simple_search.tsp(matrix)
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

route, dist = simple_search.tsp(distance_matrix)
print(f"Маршрут: {route}, Длина: {dist}")