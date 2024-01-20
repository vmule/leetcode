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

        _len = 0
        for string in strs:
            _len = len(string) + 2
            encoded = encoded + str(_len) + "#" + string

        return encoded

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, _str):
        # write your code here

        decoded = []

        if len(_str) < 1:
            return decoded

        left, right = 0, 0

        while right < len(_str):
            left = right + 2
            right = right + int(_str[(right)])
            decoded.append(_str[left:right])

        return decoded
