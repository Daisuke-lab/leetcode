class SegmentTree:
    def __init__(self, n):
        self.maxes = [0 for i in range(2*n)]
        self.n = n
    def update(self, i, num):
        i += self.n
        self.maxes[i] = num
        i //= 2
        while i > 0:
            self.maxes[i] = max(self.maxes[i*2], self.maxes[i*2+1])
            i //= 2
    
    def get_range_max(self, i, j):
        i += self.n
        j += self.n
        max_num = 0
        while i <= j:
            if i % 2 == 1:
                max_num = max(max_num, self.maxes[i])
                i += 1
            if j % 2 == 0:
                max_num = max(max_num, self.maxes[j])
                j -= 1
            i //= 2
            j //= 2
        return max_num
                 

class Solution:
    # you want the numbers that is bigger than curr => compression
    # take the longest subsequcne out of them => segment tree
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = self.compress(nums)
        n = len(nums)
        segment_tree = SegmentTree(n)
        answer = 1
        for num in nums:
            max_length = segment_tree.get_range_max(0, num-1)
            segment_tree.update(num, max_length+1)
            answer = max(max_length + 1, answer)
        #print(segment_tree.maxes)
        return answer
            

    def compress(self, nums):
        # Convert 
        # from [10,9,2,5,3,7,101,18]
        # to   [5,4,0,2,1,3,7,6]
        index_map = {}
        i = -1
        prev = None
        sorted_nums = sorted(nums)
        for num in sorted_nums:
            if prev != num:
                i += 1
                prev = num
                index_map[num] = i
        compressed_nums = []
        for num in nums:
            compressed_nums.append(index_map[num])
        return compressed_nums