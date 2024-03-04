from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result = 0
        score = 0

        tokens.sort()
        l = 0
        r = len(tokens) - 1

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                result = max(result, score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        return result
