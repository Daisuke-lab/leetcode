class Solution:
    # You want to make all close to the average
    # 0. check if it's possible
    # 1. find the median
    # 2. choose closest num in average
    # 3. calculate how many operation you need to reach the number
    # the average doesn't mean the number that all cell can reach. => It is. if the condition below is fulfilled
    # How do you know if all the elements are equal?? => the reminder of x is always the same
    
    # [1, 500, 499] => average: 166. 1 would be closest to the everage but cleary not the right answer
    # mode (frequent) ?? => [1,1,1,2,500,500,500] => let's say 1. but 2 is more efficient
    # median?? => [1,1,1,2,500,500,500] => median is 2. this looks right.
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        self.ROW = len(grid)
        self.COL = len(grid[0])
        fixed_reminder = None
        self.min_heap = []
        self.max_heap = []
        for i in range(self.ROW):
            for j in range(self.COL):
                num = grid[i][j]
                if fixed_reminder is None:
                    fixed_reminder = num % x
                elif fixed_reminder != num % x:
                    return -1
                min_num = self.min_heap[0] if self.min_heap else float("inf")
                if num < min_num:
                    heapq.heappush(self.max_heap, -num)
                else:
                    heapq.heappush(self.min_heap, num)

                if len(self.max_heap) > len(self.min_heap) + 1:
                    popped_num = -heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, popped_num)
                elif len(self.max_heap) < len(self.min_heap):
                    popped_num = -heapq.heappop(self.min_heap)
                    heapq.heappush(self.max_heap, popped_num)
        target = -self.max_heap[0]
        #print(target)
        answer = 0
        for num in self.min_heap:
            #print(f"num:{num}, result:{(num - target) // x}")
            answer += (num - target) // x
        for num in self.max_heap:
            num *= -1
            #print(f"num:{num}, result:{(num - target) // x}")
            answer += (target - num) // x
        return answer
                
        