class Solution:

    def isOneEditDistance(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return False

        if abs(len(s1) - len(s2)) > 1:
            return False

        counter = 0
        s1_index = 0
        s2_index = 0

        if len(s2) < len(s1):
            s1, s2 = s2, s1

        while s1_index < len(s1) and s2_index < len(s2):
            if s1[s1_index] != s2[s2_index]:
                counter += 1
                if len(s1) == len(s2):
                    s1_index += 1
            elif s1[s1_index] == s2[s2_index]:
                s1_index += 1
            s2_index += 1
            if counter > 1:
                return False
        return True


a = Solution()
assert a.isOneEditDistance("cat", "cut") is True
assert a.isOneEditDistance("cat", "chat") is True
assert a.isOneEditDistance("cat", "at") is True
assert a.isOneEditDistance("at", "cat") is True
assert a.isOneEditDistance("cat", "dog") is False
assert a.isOneEditDistance("cat", "act") is False
assert a.isOneEditDistance("cat", "cat") is False
assert a.isOneEditDistance("dog", "doggo") is False
assert a.isOneEditDistance("a", "calamaro") is False
assert a.isOneEditDistance("a", "aaaaaaaaaaaaaaaaaaaaaaa") is False

print("All tests passed!!")
