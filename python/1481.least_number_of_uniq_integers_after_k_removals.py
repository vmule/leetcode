from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = [[] for _ in range(len(arr) + 1)]
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
            freq[value].append(key)

        i = 1
        result = len(count)
        print(freq)
        while i < len(freq) and k > 0:
            for _ in freq[i]:
                if k >= i:
                    k -= i
                    result -= 1
                else:
                    break
            i += 1
        return result
