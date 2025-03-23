# Count the Number of Complete Components
# Problem Link : https://leetcode.com/problems/count-the-number-of-complete-components/description/?envType=daily-question&envId=2025-03-22
'''
Problem description:
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.
'''
from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list.
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = [False] * n
        complete_count = 0
        
        # Traverse each component using BFS.
        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True
                nodes = []
                edgeCount = 0  # Will count each edge twice.
                
                while queue:
                    node = queue.popleft()
                    nodes.append(node)
                    edgeCount += len(g[node])
                    for neighbor in g[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Since each edge is counted twice, divide by 2.
                edgeCount //= 2
                m = len(nodes)
                # Check if the component is complete.
                if edgeCount == m * (m - 1) // 2:
                    complete_count += 1
                    
        return complete_count
tcs = [[6, [[0,1],[0,2],[1,2],[3,4]]], [6, [[0,1],[0,2],[1,2],[3,4],[3,5]]], [3, [[2,0],[2,1]]], [4, [[1,0],[3,1],[3,2]]]]
a = Solution()
for tc in tcs:
    print(a.countCompleteComponents(*tc))
'''
Algorithm explained:
1. Construct an adjacency list data structure to store the undirected unweighted graph
2. iterate through all the vertices of the graph
3. if the vertex is unvisited, then we add it to the doubly linked list (BFS) or just a list (DFS)
4. Then while the queue (doubly linked list)(BFS)/stack(dfs) is non-empty, pop (stack DFS) or popleft (doubly linked list DFS), add it to the nodes list (helps count the number of elements in a connected component)
5. explore all the neighbours and mark them as visied and append them to the stack / doubly linked list
6. For each popped node, add the number of edges to the edge count.
7. Each edge is counted twice because it is an undirected graph, and if the edge count is equal to n*(n-1)/2, then it is a complete graph
'''
