class Solution:
    def reverse(self, x: int) -> int:
        upperlimt = 2**31 - 1
        lowerlimit = -(2**31)
        negative = False
        if x < 1:
            negative = True
        a = str(abs(x))
        res = int(a[::-1])
        if negative:
            if -1 * res >= lowerlimit:
                return -1 * res
        elif res <= upperlimt:
            return res
        return 0
