"""
Given an array nums of distinct integers, return all the possible
permutations
. You can return the answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

"""

class Solution:
    def permute(self, nums):
        res = []
        def helper(nums, index, res):
            if index >= len(nums):
                res.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                helper(nums, index + 1, res)
                # Backtracking - So the permutation of all the string
                # Should be generated from the original string.
                nums[index], nums[i] = nums[i], nums[index]
        helper(nums, 0, res)
        return res

s = Solution()
print(s.permute([1,2,3]))