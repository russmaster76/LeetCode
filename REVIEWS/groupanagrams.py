import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        - Array of strings and we want to group all the anagrams together.
        - All lowercase strings
        - every string in strs should be included in result
        
        SOLUTION IDEA
        - Hashmap key = the given anagram in some form where order does not matter, value = list of all of the strings that fit that key within strs
        """
        
        result = collections.defaultdict(list)
        
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            result[tuple(freq)].append(s)
        
        return result.values()
        
        
        
        