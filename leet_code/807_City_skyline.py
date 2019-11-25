#807. Max Increase to Keep City Skyline
#https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        #left right
        a = []
        for line in grid:
            a.append(max(line))
        #top down
        b = []
        for i in range(len(grid)):
            b.append(max([row[i] for row in grid]))
            
            
        print(a)
        print(b)
        
        acc = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                acc += min([b[i], a[j]]) - grid[i][j]
        
        return acc

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

s = Solution()

s.maxIncreaseKeepingSkyline(grid)
