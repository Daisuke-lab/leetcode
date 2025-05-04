class Solution:
    # If it's all positive, multitply everything
    # If you have negatives, don't include the last negative and multiply everything
    # If you have 0, you can think of it as subaary
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        current_product = 1
        for num in nums:
            if num == 0:
                max_product = max(0, max_product)
                current_product = 1
            else:
                current_product *= num
                max_product = max(current_product, max_product)
        
        current_product = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num == 0:
                current_product = 1
            else:
                current_product *= num
                max_product = max(current_product, max_product)
        return max_product

 