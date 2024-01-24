from typing import List


class Solution:
    # n * logn, actually, will need to rewrite
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1

            if len(nums) == 1 and nums[0] == target:
                return 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return 0

        res = False
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                if binary_search(row, target):
                    res = True
            else:
                continue
        return res
