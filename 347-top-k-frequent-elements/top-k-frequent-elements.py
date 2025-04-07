class Solution:
    # Hashmap: n + nlogn
    # min Heap with size k 3n
    # 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        max_heap = []
        for num, count in count_map.items():
            max_heap.append((-count, num))
        heapq.heapify(max_heap)
        answer = []
        while k > 0:
            k -= 1
            _, num = heapq.heappop(max_heap)
            answer.append(num)
        return answer



        