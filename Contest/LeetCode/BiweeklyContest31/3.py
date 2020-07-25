# 1525. Number of Good Ways to Split a String
# User Accepted:2968
# User Tried:3451
# Total Accepted:3050
# Total Submissions:4617
# Difficulty:Medium
# You are given a string s, 
# a split is called good if you can split s into 2 non-empty strings p and q 
# where its concatenation is equal to s and the number of distinct letters in p and q are the same.
# Return the number of good splits you can make in s.

# Example 1:
# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

# Example 2:
# Input: s = "abcd"
# Output: 1
# Explanation: Split the string as follows ("ab", "cd").

# Example 3:
# Input: s = "aaaaa"
# Output: 4
# Explanation: All possible splits are good.

# Example 4:
# Input: s = "acbadbaada"
# Output: 2
 
# Constraints:
# s contains only lowercase English letters.
# 1 <= s.length <= 10^5

from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        cnt = 0
        forward = Counter(s[0])
        backward = Counter(s[1:])

        if len(forward) == len(backward):
                cnt += 1

        for c in s[1:]:
            forward += Counter(c)
            backward -= Counter(c)
            if len(forward) == len(backward):
                cnt += 1
            
        return cnt
