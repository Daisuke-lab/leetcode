class Solution:
    # Brute Force solution
    # try every partition 
    # O(2^n)

    # DP
    # i and j
    # you want to return count
    # you also want to return min number and max number
    # O(n^2)

    # args: i, j
    # output: count, min_num, max_num

    # base case: i = j => return 1, nums[i], nums[j]
    # merge: find curr max and min and if it works, + 1
    
    # can you do bottom up
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
                #acc = (acc - memo[i]) % mod
                acc = (acc - (memo[i - 1] if i > 0 else 1)) % mod
                if decrease_queue[0][0] == i:
                    decrease_queue.popleft()
                if increase_queue[0][0] == i:
                    increase_queue.popleft()
                i += 1
            # you cache the max number of partitions from 0 to j
            memo[j] = acc
            # why multiply by 2??
            # In the next iteration, [x,x,x] [y]
            acc = (acc * 2) % mod
        print(memo)
        return memo[-1]            