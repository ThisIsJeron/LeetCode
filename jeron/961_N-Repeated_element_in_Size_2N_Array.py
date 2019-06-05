# 929. 961. N-Repeated Element in Size 2N Array - Easy

# Initial thoughts:
# initially thought of checking number of times an item shows up and seeing if
# it matched len(A)/2 and removing the items if it did not. However, stumbled upon
# this library

# Implementation:

from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        test = Counter(A)
        for key,val in test.items():
            if val == len(A)/2:
                return key


# Afterthoughts:
# It's not very fast. Also, don't know if we can use this library.

# Results:
# Runtime: 56 ms, faster than 54.27% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 14.4 MB, less than 5.23% of Python3 online submissions for N-Repeated Element in Size 2N Array.
