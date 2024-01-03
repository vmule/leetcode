from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            myMap[key].append(string)

        return myMap.values()
