from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if (m - 1 < 0 or nums[m - 1] != nums[m]) and (
                m + 1 > len(nums) - 1 or nums[m] != nums[m + 1]
            ):
                return nums[m]

            # [1,1,2,3, 3 ,4,4,8,8]
            print(m)

            if nums[m - 1] == nums[m]:
                leftSize = m - 1
            else:
                leftSize = m

            # leftSize = 3
            # if leftSize is odd
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1
            print(l, r)
