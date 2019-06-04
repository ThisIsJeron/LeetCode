# 929. Unique Email Addresses - Easy

# Initial thoughts:
# Thought of using helper functions but this is easily doable without

# Implementation:

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        toReturn = 0
        for x in range(0, len(emails)):
            atSplit = emails[x].split("@")
            plusSplit = atSplit[0].split("+")
            periodSplit = plusSplit[0].split(".")
            toCheck = ""
            for y in periodSplit:
                toCheck += y
            toCheck = toCheck + "@" + atSplit[1]
            emails[x] = ""
            if toCheck not in emails:
                emails[x] = toCheck
                toReturn += + 1
        return toReturn

# Afterthoughts:
# String manipulation tricks helped, learn how to use split. Printing takes a
# lot of runtime. Almost duplicated the array, but was able to do it in place. 

# Results:
# Runtime: 48 ms, faster than 78.29% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 13.2 MB, less than 55.53% of Python3 online submissions for Unique Email Addresses.
