# Problem link : https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04
'''
Problem description:
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
'''
from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = {}
        for domino in dominoes:
            sorted_domino_tuple = tuple(sorted(domino))
            counter[sorted_domino_tuple] = counter.get(sorted_domino_tuple, 0) + 1
        num_equivalent_pairs = 0
        for k, v in counter.items():
            num_equivalent_pairs += v*(v-1)//2
        return num_equivalent_pairs

a = Solution()
tcs = [[[1,2],[2,1],[3,4],[5,6]], [[1,2],[1,2],[1,1],[1,2],[2,2]]]
for tc in tcs:
    print(a.numEquivDominoPairs(tc))

'''
Algorithm explanation: Self explanatory
'''
