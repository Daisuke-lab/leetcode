
class Solution:
    # If you know it's not in the same component, it immediately can return -1
    # 
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nums = self.get_sorted_nums(nums)
        self.ancestors = self.build_binary_lifting(n, nums, maxDiff)
        
        distances = []
        for src, dest in queries:
            src = self.get_curr_index(src)
            dest = self.get_curr_index(dest)
            curr = self.query(min(src, dest), max(src, dest))
            distances.append(curr if curr < float("inf") else -1)
        return distances


            
    def query(self, src, dest, jump=None):
        jump = jump if jump is not None else self.lift_height - 1
        if src == dest:
            return 0
        # if src is reachable to bigger number than dest
        if self.ancestors[src][0] >= dest:
            return 1
        # if farthest from src is smaller than dest
        if self.ancestors[src][jump] < dest:
            return float("inf")
        # find spot just before it exceeds dest
        for next_jump in range(jump, -1, -1):
            if self.ancestors[src][next_jump] < dest:
                break 
        steps = 1 << next_jump
        next_src = self.ancestors[src][next_jump]
        return steps + self.query(next_src, dest, next_jump)

    
    def build_binary_lifting(self, n, nums, maxDiff):
        self.lift_height = ceil(math.log(n, 2)) + 1
        ancestors = [[
            -1 for j in range(self.lift_height)]
            for i in range(n)]

        # for i in range(n):
        #     for j in range(i, n):
        #         # insert the the biggest neighbor as parents
        #         if nums[j] - nums[i] <= maxDiff:
        #             ancestors[i][0] = j
        #         else:
        #             break
        j = 0
        for i in range(n):
            while j+1 < n and nums[j+1] - nums[i] <= maxDiff:
                j += 1
            ancestors[i][0] = j

        for jump in range(1, self.lift_height):
            for node in range(n):
                ancestors[node][jump] = ancestors[ancestors[node][jump-1]][jump-1]
        return ancestors
        

            

    def get_sorted_nums(self, nums):
        nums_indices = sorted([(num, i) for i, num in enumerate(nums)])
        self.index_map = {num_index[1]: i for i, num_index in enumerate(nums_indices)}
        return [num for num, i in nums_indices]

    def get_curr_index(self, i):
        return self.index_map[i]
    
        
        