import numpy as np


def get_smallest_cycle(tem_graph):
    graph = np.array(tem_graph)
    node_num = len(graph)
    for i in range(node_num):
        for j in range(node_num):
            if graph[i][j] == 0:
                graph[i][j] = 10000
    result = 10000
    changed_graph = graph.copy()
    for k in range(node_num):
        for i in range(k):
            for j in range(i + 1, k):
                if result > changed_graph[i][j] + graph[i][k] + graph[k][j]:
                    result = changed_graph[i][j] + graph[i][k] + graph[k][j]
        for i in range(node_num):
            for j in range(node_num):
                changed_graph[i][j] = min(changed_graph[i][j], changed_graph[i][k] + changed_graph[k][j])
    result = int(result)
    if result > node_num:
        return 0, []
    else:
        visited_list = []
        for i in range(node_num):
            ans, cycle_list = find_cycle(graph, i, i, result, visited_list)
            if ans:
                return result, cycle_list


def find_cycle(graph, root, node, result, visited_list):
    ans = False
    new_visited_list = visited_list.copy()
    new_visited_list.append(node)
    if len(new_visited_list) == result and graph[node][root] == 1:
        ans = True
        return ans, new_visited_list
    if len(new_visited_list) == result:
        return ans, new_visited_list
    if len(new_visited_list) < result:
        for i in range(len(graph)):
            if graph[i][node] == 1 and i not in new_visited_list:
                ans, visited_list_i = find_cycle(graph, root, i, result, new_visited_list)
                if ans:
                    return ans, visited_list_i
    return False, visited_list


def even_cycle_coloring(graph, node_list, c1, c2, color):
    node = node_list[0]
    next_color = c1
    color_number = 0
    node_num = len(node_list)
    colored_node = []
    while color_number < node_num:
        color[node] = next_color
        color_number += 1
        if next_color == c1:
            next_color = c2
        else:
            next_color = c1
        colored_node.append(node)
        for next_node in node_list:
            if graph[next_node][node] == 1 and next_node not in colored_node:
                node = next_node
                break
    return color


def odd_cycle_coloring(graph, node_list, c1, c2, c3, color):
    node = node_list[0]
    color[node] = c3
    next_color = c1
    color_number = 1
    node_num = len(node_list)
    colored_node = [node]
    for next_node in node_list:
        if graph[next_node][node] == 1 and next_node not in colored_node:
            node = next_node
    while color_number < node_num:
        color[node] = next_color
        if next_color == c1:
            next_color = c2
        else:
            next_color = c1
        color_number += 1
        colored_node.append(node)
        for next_node in node_list:
            if graph[next_node][node] == 1 and next_node not in colored_node:
                node = next_node
                break
    return color


def no_cycle_coloring(graph, node_list, c1, c2, color):
    node = node_list[0]
    next_node_list = [node]
    next_color = c1
    color_number = 0
    node_num = len(node_list)
    colored_node = []
    while color_number < node_num:
        if len(next_node_list) == 0:
            for node in node_list:
                if node not in colored_node:
                    next_node_list = [node]
                    break
        coloring_node_list = np.array(next_node_list)
        next_node_list = []
        for node in coloring_node_list:
            color[node] = next_color
            colored_node.append(node)
            color_number += 1
            for child in node_list:
                if graph[node][
                    child] == 1 and child not in colored_node and child not in next_node_list and child not in coloring_node_list:
                    next_node_list.append(child)
        if next_color == c1:
            next_color = c2
        else:
            next_color = c1
    return color


def check_valid(graph, subgraph, color):
    is_valid = True
    for node1 in subgraph:
        for node2 in subgraph:
            if graph[node1][node2] == 1 and color[node1] == color[node2]:
                is_valid = False
    return is_valid


def local_optimal_coloring_algorithm(graph):
    cycle_list = []
    tem_graph = graph.copy()
    remain_node_list = []
    max_color_number = 2
    print(graph[69][69])
    color = []
    for i in range(len(graph[0])):
        color.append(0)
    for i in range(len(graph[0])):
        remain_node_list.append(i)
    while 1 > 0:
        result, cycle_node_index_list = get_smallest_cycle(tem_graph)
        if result == 0:
            break
        cycle_node_list = []
        for index in cycle_node_index_list:
            cycle_node_list.append(remain_node_list[index])
        last_graph = tem_graph.copy()
        last_node = remain_node_list.copy()
        tem_graph = [j for num, j in enumerate(last_graph) if num not in cycle_node_index_list]
        remain_node_list = [j for num, j in enumerate(last_node) if num not in cycle_node_index_list]
        for i in range(len(tem_graph)):
            row = tem_graph[i].copy()
            tem_graph[i] = [j for num, j in enumerate(row) if num not in cycle_node_index_list]
        cycle_list.append(cycle_node_list)
    no_cycle_subgraph = remain_node_list
    main_sub_graph = no_cycle_subgraph
    color = no_cycle_coloring(graph, no_cycle_subgraph, 1, 2, color)
    for i in tem_graph:
        print(i)
    print(tem_graph[10][10])
    print(remain_node_list)
    return 0,0
    for cycle in cycle_list:
        main_sub_graph = main_sub_graph + cycle
        print(len(main_sub_graph))
        if len(cycle) % 2 == 0:
            is_valid = False
            while not is_valid:
                for color1 in range(1, max_color_number + 1):
                    for color2 in range(1, max_color_number + 1):
                        if color1 == color2:
                            continue
                        color = even_cycle_coloring(graph, cycle, color1, color2, color)
                        is_valid = check_valid(graph, main_sub_graph, color)
                        if is_valid:
                            break
                    if is_valid:
                        break
                if not is_valid:
                    max_color_number += 1
        if len(cycle) % 2 == 1:
            is_valid = False
            while not is_valid:
                for color1 in range(1, max_color_number + 1):
                    for color2 in range(1, max_color_number + 1):
                        for color3 in range(1, max_color_number + 1):
                            if color1 == color2 or color1 == color3 or color2 == color3:
                                continue
                            print(color1, color2, color3)
                            color = odd_cycle_coloring(graph, cycle, color1, color2, color3, color)
                            is_valid = check_valid(graph, main_sub_graph, color)
                            if is_valid:
                                break
                        if is_valid:
                            break
                    if is_valid:
                        break
                if not is_valid:
                    max_color_number += 1
    return max_color_number, color
