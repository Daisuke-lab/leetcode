class Solution:
    # Brute Force
    # go through all patterns
    # O(n^2)

    # monotonous stack
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            j = i
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                height = heights[j]
                width = i - j
                max_area = max(max_area, height*width)
            heights[j] = heights[i]
            stack.append(j)
        while stack:
            j = stack.pop()
            height = heights[j]
            width = i - j + 1
            max_area = max(max_area, height*width)
        return max_area