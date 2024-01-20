from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        for i in matches:
            # winners
            winners[i[0]] = winners.get(i[0], 0) + 1
            # losers
            losers[i[1]] = losers.get(i[1], 0) + 1

        answer = [[] for _ in range(2)]

        for key, value in winners.items():
            if winners[key] >= 1 and key not in losers:
                answer[0].append(key)

        for key, value in losers.items():
            if value == 1:
                answer[1].append(key)

        return sorted(answer[0]), sorted(answer[1])
