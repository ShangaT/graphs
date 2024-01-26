#!/usr/bin/python
import numpy as np
def main(graph):
    power = 1
    m_p = dict()
    result = []
    while True:        
        result = np.linalg.matrix_power(graph, power)        
        m_p[f'A^{power}'] = result
        if np.all(result == 0): break
        power += 1
    for i in m_p:
        print(f'{i}\n{m_p[i]}\n')

    reachability_matrix = np.sum(list(m_p.values()), axis=0)
    print(f'Матрица достижимости:\n{reachability_matrix}\n')

    sigma_i = dict()
    sigma_j = dict()
    for i in m_p:
        sigma_i[f'Сигма i для {i}'] = np.sum(m_p[i], axis=1)
        sigma_j[f'Сигма j для {i}'] = np.sum(np.transpose(m_p[i]), axis=1)   
    for i in sigma_i:
        print(f'{i} = {sigma_i[i]}')
    print()
    for i in sigma_j:
        print(f'{i} = {sigma_j[i]}')

    qi_reachability = np.sum(reachability_matrix, axis=1)
    qj_reachability = np.sum(np.transpose(reachability_matrix), axis=1)
    print(f'\nСигма i для матрицы достижимости = {qi_reachability}')
    print(f'Сигма j для матрицы достижимости = {qj_reachability}\n')

    vertex_0 = []
    vertex_1 = [list(range(1,len(graph)+1))]
    for i, j in sigma_j.items():
        if np.any(j == 0):
            vertex_0.append(list(np.where(j == 0)[0] + 1))
    for i, j in sigma_j.items():
        if np.any(j > 0):
            vertex_1.append(list(np.where(j > 0)[0] + 1))
    pi = dict()
    for i in range(min(len(vertex_1), len(vertex_0))):
        s = set(vertex_1[i]) & set(vertex_0[i])
        pi[i] = s
    print(f'Порядок элементов {pi}')

    for i, val in enumerate(pi, start = 0):
        if val != {}:
            pi_max = i
    print(f'Тактнрость системы: {pi_max}')

    contour = np.all(np.diag(reachability_matrix) == 0)
    if contour:
        print('Контуров нет')

    entry = []
    for i, val in enumerate(qj_reachability, start = 1):
        if val == 0:
            entry.append(i)
    print(f'Входные элементы: {entry}')

    ex = []
    for i, val in enumerate(qi_reachability, start = 1):
        if val == 0:
            ex.append(i)
    print(f'Выходные элементы: {ex}')

    hanging_vertices = []
    for i in range(len(qi_reachability)):
        if qi_reachability[i] == 0 and qj_reachability[i] == 0:
            hanging_vertices.append(qi_reachability[i])
        else: hanging_vertices = 'Висящих вершин нет'
    print(hanging_vertices)

    print('\nПути длинной лямбда:')
    ways_lambda = dict()
    for key, matrix in m_p.items():
        ways_key = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    ways_key[f'a{i+1}{j+1}'] = matrix[i][j]
        ways_lambda[key] = ways_key
        print(f'Лямбда = {key.replace("A^", "")}: {ways_lambda[key]}')

    ways = dict()
    for i in range(len(reachability_matrix)):
        for j in range(len(reachability_matrix[0])):
            if reachability_matrix[i][j] != 0:
                ways[f'a{i+1}{j+1}'] = reachability_matrix[i][j]
    print(f'\nВсевозможные пути: {ways}\n')

    matrix = np.transpose(reachability_matrix)
    for i in range(len(matrix)):
        elements = []
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                elements.append(j+1)
        print(f'В формировании {i+1} участвуют {elements}')

graph_1 = [[0,1,0,0,0,1,0,0],
          [0,0,0,0,1,1,0,0],
          [0,0,0,1,0,0,0,1],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,1,0],
          [0,0,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]

graph_2 = [[0,0,0,0,0,0,0,0,0,0],
           [1,0,1,0,0,0,0,0,0,1],
           [0,0,0,1,0,0,0,0,0,0],
           [0,0,0,0,1,0,0,0,0,1],
           [0,0,0,0,0,0,1,0,0,0],
           [0,0,0,0,1,0,0,0,0,0],
           [0,0,0,0,0,1,0,0,0,0],
           [1,0,0,0,0,0,1,0,0,0],
           [0,1,0,0,0,0,0,1,0,0],
           [0,0,0,0,0,0,0,0,0,0]]

print('\nГРАФ №1')
main(graph_1)
print('\nГРАФ №2')
main(graph_2)



# graph_0 = [[0,0,0,0,1,0,0,1,0,0],
#            [0,0,0,0,1,0,1,0,0,0],
#            [0,0,0,0,0,1,0,0,1,0],
#            [0,0,0,0,0,1,1,0,0,0],
#            [0,0,0,0,0,0,1,1,0,1],
#            [0,0,0,0,0,0,0,0,0,1],
#            [0,0,0,0,0,0,0,1,1,0],
#            [0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0]]