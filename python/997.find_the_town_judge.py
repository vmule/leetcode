from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) == n:
            return -1
        if n == 1 and len(trust) == 0: 
            return 1
        if n >= 1 and len(trust) == 0:
            return -1

        trust_count = defaultdict(int)
        trusters = defaultdict(int)
        for e in trust:
            trust_count[e[1]] += 1
            trusters[e[0]] += 1

        for key, value in trust_count.items():
            if value == n-1 and key not in trusters:
                return key
        return -1
