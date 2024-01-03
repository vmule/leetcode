from typing import Dict
from typing import List
from typing import Set


class Solution:
    """
    https://leetcode.com/problems/top-k-frequent-elements
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Alternative solutions, fails for very large list

        # nums_set: Set[int] = set(nums)
        # output: List[int] = []
        #
        # for _ in range(k):
        #     output.append(max(nums_set, key=nums.count))
        #     nums_set.remove(output[-1])
        # return output

        my_dict: Dict[int, int] = {}
        output: List[int] = []

        for element in nums:
            if element in my_dict:
                my_dict[element] += 1
            else:
                my_dict[element] = 1
        for _ in range(k):
            champion = max(my_dict, key=my_dict.__getitem__)
            output.append(champion)
            del my_dict[champion]
        return output
