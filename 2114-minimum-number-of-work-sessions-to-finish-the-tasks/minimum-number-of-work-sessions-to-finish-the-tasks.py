class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        self.n = len(tasks)
        self.memo = {}
        self.tasks = tasks
        self.session_time = sessionTime
        self.all_visited = (1 << self.n) - 1
        return self.dp(0, 0)

    def dp(self, visited, remain_time):
        if visited == self.all_visited:
            return 0
        if (visited, remain_time) in self.memo:
            return self.memo[(visited, remain_time)]
        result = float("inf")
        for i in range(self.n):
            unvisited = visited & (1 << i) == 0
            if unvisited:
                new_visited = visited | (1 << i)
                if self.tasks[i] <= remain_time:
                    result = min(result, self.dp(new_visited, remain_time - self.tasks[i]))
                else:
                    result = min(result, self.dp(new_visited, self.session_time - self.tasks[i]) + 1)
        self.memo[(visited, remain_time)] = result
        return result
        