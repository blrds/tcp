import numpy as np
import random
import threading
import time

def genetic_algorithm(self, matrix, population_size=100, generations=500, mutation_rate=0.01):
    n = len(matrix)
    
    # Создание начальной популяции
    population = [random.sample(range(n), n) for _ in range(population_size)]

    def calculate_path_length(path):
        """Вычисляет длину маршрута для данного порядка узлов."""
        length = 0
        for i in range(len(path) - 1):
            length += matrix[path[i]][path[i + 1]]
        length += matrix[path[-1]][path[0]]  # Возврат к начальной точке для замыкания пути
        return length

    def selection(population, fitness_scores, num_parents):
        """Отбор индивидов на основе вероятности, пропорциональной их приспособленности (1 / длине маршрута)."""
        selection_probs = [1 / score for score in fitness_scores]
        total_prob = sum(selection_probs)
        selection_probs = [p / total_prob for p in selection_probs]
        parents = random.choices(population, weights=selection_probs, k=num_parents)
        return parents

    def crossover(parent1, parent2):
        """Оператор кроссовера (частично сопоставляющий кроссовер, PMX) для создания нового потомка."""
        start, end = sorted(random.sample(range(n), 2))

        # Частичное копирование сегмента из первого родителя
        child = [-1] * n
        child[start:end] = parent1[start:end]
        # Заполнение оставшихся позиций на основе второго родителя
        for i in range(start, end):
            if parent2[i] not in child:
                for j in range(n):
                    if child[j] == -1:
                        child[j] = parent2[i]
                        break

        # Заполнение остальных значений из второго родителя
        for i in range(n):
            if child[i] == -1:
                for j in range(n):
                    if parent2[j] not in child:
                        child[i] = parent2[j]
        
        return child

    def mutate(path, mutation_rate):
        """Мутация путем случайной перестановки двух узлов в маршруте."""
        for i in range(n):
            if random.random() < mutation_rate:
                j = random.randint(0, n - 1)
                path[i], path[j] = path[j], path[i]
        return path

    def iter(best_path, best_length, population):
        # Оценка приспособленности каждого индивида в популяции
        fitness_scores = [calculate_path_length(individual) for individual in population]

        # Отбор лучших маршрутов
        num_parents = population_size // 2
        parents = selection(population, fitness_scores, num_parents)

        # Создание нового поколения через кроссовер и мутацию
        new_population = []
        for i in range(0, num_parents, 2):
            parent1, parent2 = parents[i], parents[(i + 1) % num_parents]
            child1 = mutate(crossover(parent1, parent2), mutation_rate)
            child2 = mutate(crossover(parent2, parent1), mutation_rate)
            new_population.extend([child1, child2])
        
        population = new_population

        # Обновление лучшего найденного решения
        for individual, length in zip(population, fitness_scores):
            if length < best_length:
                best_length = length
                best_path = individual

        return best_path, best_length, population

    best_path = None
    best_length = float('inf')

    if generations != -1 :
        for _ in range(generations):
            best_path, best_length, population = iter(best_path, best_length, population)
    else :
        self.stopped = False
        i = 100 * n
        while not self.stopped and i > 0:
            time.sleep(0.01)
            best_path, best_length1, population = iter(best_path, best_length, population)
            if best_length == best_length1 :
                i=i-1
            else:
                i = 100 * n
                best_length = best_length1
            self.final_path = best_path + [best_path[0]]
            self.final_res = best_length
    # Возвращаем лучший найденный путь и его длину
    return best_path + [best_path[0]], best_length


class GeneticAlgorithm(threading.Thread):
    def __init__(self, matrix, population_size=100, generations=500, mutation_rate=0.01):
        threading.Thread.__init__(self)
        self.final_path = []
        self.final_res = float('inf')
        self.stopped = True
        self.matrix=matrix
        self.population=population_size
        self.gen=generations
        self.mutation=mutation_rate

    def run(self):
        return genetic_algorithm(self, self.matrix, self.population, self.gen, self.mutation)

