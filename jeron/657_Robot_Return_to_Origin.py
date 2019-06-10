# 657. Robot Return to Origin - Easy

# Initial thoughts:
# make a list x and y and 4 if statements

# Implementation:

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        A = [0, 0]
        moves = list(moves)
        for x in moves:
            if x == 'U':
                A[1] += 1
            if x == 'D':
                A[1] -= 1
            if x == 'R':
                A[0] += 1
            if x == 'L':
                A[0] -= 1
        if A[0] == 0 and A[1] == 0:
            return True
        else:
            return False

# Afterthoughts:
# Not fast.

# Results:
# Runtime: 88 ms, faster than 13.85% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 13.4 MB, less than 18.13% of Python3 online submissions for Robot Return to Origin.
