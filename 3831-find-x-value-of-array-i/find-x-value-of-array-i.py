class Solution:
    # product prefix/suffix
    # 1,  2,  6, 12,70
    # 120,120,60,20,5
    # prefix[2] = nums[0] * nums[1] * nums[2]
    # suffix[2] = nums[2] * nums[3] * nums[4]

    # reminder of proeuct: prefix/suffix
    # 1, 2, 0, 0, 0
    # 0, 0, 0, 2, 2

    # O(n^2)
    # 1, 2, 0, 1, 2

    # sliding window
    # O(n^2)

    # O(n) or O(nlogn)
    # but you have to increment memo more than once in O(n) times then
    # 
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        self.answer = [0 for i in range(k)]
        self.memo = [[
            0 for i in range(k)]
            for j in range(len(nums))]
        for i in range(len(nums)):
            r =  nums[i] % k
            self.memo[i][r] += 1
            if i == 0:
                continue
            for r in range(k):
                new_r = (r * nums[i]) %k
                self.memo[i][new_r] += self.memo[i-1][r]


        for i in range(len(self.memo)):
            for r in range(k):
                self.answer[r] += self.memo[i][r]
        return self.answer
