import sys
import re
import collections
from math import prod

class Round:

    counting_dict = collections.Counter()

    round_separator_regex = re.compile(r',')

    def __init__(self, round_string):
        self.count = self.counting_dict.copy()
        self.build_round(round_string)

    def build_round(self, round_string):
        for char in self.round_separator_regex.split(round_string):
            count, key = char.split()
            self.count[key] += int(count)
        print(self.count)

    def __str__(self):
        return str(self.count)

class Game:

    game_separator_regex = re.compile(r':')
    round_separator_regex = re.compile(r';')

    def __init__(self, game_string):
        game_id_string, game_rounds = game_string.split(':')
        self.rounds = []
        self.game_id_string = game_id_string
        for round_string in self.round_separator_regex.split(game_rounds):
            self.add_round(Round(round_string))

    def add_round(self, round):
        self.rounds.append(round)

    def get_min_power_of_cubes_shown(self):
        red = max([self.rounds[i].count['red'] for i in range(len(self.rounds))])
        green = max([self.rounds[i].count['green'] for i in range(len(self.rounds))])
        blue = max([self.rounds[i].count['blue'] for i in range(len(self.rounds))])
        print(self.game_id_string, red, blue, green)
        return prod([red, blue, green])
    def __str__(self):
        return str(self.rounds)

class Solution:
    def solve(self, file):
        power_of_cubes = 0
        for row in open(file, 'r'):
            power_of_cubes += Game(row).get_min_power_of_cubes_shown()
        return power_of_cubes

print(Solution().solve(sys.argv[1]))