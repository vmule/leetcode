class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # char/words mapped to the initial index where they appear
        dict_p = {}
        dict_s = {}

        seq_p = []
        seq_s = []

        for index, char in enumerate(pattern):
            if char in dict_p:
                seq_p.append(dict_p[char])
            else:
                dict_p[char] = index
                seq_p.append(dict_p[char])

        for index, word in enumerate(s.split()):
            if word in dict_s:
                seq_s.append(dict_s[word])
            else:
                dict_s[word] = index
                seq_s.append(dict_s[word])

        return seq_p == seq_s
