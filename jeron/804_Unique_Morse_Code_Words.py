# 804. Unique Morse Code Words - Easy

# Initial thoughts:
# Similar to the last one in that we are overwriting the original array

# Implementation:

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        toReturn = 0
        for y in range(0, len(words)):
            toReplace = ""
            for x in words[y]:
                toReplace = toReplace + morse[ord(x) - 97]
            if toReplace not in words:
                words[y] = toReplace
                toReturn += 1

        return toReturn

# Afterthoughts:
# ord('a') = 97, so ord('a') - 97 = 0.
# chr(97) gives you 'a'

# Results:
# Runtime: 36 ms, faster than 93.05% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.1 MB, less than 85.87% of Python3 online submissions for Unique Morse Code Words.
