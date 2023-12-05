import sys
import re
class Solution:
    def solve(self, file):
        sum = 0
        for row in open(file, 'r'):
            
            nums_in_row = re.sub('[A-Za-z]', '', row).strip()
            sum += int(nums_in_row[0] + nums_in_row[-1])
            print(sum)
        return sum

solution = Solution().solve(sys.argv[1])
print(solution)