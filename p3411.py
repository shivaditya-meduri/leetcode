# Maximum Subarray With Equal Products
# Link : https://leetcode.com/problems/maximum-subarray-with-equal-products/description/

from math import gcd
from functools import reduce
class Solution:
    def gcd(self, arr):
        return reduce(gcd, arr)
    def lcm(self, arr):
        lcm2nums = lambda a, b: abs(a*b)//gcd(a, b)
        return reduce(lcm2nums, arr)
    def is_product_equivalent(self, arr):
        multiply = lambda a,b : a*b
        if reduce(multiply, arr) == self.lcm(arr) * self.gcd(arr):
            return True
        else:
            return False
    def maxLength(self, nums: List[int]) -> int:
        len_nums = len(nums)
        maxlen = 0
        for i in range(len_nums):
            for j in range(i+1, len_nums+1):
                subarr = nums[i:j]
                if self.is_product_equivalent(subarr):
                    maxlen = max(maxlen, j-i)
                
        return maxlen    
    
