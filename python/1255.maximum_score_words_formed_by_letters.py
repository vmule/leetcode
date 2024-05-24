class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def can_form_word(word, letter_count):
            word_count = Counter(word)
            for c in word_count:
                print(c)
                if word_count[c] > letter_count.get(c, 0):
                    return False
            return True

        def get_score(word):
            word_score = 0
            for c in word:
                word_score += score[ord(c) - 97]
            return word_score

        def backtrack(i):
            if i == len(words):
                return 0
            result = backtrack(i+1)
            if can_form_word(words[i], letter_count):
                for c in words[i]:
                    letter_count[c] -= 1
                result = max(result, get_score(words[i]) + backtrack(i+1))
                for c in words[i]:
                    letter_count[c] += 1
            return result

        letter_count = Counter(letters)
        return backtrack(0)
