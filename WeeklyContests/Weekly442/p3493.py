# Properties Graph
# Problem link : https://leetcode.com/problems/properties-graph/?slug=maximum-containers-on-a-ship&region=global_v2
'''
Problem description:
You are given a 2D integer array properties having dimensions n x m and an integer k.

Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.

Construct an undirected graph where each index i corresponds to properties[i]. There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k, where i and j are in the range [0, n - 1] and i != j.

Return the number of connected components in the resulting graph.
'''
from typing import List
class Solution:
    def intersect(self, a, b):
        return len(set(a).intersection(set(b)))
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n, m = len(properties), len(properties[0])
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j and (j not in g[i]):
                    if self.intersect(properties[i], properties[j]) >= k:
                        g[i].append(j)
                        g[j].append(i)
        # DFS algorithm to find the number of connected components
        visited = [False for _ in range(n)]
        ncs = 0
        for i in range(n):
            if not visited[i]:
                stack = [i]
                while stack:
                    vi = stack.pop()
                    visited[vi] = True
                    for vj in g[vi]:
                        if not visited[vj]:
                            stack.append(vj)
                ncs += 1    
        return ncs
    
a = Solution()
tcs = [[[[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], 1], [[[1,2,3],[2,3,4],[4,3,5]], 2], [[[1,1],[1,1]], 2]]
for tc in tcs:
    print(a.numberOfComponents(*tc))

'''
Algorithm explained:

1. Based on the given description, we can construct an adjacency list representation of the undirected graph
2. Once the graph is constructed, We can use a simple DFS algorithm to find all the connected components
3. We explore all the vertices of the graph and for each vertex, add it to the stack and we pop it (will be a queue and popleft for BFS) and we add all it's neighbours to the stack and keep exploring until the stack is empty. We mark nodes as visited if we explore all of its nodes.
4. If the while loop ends and we have another unvisited node, we increment the number of connected components by 1
5. Finally, we return the number of connected components
'''