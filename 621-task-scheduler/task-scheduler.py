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
        _ = -len(count_map) - 1
        for task, count in count_map.items():
            _ += 1
            heap.append((-count, _, task))
        
        heapq.heapify(heap)
        intervals = 0
        waiting = 0
        interval_map = {}
        queue = collections.deque()
        while heap or queue:

            intervals += 1
            if queue and intervals - queue[0][1] > n:
                heapq.heappush(heap, queue.popleft())
            if len(heap) == 0:
                continue

            #print(interval_map, intervals, heapq.nsmallest(1, heap)[0])
            count, _, task = heapq.nsmallest(1, heap)[0]
            if task in interval_map and (intervals - interval_map[task]) <= n:
                continue
            count, _, task = heapq.heappop(heap)
            interval_map[task] = intervals
            # because it's max heap and count is treated as negative, it's +1
            count += 1
            if count < 0:
                queue.append((count, intervals, task))
            #waiting = queue[0]
            
        return intervals
            