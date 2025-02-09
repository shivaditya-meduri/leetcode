# Problem link : https://leetcode.com/problems/count-number-of-bad-pairs/?envType=daily-question&envId=2025-02-09
from typing import List
from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ### Optimized
        # nums[j]-nums[i] != j-i can be rearranged as nums[j]-j != nums[i]-i
        n = len(nums)
        d = Counter([nums[i]-i for i in range(n)])
        tot_pairs = n*(n-1)//2 # nc2
        nb_good_pairs = 0
        for val, count in d.items():
            nb_good_pairs += count*(count-1)//2
        nb_bad_pairs = tot_pairs - nb_good_pairs
        return nb_bad_pairs