class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) < 1:
            return ""

        have_dict = {}
        need_dict = {}

        for e in t:
            need_dict[e] = 1 + need_dict.get(e, 0)

        have = 0
        need = len(need_dict)

        result = [-1, -1]
        resLen = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            have_dict[c] = 1 + have_dict.get(c, 0)

            if c in need_dict and have_dict[c] == need_dict[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    result = [l, r]
                    resLen = r - l + 1
                have_dict[s[l]] -= 1
                if s[l] in need_dict and have_dict[s[l]] < need_dict[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        if resLen != float("infinity"):
            return s[l : r + 1]
        else:
            return ""
