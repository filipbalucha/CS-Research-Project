import cProfile
from os import path
import pstats
from Astar import *
from Constants import *

heuristic_functions = ['DIAGONAL', 'MULTIPLICATION', 'DETERMINISTIC', 'CROSS']

if __name__ == '__main__':
    for heuristic_function in heuristic_functions:
        file_name = 'results_{}.txt'.format(heuristic_function.lower())
        with open(path.join(LOCATION_OF_RESULTS, file_name), 'w') as out:
            out.write('%;Avg path cost;Avg comp time\n')
            for obstacle_percentage in OBSTACLE_PERCENTAGES:
                print('Obstacles: {}%'.format(obstacle_percentage))
                print('\tHeuristic: {}'.format(heuristic_function))
                running_times = []
                path_costs = []
                for map_number in range(NUM_OF_MAPS):
                    print('\t\tMap no.: {} '.format(map_number))
                    file_name = 'OP_{}%/map_{}.txt'.format(obstacle_percentage, map_number)
                    with open(path.join(LOCATION_OF_FILES, file_name), 'r') as raw_map:
                        starts = []
                        goals = []

                        for _ in range(NUM_OF_SCENARIOS):
                            coordinates = next(raw_map).split(';')
                            coordinates = list(map(int, coordinates))
                            start = tuple((coordinates[0], coordinates[1]))
                            goal = tuple((coordinates[2], coordinates[3]))
                            starts.append(start)
                            goals.append(goal)

                        map_array = [list(line) for line in raw_map]

                        for x in range(NUM_OF_SCENARIOS):
                            print('\t\t\tScenario: {}'.format(x+1))
                            for _ in range(NUM_OF_RUNS):
                                pr = cProfile.Profile()
                                pr.run('a_star_search(map_array, starts[x], goals[x], heuristic_function)')
                                ps = pstats.Stats(pr)
                                running_times.append(ps.total_tt)
                            path_cost = a_star_search(map_array, starts[x], goals[x], heuristic_function)
                            path_costs.append(path_cost)

                avg_running_time = round(sum(running_times)/len(running_times)*1000, 3)
                avg_path_length = round(sum(path_costs) / len(path_costs), 3)
                out.write('{};{};{}\n'.format(obstacle_percentage, avg_path_length, avg_running_time))
