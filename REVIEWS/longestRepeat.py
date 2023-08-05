class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        Go Through the given string and find the longest possible set of repeating characters, while replacing up to K characters within that substring.
        - Iterate through string once if possible
        - sliding window, keep track of longest substring within the string that allows k replacements
        - Dictionary of frequency of all characters within the current window (as we iterate)
        - int variable of the freq of most common character within current window
        - as we iterate through each character, then we would check to see if the amount of characters that arent the most common are more than k
          and if they are, they we would move the window up.
        - eventually, once the loop is done iterating, we will have the longest substring
        - 
        """
        
        freq = {}
        
        l = 0
        
        maxf = 0
        
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])
            
            if((r - l + 1) - maxf > k):
                freq[s[l]] -= 1
                l += 1
        
        return(r - l + 1)
        
        
        