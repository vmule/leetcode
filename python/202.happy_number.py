class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            if n == 1:
                return True

            seen.add(n)
            n = self.sumOfSquares(n)
        return False

    def sumOfSquares(self, n):
        output = 0
        while n != 0:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output
