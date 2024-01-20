from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if two reminders are the same it means their sum is a multiple of the element
        # they were % by

        # store the reminders in a hashmap with their index as value
        # if we find another reminder that is equal
        # we calculate the distance, and if it's >= 2 we return true

        rem = {}
        rem[0] = -1
        total = 0

        for index, value in enumerate(nums):
            total += value
            reminder = total % k

            if reminder in rem:
                l_index = rem[reminder]
                if index - l_index >= 2:
                    return True
            else:
                rem[reminder] = index
        return False
