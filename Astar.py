# class PriorityQueue, function reconstruct_path
# and the core loop of a_star_search function
# along with nested functions h_diagonal_distance and h_cross_product
# retrieved from https://www.redblobgames.com/pathfinding/a-star/, publlished in 2014 by Red Blob Games

import heapq
from random import random

from Constants import *
from Visualization import visualize


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return path


def a_star_search(graph, start, goal, heuristic_name):

    def h_diagonal_distance():
        # (x1, y1) = goal
        # (x2, y2) = next
        # dx = abs(x1 - x2)
        # dy = abs(y1 - y2)
        dx = abs(goal[0] - next[0])
        dy = abs(goal[1] - next[1])
        return DS * (dx + dy) + (DD - 2 * DS) * min(dx, dy)

    def h_multiplication_by_constant():
        return h_diagonal_distance() * CONSTANT

    def h_deterministic_random_number():
        return h_diagonal_distance() + random()

    def h_cross_product():
        # (x1, y1) = goal
        # (x2, y2) = next
        # (x3, y3) = start
        # dx1 = x2 - x1
        # dy1 = y2 - y1
        # dx2 = x3 - x1
        # dy2 = y3 - y1
        dx1 = next[0] - goal[0]
        dy1 = next[1] - goal[1]
        dx2 = start[0] - goal[0]
        dy2 = start[1] - goal[1]
        return h_diagonal_distance() + abs(dx1 * dy2 - dx2 * dy1)

    def neighbors(current_node):

        def is_passable(node):
            (x, y) = node
            return graph[y][x] == PASSABLE

        list_of_neighbors = []
        passable = {'N': False, 'E': False, 'S': False, 'W': False}  # offsets for cardinal directions

        # process cardinal directions
        for key in offsets_cardinal.keys():
            offset = offsets_cardinal[key]
            offset_node = tuple([sum(x) for x in zip(current_node, offset)])
            if is_passable(offset_node):
                list_of_neighbors.append((offset_node, DS))
                passable[key] = True

        # process intermediate directions based on cardinal
        for dir1, dir2 in [('N', 'W'),
                           ('N', 'E'),
                           ('S', 'W'),
                           ('S', 'E')]:
            if passable[dir1] and passable[dir2]:
                offset = offsets_intermediate[(dir1, dir2)]
                offset_node = tuple([sum(x) for x in zip(current_node, offset)])
                if is_passable(offset_node):
                    list_of_neighbors.append((offset_node, DD))

        return list_of_neighbors

    heuristic_list = {
        'DIAGONAL': h_diagonal_distance,
        'MULTIPLICATION': h_multiplication_by_constant,
        'DETERMINISTIC': h_deterministic_random_number,
        'CROSS': h_cross_product
    }

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    heuristic = heuristic_list[heuristic_name]

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            visualize(graph, heuristic_name, cost_so_far, path, cost_so_far[goal])
            return cost_so_far[goal]

        for next, cost_to_next in neighbors(current):
            new_cost = cost_so_far[current] + cost_to_next
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic()
                frontier.put(next, priority)
                came_from[next] = current
    return 0
