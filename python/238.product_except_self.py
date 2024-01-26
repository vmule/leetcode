from typing import List


class Solution:
    """
    https://leetcode.com/problems/product-of-array-except-self
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums))

        # set initial prefix to 1, which is out of bound, before the array begins
        prefix = 1
        for i in range(len(nums)):
            # for each element in nums, set ans at index i to the prefix
            # then multiply the value in nums at index i by the prefix
            # [1,2,3,4]
            # 1 * 1
            # 1 * 1
            # 1 * 2
            # 2 * 3
            # [1,1,2,6]
            answer[i] = prefix
            prefix = prefix * nums[i]

        # set initial postfix to 1, which is out of bound, after the array end
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # going in reverse
            # for each element in nums, set and at index i to the postfix
            # then multiply the value in ans at index i by the postfix
            # 1 * 6
            # 4 * 2
            # 12 * 1
            # 24 * 1
            answer[i] = answer[i] * postfix
            postfix = postfix * nums[i]

        return answer
