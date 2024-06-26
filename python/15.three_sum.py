from typing import List


class Solution:
    """
    https://leetcode.com/problems/3sum
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                Sum = value + nums[left] + nums[right]
                if Sum > 0:
                    right -= 1
                elif Sum < 0:
                    left += 1
                else:
                    results.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return results
