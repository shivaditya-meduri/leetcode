# Problem link : https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/?envType=daily-question&envId=2025-06-14
# Find the difference of the max and the min number which can be created by changing all occurrences of exactly one digit in the num to any digit in 0-9
class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Optimal
        curr = num
        digits = []
        while curr!=0:
            digits.append(curr%10)
            curr = curr//10
        MSD_not9 = None
        for di in reversed(digits):
            if di != 9:
                MSD_not9 = di
                break
        MSD_not0 = None
        for di in reversed(digits):
            if di != 0:
                MSD_not0 = di
                break
        max_num, min_num = 0, 0
        for ind, di in enumerate(digits):
            if di == MSD_not9:
                max_num += 9 * 10**ind
            else:
                max_num += di * 10**ind
            if di != MSD_not0:
                min_num += di * 10**ind
        return max_num - min_num
            

    def minMaxDifference_bruteforce(self, num: int) -> int:
        # Brute Force solution
        curr = num
        digits = []
        while curr!=0:
            digits.append(curr%10)
            curr = curr//10
        digits_unique = set(digits)
        max_num, min_num = num, num
        for di in digits_unique:
            # max di -> 9
            num_max_i = 0
            for ind, dj in enumerate(digits):
                if dj == di:
                    num_max_i += (10**ind)*9
                else:
                    num_max_i += (10**ind)*dj
            max_num = max(max_num, num_max_i)
            # min di -> 0
            num_min_i = 0
            for ind, dj in enumerate(digits):
                if dj == di:
                    num_min_i += (10**ind)*0
                else:
                    num_min_i += (10**ind)*dj
            min_num = min(min_num, num_min_i)
        return max_num-min_num
'''
Optimal Algorithm:
1. Find the mast significant non 9 digit and convert it to 9 and apply that mapping for all the digits and that gives the maximum number which can be created
2. Do the same as above but instead of most significant non-9 digit, take the most significant non-0 digit and map it to 0
3. Calculate the difference and return it
'''
