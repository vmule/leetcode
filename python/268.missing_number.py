class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        setN = set(nums)
        for n in range(len(nums)+1):
            if n not in setN:
                return n
