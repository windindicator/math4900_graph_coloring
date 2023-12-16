import random
import numpy as np


def check_smallest_cycle(tem_graph, smallest_cycle):
    graph = np.array(tem_graph)
    node_num = len(graph)
    for i in range(node_num):
        for j in range(node_num):
            if graph[i][j] == 0:
                graph[i][j] = node_num + 2
    result = node_num + 2
    changed_graph = graph
    for k in range(node_num):
        for i in range(k):
            for j in range(i + 1, k):
                result = min(result, changed_graph[i][j] + graph[i][k] + graph[j][k])
        if smallest_cycle > result:
            return False
        for i in range(k):
            for j in range(k):
                changed_graph[i][j] = min(changed_graph[i][j], changed_graph[i][k] + changed_graph[j][k])
    return True


def create_data(n, max_degree, smallest_cycle, edge_num):
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        graph.append(row)
    count = 0
    while count < edge_num:
        node1 = int(random.random() * n)
        node2 = int(random.random() * n)
        print(node1,node2)
        if node1 == node2:
            continue
        if graph[node1][node2] == 1:
            continue
        if sum(graph[node1]) >= max_degree or sum(graph[node2]) >= max_degree:
            continue
        tem_graph = np.array(graph)
        tem_graph[node1][node2] = 1
        tem_graph[node2][node1] = 1
        if smallest_cycle != 3:
            if not check_smallest_cycle(tem_graph, smallest_cycle):
                continue
        graph[node1][node2] = 1
        graph[node2][node1] = 1
        count += 1
        print(count)
    return graph


n = 100

for i in range(10):
    edge_num = 400
    max_degree = 10 + i
    smallest_cycle = 3
    graph = create_data(n, max_degree, smallest_cycle, edge_num)
    array = np.array(graph)
    np.save("n=" + str(n) + "_max_degree=" + str(max_degree) + "_edge_num=" + str(edge_num) + "_smallest_cycle=" + str(
        smallest_cycle), array)
    print(i)
