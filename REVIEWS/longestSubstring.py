class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        longest substring without repeating characters
        any character possible
        - We want the longest substring without any repeating characters (no more than one of each character allowed) 
        - return the length of that substring, not the substring itself.
        
        - HASHSET
        - If its in the hashset, its in the substring.
        
        - create a hashset
        - create a left pointer, and that will be the left of the sliding window
        - right pointer will be created with a for loop
        - at the beginning of each loop, we want to see if the current character is in the current substring, and if it is, move the left pointer up to the right, 
        and remove all characters that we come across from the hashmap. get length of how long the window
        log max of current max and window that just closed return max
        """
        
        present = set()
        
        result = 0
        
        l = 0
        
        for i, r in enumerate(s):
            while r in present:
                present.remove(s[l])
                l += 1
            
            present.add(r)
            
            result = max(result, i - l + 1)
        
        return result
            
            
        