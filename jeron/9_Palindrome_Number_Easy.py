# 9. Palindrome Number - Easy

# Initial thoughts:
# I had solved this in the past but I forgot the solution so starting from fresh
# I wanted to use double for loops and compare each character which is dumb

# Implementation:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy = str(x)

        if str(x) == copy[::-1]:
            return True
else:
    return False

# Afterthoughts:
# it works I guess

# Results:
# Runtime: 80 ms, faster than 77.47% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.3 MB, less than 46.56% of Python3 online submissions for Palindrome Number.
