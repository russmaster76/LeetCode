class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        nums.sort()
        
        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if n == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([n,nums[l],nums[r]])
                    while nums[l] == nums[l -1]:
                        l += 1
        
        
        return result