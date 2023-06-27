class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupeList = set()
        for i in nums:
            if i in dupeList:
                return True
            else:
                dupeList.add(i)
        
        return False