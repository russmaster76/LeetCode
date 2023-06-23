class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        output = 0
        h = max(height)
        while l < r:
            output = max(output, min(height[l], height[r]) * (r - 1))
            if height[l] > height[r]:
                l += 1
            elif height[r] > height[l]:
                r -= 1
            
            if(r-1) * h <= output: break
        
        return output