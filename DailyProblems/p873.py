# Problem link : https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-02-27
'''
Problem description:
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
'''
from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        maxArr = arr[-1]
        arrSet = set(arr)
        bestSeries = []
        for i in range(n-2):
            for j in range(i+1, n-1):
                fib0, fib1 = arr[i], arr[j]
                series = [fib0, fib1]
                while True:
                    fib2 = fib0 + fib1
                    if fib2 in arrSet:
                        series.append(fib2)
                        fib0, fib1 = fib1, fib2
                    else:
                        if (len(series)>=3) and (len(series) > len(bestSeries)):
                            bestSeries = series
                        break
        return len(bestSeries)

a = Solution()
tcs = [[1,2,3,4,5,6,7,8], [1,3,7,11,12,14,18]]
for tc in tcs:
    print(a.lenLongestFibSubseq(arr=tc))
