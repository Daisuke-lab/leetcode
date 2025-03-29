class Solution:
    # Let's assume that we have no "0"
    # If you have even numbers of negative integers
    # => just multiply everything
    # If you have odd numbers of negative integers
    # => you can split the array into two both having even number of negative integers, excluding the middle negative number
    #  | 
    # \_/
    # So simply check from the both directions, either of direction find the max product
    # You can check from both directions even when you have even number of negative integers although it is not necessary

    # Ok. now what if you have 0?
    # you can think of 0 as splitter as well.
    # you split array into two and check from both directions
    # ------------------>       -----> ------> ----->
    # [1,2,0,3,4,5,0,9,9]    => [1,2], [3,4,5], [9,9]
    # <------------------       <----  <------ <-----
    # But practically you don't have to split your array. you can just check from both directions in one array
    # but don't forget you reset the product with "0"
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0
        for i in range(n):
            print("suffix:", suffix, (suffix or 1))
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        print(res)
        return res