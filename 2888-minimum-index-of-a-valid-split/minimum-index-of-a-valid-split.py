class Solution:
    # How do you know if it's dominant => O(n)
    # just cut it when it's just more than half O(n) in the worse case
    # 
    def minimumIndex(self, nums: List[int]) -> int:
        dominant_num = nums[0]
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
            if count_map[dominant_num] <= count_map[num]:
                dominant_num = num

        dominant_count = 0
        for i in range(len(nums)):
            if nums[i] == dominant_num:
                dominant_count += 1
            threshold = ( (i + 1) // 2 ) + 1
            if dominant_count >= threshold:
                remaining_count = count_map[dominant_num] - dominant_count
                latter_threshold = ( (len(nums) - i - 1) // 2 ) + 1
                if remaining_count >= latter_threshold:
                    return i
                else:
                    return -1