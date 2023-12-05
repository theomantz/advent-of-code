import sys
import re
class Solution:
    string_nums_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    def solve(self, file):
        sum = 0
        for row in open(file, 'r'):
            new_row = re.sub(r'one|two|three|four|five|six|seven|eight|nine', lambda m: self.string_nums_map[m.group()], row)
            match = re.findall(r'[0-9]', new_row)
            sum += int(match[0] + match[-1])
        return sum

solution = Solution().solve(sys.argv[1])
print(solution)