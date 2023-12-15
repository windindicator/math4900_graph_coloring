def update_u1(graph, color, k):
    u1 = []
    u2 = []
    for i in range(len(graph[0])):
        if color[i] == 0:
            is_u1 = True
            for j in range(len(graph[i])):
                if graph[i][j] == 1 and color[j] == k:
                    is_u1 = False
                    break
            if is_u1:
                u1.append(i)
            else:
                u2.append(i)
    return u1, u2


def compute_largest(graph, u1, u2):
    max_degree = 0
    best_node = u1[0]
    for node in u1:
        degree = 0
        for neighbor in u2:
            if graph[node][neighbor] == 1:
                degree += 1
        if degree > max_degree:
            max_degree = degree
            best_node = node
    return best_node


def reset_u1(color):
    u1 = []
    for i in range(len(color)):
        if color[i] == 0:
            u1.append(i)
    return u1


def get_first_node(graph, u1):
    max_node = u1[0]
    max_degree = 0
    for node in u1:
        degree = 0
        for i in u1:
            if graph[node][i] == 1:
                degree += 1
        if degree > max_degree:
            max_degree = degree
            max_node = node
    return max_node


def Recursive_Largest_First_Algorithm(graph):
    color_num = 0
    color = []
    for i in range(len(graph[0])):
        color.append(0)
    while min(color) == 0:
        color_num += 1
        u1 = reset_u1(color)
        first_node = get_first_node(graph, u1)
        color[first_node] = color_num
        u1, u2 = update_u1(graph, color, color_num)
        while len(u1) > 0:
            node = compute_largest(graph, u1, u2)
            color[node] = color_num
            u1, u2 = update_u1(graph, color, color_num)
    return color, color_num
