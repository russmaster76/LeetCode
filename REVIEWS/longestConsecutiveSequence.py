class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numsSet = set(nums)

        longest = 0
        
        for n in numsSet:
            if (n-1) not in numsSet:
                length = 1
                while n + length in numsSet:
                    length += 1
                
                longest = max(longest, length)
        
        return longest