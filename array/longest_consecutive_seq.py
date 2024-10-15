"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""
def LIS(nums):
    nums_set = set(nums)
    res = 0

    for num in nums:
        sequence = 1
        if num - 1 not in nums_set:
            while sequence + num in nums_set:
                sequence += 1
        res = max(res, sequence)
    return res

print(4 == LIS([100, 4, 200, 1, 3, 2]))
print(9 == LIS([0,3,7,2,5,8,4,6,0,1]))