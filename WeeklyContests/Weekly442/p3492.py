# Maximum Containers on a ship
# Problem link : https://leetcode.com/problems/maximum-containers-on-a-ship/
'''
Problem description:
You are given a positive integer n representing an n x n cargo deck on a ship. Each cell on the deck can hold one container with a weight of exactly w.

However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, maxWeight.

Return the maximum number of containers that can be loaded onto the ship.
'''
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        totalWeight = w * n**2
        if totalWeight <= maxWeight:
            return n**2
        else:
            return maxWeight//w
        
# Simple algorithm, no need to explain
