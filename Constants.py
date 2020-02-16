import numpy as np

LOCATION_OF_FILES = 'data/benchmarks/'
LOCATION_OF_RESULTS = 'data/results/'

MIN_OBSTACLE_PERCENTAGE = 0
MAX_OBSTACLE_PERCENTAGE = 10
STEP = 0.5
OBSTACLE_PERCENTAGES = np.arange(MIN_OBSTACLE_PERCENTAGE,
                                 MAX_OBSTACLE_PERCENTAGE + 0.01,
                                 STEP)

OBSTACLE = '1'
PASSABLE = '0'
DS = 10
DD = 14

NUM_OF_MAPS = 10
NUM_OF_SCENARIOS = 20
NUM_OF_RUNS = 10
MAP_WIDTH = 192
MAP_HEIGHT = 108

CONSTANT = 1.0 + 1/(MAP_WIDTH + MAP_HEIGHT)  # maximum expected path length is given by DS/(DS*(MAP_WIDTH + MAP_HEIGHT))


offsets_cardinal = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

offsets_intermediate = {
    ('N', 'W'): (-1, -1),
    ('N', 'E'): (1, -1),
    ('S', 'W'): (-1, 1),
    ('S', 'E'): (1, 1)
}
