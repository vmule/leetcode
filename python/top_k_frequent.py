from typing import Dict
from typing import List


class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-elements
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # _dict = {}
        _dict: Dict[int, int] = {}
        output = []
        for element in nums:
            if element in _dict:
                _dict[element] += 1
            else:
                _dict[element] = 1
        for _ in range(k):
            champion = max(_dict, key=_dict.get)
            output.append(champion)
            del _dict[champion]
        return output
