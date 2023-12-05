import sys
import re
from pprint import pprint
class Node:
    def __init__(self, m: re.Match, row):
        self.value = m.group(0)
        self.start_index = m.start()
        self.end_index = m.end()
        self.row_index = row
        
    def __str__(self):
        return str("v: {self.value}, si: {self.start_index}, ei: {self.end_index}, ri: {self.row_index}".format(self=self))
class Grid:
    grid_row_regex = re.compile(r'(\d+)|(\.+)|([*#+-@#])')
    def __init__(self, grid_string):
        self.grid = []
        self.build_grid(grid_string)
    
    def build_grid(self, grid_string):
        for index, row in enumerate(grid_string.split()):
            self.grid.append(self.build_row(row, index))

    def build_row(self, row_string, column_index):
        return [self.build_node(i, column_index) for i in self.grid_row_regex.finditer(row_string) if i is not None and i != '']

    def append_row(self, row_string):
        self.grid.append(self.build_row(row_string, len(self.grid) - 1))

    def build_node(self, m: re.Match, column_index) -> Node:
        if m.group(0).isdigit():
            return Number(m, column_index)
        else:
            return Symbol(m, column_index)
        
    def __str__(self):
        return str([[str(node) for node in row] for row in self.grid])



class Number(Node):
    def __init__(self, m: re.Match, row):
        self.value = m.group(0)
        self.number = m.group(0)
        self.start_index = m.start()
        self.end_index = m.end()
        self.row_index = row

class Symbol(Node):
    def __init__(self, m: re.Match, row):
        self.value = m.group(0)
        self.symbol = m.group(0)
        self.start_index = m.start()
        self.end_index = m.end()
        self.row_index = row
    
    def build_symbol(self, symbol_string):
        for row in symbol_string.split():
            self.symbol.append(self.build_row(row))
    
    def build_row(self, row_string):
        return [char for char in row_string]

class Solution:
    def solve(self, file):
        for grid in open(file):
            grid = Grid(grid)
            print(grid)
            

Solution().solve(sys.argv[1])