class Solution:
    # Bucket List + hashmap
    # compress
    # quick selecct 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [set() for i in range(len(nums) + 1)]
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
                buckets[1].add(num)
            else:
                curr_count = count_map[num]
                buckets[curr_count].remove(num)
                count_map[num] += 1
                buckets[curr_count+1].add(num)
        unique_sorted_nums = []
        for i in range(len(buckets) -1, -1, -1):
            bucket = buckets[i]
            for num in bucket:
                unique_sorted_nums.append(num)
            if len(unique_sorted_nums) == k:
                return  unique_sorted_nums

    def create_unique_nums(self, nums):
        buckets = [set() for i in range(len(nums) + 1)]
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
                buckets[1].add(num)
            else:
                curr_count = count_map[num]
                buckets[curr_count].remove(num)
                count_map[num] += 1
                buckets[curr_count+1].add(num)
        unique_sorted_nums = []
        for i in range(len(buckets) -1, -1, -1):
            bucket = buckets[i]
            for num in bucket:
                unique_sorted_nums.append(num)
        return  unique_sorted_nums
        

        