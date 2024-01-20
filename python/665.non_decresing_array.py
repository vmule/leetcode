from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        changed = 0

        for i in range(len(nums) - 1):
            # if the next number is increasing just go to the next
            # iteration of the loop
            if nums[i] <= nums[i + 1]:
                continue

            # case 1: [2, 4, 3], i = 1
            # it becomes [2, 3, 3]
            # check if i == 0 to avoid going out of bound
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]

            # case 2: [3, 4, 2], i = 1
            # it becomes [3, 4, 4]
            else:
                nums[i + 1] = nums[i]
            changed += 1

            # if we have changed more than one element return False
            if changed > 1:
                return False

        return True
