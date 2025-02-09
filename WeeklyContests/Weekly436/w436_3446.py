from typing import List
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # Bottom Left Triangle
        for i in range(n):
            sp_h, sp_w = i, 0
            diag_elems = []
            while 0<=sp_h<n and 0<=sp_w<n:
                diag_elems.append(grid[sp_h][sp_w])
                sp_h += 1
                sp_w += 1
            diag_elems.sort(reverse=True)
            sp_h, sp_w = i, 0
            j = 0
            while 0<=sp_h<n and 0<=sp_w<n:
                grid[sp_h][sp_w] = diag_elems[j]
                sp_h += 1
                sp_w += 1
                j += 1
        # Top Right Triangle
        for i in range(1, n):
            sp_h, sp_w = 0, i
            diag_elems = []
            while 0<=sp_h<n and 0<=sp_w<n:
                diag_elems.append(grid[sp_h][sp_w])
                sp_h += 1
                sp_w += 1
            diag_elems.sort()
            sp_h, sp_w = 0, i
            j = 0
            while 0<=sp_h<n and 0<=sp_w<n:
                grid[sp_h][sp_w] = diag_elems[j]
                sp_h += 1
                sp_w += 1
                j += 1
        return grid