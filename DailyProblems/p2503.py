# Problem link : https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/?envType=daily-question&envId=2025-03-28
'''
Problem description:
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.
'''
# Basic Flood fill algorithm
from typing import List
class Solution:
    def flood_fill(self, h, w, query, visited, grid):
        if grid[h][w] >= query:
            return
        visited[h][w] = 1
        for d_h, d_w in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            h2, w2 = h+d_h, w+d_w
            if 0<=h2<len(grid) and 0<=w2<len(grid[0]):
                if not visited[h2][w2]:
                    self.flood_fill(h2, w2, query, visited, grid)
        return
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        start_w, start_h = 0, 0
        height, width = len(grid), len(grid[0])
        answer = []
        for query in queries:
            visited = [[0 for _ in range(width)] for _ in range(height)]
            self.flood_fill(0, 0, query, visited, grid)
            answer.append(sum(sum(l) for l in visited))
        return answer
# The above solution is inefficient as we are redoing flood fill for each of the queries. We can instead try to take advantage of previous floodfills from other queries.
### Optimized algorithm where we don't have to run DFS flood fill multiple times
from typing import List
import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        height, width = len(grid), len(grid[0])
        queries = sorted([[q, i] for i, q in enumerate(queries)])
        heap = [[grid[0][0], 0, 0]]
        visited = [[False]*width for _ in range(height)]
        visited[0][0] = True
        answers = [0 for i in range(len(queries))]
        count = 0
        for query, queryIndex in queries:
            while heap and query > heap[0][0]:
                gv, h, w = heapq.heappop(heap)
                count += 1
                for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nh, nw = h+dh, w+dw
                    if 0<=nh<height and 0<=nw<width:
                        if not visited[nh][nw]:
                            visited[nh][nw] = True
                            heapq.heappush(heap, [grid[nh][nw], nh, nw])
            answers[queryIndex] = count
        return answers
a = Solution()
tcs = [[[[1,2,3],[2,5,7],[3,5,1]], [5,6,2]], [[[5,2,1],[1,1,2]], [3]]]
for tc in tcs:
    print(a.maxPoints(*tc))

'''
Algorithm explained:
1. The efficient algorithm takes advantage of previous flood filles from queries already analyzed.
2. We can sort the queries in ascending order and cells which are traveres by previous queries can definitely be tranversed by the current query as the query number is greater than before and before was already greater than cell.
3. We use a heapq to ensure that we select the minimum possible cell value from available neighbours to eplore the cases which are actually reachab
'''
