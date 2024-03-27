class Solution:
    def isUgly(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                break

        return n == 1

        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
            if n == 1:
                break
        return n == 1
