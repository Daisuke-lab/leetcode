class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = {}
        for task in tasks:
            count_map[task] = count_map.get(task, 0) + 1
        task_queue = [(-count, task) for task, count in count_map.items()]
        heapq.heapify(task_queue)
        waiting_queue = []
        interval = 0
        while task_queue or waiting_queue:
            interval += 1
            if waiting_queue and interval - waiting_queue[0][0] > n:
                past_interval, count, task = waiting_queue.pop(0)
                heapq.heappush(task_queue, (-count, task))
            if not task_queue:
                # idling
                continue
            count, task = heapq.heappop(task_queue)
            count *= -1
            count -= 1
            if count > 0:
                waiting_queue.append((interval, count, task))
        return interval
            