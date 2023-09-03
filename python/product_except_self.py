from typing import List


class Solution:
    """
    https://leetcode.com/problems/product-of-array-except-self
    """

    def prod(self, nums: List[int]) -> int:
        result = 1
        for _, e in enumerate(nums):
            result = result * e
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prod = self.prod(nums)
        for index, value in enumerate(nums):
            # print(index)
            if value == 0:
                nums[index] = 1
                nonzero_prod = self.prod(nums)
                answer.append(nonzero_prod)
                nums[index] = 0
            else:
                answer.append(prod // nums[index])
        return answer
