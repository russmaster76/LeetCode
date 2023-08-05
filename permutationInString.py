class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        s1freq = {}
        
        for c in s1:
            s1freq[c] = s1freq.get(c, 0) + 1
        
        l = 0
        r = len(s1 - 1)
        
        while l < r and r < len(s2):
            s2freq = {}
            s2freq[s2freq.get(s2[l], 0)