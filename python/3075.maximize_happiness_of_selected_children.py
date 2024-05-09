class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        decrement = 0
        happiness.sort()
        result = 0

        while k > 0:
            happy_value = happiness[-1] + decrement
            if happy_value > 0:
                result += happy_value
            decrement -= 1
            happiness.pop()
            k -= 1
        
        return result
