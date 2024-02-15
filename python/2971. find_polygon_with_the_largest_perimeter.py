class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        sidesSum = 0
        area = 0

        for i in nums:
            if sidesSum > i:
                area = sidesSum + i
            sidesSum += i
        return area
