# You are given a string, s, and a list of words, words, 
# that are all of the same length. Find all starting indices 
# of substring(s) in s that is a concatenation of each word 
# in words exactly once and without any intervening characters.

# Example 1:
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.

# Example 2:
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        lens = len(s)
        lenw = len(words[0])
        lenws = lenw * len(words)
        times = {}
        if lens < lenws:
            return []
        
        for word in words:
            if word in times:
                times[word] += 1
            else:
                times[word] = 1
        res = []
        for i in range(min(lenw, lens - lenws + 1)):
            sstart = i
            wstart = sstart
            curr = {}
            while sstart + lenws <= lens:
                word = s[wstart : wstart + lenw]
                wstart += lenw
                if word not in times:
                    sstart = wstart
                    curr.clear()
                else:
                    if word in curr:
                        curr[word] += 1
                    else:
                        curr[word] = 1
                    while curr[word] > times[word]:
                        curr[s[sstart : sstart + lenw]] -= 1
                        sstart += lenw
                    if wstart - sstart == lenws:
                        res.append(sstart)
        
        return res
