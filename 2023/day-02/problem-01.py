import sys
import re
import collections

class Round:

    counting_dict = collections.Counter({
        'red': 12,
        'green': 13,
        'blue': 14
    })

    round_separator_regex = re.compile(r',')

    def __init__(self, round_string):
        self.count = self.counting_dict.copy()
        self.valid = True
        self.build_round(round_string)

    def build_round(self, round_string):
        for char in self.round_separator_regex.split(round_string):
            count, key = char.split()
            self.count[key] -= int(count)
            if self.count[key] < 0:
                self.valid = False
                break
    def is_valid(self):
        return self.valid

class Game:

    game_separator_regex = re.compile(r':')
    round_separator_regex = re.compile(r';')

    def __init__(self, game_string):
        game_id_string, game_rounds = game_string.split(':')
        self.game_id = int(game_id_string.split()[1])
        self.rounds = []
        for round_string in self.round_separator_regex.split(game_rounds):
            self.add_round(Round(round_string))

    def add_round(self, round):
        self.rounds.append(round)

    def valid_game(self):
        for round in self.rounds:
            if not round.is_valid():
                return False
        return True

    def get_points(self):
        return self.game_id if self.valid_game() else 0

class Solution:
    def solve(self, file):
        game_sum = 0
        for row in open(file, 'r'):
            game_sum += Game(row).get_points()
        return game_sum

print(Solution().solve(sys.argv[1]))