from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        max_num = max(nums)
        left = 0
        result = 0
        count = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == max_num:
                count += 1
            while count >= k:
                result += n - right
                if nums[left] == max_num:
                    count -= 1
                left += 1
        return result
