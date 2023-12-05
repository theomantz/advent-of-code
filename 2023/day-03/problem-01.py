import re
class Grid:
    grid_row_regex = re.compile(r'\d+|.+|[*#+-@#]')
    def __init__(self, grid_string):
        self.grid = []
        self.build_grid(grid_string)
    
    def build_grid(self, grid_string):
        for index, row in enumerate(grid_string.split()):
            self.grid.append(self.build_row(row, index))

    def build_row(self, row_string, column_index):
        return self.grid_row_regex.sub(row_string, lambda m: self.build_node(m, column_index))

    def build_node(self, m: re.Match, column_index):
        if m.group(0).isdigit():
            return Number(m, column_index)
        else:
            return Symbol(m, column_index)

class Number:
    def __init__(self, m: re.Match, row):
        self.number = m.group(0)
        self.start_index = m.start()
        self.end_index = m.end()
        self.row_index = row

    def __str__(self):
        return { 
            number: str(self.number),
            start_index: str(self.start_index),
            end_index: str(self.end_index),
            row_index: str(self.row_index)
        }

class Symbol:
    def __init__(self, m: re.Match, row):
        self.symbol = m.group(0)
        self.start_index = m.start()
        self.end_index = m.end()
        self.row_index = row
    
    def build_symbol(self, symbol_string):
        for row in symbol_string.split():
            self.symbol.append(self.build_row(row))
    
    def build_row(self, row_string):
        return [char for char in row_string]

    def __str__(self):
        return {
            symbol: str(self.symbol),
            start_index: str(self.start_index),
            end_index: str(self.end_index),
            row_index: str(self.row_index)
        }