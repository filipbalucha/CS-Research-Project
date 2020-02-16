from os import path, makedirs
from random import randint
from Astar import *
from Constants import *


def create_folders():
    for x in OBSTACLE_PERCENTAGES:
        try:
            path = 'data/benchmarks/OP_{}%'.format(x)
            makedirs(path)
        except FileExistsError:
            continue


def get_random_map(obstacle_percentage):
    obstacle_percentage /= 100
    line_of_obstacles = [OBSTACLE for _ in range(MAP_WIDTH + 1)]
    map_array = [line_of_obstacles]
    num_of_obstacles = 0

    for _ in range(MAP_HEIGHT):
        line = []
        for _ in range(MAP_WIDTH):
            if random() <= obstacle_percentage:
                line.append(OBSTACLE)
                num_of_obstacles += 1
            else:
                line.append(PASSABLE)
        line.append(OBSTACLE)
        map_array.append(line)

    map_array.append(line_of_obstacles)
    obstacle_percentage = num_of_obstacles*100/(MAP_HEIGHT * MAP_WIDTH)
    print('\tGenerated obstacle percentage: {}%'.format(round(obstacle_percentage, 2)))

    return map_array


def generate_benchmarks():
    for obstacle_percentage in OBSTACLE_PERCENTAGES:
        print('\nNow generating maps with {}% of obstacles'.format(obstacle_percentage))
        for map_num in range(NUM_OF_MAPS):
            map_array = get_random_map(obstacle_percentage)
            scenarios = set()
            while len(scenarios) != NUM_OF_SCENARIOS:
                while True:
                    x1 = randint(0, MAP_WIDTH)
                    y1 = randint(0, MAP_HEIGHT)
                    start = (x1, y1)
                    x2 = randint(0, MAP_WIDTH)
                    y2 = randint(0, MAP_HEIGHT)
                    goal = (x2, y2)
                    if map_array[y1][x1] != OBSTACLE and map_array[y2][x2] != OBSTACLE and start != goal:
                        break
                path_cost = a_star_search(map_array, start, goal, 'DIAGONAL')
                if path_cost != 0:
                    scenarios.add((start, goal))

            file_name = 'OP_{}%/map_{}.txt'.format(obstacle_percentage, map_num)
            with open(path.join(LOCATION_OF_FILES, file_name), 'w') as out:
                for (x1, y1), (x2, y2) in scenarios:
                    out.write('{};{};{};{}\n'.format(x1, y1, x2, y2))
                for line in map_array:
                    out.write(OBSTACLE + ''.join([char for char in line]) + '\n')


if __name__ == '__main__':
    create_folders()
    generate_benchmarks()
