class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        map_s = []
        map_t = []

        i = 0
        while i < len(s):
            if s[i] in dict_s:
                map_s.append(dict_s[s[i]])
            else:
                dict_s[s[i]] = i
                map_s.append(dict_s[s[i]])

            if t[i] in dict_t:
                map_t.append(dict_t[t[i]])
            else:
                dict_t[t[i]] = i
                map_t.append(dict_t[t[i]])
            i += 1
        return map_s == map_t
