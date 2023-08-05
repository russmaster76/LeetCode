class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxf = 0
        l = 0
        
        freq = {}
        
        for i, r in enumerate(s):
            freq[r] = freq.get(r, 0) + 1
            maxf = max(maxf, freq[r])
            if (i - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
        
        return (i - l + 1)