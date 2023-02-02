class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        difference = 0
        for i, value in enumerate(nums):
            difference = target - value
            if (difference in dictionary):
                return([i, dictionary[difference]])
            
            dictionary[value] = i
