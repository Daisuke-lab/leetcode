class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        answer_map = {}
        i = 0
        min_heap = []
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                size = r - l + 1
                heapq.heappush(min_heap, (size, r))
                i += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            answer_map[query] = min_heap[0][0] if min_heap else -1
        return [answer_map[query] for query in queries]

        