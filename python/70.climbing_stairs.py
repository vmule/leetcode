class Solution:
    def climbStairs(self, n: int) -> int:
        # looks like fibonacci
        one = 1
        two = 1

        for _ in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one
