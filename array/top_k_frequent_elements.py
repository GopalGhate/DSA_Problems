"""
TC  = K * log M
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

from heapq import heapify, heappush, heappop
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        freq_hash = Counter(nums)
        heap = [(-freq, num) for num, freq in freq_hash.items()]
        heapify(heap)
        res = []
        while k > 0:
            freq, num = heappop(heap)
            res.append(num)
            k -= 1
        return res
s = Solution()
print([1, 2] == s.topKFrequent([1,1,1,2,2,3], 2))