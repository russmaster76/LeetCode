class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        containsNums = set(nums)
        longest = 0
        
        for n in nums:
            if(n-1) not in containsNums:
                length = 1
                while(n + length in containsNums):
                    length += 1
                longest = max(length, longest)
        
        return longest
        