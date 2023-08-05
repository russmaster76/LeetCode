class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        - find all possible trios that add to 0 within the array
        - we are not able to use duplicate triplets
        
        - array unsorted, sort the array.
        - sort from smallest to largest, so that the smallest value is at nums[0]
        - create two different pointers, and for each negative value within the array, we will have a left pointer at the point right after the value
            and a right pointer on the last value of the array. Then we will do the necessary calcuations, find out it we are above or below 0, and adjust our pointers
            based on that information. If its smaller than 0, then we move the left pointer, and if its bigger then we move the right pointer
            = 0, we just want to add it to our result array, and also move one of the pointers so that there are no duplicate results in the result
            
        """
        
        nums.sort()
        
        result = []
        
        for i, n in enumerate(nums):
            
            if n > 0:
                break
            
            if i > 0 and n == nums[i - 1]:
                continue
            
            
            l = i + 1
            r = len(nums) - 1
            
            while(l < r):
                
                threeSum = n + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                
                elif threeSum < 0:
                    l += 1
                
                else:
                    result.append([n,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
        
        return result
                    

        
        