"""
Problem definition:
We want to build a function that can find and count keywords in an input document, as well as generating a short snippet from the input text that contains all of the searched keywords.
We'd also like to optionally ignore the case of both input and keywords when performing the search.
More specifically:
Given the input:
```
  "document": <string>,
  "keywords": [<string>, ...],
  "ignore_case": <boolean>
```
Produce an output containing:
```
  "match": <boolean>
  "counts": {
    <string>: <int>
  },
  "snippet": <string>
```
where:
 - *match*: true iff all keywords in `keywords` appear in `document` at least once
 - *count*: a count of how many times each keyword appears in `document`
 - *snippet*: a substring of `document` that contains all keywords at least once (ideally, the shortest such substring)
For example, given the input:
```
  "document": "Fuzzy Wuzzy was a bear, Fuzzy Wuzzy had no hair, Fuzzy Wuzzy wasn't fuzzy, was he?",
  "keywords": ["fuzzy", "wuzzy", "bear"],
  "ignore_case": true
```
The expected output would be:
```
  "match": true,
  "counts": {
    "fuzzy": 4,
    "wuzzy": 3,
    "bear": 1
  },
  "snippet": "bear, Fuzzy Wuzzy"
```
Note that:
 - Regardless of the value of 'ignoreCase', the case in the output should be the same as originally supplied in the input.
    (e.g. the keys in 'counts' should match 'keywords', and 'snippet' should preserve the case of 'document')
 - If 'match' is false, the value of the other two output fields is undefined, and can be set to implementation-convenient values.

"""
import re
from collections import Counter


def Search(document, keywords, ignore_case=True):

    if ignore_case:
        document = document.lower()

    raw_words = document.split(" ")

    stripped_words = []
    pattern = re.compile("[\W_]+")
    for e in raw_words:
        w = pattern.sub("", e)
        stripped_words.append(w)

    have = 0
    resLen = len(stripped_words) + 1
    result = [-1, -1]

    count_have = {}
    count_need = Counter(keywords)
    need = len(count_need)
    left = 0

    for right in range(len(stripped_words)):
        w = stripped_words[right]
        count_have[w] = count_have.get(w, 0) + 1

        if w in count_need and count_have[w] == count_need[w]:
            have += 1
        while have == need:
            left_w = stripped_words[left]
            if (right - left + 1) < resLen:
                result = [left, right]
                resLen = right - left + 1
            count_have[left_w] -= 1
            if left_w in count_need and count_have[left_w] < count_need[left_w]:
                have -= 1
            left += 1

    left, right = result
    if resLen < len(stripped_words) + 1:
        snippet = " ".join(raw_words[left : right + 1])
    else:
        snippet = ""

    # if snippets is not found it means not all keywords are present
    # count keywords only if snippet is found

    match = False
    counts = {}

    if len(snippet) > 0:
        match = True
        general_counts = Counter(stripped_words)

        for keyword in keywords:
            if ignore_case:
                if keyword.lower() not in general_counts:
                    return {"match": False, "counts": {}, "snippet": ""}
                else:
                    counts[keyword] = general_counts.get(keyword.lower())
            else:
                if keyword not in general_counts:
                    return {"match": False, "counts": {}, "snippet": ""}
                else:
                    counts[keyword] = general_counts.get(keyword)

    return {"match": match, "counts": counts, "snippet": snippet}


print(" ")
document = (
    "Fuzzy Wuzzy was a bear, Fuzzy Wuzzy had no hair, Fuzzy Wuzzy wasn't fuzzy, was he?"
)


ignore_case = False
keywords = ["fuzzy", "wuzzy", "bear"]
result = Search(document, keywords, ignore_case)
# print(result)
assert result["match"] is False
print("Test 1: passed")
print(" ")

ignore_case = False
keywords = ["Frank", "wuzzy", "bear"]
result = Search(document, keywords, ignore_case)
# print(result)
assert result["match"] is False
print("Test 2: passed")
print(" ")

ignore_case = False
keywords = ["Fuzzy", "Wuzzy", "bear"]
result = Search(document, keywords, ignore_case)
# print(result)
assert result["match"] is True
assert result["snippet"] == "bear, Fuzzy Wuzzy"
print("Test 3: passed")
print(" ")

ignore_case = True
keywords = ["fuzzy", "wuzzy", "bear"]
result = Search(document, keywords, ignore_case)
# print(result)
assert result["match"] is True
assert result["snippet"] == "bear, fuzzy wuzzy"
print("Test 4: passed")
print(" ")

ignore_case = True
keywords = ["Frank", "wuzzy", "bear"]
result = Search(document, keywords, ignore_case)
# print(result)
assert result["match"] is False
print("Test 5: passed")
print(" ")
