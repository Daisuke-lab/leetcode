class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # you should execute a variety of tasks as many as possible because interfval is the same for all the task
        # you want to start with the higher number of char
        # Heap can be fast because the max number of tasks changes
        # You also maintain the prev task => you need to use hashmap to maintain the last interval
        # you also maintain the count for intervals
        # you also need hashmap for initial count
        # 1. create count_map O(n)
        # 2. create heap O(n)
        # 3. execute task (check interval and prev acoordingly)
        # 4. insert a new (count, "A") O(logm) * n m: the apperarnce of a character
        
        count_map = defaultdict(int)
        for task in tasks:
            count_map[task] += 1
        heap = []
        for task, count in count_map.items():
            heap.append((-count, task))
        
        heapq.heapify(heap)
        intervals = 0
        queue = collections.deque()
        while heap or queue:

            intervals += 1
            if queue and intervals - queue[0][1] > n:
                count, _, task = queue.popleft()
                heapq.heappush(heap, (count, task))
            if len(heap) == 0:
                continue
            count, task = heapq.heappop(heap)
            # because it's max heap and count is treated as negative, it's +1
            count += 1
            if count < 0:
                queue.append((count, intervals, task))
            
        return intervals
            