'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


from typing import List
from collections import defaultdict

class Solution:
    def getSignature(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)

        result.extend(groups.values())

        return result

