class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        chars_freq = {}
        for ch in s:
            chars_freq[ch] = chars_freq.get(ch,0)+1
        for ch in t:
            if ch not in chars_freq:
                return False
            else:
                if chars_freq[ch] == 0:
                    return False
                else:
                    chars_freq[ch]-=1
        return True


'''
242. Valid Anagram
Solved
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
