# 771. Jewels and Stones - Easy

# Initial thoughts:
# I had solved this in the past too but I forget how I solved it
# I wanted to use double for loops and compare each character - brute force. This actually worked

# Implementation:

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        toReturn = 0
        for x in J:
            for y in S:
                if x == y:
                    S.remove(y)
                    toReturn += 1

        return toReturn

# Afterthoughts:
# Whatever my Java solution was, it was better

# Results:
# Runtime: 28 ms, faster than 99.45% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.1 MB, less than 70.45% of Python3 online submissions for Jewels and Stones.
