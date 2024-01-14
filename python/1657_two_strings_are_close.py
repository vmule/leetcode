from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count_w1 = Counter(word1)
        count_w2 = Counter(word2)

        w1_occurrences = {}
        w2_occurrences = {}

        for e in count_w1.values():
            w1_occurrences[e] = w1_occurrences.get(e, 0) + 1
        for e in count_w2.values():
            w2_occurrences[e] = w2_occurrences.get(e, 0) + 1

        # Worse runtime, better memory space
        # if sorted(count_w1.values()) == sorted(count_w2.values()) and set(word1) == set(word2)

        # Better runtime, worse memory space
        if w1_occurrences == w2_occurrences and set(word1) == set(word2):
            return True
        return False
