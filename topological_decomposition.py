#!/usr/bin/python
def search_g(graph):
    dict_g = dict()
    s = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                s.append(j+1)            
        dict_g[i+1] = s
        s = []
    return dict_g

def search_q(graph):
    t_matrix = [[0 for j in range(len(graph))] for i in range(len(graph[0]))]
    for i in range(len(graph)):
            for j in range(len(graph[i])):
                t_matrix[j][i] = graph[i][j]
    return search_g(t_matrix)

def achievable_vertices(graph, start): #находим достижимые вершины
    visited = []
    def dfs(start):
        if start in visited:
            return
        visited.append(start)
        for i in graph[start]:
            if not i in visited:
                dfs(i)
    dfs(start)
    return visited

def main(graph):
    vertexes_v = dict() 
    v = list(range(1, len(graph)+1)) 
    v_i = []
    G = search_g(graph)
    r = search_g(graph)
    q = search_q(graph)
    m=0 #счетчик для индексации v

    while True: #находим v
        v = set(v) - set(v_i)       
        if not v: break
        r_i = achievable_vertices(r, min(v))
        q_i = achievable_vertices(q, min(v))
        v_i = set(r_i) & set(q_i)      

        for i in v_i:
            del r[i]
            del q[i]
        for key in r: r[key] = [value for value in r[key] if value not in v_i]
        for key in q: q[key] = [value for value in q[key] if value not in v_i]

        m += 1
        vertexes_v[f'v{m}'] = v_i

    mas = []
    connections = dict() #находим связи между v и g
    for i in vertexes_v:
        for j in vertexes_v[i]:
            for k in G[j]:
                if k not in vertexes_v[i]:
                    mas.append(k)
                    connections[i] = mas
        mas = []

    connections_v = dict() #находим связи между v
    for i in vertexes_v:
        for j in connections:
            for k in connections[j]:
                if k in vertexes_v[i]:
                    mas.append(j)
                    connections_v[i] = mas
        mas = []

    final_connections_v = dict() #удаляем повторяющиеся связи
    for i in connections_v:
        final_connections_v[i] = list(set(connections_v[i]))

    print(vertexes_v)
    print(f'G^(-1) = {connections_v}')
    print(f'Финальный G^(-1) = {final_connections_v}')
    print('')

# graph_1 = [[1, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
#            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
#            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
#            [0, 0, 1, 1, 0, 0, 1, 0, 0, 0], 
#            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
#            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
#            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
#            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], 
#            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
#            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

# graph_2 = [[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#            [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#            [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

graph_1 = [[0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

graph_2 = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

graph_3 = [[0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 0]]

print('ГРАФ №1')
main(graph_1)

print('ГРАФ №2')
main(graph_2)

print('ГРАФ №3')
main(graph_3)