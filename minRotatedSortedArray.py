class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        curr_min = float("inf")
        
        while l < r:
            m = (r - l) // 2
            curr_min = min(curr_min, nums[m])
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return min(curr_min, nums[l])
