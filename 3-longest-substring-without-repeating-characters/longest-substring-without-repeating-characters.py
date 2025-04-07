class Solution:
    # you can do it queue/stack
    # visited to find duplicate
    # 
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        visited = set()
        stack_queue = []
        for c in s:
            if c not in visited:
                visited.add(c)
                stack_queue.append(c)
            else:
                max_length = max(max_length, len(stack_queue))
                while stack_queue[0] != c:
                    removing_c = stack_queue.pop(0)
                    visited.remove(removing_c)
                stack_queue.pop(0)
                stack_queue.append(c)
        max_length = max(max_length, len(stack_queue))
        return max_length