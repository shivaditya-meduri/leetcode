### Efficient solution using sieving
from typing import List
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        MAX = 10**5 + 1
        minIndex = [float('inf')]*MAX
        for i, e in enumerate(elements):
            if i<minIndex[e]:
                minIndex[e] = i
        bestCandidates = [float('inf')]*MAX
        for d in range(1, MAX):
            if minIndex[d] != float('inf'):
                for m in range(d, MAX, d):
                    if minIndex[d] < bestCandidates[m]:
                        bestCandidates[m] = minIndex[d]
        result = []
        for gi in groups:
            if bestCandidates[gi] == float('inf'):
                result.append(-1)
            else:
                result.append(bestCandidates[gi])
        return result