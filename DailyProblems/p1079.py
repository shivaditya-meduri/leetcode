# Problem link : https://leetcode.com/problems/letter-tile-possibilities/description/?envType=daily-question&envId=2025-02-17
'''
Problem description:
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
'''
# Recursive solution
from collections import Counter
import math
class Solution:
    def count_r(self, index, remaining, current, all_dist):
            result = 0
            if index == len(all_dist):
                # Base Case
                if remaining == 0:
                    tot_arrangements = math.factorial(sum(current))
                    for ri in current:
                        tot_arrangements = tot_arrangements//math.factorial(ri)
                    return tot_arrangements
                else:
                    return 0
            else:
                # Other cases
                max_use = min(all_dist[index], remaining)
                for use in range(max_use+1):
                    result += self.count_r(index+1, remaining-use, current+[use], all_dist)
                return result
    def numTilePossibilities(self, tiles: str) -> int:
        tot_cnt = len(tiles)
        all_dist = list(Counter(list(tiles)).values())
        ways = 0
        for r in range(1, tot_cnt+1):
            ways += self.count_r(0, r, [], all_dist)
        return ways
