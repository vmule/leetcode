from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums

        xor = 0
        for n in nums:
            xor ^= n
        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit = diff_bit << 1

        a = 0
        b = 0
        for n in nums:
            if diff_bit & n:
                a ^= n
            else:
                b ^= n

        return [a, b]
