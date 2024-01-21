from typing import List


class Solution:
    """
    https://leetcode.com/problems/search-in-rotated-sorted-array
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # if the value at mid is greather or equal then the most left value
            # we are in the left sorted portion of the array left portion
            # target = 0
            # [4,5,6,7,0,1,2]
            # middle would be 7
            # 7 >= 4
            if nums[mid] >= nums[left]:
                # [4,5,6,7] target = 0, l = 4, mid = 7
                # if target is greater than the value at index mid
                # or the smaller than the value at index left
                # it means our result is in the part of the array between mid+1 and right
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                # else it means our result is in the array between left and mid-1
                else:
                    right = mid - 1
            # if not we are in the array sorted right portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
