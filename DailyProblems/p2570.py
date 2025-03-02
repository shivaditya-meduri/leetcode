# Problem link : https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02
'''
Problem description:
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.
'''
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        agg_nums = []
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1][0]<nums2[p2][0]:
                agg_nums.append(nums1[p1])
                p1 += 1
            elif nums1[p1][0]>nums2[p2][0]:
                agg_nums.append(nums2[p2])
                p2 += 1
            else:
                agg_nums.append([nums1[p1][0], nums1[p1][1]+nums2[p2][1]])
                p1 += 1
                p2 += 1
        while p1<len(nums1):
            agg_nums.append(nums1[p1])
            p1+=1
        while p2<len(nums2):
            agg_nums.append(nums2[p2])
            p2+=1
        return agg_nums
