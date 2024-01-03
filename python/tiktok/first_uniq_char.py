class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, element in enumerate(s):
            print(element)
            if element not in s[index + 1 :] and element not in s[:index]:
                return index
        return -1

    def firstUniqChar2(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
