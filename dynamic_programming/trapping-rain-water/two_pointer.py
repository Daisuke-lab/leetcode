class Solution:
    def trap(self, height: List[int]) -> int:
        # return self.recursion(height)
        return self.two_pointer(height)

    def two_pointer(self, height):

        if len(height) <= 2:
            return 0

        count = 0
        i = 1
        j = len(height) - 2

        left_tallest = height[0]
        right_tallest = height[-1]

        while i <= j:
            if height[i] > left_tallest:
                left_tallest = height[i]
            if height[j] > right_tallest:
                right_tallest = height[j]


            if left_tallest <= right_tallest:
                count += left_tallest - height[i]
                i += 1
            else:
                count += right_tallest - height[j]
                j -= 1

        return count
                       