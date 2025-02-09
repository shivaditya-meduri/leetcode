from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        nums_len = len(nums)
        leftSum = 0
        sum_arr = sum(nums)
        count = 0
        for i in range(len(nums)-1):
            leftSum = leftSum + nums[i]
            rightSum = sum_arr - leftSum
            if (leftSum-rightSum)%2 == 0:
                count += 1
        return count

a = Solution()
tcs = [[10, 10, 3, 7, 6], [1, 2, 2], [2, 4, 6, 8]]
for tc in tcs:
    print(a.countPartitions(nums=tc))
