class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = 0
        e = len(s) - 1
        while f < e:
            while f < e and not s[f].isalnum():
                f += 1
            while f < e and not s[e].isalnum():
                e -= 1
            if(s[f].lower() != s[e].lower()):
                return False
            f += 1
            e -= 1
        
        return True