class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force
        # recursion with 2 patterns (cut the begining or cut the end)
        # O(n^2)

        # Looks like 2 pointers quesitons
        # I feel like it is better to start from center => not really. the hype can be leaned to the end or start
        # it's not left and right pointers with the same reason

        # if you extend width, it increases min height
        # if you increase height, it increases wid

        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            start_i = end_i = i
            while stack and stack[-1][1]  > height:
                start_i, top_height = stack.pop()
                max_area = max(max_area, (end_i - start_i)*top_height)
            stack.append((start_i, height))


        while stack:
            i, height = stack.pop()
            max_area = max(max_area, (len(heights) - i)*height)
        return max_area
                

        