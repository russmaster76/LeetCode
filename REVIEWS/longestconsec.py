class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        - only integers, want to find the longest consecutive sequence of in order numbers.
        - return the length of the longest consecutive sequence that can be made from the given arry
        
        - convert the array to a hashset, look at each number, and run a while loop while the next number exists.
        - if a number within the set has the previous number also in the set, it should not run the while loop on that number
            because later, when that previous number is searched, then it will reach the end of that sequence. [1,2,3,7,9,34], when 3 is found , it checks if 2 exists, and if it does
            then it wont look further because when two is encoutered that sequence will be run, therefore making looking at numbers in the middle or end of sequeneces redundant. 
        """
        
        result = 0
        
        numsSet = set(nums)
        
        for n in numsSet: 
            if (n - 1) in numsSet:
                continue
            i = 1
            while n + i in numsSet:
                i += 1
            
            result = max(result, i)
        
        return result