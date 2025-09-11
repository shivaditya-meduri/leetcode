# Find the minimum amount of time to brew potions
# Problem link : https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/?slug=properties-graph&region=global_v2
'''
Problem description:
You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.
'''
from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # n wizards and m potions
        n, m = len(skill), len(mana)
        # Time sheet
        ts = [None for _ in range(n+1)]
        start_time = 0
        m_endtimes = []
        for mi in range(m):
            ts[0] = start_time
            for wi in range(1, n+1):
                ts[wi] = ts[wi-1] + skill[wi-1]*mana[mi]
            m_endtimes.append(ts[-1])
            if mi != m-1:
                prefix_sum = [0]
                for j in range(n):
                    prefix_sum.append(prefix_sum[-1]+skill[j]*mana[mi+1])
                start_time = max([ts[wj]-(prefix_sum[wj-1]) for wj in range(1, n+1)])
        minTime = max(m_endtimes)
        return minTime
    
tcs = [[[1,5,2,4], [5,1,4,2]], [[1, 1, 1], [1, 1, 1]], [[1,2,3,4], [1, 2]]]
a = Solution()
for tc in tcs:
    print(a.minTime(*tc))


'''
Algorithm explained:
1. We just have to find a minimum valid start time for potion j such that a potion can be brewed sequentially without any gaps when wizards are free.
2. We take the start time for jth potion as x and we can identify the start times of each wizard. We then have to see the previous start and end times of each wizard to see what is the minimum feasible start time for jth potion.
3. For the 0th potion, the valid start time is 0 and for the subsequent potions, we have to find the minimum valid start time for each potion.
4. After we have the end times for each of the potions, we can just return the max end time which is the minimum time required to brew all the potions.
'''
