class Solution:
    def trap(self, height: List[int]) -> int:
        return self.recursion(height)

    def recursion(self, height):
        count = height.count(0)

        if len(height) - count < 2:
            return 0
        else:
            start_index = i = -1
            end_index = j = len(height)
            while True:
                i += 1
                j -= 1
                if i == len(height):
                    break
                if height[i] != 0 and start_index == -1:
                    start_index = i
                if height[j] != 0 and end_index == len(height):
                    end_index = j

            if start_index != -1:
                count -= start_index
            if end_index != -1:
                count -= (len(height) - end_index - 1)
            new_height = [0 if _height -1 <= 0 else _height - 1 for _height in height]
            count += self.recursion(new_height)
            return count
        