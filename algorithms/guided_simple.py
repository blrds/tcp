import numpy as np
import random
import threading
import time

def guided_random_search(self, matrix, start = 0, iterations = 1000, influence_rate=0.2):
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

    def iter(best_path, best_length, edge_influence):
        new_path = best_path.copy()

        # Эвристика: более вероятно изменить ребра с низкой эффективностью
        for i in range(len(new_path) - 1):
            if random.random() < influence_rate:  # Вероятность смены направления
                current_node = new_path[i]
                next_node = new_path[i + 1]

                # Переход к узлу, который реже использовался или менее выгоден
                potential_nodes = [node for node in range(n) if node != current_node and node not in new_path[:i+1] and node != start]

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
        return best_path, best_length, edge_influence

    self.final_path = [start] + list(best_path) + [start]
    self.final_res = best_length
    # Матрица для накопления информации о "хороших" рёбрах
    edge_influence = np.ones((n, n))
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

    return [start] + list(best_path) + [start], best_length

class GuidedRandomSearch(threading.Thread):
    def __init__(self, matrix, start, iterations, influence_rate):
        threading.Thread.__init__(self)
        self.final_path = []
        self.final_res = float('inf')
        self.stopped = True
        self.matrix=matrix
        self.iterations = iterations
        self.influence_rate = influence_rate
        self.s= start

    def run(self):
        return guided_random_search(self, self.matrix, self.s, self.iterations, self.influence_rate)
