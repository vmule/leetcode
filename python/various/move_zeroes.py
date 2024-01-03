from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for index, element in enumerate(nums):
            if element == 0:
                nums.pop(index)
                nums.append(element)

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Insert the non zero elements starting from 0 index, then replace everything else with zeros
        """

        count = 0
        for index, element in enumerate(nums):
            if element != 0:
                nums[count] = nums[index]
                count += 1
        while count < len(nums):
            nums[count] = 0
            count += 1
