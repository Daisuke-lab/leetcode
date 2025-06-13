class Solution:
    # you can fix min efficiency by reverse sort
    # then you keep high speed people
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(list(zip(speed, efficiency)), reverse=True, key=lambda engineer: engineer[1])
        #print(engineers)
        min_heap = []
        max_performance = 0
        curr_sum = 0
        for speed, eff in engineers:
            heapq.heappush(min_heap, speed)
            curr_sum += speed
            max_performance = max(max_performance, (eff * curr_sum))
            if len(min_heap) == k:
                curr_sum -= heapq.heappop(min_heap)
        return max_performance % (10**9 + 7)