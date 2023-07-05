import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        minHeap = []
        for i in nums:
            count[i] = count.get(i, 0) + 1

        for element, freq in count.items():
            heapq.heappush(minHeap, (freq, element))
            if(len(minHeap) > k):
                heapq.heappop(minHeap)
        
        return [num for [count, num] in minHeap]
            
        
