from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        max = len(digits) - 1
        for i in range(max, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        digits.insert(0, 1)
        return digits
