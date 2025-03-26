# Problem link : https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2025-03-26
'''
Problem description:
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
'''
from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        grid_elements = []
        r = grid[0][0]%x
        for mi in range(m):
            for ni in range(n):
                if grid[mi][ni]%x!=r:
                    return -1
                grid_elements.append(grid[mi][ni])
        grid_elements.sort()
        u = grid_elements[len(grid_elements)//2]
        nops = sum(abs(u-grid_elements[i])//x for i in range(len(grid_elements)))
        return nops

a = Solution()
tcs = [[[[2,4],[6,8]], 2], [[[1,5],[2,3]], 1], [[[1,2],[3,4]], 2]]
for tc in tcs:
    print(a.minOperations(*tc))

'''
Algorithm explained:
1. If the remaininder divided by x of all the elements of the grid is not the same, then no matter the number of operations, we cannot make the grid unified
2. If it is indeed possible to unify all the values, then the median is the unified value which will minimize the number of operations
3. The statistical/optimization principal states The median minimizes the sum of absolute deviations. sum_1^n(ai-u) is minimized when u is the median
'''
