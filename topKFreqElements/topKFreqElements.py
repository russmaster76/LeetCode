import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        min_heap = []
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        for element, freq in counter.items():
            heapq.heappush(min_heap, (freq, element))
            if(len(min_heap) > k):
                heapq.heappop(min_heap)
        return [num for (count, num) in min_heap]