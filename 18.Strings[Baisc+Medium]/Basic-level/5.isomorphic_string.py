class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_stot = {}
        mapping_ttos = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in mapping_stot:
                if mapping_stot[char_s]!=char_t:
                    return False
            else:
                mapping_stot[char_s] = char_t
            if char_t in mapping_ttos:
                if mapping_ttos[char_t]!= char_s:
                    return False
            else:
                mapping_ttos[char_t] = char_s
        return True


'''
205. Isomorphic Strings
Solved
Easy
Topics
premium lock icon
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''
