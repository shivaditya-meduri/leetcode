# Number of ways to arrive at a destination
# Problem link : https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/?envType=daily-question&envId=2025-03-23
'''
Problem description:
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 10^9 + 7.
'''
import heapq
class Solution:
    def dijkstras(self, g, start, end):
        # Return the shortest path (time taken)
        dmap = {k: float('inf') for k in g.keys()}
        dmap[start] = 0
        previous = {k: None for k in g.keys()}
        previous[start] = start
        pq = [[0, start]]
        n = len(g.keys())
        count = {node:0 for node in g.keys()}
        count[start] = 1
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > dmap[curr_node]:
                continue
            for node, time in g[curr_node]:
                new_dist = curr_dist+time
                if new_dist < dmap[node]:
                    dmap[node] = new_dist
                    previous[node] = curr_node
                    count[node] = count[curr_node]
                    heapq.heappush(pq, [new_dist, node])
                elif new_dist == dmap[node]:
                    count[node] += count[curr_node]
        if dmap[end]!=float('inf'):
            shortest_path = [end]
            curr = end
            while curr != start:
                shortest_path.append(previous[curr])
                curr = previous[curr]
            shortest_path = shortest_path[::-1]
        else:
            shortest_path = []
#         return dmap[end], shortest_path, count[end]
        return count[end]%(10**9 + 7)
        
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = {k:[] for k in range(n)}
        for ui, vi, ti in roads:
            g[ui].append([vi, ti])
            g[vi].append([ui, ti])
        
        return self.dijkstras(g, 0, n-1)

a = Solution()
tcs = [[7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]], [2, [[1,0,10]]]]
for tc in tcs:
    print(a.countPaths(*tc))

'''
Algorithm explained:
1. Construct an adjacency list representation of the undirected graph
2. Implement dijkstra's algorithm which finds the shortest distance and the shortest path
3. To calculate the number of shortest paths possible, we simply have to maintain a count dictionary where count[node] represents the number of paths from start node to that node.
4. We set count[start] = 1
5. If we find a strictly shorter distance to a neighbour node, then we update the count[neighbour_node] to count[curr_node]
6. If we find equal shorter distance, we just update count[node] += count[curr_node]
7. We return count[end] which is the number of possible shortest paths from the start node to the end node.

'''
