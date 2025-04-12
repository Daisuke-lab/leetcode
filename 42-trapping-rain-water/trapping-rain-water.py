class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        min_height = min(heights[l], heights[r])
        direction = "left" if heights[l] > heights[r] else "right"
        water = 0
        while l < r:
            if direction == "right":
                if heights[l] < min_height:
                    water += min_height - heights[l]
                else:
                    min_height = min(heights[l], heights[r])
                    direction = "left" if heights[l] > heights[r] else "right"
            if direction == "left":
                if heights[r]< min_height:
                    water += min_height - heights[r]
                else:
                    min_height = min(heights[l], heights[r])
                    direction = "left" if heights[l] > heights[r] else "right"
            if direction == "left":
                r -=1
            else:
                l += 1


        return water
                

