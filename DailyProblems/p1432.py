# Problem link : https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/?envType=daily-question&envId=2025-06-15
# Find the difference between max and min num that can be created by changing the all occurences of a digit to another once separately without leading 0s
class Solution:
    def maxDiff(self, num: int) -> int:
        # Find the maximum number
        digits = []
        curr = num
        while curr!=0:
            digits.append(curr%10)
            curr = curr//10
        MSD_not9 = None
        for di in reversed(digits):
            if di!=9:
                MSD_not9 = di
                break
        max_num = 0
        for ind, di in enumerate(digits):
            if di != MSD_not9:
                max_num += 10**ind * di
            else:
                max_num += 10**ind * 9
        # Find the minimum number
        if digits[-1] == 1:
            MSD_not1or0 = None
            for di in reversed(digits[:-1]):
                if di!=1 and di!=0:
                    MSD_not1or0 = di
                    break
            min_num = 0
            for ind, di in enumerate(digits):
                if di!=MSD_not1or0:
                    min_num += 10**ind * di
        else:
            MSD = digits[-1]
            min_num = 0
            for ind, di in enumerate(digits):
                if di == MSD:
                    min_num += 10**ind
                else:
                    min_num += 10**ind * di
        return max_num - min_num 

'''
Algorithm explained:
1. For the max number, find the most significant non 9 digit and convert it to 9
2. For the min num, if the Most significant digit is not 1, then convert it to 1, else, for the remaining digits, find the most significant non 1 non 0 element
and convert it to 0
3. Return the difference
4. Is this more efficient than checking all the possible numbers that can be created?
            
