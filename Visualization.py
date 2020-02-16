import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


def visualize(graph, heuristic, expanded_nodes, final_path, path_cost):
    # 0 - free space
    # 1 - obstacle
    # 2 - expanded node
    # 3 - node on path
    goal = final_path[0]
    start = final_path[-1]

    for node in expanded_nodes.keys():
        (x, y) = node
        graph[y][x] = '2'
    for node in final_path:
        (x, y) = node
        graph[y][x] = '3'
    for node in (start, goal):
        (x, y) = node
        graph[y][x] = '4'

    data = np.array(graph)
    data = np.delete(data, len(graph[0])-1, 1)
    data = data.astype(int)

    cmap = colors.ListedColormap(['white', 'black', 'yellow', 'green', 'purple'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)
    ax.set_title('Heuristic {}\n'
                 'Path cost {}\n'
                 'Visited nodes {}'
                 .format(heuristic.lower(), path_cost, len(expanded_nodes.keys())))
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.5)

    plt.show()
