from typing import List


class Solution:
    """
    https://leetcode.com/problems/product-of-array-except-self
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * postfix
            postfix = postfix * nums[i]
        return answer
