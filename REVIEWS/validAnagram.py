class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap = {}
        tmap = {}
        i = 0
        if len(s) != len(t):
            return False
        
        while i < len(t):
            smap[s[i]] = smap.get(s[i], 0) + 1
            tmap[t[i]] = tmap.get(t[i], 0) + 1
            i += 1
        
        if smap == tmap:
            return True
        else:
            return False
        