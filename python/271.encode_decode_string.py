class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.

    https://www.lintcode.com/problem/659/

    """

    def encode(self, strs):
        # write your code here
        encoded = ""

        if len(strs) < 1:
            return encoded

        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string

        return encoded

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, _str):
        # write your code here

        if len(_str) < 1:
            return []

        decoded = []
        i = 0

        while i < len(_str):
            j = i
            while _str[j] != "#":
                j += 1

            length = int(_str[i:j])
            word_end = j + length
            decoded.append(_str[j + 1 : word_end + 1])
            i = word_end

        return decoded
