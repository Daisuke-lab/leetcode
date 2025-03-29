class Solution:
    # Because there is a negative value and it's mulitply not add, so you can not use kadane
    # Sliding Window?
    # Brute Force
    # n^2 0 <= i < len(nums), i <= j < len(nums) when i ==j, don't multiply
    # because you need to check all i and j, no meaning to cache
    # i is the always the start and j is always the end 
    # you can check 3 (i+1) excluding i => n^2 /2
    def maxProduct(self, nums: List[int]) -> int:
        min_product = 1
        max_product = 1
        answer = -float("inf")
        for num in nums:
            new_product1 = min_product * num
            new_product2 = max_product * num
            min_product = min(new_product1, new_product2, num)
            max_product = max(new_product1, new_product2, num)
            if max_product > answer:
                answer = max_product

            
        return answer
        