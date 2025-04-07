class Solution:
    # if it's all positive, multply everything
    # if it has even number of negatives, multiply everything
    # if it has odd number of negatives, you should ignore the first or last negative
    
    # if you have 0, think of it as dividor of array
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -float("inf")
        curr = 1
        for num in nums:
            if num == 0:
                curr = 1
                max_product = max(0, max_product)
            else:
                curr *= num
                max_product = max(curr, max_product)

        curr = 1
        for i in range(len(nums) -1, -1, -1):
            if nums[i] == 0:
                curr = 1
                max_product = max(0, max_product)
            else:
                curr *= nums[i]
                max_product = max(curr, max_product)
        return max_product