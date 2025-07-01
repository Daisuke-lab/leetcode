class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # The reason why you want to sort it, is because you want to speed up binary_lifting cnostruction
        nums = self.get_sorted_nums(nums)
        self.ancestors = self.build_binary_lifting(n, nums, maxDiff)
        
        distances = []
        for src, dest in queries:
            src = self.get_curr_index(src)
            dest = self.get_curr_index(dest)
            distance = self.query(min(src, dest), max(src, dest))
            distances.append(distance)
        return distances


    def query(self, src, dest):
        #print("SRC:", src, "DEST:", dest)
        if src == dest:
            return 0
        steps = 0
        for exponent in range(self.max_exponent, -1, -1):
            if self.ancestors[src][exponent] != -1 and self.ancestors[src][exponent] < dest:
                src = self.ancestors[src][exponent]
                steps += 2**exponent
            if src >= dest:
                break
        if self.ancestors[src][0] >= dest:
            steps += 1
            src = self.ancestors[src][0]
        return steps if src >= dest else -1

    
    def build_binary_lifting(self, n, nums, maxDiff):
        #print(nums)
        self.max_exponent = ceil(math.log(n, 2))
        ancestors = [[
            -1 for j in range(self.max_exponent + 1)]
            for i in range(n)]

        j = 0
        for i in range(n):
            # insert the the biggest neighbor as parents
            while j+1 < n and nums[j+1] - nums[i] <= maxDiff:
                j += 1
            if i != j:
                ancestors[i][0] = j
        for exponent in range(self.max_exponent+1):
            ancestors[-1][exponent] = -1

        for exponent in range(self.max_exponent+1):
            for node in range(n):
                # farest place with 2**jump from node = farest place with 2**jump-1 from 2**jump-1 ahead node from current
                prev = ancestors[node][exponent-1]
                if prev != -1:
                    ancestors[node][exponent] = ancestors[prev][exponent-1]
        #print(ancestors)
        return ancestors

    def get_sorted_nums(self, nums):
        nums_indices = sorted([(num, i) for i, num in enumerate(nums)])
        self.index_map = {num_index[1]: i for i, num_index in enumerate(nums_indices)}
        return [num for num, i in nums_indices]

    def get_curr_index(self, i):
        return self.index_map[i]
    
        
        