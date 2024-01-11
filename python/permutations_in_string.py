class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}
        window_size = 0

        for e in s1:
            s1_count[e] = 1 + s1_count.get(e, 0)

        for l in range(len(s2)):
            char = s2[l]
            s2_count[char] = 1 + s2_count.get(char, 0)
            window_size += 1

            if window_size == len(s1):
                if s2_count == s1_count:
                    return True

                first_index = l - (window_size - 1)

                if s2_count.get(s2[first_index]) == 1:
                    s2_count.pop(s2[first_index])
                else:
                    s2_count[s2[first_index]] -= 1
                window_size -= 1

        return False
