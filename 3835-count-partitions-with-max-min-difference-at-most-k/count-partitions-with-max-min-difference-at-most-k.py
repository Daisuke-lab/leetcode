class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        memo = [-1 for i in range(len(nums))]
        memo[0] = 1
        acc = 1
        decrease_queue = collections.deque()
        increase_queue = collections.deque()
        i = 0
        mod = 10 ** 9 + 7
        # i-j is a sliding window to maintain valid partition (max - min <= k)
        # If you face 
        for j in range(len(nums)):
            while decrease_queue and nums[j] > decrease_queue[-1][1]:
                decrease_queue.pop()
            decrease_queue.append((j, nums[j]))
            while increase_queue and nums[j] < increase_queue[-1][1]:
                increase_queue.pop()
            increase_queue.append((j, nums[j]))

            while decrease_queue[0][1] - increase_queue[0][1] > k:
                # you can not include partition that includes i
                # But you can keep the case when you add partition between j and j + 1
                # memo[i-1] represent the number of partitions until i without partition between i and i + 1
                # You want to keep the number with partition. That's why it's memo[i-1] not memo[i]
                if i > 0:
                    acc = (acc - memo[i-1]) % mod
                else:
                    acc = (acc -1) % mod
                if decrease_queue[0][0] == i:
                    decrease_queue.popleft()
                if increase_queue[0][0] == i:
                    increase_queue.popleft()
                i += 1
            # you cache the max number of partitions from 0 to j
            memo[j] = acc
            # why multiply by 2??
            # for every partition so far, you can choose 2 options
            # case1: add partition between j and j + 1
            # case2: don't add parititon between j and j + 1

            # ex
            # current partition [4,1], [4][1]
            # and now you have 3
            # when you partition
            # [4,1][3], [4][1][3]
            # when you don't partition
            # [4,1,3], [4][1,3]

            # That's why you multiply by 2
            acc = (acc * 2) % mod
        #print(memo)
        return memo[-1]            