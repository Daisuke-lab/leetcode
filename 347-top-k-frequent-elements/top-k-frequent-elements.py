class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        heap = []
        for num, count in count_map.items():
            heap.append((-count, num))
        heapq.heapify(heap)
        return [num for count, num in heapq.nsmallest(k, heap)]
        


        